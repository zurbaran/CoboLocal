# -*- coding: UTF-8 -*-
####################################################
# Name:        Cobo.py
# Purpose:
#
# Author:      Antonio
#
# Created:     23/07/2012
# Copyright:   (c) Antonio 2012
# Licence:     <your licence>
####################################################
# paginas de interes
# http://finance.yahoo.com/international


#################################################
# Constantes locales

webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0'}
pausareconexion = 20
prefijo = {'': '',
           '.AS': 'nl.',
           '.AT': 'gr.',
           '.AX': 'au.',
           '.BA': 'ar.',
           '.BC': 'es.',
           '.BE': 'de.',
           '.BI': 'es.',
           '.BM': 'de.',
           '.BO': 'in.',
           '.BR': 'fr.',
           '.CBT': '',
           '.CME': '',
           '.CMX': '',
           '.CO': 'dk.',
           '.DE': 'de.',
           '.DU': 'de.',
           '.EX': '',
           '.F': 'de.',
           '.HA': 'de.',
           '.HK': 'hk.',
           '.HM': 'de.',
           '.IL': 'uk.',
           '.IR': '',
           '.JK': 'id.',
           '.KL': '',
           '.JP': 'kr.',
           '.KQ': 'kr.',
           '.KS': 'kr.',
           '.L': 'uk.',
           '.LS': '',
           '.MA': 'es.',
           '.MC': 'es.',
           '.MDD': '',
           '.ME': 'ru.',
           '.MF': 'es.',
           '.MI': 'it.',
           '.MU': 'de.',
           '.MX': 'mx.',
           '.NS': 'in.',
           '.NX': 'fr.',
           '.NYB': '',
           '.NYM': '',
           '.NZ': 'nz.',
           '.OB': '',
           '.OL': 'no.',
           '.PA': 'fr.',
           '.PK': '',
           '.SA': 'br.',
           '.SG': 'de.',
           '.SI': 'sg.',
           '.SN': 'cl.',
           '.SS': '',
           '.ST': 'se.',
           '.SW': 'ch.',
           '.SZ': '',
           '.TA': 'ta.',
           '.TO': 'ca.',
           '.TW': 'tw.',
           '.TWO': 'tw.',
           '.V': 'ca.',
           '.VA': 'at.',
           '.VI': '',
           '.VX': '',
           }
# # Lista que contiene los mercados que estan fallando al descargar las cotizaciones del csv, leyendo la web para obtener la informacion
mercadosfail = ('.MC',)

####################################################
# modulos estandar importados

from time import sleep, strftime, strptime
from datetime import date, timedelta
from random import randint
import logging
import os
import urllib2
import csv


####################################################
# modulos no estandar o propios
from Cobo import carpetas, ARCHIVO_LOG
# from BBDD import datoshistoricoslee, datoshistoricosgraba, ticketcotizaciones, monedacotizaciones
import BBDD


logging.basicConfig(filename=ARCHIVO_LOG,
    format='%(asctime)sZ; nivel: %(levelname)s; modulo: %(module)s; Funcion : %(funcName)s; %(message)s',
    level=logging.DEBUG)


def _test():
    import doctest
    doctest.testmod()


def duerme(tiempo=1500):
    """

    """
    x = (randint(0, tiempo)) / 1000.0
    print('Pausa de %.3f segundos' % x)
    sleep(x)


def ticketsdeMercado(mercado):
    """

    """
    # global webheaders
    # habra que buscar los ticket y utilizar como fin de pagina el texto en la primera
    # <a href="/q/cp?s=%5EDJA&amp;c=1">Last< donde c=1 indica el final de la pagina
    # en los casos donde solo hay una pagina, no encontrariamos cadena dando valor -1
    # los tickets se encuentan en detras de la cadena <b><a href="/q?s= y como final ">
    ticketsanadidos = []
    ultimapagina = 0
    pagina = 0
    mercado = mercado.strip()
    while pagina <= ultimapagina:
        print('')
        url = 'http://finance.yahoo.com/q/cp?s=' + mercado + '&c=' + str(pagina)
        print(url)

        web = None
        while web == None:
            try:
                r = urllib2.Request(url, headers=webheaders)
                f = urllib2.urlopen(r)
                web = (f.read()).decode('UTF-8')
                f.close()
            except urllib2.HTTPError as e:
                print('Conexion Perdida')
                print(e.code)
                if e.code == 500:
                    return ticketsanadidos
                else:
                    web = None
                    raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
            except (urllib2.URLError, IOError, urllib2.httplib.BadStatusLine) as e:
                print('Conexion Erronea')
                # print(e.reason)
                print(url, e)
                web = None
                logging.debug('Error: %s; Mercado: %s; Url: %s' % (e, mercado.encode('UTF-8'), url.encode('UTF-8')))
                print ('Pausa de %d segundos' % pausareconexion)
                sleep(pausareconexion)

        if ultimapagina == 0:
            busqueda = 'Next</a> | <a href="/q/cp?s=' + (mercado.upper().replace('^', '%5E')) + '&amp;c='
            ultimapaginainicio = web.find(busqueda)
            if ultimapaginainicio == -1:
                ultimapagina = 0
            else:
                ultimapaginainicio = ultimapaginainicio + len(busqueda)
                ultimapaginafinal = web.find('">Last</a></div>', ultimapaginainicio)
                ultimapagina = int(web[ultimapaginainicio:ultimapaginafinal])

        print("Mercado %s Pagina %d de %d" % (mercado, pagina, ultimapagina))

        ticketfin = 0
        while True:
            ticketinicio1 = web.find('<b><a href="/q?s=', ticketfin)
            ticketinicio = ticketinicio1 + len('<b><a href="/q?s=')
            if ticketinicio1 == -1:
                break

            ticketfin = web.find('">', ticketinicio)

            ticket = (web[ticketinicio:ticketfin].strip()).upper()
            # print ticket
            if (ticket not in ticketsanadidos) and ('%20' not in ticket):
                ticketsanadidos.append(ticket)

        duerme()
        pagina += 1
    print('')
    print(("%8d Tickets componen el mercado %s" % (len(ticketsanadidos), mercado)))
    print('')

    return ticketsanadidos


def descargaHistoricoAccion(naccion, **config):
    # global webheaders
    """ Funcion para la descarga de las cotizaciones historicas de una accion.
    Parametros : naccion - nombre de la accion
                fechaini - fecha de inicio
                fechafin - fecha fin
                timming - timming
                actualizar - False/True
    el formato del las fecha debe ser AAAA-MM-DD

    las posiblidades del timming son:   d - 1 -diario
                                        w - 2 - semanal
                                        m - 3 - mensual
                                        v - 4 - muestra dividendos

    el return devuelve o:
        los datos
        que ha habido pago de dividendos
        o que la url no es valida
    """

    naccion = naccion.upper()
    fechaini = config.get('fechaini', None)
    fechafin = config.get('fechafin', None)
    timming = config.get('timming', "d")
    actualizar = config.get('actualizar', False)
    txt = config.get('txt', True)
#    if timming in '1dD':
#        timming = 'd'
#    elif timming in '2wW':
#        timming ='w'
#    elif timming in '4vV':
#        timming = 'v'
#    else:
#        timming ='m'

    if fechafin == None:
        fechafin = ((date.today().timetuple()))
        anofin = str(fechafin[0])
        mesfin = str(fechafin[1])
        diafin = str(fechafin[2])

    else:
        fechafin = fechafin.split('-')
        anofin = (fechafin[0])
        mesfin = (fechafin[1])
        diafin = (fechafin[2])

    mesfin = str(int(mesfin) - 1)
    # La barra de hoy no puede estar "acabada" por eso no se descarga.
    # Si la guardamos y efectivamente no esta acabada, cuando vuelva a descargar los datos
    # y al comprobar la ultima guardada con la primera descargada, no coincidiran y pensara que hay un pago de dividendos
    diafin = str(int(diafin) - 1)
    # comprobandodividendo=False
    if fechaini == None:  # hay un caso en el que nos puede interesar que la funcion cambie el estado de actualizar en el caso de que venga de 'actualizacionDatosHisAccion' con actualizar=True pero con fechaini=None
        actualizar = False
        url = "http://ichart.finance.yahoo.com/table.csv?s=" + naccion + "&d=" + mesfin + "&e=" + diafin + "&f=" + anofin + "&g=" + timming + "&ignore=.csv"
    else:
        fechaini = fechaini.split("-")
        anoini, mesini, diaini = fechaini
        mesini = str(int(mesini) - 1)
        actualizar = True
        url = "http://ichart.finance.yahoo.com/table.csv?s=" + naccion + "&a=" + mesini + "&b=" + diaini + "&c=" + anoini + "&d=" + mesfin + "&e=" + diafin + "&f=" + anofin + "&g=" + timming + "&ignore=.csv"
    f = None
    r = urllib2.Request(url, headers=webheaders)

    punto = naccion.find('.')
    if punto == -1:
        sufijo = ''
    else:
        sufijo = naccion[punto:]

    if sufijo in prefijo:
    # if prefijo.has_key(sufijo):
        preurl = "http://" + prefijo[sufijo] + "finance.yahoo.com/q/hp?s=" + naccion
    else:
        preurl = "http://finance.yahoo.com/q/hp?s=" + naccion
        logging.debug('Error: Falta relacion Prefijo-Sufijo; Sufijo: %s' % sufijo)

    r.add_header('Referer', preurl)

    # abrimos la pagina donde esta la informacion de las cotizaciones historicos del pais al que le corresponde la accion
    # la abrimos para hacerle creer que venimos de aqui
    # hemos observado casos donde hasta que no entrabamos en esta pagina no actualizaba correctamente la informacion en el archivo que nos descargamos posteriormente
    r1 = urllib2.Request(preurl, headers=webheaders)
    try:
        urllib2.urlopen(r1)
    except:
        pass
    duerme(tiempo=1000)

    while f == None:
        try:
            f = urllib2.urlopen(r)
            print (url)
        except urllib2.HTTPError as e:
            print(e.code)
            print('Url invalida, accion no disponible')
            print(url)
            f = None
            return 'URL invalida'
        except (urllib2.URLError, IOError, urllib2.httplib.BadStatusLine) as e:
            print('Conexion Perdida')
            # print(e.reason)
            print(url, e)
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, naccion.encode('UTF-8'), url.encode('UTF-8')))
            f = None
            print ('Pausa de %d segundos' % pausareconexion)
            sleep(pausareconexion)

            # cuando la conexion se pierde, pasa por aqui, dando como error
            # [Errno 11004] getaddrinfo failed
#        except IOError as e:
#            print('Conexion Erronea')
#            print(url, e)
#            f = None
#            sleep (pausareconexion)
#            print ('Pausa de %d segundos' % pausareconexion)

    lineas = f.readlines()
    f.close()
    if not (lineas[0] == "Date,Open,High,Low,Close,Volume,Adj Close\n"):
        print('Informacion invalida, accion no disponible')
        return 'URL invalida'
# en la mayoria de los casos, en la web el historico existe, pero la descarga del archivo no, la accion ha desaparecido y yahoo elimina el archivo sin eliminar en la web el historico

    datosaccion = BBDD.datoshistoricoslee(naccion)

    if actualizar:
        penultimoregistro = len(datosaccion) - 2
        del datosaccion[penultimoregistro:]
    else:
        datosaccion = []

    i = len(lineas) - 1
    print(('%d Registros de la accion' % i))
    while i > 0:
        linea_datos = lineas[i]
        columnas = linea_datos.split(",")
        # tengo que probar a sustituir los float por la funcion Decimal
        fecha = str(columnas[0])
        apertura = float(columnas[1])
        maximo = float(columnas[2])
        minimo = float(columnas[3])
        cierre = float(columnas[4])
        volumen = int(columnas[5])
        cierreajustado = float(columnas[6])

        if cierre == 0.0 or apertura == 0.0 or cierreajustado == 0.0:  # tenemos en cuenta que cierre sea 0 en ese caso no podriamos hacer la division de ajuste
            aperturaajustado = 0.0
        else:
            aperturaajustado = round(apertura * (cierreajustado / cierre), 3)

        if cierre == 0.0 or maximo == 0.0 or cierreajustado == 0.0:
            maximoajustado = 0.0
        else:
            maximoajustado = round(maximo * (cierreajustado / cierre), 3)

        if cierre == 0.0 or minimo == 0.0 or cierreajustado == 0.0:
            minimoajustado = 0.0
        else:
            minimoajustado = round(minimo * (cierreajustado / cierre), 3)

        cierreajustado = round(cierreajustado, 3)

        # hacemos esto para que no hayan datos a cero, eliminando en el caso de que algun dato llege a cero todo la lista de datos anterior al dato donde es cero
# #        if aperturaajustado == 0.0 or maximoajustado == 0.0 or minimoajustado == 0.0 or cierreajustado == 0.0:
# #            datosaccion = []
# #        else:

        if actualizar:
            registrodescargadoprimero = (fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado)
            if len(datosaccion) > 1:
                registroalmacenadoultimo = datosaccion[-1][0:5]  # no queremos comparar el volumen
            else:
                registroalmacenadoultimo = ('0000-00-00', 0.0, 0.0, 0.0, 0.0)

            actualizar = False
            if (registroalmacenadoultimo != registrodescargadoprimero):
                print('El historico ha cambiado por el pago de un dividendo, hay que hacer una descarga completa nueva')
                # print 'Borrando todos los datos almacenados'
                # borraTicket(naccion, BBDD=False)
                return 'Pago Dividendos'

        else:
            datosaccion.append((fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado, volumen))

        i -= 1

    BBDD.datoshistoricosgraba(naccion, datosaccion)

    if txt:
        nombre = (str(naccion)).replace('.', '_')
        archivo = os.path.join(os.getcwd(), carpetas['Historicos'], nombre + '.' + timming + '.csv')
        j = open(archivo, 'w')
        writercsv = csv.writer(j, delimiter=';', lineterminator='\n', doublequote=True)
        for n in datosaccion:

            fecha, apertura, maximo, minimo, cierre, volumen = n
            apertura = str(apertura).replace('.', ',')
            maximo = str(maximo).replace('.', ',')
            minimo = str(minimo).replace('.', ',')
            cierre = str(cierre).replace('.', ',')
            volumen = str(volumen).replace('.', ',')

            n = (fecha, apertura, maximo, minimo, cierre, volumen)

            writercsv.writerow(n)
            # j.write(str(n)+'\n')
        j.close()
    return datosaccion


def cotizacionesTicket(nombreticket):
    """

    """
    nombreticket = nombreticket.upper()
    # habilitar en la funcion la posibilidad de descargar multiples tickets, tienen que ir separados o unidos por '+'
    # Tendriamos que separar nombreticket con un split y obtener una lista, comprobar la longitud de la misma, hacer la descarga, leer las lineas, comparar la lista inicial con la lista obtenida, crear un bucle en el else despues del try de la conxion en el que actualiza la BBDD

    urldatos = "http://download.finance.yahoo.com/d/quotes.csv?s=" + nombreticket + "&f=nsxkhjgl1a2ve1&e=.csv"
    datosurl = None
    r = urllib2.Request(urldatos, headers=webheaders)

    punto = nombreticket.find('.')
    if punto == -1:
        sufijo = ''
    else:
        sufijo = nombreticket[punto:]
    if sufijo in prefijo:
    # if prefijo.has_key(sufijo):
        r.add_header('Referer', "http://" + prefijo[sufijo] + "finance.yahoo.com/q/hp?s=" + nombreticket)
    else:
        logging.debug('Error: Falta relacion Prefijo-Sufijo; Sufijo: %s' % sufijo)

    while datosurl == None:
        try:
            f = urllib2.urlopen(r)
            datosurl = ((f.read().strip()).replace(',N/A', ',NULL')).decode('UTF-8')  # UTF-16le
            f.close()
        except urllib2.HTTPError as e:
            print('Conexion Perdida')
            print(e.code)
            datosurl = None
            raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
        except (urllib2.URLError, IOError, urllib2.httplib.BadStatusLine) as e:
            print('Conexion Erronea')
            print(e)
            datosurl = None
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, nombreticket.encode('UTF-8'), urldatos.encode('UTF-8')))
            print ('Pausa de %d segundos' % pausareconexion)
            sleep(pausareconexion)
            # raw_input( 'Pulsa una tecla cuando este reestablecida la conexion para continuar' )
#        except IOError as e:
#            print('Conexion Erronea')
#            print(e)
#            datosurl = None
#            sleep (pausareconexion)
#            print ('Pausa de %d segundos' % pausareconexion)
#            #raw_input( 'Pulsa una tecla cuando este reestablecida la conexion para continuar' )
    # FIXME: crear exclusion con una condicion para los tickets .MC que ademas contengan en la informacion descargada "No such ticker symbol.", leyendo la informacion de la web
    # los tickets con sufijo .MC estan contestando asi u'"BBVA.MC","BBVA.MC","N/A",NULL,NULL,NULL,NULL,0.00,0,NULL,"No such ticker symbol. <a href="/l">Try Symbol Lookup</a> (Look up: <a href="/l?s=BBVA.MC">BBVA.MC</a>)"'
    if sufijo in mercadosfail and \
       ',"N/A",NULL,NULL,NULL,NULL,0.00,0,NULL,"No such ticker symbol. <a href="/l">Try Symbol Lookup</a> (Look up: <a href="/l?s=' in datosurl and \
       __name__ != '__main__':
        datosurl = cotizacionesTicketWeb(nombreticket)

    if __name__ != '__main__':
        BBDD.ticketcotizaciones(nombreticket, datosurl)

    return datosurl


def cotizacionesTicketWeb(nombreticket):
    """
    >>> nombreticket='AAPL'
    >>> len(cotizacionesTicketWeb(nombreticket))==len(cotizacionesTicket(nombreticket))
    True
    """
    nombreticket = nombreticket.upper()
    # habilitar en la funcion la posibilidad de descargar multiples tickets, tienen que ir separados o unidos por '+'
    # Tendriamos que separar nombreticket con un split y obtener una lista, comprobar la longitud de la misma, hacer la descarga, leer las lineas, comparar la lista inicial con la lista obtenida, crear un bucle en el else despues del try de la conxion en el que actualiza la BBDD

    web = None
    error = 'N/A'
    punto = nombreticket.find('.')
    if punto == -1:
        sufijo = ''
    else:
        sufijo = nombreticket[punto:]
    if sufijo in prefijo:
    # if prefijo.has_key(sufijo):
        urldatos = "http://" + prefijo[sufijo] + "finance.yahoo.com/q?s=" + nombreticket
    else:
        urldatos = "http://finance.yahoo.com/q?s=" + nombreticket

    r = urllib2.Request(urldatos, headers=webheaders)

    while web == None:
        try:
            f = urllib2.urlopen(r)
            web = f.read().decode('UTF-8')
            f.close()
        except urllib2.HTTPError as e:
            print('Conexion Perdida')
            print(e.code)
            web = None
            raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
        except (urllib2.URLError, IOError, urllib2.httplib.BadStatusLine) as e:
            print('Conexion Erronea')
            print(e)
            web = None
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, nombreticket.encode('UTF-8'), urldatos.encode('UTF-8')))
            print ('Pausa de %d segundos' % pausareconexion)
            sleep(pausareconexion)
    # datonombre, datoticket, datomercado, datomax52, datomaxDia, datomin52, datominDia, datoValorActual, datovolumenMedio, datovolumen, datoerror
    # "Apple Inc.","AAPL","NasdaqNM",705.07,N/A,419.00,N/A,431.144,20480200,6870,"N/A"

    inicio = web.find('<div class="yfi_rt_quote_summary"><div class="hd"><div class="title"><h2>') + len('<div class="yfi_rt_quote_summary"><div class="hd"><div class="title"><h2>')
    fin = web.find('</h2> <span class="rtq_exch">', inicio) - len(nombreticket) - 2
    datonombre = web[inicio:fin].strip()

    inicio = web.find('<span class="rtq_dash">-</span>', fin) + len('<span class="rtq_dash">-</span>')
    fin = web.find(' ', inicio)
    datomercado = web[inicio:fin].strip()

    inicio = web.find('<span id="yfs_l84_' + nombreticket.lower() + '">') + len('<span id="yfs_l84_' + nombreticket.lower() + '">')
    fin = web.find('</span></span>', inicio)
    try:
        datoValorActual = float(web[inicio:fin].replace(',', '.'))
    except ValueError:
        datoValorActual = 'NULL'
        error = 'No such ticker symbol.'

    # Con el mercado abierto este datos es correcto buscarlo asi
    # FIXME: Con el mercado cerrado este datos es <td class="yfnc_tabledata1"><span>N/A</span> - <span>N/A</span>
    inicio = web.find('<span id="yfs_g53_' + nombreticket.lower() + '">') + len('<span id="yfs_g53_' + nombreticket.lower() + '">')
    fin = web.find('</span></span>', inicio)
    try:
        datominDia = round(float(web[inicio:fin].replace(',', '.')),3)  # FIXME: Este dato puede se N/A, no siendo posible la conversion a float
    except ValueError:
        datominDia = 'NULL'
    inicio = web.find('<span id="yfs_h53_' + nombreticket.lower() + '">') + len('<span id="yfs_h53_' + nombreticket.lower() + '">')
    fin = web.find('</span></span>', inicio)
    try:
        datomaxDia = round(float(web[inicio:fin].replace(',', '.')),3)  # FIXME: Este dato puede se N/A, no siendo posible la conversion a float
    except ValueError:
        datomaxDia = 'NULL'
        inicio = web.find('</th><td class="yfnc_tabledata1"><span>')+len('</th><td class="yfnc_tabledata1"><span>')
    
    inicio = web.find('<td class="yfnc_tabledata1"><span>', inicio) + len('<td class="yfnc_tabledata1"><span>')
    fin = web.find('</span> - <span>', inicio)
    try:
        datomin52 = round(float(web[inicio:fin].replace(',', '.')),3)
    except ValueError:
        datomin52 = 'NULL'
    inicio = fin + len('</span> - <span>')
    fin = web.find('</span></td></tr><tr><th scope="row" width="48%">', inicio)
    try:
        datomax52 = round(float(web[inicio:fin].replace(',', '.')),3)
    except ValueError:
        datomax52 = 'NULL'

    inicio = web.find('<span id="yfs_v53_' + nombreticket.lower() + '">') + len('<span id="yfs_v53_' + nombreticket.lower() + '">')
    fin = web.find('</span></td></tr><tr><th', inicio)
    try:
        datovolumen = int((web[inicio:fin].replace(',', '')).replace('.', ''))
    except ValueError:
        datovolumen = 'NULL'
		
    inicio = web.find('(3m)</span>:</th><td class="yfnc_tabledata1">') + len('(3m)</span>:</th><td class="yfnc_tabledata1">')
    fin = web.find('</td></tr><tr><th scope="row" width="48%">', inicio)
    try:
        datovolumenMedio = int((web[inicio:fin].replace(',', '')).replace('.', ''))
    except ValueError:
        datovolumenMedio = 'NULL'

    datosurl = u'"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s"'%(datonombre, nombreticket, datomercado, str(datomax52), str(datomaxDia), str(datomin52), str(datominDia), str(datoValorActual), str(datovolumenMedio), str(datovolumen), error)
    return datosurl


def cotizacionesMoneda(nombreticket):
    """

    """
    nombreticket = nombreticket.upper()
    urldatos = "http://download.finance.yahoo.com/d/quotes.csv?s=" + nombreticket + "&f=sl1e1&e=.csv"
    datosurl = None
    r = urllib2.Request(urldatos, headers=webheaders)

# #    punto = nombreticket.find('.')
# #    if punto == -1:
# #        sufijo = ''
# #    else:
# #        sufijo = nombreticket[punto:]
# #    r.add_header('Referer', "http://" + prefijo[sufijo] + "finance.yahoo.com/q/hp?s=" + nombreticket)

    while datosurl == None:
        try:
            f = urllib2.urlopen(r)
            # f= urllib.urlopen (urldatos)
            datosurl = ((f.read().strip()).replace(',N/A', ',NULL')).decode('UTF-8')  # UTF-16le
            f.close()
        except urllib2.HTTPError as e:
            print('Conexion Perdida')
            print(e.code)
            datosurl = None
            raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
        except (urllib2.URLError, IOError, urllib2.httplib.BadStatusLine) as e:
            print('Conexion Erronea')
            # print(e.reason)
            print(e)
            datosurl = None
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, nombreticket.encode('UTF-8'), urldatos.encode('UTF-8')))
            print ('Pausa de %d segundos' % pausareconexion)
            sleep(pausareconexion)

    BBDD.monedacotizaciones(nombreticket, datosurl)
    return datosurl


def subirtimming(datos, **config):
    '''
    Pasa un timming inferior a uno superior, el orden seria diario, semana y mensual

    >>> historicoDiario = [('2010-02-01', 20.7, 20.7, 19.6, 19.65, 165900), ('2010-02-02', 19.51, 19.98, 19.51, 19.6, 148000), ('2010-02-03', 19.6, 19.71, 19.3, 19.3, 226500), ('2010-02-04', 19.26, 19.48, 18.5, 18.5, 16900), ('2010-02-05', 18.5, 18.5, 17.5, 18.08, 238900), ('2010-02-08', 19.82, 19.82, 17.4, 18.9, 131900), ('2010-02-09', 19.49, 19.69, 18.05, 18.22, 618500), ('2010-02-10', 18.4, 19.75, 16.35, 17.5, 4991800), ('2010-02-11', 17.55, 18.45, 17.11, 17.72, 4494800), ('2010-02-12', 17.35, 20.25, 17.34, 19.76, 3526300), ('2010-02-16', 20.0, 20.24, 19.25, 20.0, 1223500), ('2010-02-17', 20.2, 20.2, 19.5, 19.87, 1026300), ('2010-02-18', 19.25, 19.78, 19.05, 19.69, 1680500), ('2010-02-19', 19.56, 19.67, 19.4, 19.5, 1230600), ('2010-02-22', 19.16, 19.59, 19.0, 19.33, 703900), ('2010-02-23', 19.33, 19.33, 18.92, 18.95, 1126800), ('2010-02-24', 18.72, 19.32, 18.62, 18.97, 832300), ('2010-02-25', 18.55, 19.66, 18.4, 19.28, 574400), ('2010-02-26', 19.17, 20.76, 18.75, 19.5, 1687900), ('2010-03-01', 19.63, 20.28, 19.6, 20.25, 766500), ('2010-03-02', 20.07, 20.53, 20.0, 20.5, 538000), ('2010-03-03', 20.18, 20.52, 20.02, 20.32, 563700), ('2010-03-04', 20.23, 20.4, 19.84, 19.96, 629100), ('2010-03-05', 20.09, 20.09, 19.3, 19.6, 440700), ('2010-03-08', 19.57, 20.0, 19.48, 19.5, 183800), ('2010-03-09', 19.37, 19.79, 19.25, 19.37, 263100), ('2010-03-10', 19.3, 19.3, 18.93, 18.99, 561200), ('2010-03-11', 18.91, 19.27, 18.75, 18.89, 595000), ('2010-03-12', 18.91, 19.77, 18.91, 19.4, 617400), ('2010-03-15', 19.4, 19.4, 18.77, 18.98, 388700), ('2010-03-16', 18.62, 19.6, 18.62, 19.51, 274400), ('2010-03-17', 19.6, 20.14, 19.32, 20.03, 322000), ('2010-03-18', 19.88, 20.65, 19.81, 20.06, 464600), ('2010-03-19', 20.22, 20.25, 19.88, 20.08, 346300), ('2010-03-22', 19.95, 20.23, 19.95, 20.11, 256800), ('2010-03-23', 20.17, 21.18, 20.1, 20.99, 498900), ('2010-03-24', 20.86, 20.91, 20.45, 20.83, 475000), ('2010-03-25', 20.85, 21.99, 20.8, 21.58, 838600), ('2010-03-26', 21.64, 22.09, 21.39, 22.0, 832400), ('2010-03-29', 22.0, 22.0, 21.53, 21.9, 149200), ('2010-03-30', 21.8, 22.04, 21.6, 21.91, 189500), ('2010-03-31', 21.84, 21.84, 21.58, 21.73, 311100), ('2010-04-01', 21.79, 22.08, 21.46, 21.81, 248900), ('2010-04-05', 21.71, 21.89, 21.45, 21.79, 517500), ('2010-04-06', 21.66, 22.12, 21.48, 22.06, 1717000), ('2010-04-07', 21.93, 22.1, 21.68, 22.02, 360900), ('2010-04-08', 21.89, 22.2, 21.74, 22.03, 303300), ('2010-04-09', 21.99, 22.23, 21.85, 22.16, 220700), ('2010-04-12', 22.22, 22.56, 21.91, 22.33, 222100), ('2010-04-13', 22.43, 22.71, 21.69, 21.9, 605600), ('2010-04-14', 21.86, 22.21, 21.86, 21.99, 507300), ('2010-04-15', 21.89, 22.0, 21.87, 21.98, 104600), ('2010-04-16', 21.9, 21.96, 21.41, 21.81, 373400), ('2010-04-19', 21.85, 21.93, 21.63, 21.83, 190000), ('2010-04-20', 21.96, 22.25, 21.78, 21.92, 311900), ('2010-04-21', 21.88, 22.0, 21.68, 21.93, 204300), ('2010-04-22', 21.73, 21.81, 21.57, 21.68, 94400), ('2010-04-23', 21.58, 21.71, 21.38, 21.59, 143000), ('2010-04-26', 21.46, 21.92, 21.46, 21.67, 70500), ('2010-04-27', 21.54, 21.6, 21.27, 21.38, 189300), ('2010-04-28', 21.38, 21.5, 20.54, 20.95, 551400), ('2010-04-29', 21.01, 21.09, 20.7, 21.0, 628400), ('2010-04-30', 21.08, 21.08, 20.59, 20.75, 324100), ('2010-05-03', 20.7, 20.88, 20.48, 20.76, 412900), ('2010-05-04', 20.56, 20.56, 20.12, 20.44, 272300), ('2010-05-05', 20.32, 20.32, 19.86, 19.96, 259300), ('2010-05-06', 19.85, 20.1, 18.7, 19.5, 395800), ('2010-05-07', 19.56, 21.43, 19.55, 20.32, 1211800), ('2010-05-10', 20.94, 21.2, 20.35, 21.15, 232000), ('2010-05-11', 20.98, 21.75, 20.88, 21.7, 262600), ('2010-05-12', 21.7, 22.33, 21.66, 22.08, 295000), ('2010-05-13', 22.19, 22.31, 22.0, 22.14, 437800), ('2010-05-14', 22.05, 22.19, 21.76, 22.0, 252800), ('2010-05-17', 22.0, 22.56, 21.84, 22.03, 245900), ('2010-05-18', 22.09, 22.54, 21.85, 21.89, 223300), ('2010-05-19', 21.81, 21.96, 21.4, 21.83, 180000), ('2010-05-20', 21.43, 21.56, 20.6, 20.69, 494800), ('2010-05-21', 20.47, 20.9, 20.1, 20.9, 369700), ('2010-05-24', 20.78, 21.0, 20.5, 20.77, 300400), ('2010-05-25', 20.5, 20.6, 20.22, 20.29, 582400), ('2010-05-26', 20.42, 21.02, 20.24, 20.26, 273200), ('2010-05-27', 20.41, 21.09, 20.26, 21.03, 304300), ('2010-05-28', 20.85, 21.31, 20.8, 21.07, 125700), ('2010-06-01', 21.04, 21.51, 20.8, 21.01, 214900), ('2010-06-02', 21.09, 21.44, 20.86, 21.13, 60900), ('2010-06-03', 21.27, 21.4, 20.8, 21.04, 141300), ('2010-06-04', 20.6, 21.08, 20.0, 20.0, 206900), ('2010-06-07', 20.0, 20.2, 19.54, 19.71, 173200), ('2010-06-08', 19.71, 19.79, 18.93, 19.17, 680800), ('2010-06-09', 19.22, 19.73, 19.0, 19.39, 245100), ('2010-06-10', 19.57, 20.01, 19.52, 20.0, 192800), ('2010-06-11', 19.87, 20.51, 19.42, 20.48, 76600), ('2010-06-14', 20.51, 21.49, 20.49, 20.75, 175600), ('2010-06-15', 20.88, 21.15, 20.24, 21.05, 84000), ('2010-06-16', 20.87, 21.35, 20.86, 21.23, 89200), ('2010-06-17', 21.4, 21.57, 20.89, 21.46, 74600), ('2010-06-18', 21.45, 21.54, 21.31, 21.48, 135400), ('2010-06-21', 21.65, 21.99, 21.28, 21.34, 244800), ('2010-06-22', 21.32, 21.5, 20.53, 20.75, 246300), ('2010-06-23', 20.68, 20.88, 20.31, 20.54, 106700), ('2010-06-24', 20.4, 20.6, 20.0, 20.04, 77700), ('2010-06-25', 20.21, 20.25, 19.5, 20.01, 747000), ('2010-06-28', 19.96, 20.26, 19.56, 20.12, 156100), ('2010-06-29', 19.87, 20.93, 19.4, 19.9, 369700), ('2010-06-30', 19.95, 20.57, 19.62, 19.67, 393900), ('2010-07-01', 19.73, 20.12, 19.29, 20.12, 364900), ('2010-07-02', 20.29, 20.29, 19.73, 20.03, 162000), ('2010-07-06', 20.38, 21.2, 19.9, 20.27, 254200), ('2010-07-07', 20.66, 21.91, 20.23, 21.57, 1712900), ('2010-07-08', 20.96, 20.96, 20.1, 20.38, 2556300), ('2010-07-09', 19.61, 19.9, 19.33, 19.44, 1257300), ('2010-07-12', 19.47, 19.6, 19.1, 19.4, 287700), ('2010-07-13', 19.46, 19.65, 19.3, 19.56, 286400), ('2010-07-14', 19.45, 19.73, 19.25, 19.56, 272800), ('2010-07-15', 19.62, 19.62, 19.22, 19.26, 270200), ('2010-07-16', 19.16, 19.16, 18.79, 18.79, 358900), ('2010-07-19', 18.88, 19.06, 18.75, 18.78, 361900), ('2010-07-20', 18.68, 18.85, 18.41, 18.82, 441900), ('2010-07-21', 18.82, 19.07, 18.73, 18.98, 374000), ('2010-07-22', 19.07, 19.11, 18.39, 19.0, 212700), ('2010-07-23', 18.93, 19.54, 18.89, 19.34, 226300), ('2010-07-26', 19.35, 19.35, 18.87, 19.0, 793600), ('2010-07-27', 19.01, 19.2, 18.78, 18.87, 317600), ('2010-07-28', 18.85, 19.07, 18.84, 19.02, 235600), ('2010-07-29', 19.07, 19.25, 18.92, 19.04, 143700), ('2010-07-30', 18.9, 19.29, 18.76, 19.24, 208300)]
    >>> historicoSemanal = [('2010-02-01', 20.7, 20.7, 17.5, 18.08, 159200), ('2010-02-08', 19.82, 20.25, 16.35, 19.76, 2752600), ('2010-02-16', 20.0, 20.24, 19.05, 19.5, 1290200), ('2010-02-22', 19.16, 20.76, 18.4, 19.5, 985000), ('2010-03-01', 19.63, 20.53, 19.3, 19.6, 587600), ('2010-03-08', 19.57, 20.0, 18.75, 19.4, 444100), ('2010-03-15', 19.4, 20.65, 18.62, 20.08, 359200), ('2010-03-22', 19.95, 22.09, 19.95, 22.0, 580300), ('2010-03-29', 22.0, 22.08, 21.46, 21.81, 224600), ('2010-04-05', 21.71, 22.23, 21.45, 22.16, 623800), ('2010-04-12', 22.22, 22.71, 21.41, 21.81, 362600), ('2010-04-19', 21.85, 22.25, 21.38, 21.59, 188700), ('2010-04-26', 21.46, 21.92, 20.54, 20.75, 352700), ('2010-05-03', 20.7, 21.43, 18.7, 20.32, 510400), ('2010-05-10', 20.94, 22.33, 20.35, 22.0, 296000), ('2010-05-17', 22.0, 22.56, 20.1, 20.9, 302700), ('2010-05-24', 20.78, 21.31, 20.22, 21.07, 317200), ('2010-06-01', 21.04, 21.51, 20.0, 20.0, 156000), ('2010-06-07', 20.0, 20.51, 18.93, 20.48, 273700), ('2010-06-14', 20.51, 21.57, 20.24, 21.48, 111700), ('2010-06-21', 21.65, 21.99, 19.5, 20.01, 284500), ('2010-06-28', 19.96, 20.93, 19.29, 20.03, 289300), ('2010-07-06', 20.38, 21.91, 19.33, 19.44, 1445100), ('2010-07-12', 19.47, 19.73, 18.79, 18.79, 295200), ('2010-07-19', 18.88, 19.54, 18.39, 19.34, 323300), ('2010-07-26', 19.35, 19.35, 18.76, 19.24, 339700)]
    >>> historicoMensual = [('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400)]
    >>> historicoMensual2 = subirtimming(historicoDiario, timming='m')
    >>> historicoSemanal2 = subirtimming(historicoDiario, timming='w')
    >>> historicoSemanal=[(n[:5]) for n in historicoSemanal]
    >>> historicoMensual=[(n[:5]) for n in historicoMensual]
    >>> historicoSemanal2=[(n[:5]) for n in historicoSemanal2]
    >>> historicoMensual2=[(n[:5]) for n in historicoMensual2]
    >>> historicoSemanal==historicoSemanal2
    True
    >>> historicoMensual==historicoMensual2
    True
    '''
    timming = (config.get('timming', 'm')).lower()
    datostimming = []

    fechadatos = 0
    aperturadatos = 1
    maximodatos = 2
    minimodatos = 3
    cierredatos = 4
    volumendatos = 5

    inicio = 0
    if len(datos) > 0:
        if timming == 'm':
            # %Y     Year with century as a decimal number.
            # %m     Month as a decimal number [01,12].
            fechaagr = strftime('%Y, %m', strptime(datos[0][fechadatos], '%Y-%m-%d'))
        elif timming == 'w':
            # %w     Weekday as a decimal number [0(Sunday),6].
            # el siguiente domigo a la fecha de inico
            fechaagr = map(int, (((datos[0][fechadatos]).split('-'))))
            fechaagr = (date(fechaagr[0], fechaagr[1], fechaagr[2]))
            fechaagr += timedelta(days=6 - fechaagr.weekday())

        i = 0
        while i < len(datos):
            fecha = datos[i][fechadatos]
            fecha = strptime(fecha, '%Y-%m-%d')
# FIXME : en mensual es correcto, cuando cambia de ANO y MES, pero en semanal hay que acumular de domingo a domingo, siendo el corte el domingo siguiente
            if (timming == 'm' and fechaagr != strftime('%Y, %m', fecha)) or (timming == 'w' and datos[i][fechadatos] >= str(fechaagr)):
                if timming == 'm':
                    fechaagr = strftime('%Y, %m', fecha)
                elif timming == 'w':
                    fechaagr = map(int, (((datos[i][fechadatos]).split('-'))))
                    fechaagr = (date(fechaagr[0], fechaagr[1], fechaagr[2]))
                    fechaagr += timedelta(days=6 - fechaagr.weekday())

                maximo = max([(n[maximodatos]) for n in datos][inicio:i])
                minimo = min([(n[minimodatos]) for n in datos][inicio:i])
                # al generar los timmings hicimos que acumulase el volumen en vez de promediarlo como lo teniamos anteriormente
                volumen = sum([(n[volumendatos]) for n in datos][inicio:i]) / len([(n[volumendatos]) for n in datos][inicio:i])

                datostimming.append((datos[inicio][fechadatos], datos[inicio][aperturadatos], maximo, minimo, datos[i - 1][cierredatos], volumen))
                inicio = i
            i += 1

        maximo = max([(n[maximodatos]) for n in datos][inicio:i])
        minimo = min([(n[minimodatos]) for n in datos][inicio:i])
        # al generar los timmings hicimos que acumulase el volumen en vez de promediarlo como lo teniamos anteriormente
        volumen = sum([(n[volumendatos]) for n in datos][inicio:i]) / len([(n[volumendatos]) for n in datos][inicio:i])
        datostimming.append((datos[inicio][fechadatos], datos[inicio][aperturadatos], maximo, minimo, datos[-1][cierredatos], volumen))

    return datostimming


if __name__ == '__main__':
    _test()
