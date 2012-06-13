# -*- coding: UTF-8 -*-


############################################################
# modulos estandar importados

#import urllib
import urllib2
try:
    from pysqlite2 import dbapi2 as sqlite3
except ImportError:
    print ('Modulo de pysqlite2 deshabilitado. Cargando sqlite3 nativo')
    import sqlite3
from datetime import date, datetime, timedelta
from time import sleep
#from adodbapi.adodbapi import type
try:
    import cPickle as pickle
except ImportError:
    print ('Modulo cPickle deshabilitado')
    import pickle   # TODO: buscar la manera de comprimir los datos para que ocupen menos en el HD.
    # una posiblidad es utilizar el modulo zlib zlib.compress(datos) zlib.descompress(datos)
import os
#import wx
from random import randint
import glob
import csv
from collections import deque
import logging
#import traceback
#from decimal import Decimal
#import sys
#import locale

#################################################
setdefaultencoding = ('UTF-8')
#sys.setdefaultencoding('UTF-8')
#locale.setlocale(locale.LC_ALL, "")


##########################
# Constantes locales
sufijosexcluidos = ('.BA', '.BC', '.BE', '.BI', '.BM', '.BO', '.CBT', '.CME', '.CMX', '.DU', '.EX', '.F', '.HA', '.HM', '.JK', '.KL', '.KQ', '.KS', '.MA',
                    '.MF', '.MU', '.MX', '.NS', '.NYB', '.NYM', '.NZ', '.SA', '.SG', '.SI', '.SN', '.SS', '.SZ', '.TA', '.TW', '.TWO', '.VA',)
webheaders = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko/20100101 Firefox/11.0' }
carpetas = {'Analisis':'Analisis', 'Backtest':'Backtest', 'Datos':'Datos', 'Historicos':'Historicos', 'Log':'Log', 'Graficos': 'amstock'}
difregactualizar = {'d':10, 'w':15, 'm':33, 'noActualizados':120}# Expresa la diferencia entre los registros para hacer una actualizacion
pausareconexion = 20
backtestoperacionessospechosas = 1.50



#import logging.config
ARCHIVO_LOG = os.path.join(os.getcwd(), carpetas['Log'], "general.log")
#CONFIG_LOG = os.path.join(os.getcwd(), carpetas['Log'], "logging.conf")

#logging.config.fileConfig(CONFIG_LOG)
#logging.basicConfig(filename = ARCHIVO_LOG)
#logging.captureWarnings(True)
#basic setup with ISO 8601 time format
logging.basicConfig(filename = ARCHIVO_LOG, format = '%(asctime)sZ; nivel: %(levelname)s; modulo: %(module)s; Funcion : %(funcName)s; %(message)s', level = logging.DEBUG)
logging.debug('\n')
logging.debug('Inicio de Aplicacion')
#logging.basicConfig(filename='/tmp/test.log', , level=logging.INFO)
# switch to UTC / GMT
#logging.Formatter.converter = time.gmtime
#logging.info('blah blah')
#logging.debug('you won\'t see this')
# change the logging level
#logging.getLogger().setLevel(logging.DEBUG)
#logging.debug('you should see this')

############################################################
# modulos propios importados


############################################################
# comprobaciones especiales

#assert

# Buscar tickets duplicados en la BBDD
# SELECT `tiket`, count(*) FROM `componentes` GROUP BY `tiket` HAVING count(*) > 1

# Lista de los distintos mercados a los que pertenecen los tickets y cantidad de tickets para cada uno de ellos
# SELECT `mercado`, count(*) FROM `componentes` GROUP BY `mercado` HAVING count(*) > 0

# Buscar tikets a las que les falte relacion entre mercados y monedas
# SELECT `tiket`,`mercado` FROM `componentes` where `mercado` not in (SELECT `nombreUrl` FROM `mercado_moneda`)

#Cualquier rentabilidad positiva dividido por 1, esa rentabilidad te dara la negativa y al reves 1- la rentabilidad negativa dividido por esa negativa te da la positiva
#35 dividido por 1,35 te da 25,925 y al reves 1- 0,25925 =0,7407. Que si lo dividimos por el nos da 35.       25,925/0.7407=35
# rentabilidadnegativa= - (rentabilidadpositiva / (1+rentabilidadpositiva))
# rentabilidadpositiva= 1-(rentabilidadnegativa / (1-rentabilidadnegativa))


############################################################
# definicion de funciones

def _test():
    import doctest
    doctest.testmod()
    #TODO: implementar pruebas doctest
    # ejemplos en : http://mundogeek.net/archivos/2008/09/17/pruebas-en-python/  http://magmax9.blogspot.com.es/2011/09/python-como-hacer-pruebas-1.html
    #Externalizar los test
    #doctest.testfile('example2.txt')

def ExistenDatos(naccion):
    """
    
    """
    tickets = obtenTicketsBBDD(naccion)
    naccion = naccion.upper()
    if naccion in tickets:
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), carpetas['Datos'], nombre + ".pck")

        if os.path.exists(archivo):
            return True
        else:
            print('No existe historico descargado')
            #errorenTicket( naccion )# no nos interesa guardar el error cuando la razon es que no existe el historico
            return False
    else:
        print ('No existe informacion de cotizaciones en BBDD')
        #borraTicket (ticket, BBDD=False) # No tiene sentido que intente borrar los archivos, no exista tickets en el diccionario y no puedo componer el nombre de los archivos
        errorenTicket(naccion)
        return False


def LeeDatos(naccion):
    """
    
    """
    naccion = naccion.upper()
    tickets = obtenTicketsBBDD(naccion)
    if naccion in tickets:
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), carpetas['Datos'], nombre + ".pck")

        historicoMensual = []
        historicoSemanal = []
        historicoDiario = []
        correcciones = {}

        if os.path.exists(archivo):
            archivo = file(archivo)
            #f = open(archivo, "r")
            #codificado = f.read()
            #f.close()
            try:
                #datos = pickle.Unpickler(archivo)
                datos = pickle.load(archivo)
                #datos = pickle.loads(codificado)
            except (KeyError, EOFError, pickle.UnpicklingError) as e:# no entiendo porque, pero hay archivos de historicos que estan completamente en blanco, aunque ocupan como si no, la cosa es que cuando descodifico los datos con pickle me da un KeyError: '\x00', esta excepcion sirve para controlar esto
                archivo.close()
                borraTicket (naccion, BBDD = False, codigo = False)# Borramos solo los archivos
                errorenTicket(naccion)
                #sys.excepthook = lambda exc_type, exc_value, exc_traceback: logging.debug('UNCAUGHT EXCEPTION %r: %s' % (exc_type, traceback.format_tb(exc_traceback)))
                logging.debug('Error: %s; Accion: %s; Funcion LeeDatos al utilizar pickle, Archivo: %s' % (e, naccion.encode('UTF-8'), archivo))
                #log(nombrelog = 'LeeDatos', error = KeyError, explicacion = 'Accion; archivo', variables = ('Funcion LeeDatos al utilizar pickle', naccion, archivo))
#            except EOFError:# no entiendo porque, pero hay archivos de historicos que estan completamente en blanco, aunque ocupan como si no, la cosa es que cuando descodifico los datos con pickle me da un KeyError: '\x00', esta excepcion sirve para controlar esto
#                archivo.close()
#                borraTicket (naccion, BBDD = False, codigo = False)# Borramos solo los archivos
#                errorenTicket(naccion)
#                #sys.excepthook = lambda exc_type, exc_value, exc_traceback: logging.debug('UNCAUGHT EXCEPTION %r: %s' % (exc_type, traceback.format_tb(exc_traceback)))
#                logging.debug( Error: %s; Accion: %s; Funcion LeeDatos al utilizar pickle, Archivo: %s' % (__name__, EOFError, naccion, archivo))
#                #log(nombrelog = 'LeeDatos', error = EOFError, explicacion = 'Accion; archivo', variables = ('Funcion LeeDatos al utilizar pickle', naccion, archivo))
#            except pickle.UnpicklingError:
#                archivo.close()
#                borraTicket (naccion, BBDD = False, codigo = False)# Borramos solo los archivos
#                errorenTicket(naccion)
#                #sys.excepthook = lambda exc_type, exc_value, exc_traceback: logging.debug('UNCAUGHT EXCEPTION %r: %s' % (exc_type, traceback.format_tb(exc_traceback)))
#                logging.debug( Error: %s; Accion: %s; Funcion LeeDatos al utilizar pickle, Archivo: %s' % (__name__, pickle.UnpicklingError, naccion, archivo))
#                #log(nombrelog = 'LeeDatos', error = pickle.UnpicklingError, explicacion = 'Accion; archivo', variables = ('Funcion LeeDatos al utilizar pickle', naccion, archivo))

            else:
                historicoMensual = datos['historicoMensual']
                historicoSemanal = datos['historicoSemanal']
                historicoDiario = datos['historicoDiario']
                correcciones = datos['correcciones']

        return (historicoMensual,
                historicoSemanal,
                historicoDiario,
                correcciones)
    else:
        errorenTicket(naccion)


def grabaDatos(naccion,
               historicoMensual,
               historicoSemanal,
               historicoDiario,
               correcciones,):
    """
    
    """
    naccion = naccion.upper()
    datos = {'historicoMensual':historicoMensual,
             'historicoSemanal':historicoSemanal,
             'historicoDiario':historicoDiario,
             'correcciones':correcciones}

    # los nombres de los archivos hay que tratarlos asi, porque si no se corre el riesgo de utilizar nombres "protegidos" de archivos como son el caso de CON.DE, AUX.V
    tickets = obtenTicketsBBDD(naccion)
    nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
    archivo = os.path.join(os.getcwd(), carpetas['Datos'], nombre + ".pck")
    archivo = file(archivo, "w")
    pickle.dump(datos, archivo)
    archivo.close()

    #codificado = pickle.dumps(datos)
    #f = open(archivo, "w")
    #f.write(codificado)
    #f.close()

def duerme(tiempo = 1500):
    """
    
    """
    x = (randint(0, tiempo)) / 1000.0
    print('Pausa de %.3f segundos' % x)
    sleep (x)
    print('')


def ticketsdeMercado(mercado):
    """
    
    """
    #global webheaders
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
                r = urllib2.Request(url, headers = webheaders)
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
                #print(e.reason)
                print(url, e)
                web = None
                logging.debug('Error: %s; Mercado: %s; Url: %s' % (e, mercado.encode('UTF-8'), url.encode('UTF-8')))
                print ('Pausa de %d segundos' % pausareconexion)
                sleep (pausareconexion)

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
            #print ticket
            if (ticket not in ticketsanadidos) and ('%20' not in ticket):
                ticketsanadidos.append(ticket)

        duerme()
        pagina += 1
    print('')
    print(("%8d Tickets componen el mercado %s" % (len(ticketsanadidos), mercado)))
    print('')

    return ticketsanadidos


def descargaHistoricoAccion (naccion, **config):
    #global webheaders
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
    timming = config.get('timming', "m")
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

    #comprobandodividendo=False

    if fechaini == None:# hay un caso en el que nos puede interesar que la funcion cambie el estado de actualizar en el caso de que venga de 'actualizacionDatosHisAccion' con actualizar=True pero con fechaini=None
        actualizar = False
        url = "http://ichart.finance.yahoo.com/table.csv?s=" + naccion + "&d=" + mesfin + "&e=" + diafin + "&f=" + anofin + "&g=" + timming + "&ignore=.csv"
    else:
        fechaini = fechaini.split("-")
        anoini, mesini, diaini = fechaini
        mesini = str(int(mesini) - 1)
        actualizar = True
        url = "http://ichart.finance.yahoo.com/table.csv?s=" + naccion + "&a=" + mesini + "&b=" + diaini + "&c=" + anoini + "&d=" + mesfin + "&e=" + diafin + "&f=" + anofin + "&g=" + timming + "&ignore=.csv"
    f = None
    r = urllib2.Request(url, headers = webheaders)
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
            #print(e.reason)
            print(url, e)
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, naccion.encode('UTF-8'), url.encode('UTF-8')))
            f = None
            print ('Pausa de %d segundos' % pausareconexion)
            sleep (pausareconexion)

            # cuando la conexion se pierde, pasa por aqui, dando como error
            #[Errno 11004] getaddrinfo failed
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
#en la mayoria de los casos, en la web el historico existe, pero la descarga del archivo no, la accion ha desaparecido y yahoo elimina el archivo sin eliminar en la web el historico

    historicoMensual, historicoSemanal, historicoDiario, correcciones = LeeDatos(naccion)

    if timming == 'd':
        datosaccion = historicoDiario
    elif timming == 'w':
        datosaccion = historicoSemanal
    elif timming == 'm':
        datosaccion = historicoMensual

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

        if cierre == 0.0 or apertura == 0.0: #tenemos en cuenta que cierre sea 0 en ese caso no podriamos hacer la division de ajuste
            aperturaajustado = round(cierreajustado, 3)
        elif cierreajustado == 0.0:
            aperturaajustado = round(apertura, 3)
        else:
            aperturaajustado = round(apertura * (cierreajustado / cierre), 3)

        if cierre == 0.0 or maximo == 0.0:
            maximoajustado = round(cierreajustado, 3)
        elif cierreajustado == 0.0:
            maximoajustado = round(maximo, 3)
        else:
            maximoajustado = round(maximo * (cierreajustado / cierre), 3)

        if cierre == 0.0 or minimo == 0.0:
            minimoajustado = round(cierreajustado, 3)
        elif cierreajustado == 0.0:
            minimoajustado = round(minimo, 3)
        else:
            minimoajustado = round(minimo * (cierreajustado / cierre), 3)

        if cierreajustado == 0.0:
            cierreajustado = round(cierre, 3)
        else:
            cierreajustado = round(cierreajustado, 3)
        #comprobamos y corregimos del diccionario de las correciones
        (fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado, volumen) = correcciones.get((fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado, volumen), (fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado, volumen))

        #hacemos esto para que no hayan datos a cero, eliminando en el caso de que algun dato llege a cero todo la lista de datos anterior al dato donde es cero
        if aperturaajustado == 0.0 or maximoajustado == 0.0 or minimoajustado == 0.0 or cierreajustado == 0.0:
            datosaccion = []
        else:

            if actualizar:
                registrodescargadoprimero = (fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado)
                if len(datosaccion) > 1:
                    registroalmacenadoultimo = datosaccion[-1][0:5]#no queremos comparar el volumen
                else:
                    registroalmacenadoultimo = ('0000-00-00', 0.0, 0.0, 0.0, 0.0)

                actualizar = False
                if (registroalmacenadoultimo != registrodescargadoprimero):
                    print('El historico ha cambiado por el pago de un dividendo, hay que hacer una descarga completa nueva')
                    #print 'Borrando todos los datos almacenados'
                    #borraTicket(naccion, BBDD=False)
                    return 'Pago Dividendos'

            else:
                datosaccion.append((fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado, volumen))

        i -= 1

    if timming == 'd':
        historicoDiario = datosaccion
    elif timming == 'w':
        historicoSemanal = datosaccion
    elif timming == 'm':
        historicoMensual = datosaccion


    grabaDatos(naccion, historicoMensual, historicoSemanal, historicoDiario, correcciones)
    if txt:
        tickets = obtenTicketsBBDD(naccion)
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), carpetas['Historicos'], nombre + '.' + timming + '.csv')
        j = open(archivo, 'w')
        writercsv = csv.writer(j, delimiter = ';', lineterminator = '\n', doublequote = True)
        for n in datosaccion:

            fecha, apertura, maximo, minimo, cierre, volumen = n
            apertura = str(apertura).replace('.', ',')
            maximo = str(maximo).replace('.', ',')
            minimo = str(minimo).replace('.', ',')
            cierre = str(cierre).replace('.', ',')
            volumen = str(volumen).replace('.', ',')

            n = (fecha, apertura, maximo, minimo, cierre, volumen)

            writercsv.writerow(n)
            #j.write(str(n)+'\n')
        j.close()
    return datosaccion

#def timmingalmacenado(datosaccion):
#    registros=len (datosaccion)
#    i=1
#    sumdiffechas=0
#    while i<registros:
#            fecha=map(int,((datosaccion[i][0]).split('-')))
#            fechaanterior=map(int,((datosaccion[i-1][0]).split('-')))
#            diffechas=(date(fecha[0],fecha[1],fecha[2])-date(fechaanterior[0],fechaanterior[1],fechaanterior[2])).days
#            sumdiffechas=sumdiffechas+diffechas
#            i=i+1
#    if registros>1:
#        difregistros=sumdiffechas/(registros-1)
#    else:
#        difregistros=23
#    #difregistros=(date(fechapenultimoregistro[0],fechapenultimoregistro[1],fechapenultimoregistro[2])-date(fechaantepenultimoregistro[0],fechaantepenultimoregistro[1],fechaantepenultimoregistro[2])).days
#    if 22<difregistros or difregistros<0:
#        timming='m'
#    elif 4<=difregistros<8:
#        timming='w'
#    else:
#        timming='d'
#
#    return timming,difregistros

def actualizacionDatosHisAccion(naccion, **config):
    """
    
    """
    # TODO: Podemos intentar integrar la funcion actualizacionDatosHisAccion dentro de la propia funcion descargaHistoricoAccion, nos ahorrariamos una funcion y seguramente procesos duplicados

    historicoMensual, historicoSemanal, historicoDiario, _correcciones = LeeDatos(naccion)
    registro = {'d':'Diario', 'w':'Semanal', 'm':'Mensual'}

    timming = config.get('timming', "m")

    if timming == 'd':
        datosaccion = historicoDiario
        #difregistros = 10
    elif timming == 'w':
        datosaccion = historicoSemanal
        #difregistros = 15
    elif timming == 'm':
        datosaccion = historicoMensual
        #difregistros = 32

    if len(datosaccion) < 3:# al devolverno true=actualizar pero sin fecha, en la funcion descargaHistoricoAccion entiende que tiene que descargar todo el historico
        print('Registro %s insuficiente. Actualizacion completa' % registro[timming])
        return (None, timming, True)

    fechahoy = ((date.today().timetuple()))

    fechaultimoregistro = map(int, ((datosaccion[-1][0]).split('-')))

    desdeultimaactualizacion = (date(fechahoy[0], fechahoy[1], fechahoy[2]) - date(fechaultimoregistro[0], fechaultimoregistro[1], fechaultimoregistro[2])).days
# Comparar fecha de hoy con la del archivo he incluirla en el if con un and
# en esta funcion hay que hacer que cuando el len de datosaccion no es sufieciente, menor de 3 registros, que automaticamente responda para que la funcion de descarga descarge con un timming inferior
#    desdeultimaactualizacionarchivo=(date(fechahoy[0],fechahoy[1],fechahoy[2])-date(fechaarchivo[0],fechaarchivo[1],fechaarchivo[2])).days

    if (desdeultimaactualizacion > difregactualizar[timming]):# and (desdeultimaactualizacionarchivo>difregistros):
        print('Registro %s pendiente de una actualizacion desde %s' % (registro[timming], datosaccion[-2][0]))
        return (str(datosaccion[-3][0]), timming, True)
    else:
        print('Registro %s actualizado' % registro[timming])
        print('')
        return ((datosaccion[-1][0]), timming, False)


def corregirDatosHistoricosAccion(naccion):
    """
    
    """
    naccion = naccion.upper()
    historicoMensual, historicoSemanal, historicoDiario, correcciones = LeeDatos(naccion)

    print(' 1 - Diario')
    print(' 2 - Semanal')
    print(' 3 - Mensual')
    timming = 'None'
    while timming not in ('123'):
        timming = raw_input('Indica el timming donde quieres hacer la correccion : ')

    if timming == '1':
        datoshistoricos = historicoDiario
    elif timming == '2':
        datoshistoricos = historicoSemanal
    elif timming == '3' or timming == '' or timming == ' ':
        datoshistoricos = historicoMensual

    while True:
        x = 0
        while x < len(datoshistoricos):
            print(x , datoshistoricos[x])
            x += 1

        print('')
        print('Lista de correcciones ya realizadas')
        print(correcciones.items())

        i = int(raw_input("Indica registro a modificar : "))
        if i == '':
            break
        print("Registro a anterior")
        print(" Fecha: %s, Apertura: %.2f , Maximo : %.2f, Minimo : %.2f, Cierre : %.2f, Volumen : %d " % (datoshistoricos[i - 1]))

        print("Registro a modificar")
        print(" Fecha: %s, Apertura: %.2f , Maximo : %.2f, Minimo : %.2f, Cierre : %.2f, Volumen : %d " % (datoshistoricos[i]))

        print("Registro a posterior")
        print(" Fecha: %s, Apertura: %.2f , Maximo : %.2f, Minimo : %.2f, Cierre : %.2f, Volumen : %d " % (datoshistoricos[i + 1]))

        pregunta = raw_input(" Esta es la informacion que quieres editar ? S o cualquier tecla : ").upper()

        print('Recuerda que las fechas son AAAA-MM-DD')
        print('Recuerda que para los decimales se utiliza el punto y no la coma')

        if pregunta == 'S':

            fecha = datoshistoricos[i][0]

            while True:
                try:
                    apertura = float(raw_input(" Introduce Precio Apertura : ").replace(',', '.'))
                except ValueError:
                    print('Datos mal introducido\a')
                else:
                    if apertura == '':
                        apertura = datoshistoricos[i][1]
                    break


            while True:
                try:
                    maximo = float(raw_input(" Introduce Precio Maximo : ").replace(',', '.'))
                except ValueError:
                    print('Datos mal introducido\a')
                else:
                    if apertura == '':
                        apertura = datoshistoricos[i][2]
                    break


            while True:
                try:
                    minimo = float(raw_input(" Introduce Precio Minimo : ").replace(',', '.'))
                except ValueError:
                    print('Datos mal introducido\a')
                else:
                    if apertura == '':
                        apertura = datoshistoricos[i][3]
                    break


            while True:
                try:
                    cierre = float(raw_input(" Introduce Precio Cierre : ").replace(',', '.'))
                except ValueError:
                    print('Datos mal introducido\a')
                else:
                    if apertura == '':
                        apertura = datoshistoricos[i][4]
                    break

            while True:
                try:
                    volumen = int(raw_input(" Introduce Precio Volumen : "))
                except ValueError:
                    print('Datos mal introducido\a')
                else:
                    if apertura == '':
                        apertura = datoshistoricos[i][5]
                    break

            correcciones[datoshistoricos[i]] = (fecha, apertura, maximo, minimo, cierre, volumen)

            datoshistoricos[i] = (fecha, apertura, maximo, minimo, cierre, volumen)



        pregunta2 = raw_input(" Quieres editar otro registro? S o cualquier tecla : ")

        if not (pregunta2 in ('s', 'S')):
            break

    print("Cambios realizados")


    if timming == 'd':
        historicoDiario = datoshistoricos
    elif timming == 'w':
        historicoSemanal = datoshistoricos
    elif timming == 'm':
        historicoMensual = datoshistoricos


    grabaDatos(naccion, historicoMensual, historicoSemanal, historicoDiario, correcciones)


def analisisAlcistaAccion(naccion, **config):
    """ Analisis alcista
    timming=d/w/m, timming a analizar
    desdefecha=False/AAAA-MM-DD, fecha desde la que queremos recuperar analisis, fecha incluida, devuelbe todos los analisis cuya resistencia sea desde esta fecha
    txt=True/False, configuracion para hacer que genere archivos txt del analisis
    conEntradaLT = True/False, si queremos que nos incluya los analisis de LT, posibles entradas en LT
    MME = False/entero, Si queremos que se trace una Media Movil Exponencial, no utilizando el concepto de Maximo historico como tal
    filtro = 0.00, flotante filtro aplicado al soporte como precio de salida
    Resultado es: Resistencia,Soporte,Ruptura Resistencia,Punto LineaTendenciaInicio,Punto LineaTendenciaFin,timming del analisis
                    el formato obtenido es:
                                Resistencia , soporte , Salida Lt = fecha,apertura, maximo, minimo, cierre, volumen
                                punto LT = fecha inicio, precio inicio
                                salida Lt = Soporte anterior

    """

    #TODO: separar la funcion en la lectura, analisis y grabar datos, creando una funcion interna que nos sirva para darle la lista que contiene los datos y devuelva el analisis. De esta manera podre esternalizar la funcion y llamarla desde un programa
    #anadido un nuevo dato dando como resultado: Resistencia,Soporte,Ruptura Resistencia,Punto LineaTendenciaInicio,Punto LineaTendenciaFin, Punto de salida,timming del analisis
        #Anadiendo el Punto de Salida futuro, dandolo como valor inicial False y si en mitad del analisis el precio esta por debajo del Soporte menos el filtro cambiar todos los falses de la lista analisisalcista donde el valor es false asignandole la barra en la que ha roto el soporte-filtro=stoploss
        #anadido un nuevo parametro para hacer lo anterior, filtro de la resistencia = Stoploss

    naccion = naccion.upper()

    historicoMensual, historicoSemanal, historicoDiario, _correcciones = LeeDatos(naccion)

    conEntradaLT = config.get('conEntradaLT', True)
    MME = config.get('MME', False)
    if MME == False:
        MME2 = False
    else:
        MME2 = config.get('MME2', False)
    TAR = config.get('TAR', False)
    filtro = config.get('filtro', 0.0)
    timming = config.get('timming', "m")
    desdefecha = config.get('desdefecha', False)
    txt = config.get('txt', True)#Parametro para hacer que la funcion cree el archvo del analisis

    if desdefecha == '' or desdefecha == ' ' or desdefecha == None:
        desdefecha = False

    if timming == 'd':
        datoshistoricos2 = historicoDiario
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.01
            else:
                filtro = 3.5
    elif timming == 'w':
        datoshistoricos2 = historicoSemanal
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.02
            else:
                filtro = 2.5
    elif timming == 'm':
        datoshistoricos2 = historicoMensual
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.03
            else:
                filtro = 1.5

    analisisalcista = []
    listastoploss = []

    i = 0
    r = 0
    s = 0
    resistencia = True
    soporte = False
    stoploss = 0.0
    salidaOperacion = False
    entradapuntoLT = False

    datoshistoricos = []
    volumenMME = indicadorMME(datoshistoricos2, MME = 5, indicedatos = 'volumen')
    while i < len(datoshistoricos2):
        assert (datoshistoricos2[i][0] == volumenMME[i][0])
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos2[i]
        datoshistoricos.append((fecha, apertura, maximo, minimo, cierre, volumenMME[i][1]))
        i += 1
    del datoshistoricos2
    i = 0

    if not(MME == False):
        puntosMME = indicadorMME(datoshistoricos, MME = MME)
        if not(MME2 == False):
            puntosMME2 = indicadorMME(datoshistoricos, MME = MME2)
    if not (TAR == False):
        puntosTAR = indicadorTAR(datoshistoricos, TAR = TAR)

    while i < len(datoshistoricos):
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos[i]

        if i == 0:
            ant = 0
        else:
            ant = i - 1
        fechaanterior, _aperturaanterior, _maximoanterior, minimoanterior, cierreanterior, _volumenanterior = datoshistoricos[ant]
        _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]
        _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[s]

        if not (TAR == False):
            fechaTAR, puntoTAR = puntosTAR[ant]

            assert (fechaTAR == fechaanterior)

            if len(analisisalcista) > 0 and stoploss < (round((cierreanterior - (puntoTAR * filtro)), 3)):
                stoploss = round((cierreanterior - (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

        if not (MME == False):# and len( datoshistoricos ) >= MME:

            fechaMME, puntoMME = puntosMME[i]
            if not (MME2 == False):
                fechaMME2, puntoMME2 = puntosMME2[i]
                assert (fechaMME == fecha and fechaMME == fechaMME2)

            assert (fechaMME == fecha)

            #if i >= ( MME - 1 ):# Empieza a utilizar el indicadorMME en una barra en concreto, para la MME30 lo utiliza apartir de la barra 30(cuyo indice es 29)
            if puntoMME > 0:
                if resistencia == False and soporte == False and puntoMME < minimo:# Si no buscamos ni resistencias ni soportes es porque venimos de debajo de la MME
                    #la grafica esta completamente por encima de la MME,  y empezamos a buscar resistencias sobre la MMe
                    r = i
                    _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]
                    resistencia = True
                    soporte = False
                #elif maximo < puntoMME:# Grafica completamente bajo Media Movil Exponencial, no buscamos resistencias ni soportes, y consideramos la barra actual como resistencia
                elif maximo < puntoMME and (MME2 == False or (MME2 != False and puntoMME <= puntoMME2)):
                    # con esta logica, si hemos creado una resistencia y en algun momento bajamos una MME muy cercana a la grafica, habremos "borrado" esa resistencia anterior asignandole la barra actual como resistencia
                    r = i
                    _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]
                    resistencia = False
                    soporte = False

        #anade en analisisalcista, los puntos de entrada por Linea de tendencia
        if len(analisisalcista) > 0 and entradapuntoLT:

            LineaTendenciaInicio = analisisalcista[-1][3]
            LineaTendenciaFin = analisisalcista[-1][4]

            _fechaLTi , minimoLTi = LineaTendenciaInicio
            _fechaLTf , minimoLTf = LineaTendenciaFin

            if minimoLTi > 0 and minimoLTf > 0:

                precioentradapuntoLT = round((minimoLTi * ((1 + (((1.0 + (((minimoLTf - minimoLTi) / minimoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((i - LTi) / 12.0))), 3)

                if precioentradapuntoLT >= minimo:
                    if precioentradapuntoLT >= apertura or precioentradapuntoLT > maximo:# El precioentradapuntoLT esta por encima del maximo o abrio directamente por debajo, lo que significa que puede haber un split y utilizamos la apertura
                        precionentrada = apertura
                    else:#elif maximo>=precioentradapuntoLT:# El precioentradapuntoLT esta entre el maximo y el minimo y la paertura no la hizo por debajo
                        precionentrada = precioentradapuntoLT
                    #ultimo soporte consolidado
                    soporteanterior = analisisalcista[-1][1][0]
                    barraentradapuntoLT = (fecha, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, volumen)
                    analisisalcista.append((barraentradapuntoLT, (soporteanterior, stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming))
                    entradapuntoLT = False

        #cambia en la lista analisialcista los valores del precio de salida para cada operacion, cuando se rompe un stoploss, por la barra en la que se produce
        if stoploss >= minimo and len(analisisalcista) > 0:

            if stoploss > maximo or stoploss >= apertura:# El stoploss esta por encima del maximo o apertura, lo que significa que puede haber un split o abrio por debajo del stoploss
                salidaoperaciones = (fecha, apertura)
            else: #elif maximo >= stoploss:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)

            i2 = 0
            while i2 < len(analisisalcista):
                resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis = analisisalcista[i2]
                if salidaOperacionAnalisis == False:
                    analisisalcista[i2] = resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis
                    #analisisalcista[i2][5]=datoshistoricos[i]
                i2 += 1
            entradapuntoLT = False

        if resistencia and maximo > maximoresisten and not (minimo < minimoanterior and apertura < cierre):# No actualizamos la resistencia, si esta es la misma barra que la crea y ademas la rompe con un movimiento de abajo hacia arriba, considerando como valida la resistencia anterior

            r = i # le damos a r el indice de los datoshistoricos donde se encuentra la informacion de la resistencia y volvemos a leer los datos
            _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]

        if resistencia and minimo < minimoanterior:# resistencia consolidada
            resistencia = False
            soporte = True
            #volvemos al indice donde esta la resistencia para comprobar desde ahi los posibles soportes
            #comparamos que el movimiento viene de arriba hacia abajo, para asi considerar el minimo de la resistencia como interno en el movimiento y que en tal caso pueda ser el soporte
            if aperturaresisten > cierreresisten or i == len(datoshistoricos) - 1:#esto ultimo es porque puede que la ultima barra sea la resistencia, si le sumasemos uno nos saldriamos de rango
                i = r
            else:
                i = r + 1
            s = i
            _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[s]
            _fecha, apertura, maximo, minimo, cierre, _volumen = datoshistoricos[i]

    # Soporte alcista
        if soporte and minimo < minimosoporte and not ((maximo > maximoresisten) and (apertura > cierre)):#No actualizamos el soporte, si es la misma barra que rompe la resistencia y ademas la apertura es mayor que el cierre

            s = i
            _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[s]

        if soporte and ((maximo > maximoresisten)or i == ((len(datoshistoricos)) - 1)) and not((datoshistoricos[r] or datoshistoricos[s])  in analisisalcista):

            if r > 0:# No podremos calcular LT si no hay barras fuerra del ciclo resistencia y soporte, por eso la resistencia e inicio del ciclo tiene que ser mayor que 0
                localizaLTi = True
                localizaLTf = False
                LTi = r - 1

                LTf = s
                _fechaLTf, _aperturaLTf, _maximoLTf, minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[LTf]

                while localizaLTi:

                    if LTi >= 0:
                        _fechaLTi, _aperturaLTi, _maximoLTi, minimoLTi, _cierreLTi, _volumenLTi = datoshistoricos[LTi]
                    else:
                        localizaLTf = True
                        localizaLTi = False
                        break

    #                    print LTi
                    for j in xrange (LTi, -1, -1):
                        _fechaj, _aperturaj, _maximoj, minimoj, _cierrej, _volumenj = datoshistoricos[j]

                        #if (minimoLTi>minimoLTf or minimoLTi==0.0) and LTi>0:# Anadido el 23/01/2011 como estoy en alcista, si el minimodeLTi es mayor que el minimoLTf es porque esta por encima, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por debajo del LTf
                        if minimoLTi > minimoLTf and LTi > 0:# Anadido el 23/01/2011 como estoy en alcista, si el minimodeLTi es mayor que el minimoLTf es porque esta por encima, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por debajo del LTf
                            LTi -= 1
                            break


                        puntoLT = round((minimoLTi * ((1 + (((1.0 + (((minimoLTf - minimoLTi) / minimoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        #puntoLT = round((minimoLTi*((minimoLTf/minimoLTi)**(365.0/(7.0*(LTf-LTi))))**((7.0/365)*j-(7.0/365.0)*LTi)),3)
    #                        elif timming=='semanal':
                        #else:
                            # he deshabilitado la comprobacion del timming en esta formula porque habria que anadir la de diario, ademos sospecho que limpiando la formula, esta seria la misma independientemente el timming que utilicemos
                            #   puntoLT=round((minimoLTi*((1+(((1.0+(((minimoLTf-minimoLTi)/minimoLTi)))**(52.0/(LTf-LTi)))-1.0))**((j-LTi)/(52.0)))),3)#365/7.0

                        if puntoLT > minimoj:
                            LTi = j
                            break
                            #.....

                        if j == 0:

                            #..... las busqueda desde el ciclo resistencia y su ruptura hacia atras, ha terminado
                            # tendriamos en la variable LTi el indice de datoshitoricos de la barra de la linea de tendencia inicial donde apoyaria la LT
                            # quedaria comprobar que LTf es la mas externa
                            localizaLTi = False
                            localizaLTf = True
                            break

                LTf = r

                while localizaLTf:

    #                print "LTf, i =", LTf, i
                    if LTf <= i:
                        _fechaLTf, _aperturaLTf, _maximoLTf, minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[LTf]
                    else:
                        localizaLTf = False
                        localizaLTi = False
                        break
    #                print "LTf, i =", LTf, i
    #                while j<=i:
                    for j in xrange (LTf, i + 1):

                        _fechaj, _aperturaj, _maximoj, minimoj, _cierrej, _volumenj = datoshistoricos[j]


                        #esto lo he anadido porque se me ha dado el caso de que cuando en los primeros ciclos alcistas, si estan demasiado proximos al inicio del historico de la accion, me toma como el mismo punto el punto de LTi y LTf
                        if LTf == LTi:
                            LTf += 1
                            break

                        puntoLT = round((minimoLTi * ((1 + (((1.0 + (((minimoLTf - minimoLTi) / minimoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        #puntoLT = round((minimoLTi*((minimoLTf/minimoLTi)**(365.0/(7.0*(LTf-LTi))))**((7.0/365)*j-(7.0/365.0)*LTi)),3)

                        if puntoLT > minimoj:
                            LTf = j
                            break
                            #.....

                        if j == i:
                            localizaLTf = False
                            localizaLTi = False
                            break

            #quiero anadir aqui una ultima comprobacion de la LT desde 0 hasta i comprobandola entera, en el caso de que el
            #puntoLT sea igual al dato del indice de la tupla datoshistoricos no cambia o no lo damos por malo, pero si
            #si el puntoLT sea mayor al punto, y entonces habria que volver a calcular la LT pero esta vez tomando este nuevo punto
            # como LTi o LTf dependiendo de si esta entre '0' y 'r' o 'r' y 'i'.

                LineaTendenciaInicio = (datoshistoricos[LTi][0], datoshistoricos[LTi][3])
                LineaTendenciaFin = (datoshistoricos[LTf][0], datoshistoricos[LTf][3])


                if not (datoshistoricos[LTi][3] < datoshistoricos[LTf][3]): # comprobamos que no nos de rentabilidad negativa
                    LineaTendenciaInicio = ('0-0-0', 0.0)
                    LineaTendenciaFin = ('0-0-0', 0.0)
            else:
                LineaTendenciaInicio = ('0-0-0', 0.0)
                LineaTendenciaFin = ('0-0-0', 0.0)

            if TAR == False:
                stoploss = round((datoshistoricos[s][3] * (1 - filtro)), 3)

            else:
                stoploss = round((cierreanterior - (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

            maximoresistencia = datoshistoricos[r][2]
            aperturaruptura = datoshistoricos[i][1]
            minimoruptura = datoshistoricos[i][3]

            if maximoresistencia <= minimoruptura or maximoresistencia <= aperturaruptura:# Si el Maximo de la resistecia esta por debajo o igual del minimo de la ruptura o apertura de la ruptura, significa que puede haber un split o abrio por encima de la resistenca
                precionentrada = aperturaruptura
            else: #el maximo de la resistencia se encuetra entre la apertura y el maximo
                precionentrada = maximoresistencia

            analisisalcista.append((datoshistoricos[r], (datoshistoricos[s], stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming))
            if conEntradaLT:
                entradapuntoLT = True

            #LT=True # esto es porque hasta que no se produce un segundo soporte, no podemos calcular la linea de tendencia

            #Si la misma barra que rompe la resistencia abre arriba para cerrar por abajo del stoploss, esa barra nos saca del mercado
            if stoploss >= minimo and apertura > cierre and len(analisisalcista) > 0:

#                if maximo >= stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)
#                elif maximo < stoploss:# El stoploss esta por encima del maximo, lo que significa que puede haber un split
#                    salidaoperaciones = ( fecha, maximo )

                i2 = 0
                while i2 < len(analisisalcista):
                    resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis = analisisalcista[i2]
                    #salidaOperacionAnalisis=analisisalcista[i2][5]
                    if salidaOperacionAnalisis == False:
                        analisisalcista[i2] = resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis
                        #analisisalcista[i2][5]=datoshistoricos[i]
                    i2 += 1

            r = i #como la ultima barra que ha roto la resistencia es mas alta que la resistencia, la considero como nueva resistencia
            _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]

            resistencia = True
            soporte = False

        i += 1



    if desdefecha:
        i = 0
        while i < len(analisisalcista):
            resistencia, soporte, ruptura, LTi, LTf, salida, timming = analisisalcista[i]
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = resistencia
            if fecha >= desdefecha:
                analisisalcista = analisisalcista[i:]
                i = 0
                del resistencia, soporte, ruptura, LTi, LTf, salida, fecha, _apertura, _maximo, _minimo, _cierre, _volumen
                break
            if i == (len(analisisalcista) - 1) and fecha < desdefecha:#Ha llegado al final de analisisbajista sin encontrar una fecha de analisis mayor a desdefecha
                analisisalcista = []
            i += 1

    ###mostramos en pantalla y creamos otro archivo no codificado con la tupla
    if len(analisisalcista) > 0 and txt:
        tickets = obtenTicketsBBDD(naccion)
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), carpetas["Analisis"], nombre + "." + timming + ".analisisalcista.txt")
        j = open(archivo, "w")
        j.write(str(config) + '\n')
        for n in analisisalcista:
            #~ j.write(str(n)+'\n')
            resistencia, soporte, ruptura, LTi, LTf, salida, timming = n
            j.write("Resistencia " + str(resistencia) + '\n')
            j.write("Soporte     " + str(soporte) + '\n')
            j.write("Ruptura     " + str(ruptura) + '\n')
            j.write("LT Inicio   " + str(LTi) + '\n')
            j.write("LT Final    " + str(LTf) + '\n')
            j.write("Salida      " + str(salida) + '\n')
            j.write("Timming     " + str(timming) + '\n')
            j.write('\n')

        for n in xrange (5):
            j.write('\n')

        for n in listastoploss:
            j.write(str(n) + '\n')

        j.close()

    # formato de salida, ultimo analisis alcista, soporte anterior, todo el analisis alcista
    # hay que anadir cuando el len de analisisalcista sea mayor que 2, para cada analisis alcista hay un soporte que es el precio de salida en Lt para este.
    if len(analisisalcista) == 1: #esto esta porque puede que en el analisisalcista en el timming actual no produzca resultado al no existir resistencia alcista en el timming actual
        return (analisisalcista[-1] , 0, analisisalcista)
    elif len (analisisalcista) > 1:
        return (analisisalcista[-1] , (analisisalcista[-2][1][1]), analisisalcista) #[-2][1][1]=penultimo analisis, Soporte, stoploss
    else:
        #habria que comprobar un timming inferirior al obtener como resultado 0
        return None

def analisisBajistaAccion(naccion, **config):
    """ Analisis bajista

     timming=d/w/m, timming a analizar
    desdefecha=False/AAAA-MM-DD, fecha desde la que queremos recuperar analisis, fecha incluida, devuelbe todos los analisis cuya resistencia sea desde esta fecha
    txt=True/False, configuracion para hacer que genere archivos txt del analisis
    conEntradaLT = True/False, si queremos que nos incluya los analisis de LT, posibles entradas en LT
    MME = False/entero, Si queremos que se trace una Media Movil Exponencial, no utilizando el concepto de Maximo historico como tal
    filtro = 0.00, flotante filtro aplicado al soporte como precio de salida
    Resultado es: Resistencia,Soporte,Ruptura Resistencia,Punto LineaTendenciaInicio,Punto LineaTendenciaFin,timming del analisis
                    el formato obtenido es:
                                Resistencia , soporte , Salida Lt = fecha,apertura, maximo, minimo, cierre, volumen
                                punto LT = fecha inicio, precio inicio
                                salida Lt = Soporte anterior

    """
    naccion = naccion.upper()

    historicoMensual, historicoSemanal, historicoDiario, _correcciones = LeeDatos(naccion)

    conEntradaLT = config.get('conEntradaLT', True)
    MME = config.get('MME', False)
    if MME == False:
        MME2 = False
    else:
        MME2 = config.get('MME2', False)
    TAR = config.get('TAR', False)
    filtro = config.get('filtro', 0.0)
    timming = config.get('timming', "m")
    desdefecha = config.get('desdefecha', False)
    txt = config.get('txt', True)

    if desdefecha == '' or desdefecha == ' ' or desdefecha == None:
        desdefecha = False

    if timming == 'd':
        datoshistoricos2 = historicoDiario
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.01
            else:
                filtro = 3.5
    elif timming == 'w':
        datoshistoricos2 = historicoSemanal
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.02
            else:
                filtro = 2.5
    elif timming == 'm':
        datoshistoricos2 = historicoMensual
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.03
            else:
                filtro = 1.5

    analisisbajista = []
    listastoploss = []

    i = 0
    r = 0 # indice de la tabla de datoshistoricos que nos indica la posicion dentro de la tupla donde se encuentra la resistencia
    s = 0
    resistencia = False
    soporte = True
    stoploss = 0.0
    salidaOperacion = False
    entradapuntoLT = False

    datoshistoricos = []
    volumenMME = indicadorMME(datoshistoricos2, MME = 5, indicedatos = 'volumen')
    while i < len(datoshistoricos2):
        assert (datoshistoricos2[i][0] == volumenMME[i][0])
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos2[i]
        datoshistoricos.append((fecha, apertura, maximo, minimo, cierre, volumenMME[i][1]))
        i += 1
    del datoshistoricos2
    i = 0

    if not(MME == False):
        puntosMME = indicadorMME(datoshistoricos, MME = MME)
        if not(MME2 == False):
            puntosMME2 = indicadorMME(datoshistoricos, MME = MME2)
    if not (TAR == False):
        puntosTAR = indicadorTAR(datoshistoricos, TAR = TAR)

    while i < len(datoshistoricos):
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos[i]

        if i == 0:
            ant = 0
        else:
            ant = i - 1
        fechaanterior, _aperturaanterior, maximoanterior, _minimoanterior, cierreanterior, _volumenanterior = datoshistoricos[ant]
        _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[r]
        _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]

        if not (TAR == False):
            fechaTAR, puntoTAR = puntosTAR[ant]

            assert (fechaTAR == fechaanterior)

            if len(analisisbajista) > 0 and stoploss > (round((cierreanterior + (puntoTAR * filtro)), 3)):
                stoploss = round((cierreanterior + (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

        if not (MME == False):# and len( datoshistoricos ) >= MME:

            fechaMME, puntoMME = puntosMME[i]
            if not (MME2 == False):
                fechaMME2, puntoMME2 = puntosMME2[i]
                assert (fechaMME == fecha and fechaMME == fechaMME2)

            assert (fechaMME == fecha)

            #if i >= ( MME - 1 ):# Empieza a utilizar el indicadorMME en una barra en concreto, para la MME30 lo utiliza apartir de la barra 30(cuyo indice es 29)
            if puntoMME > 0:
                if resistencia == False and soporte == False and puntoMME > maximo:# Si no buscamos ni resistencias ni soportes y la grafica esta completamente por abajo de la MME, es porque estamos buscando soportes
                    s = i
                    _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]
                    soporte = True
                    resistencia = False
                #if puntoMME < minimo:# Media Movil Exponencial bajo grafica, no buscamos soportes ni resistencias, y consideramos la barra actual como soporte
                elif puntoMME < minimo and (MME2 == False or (MME2 != False and puntoMME2 <= puntoMME)):
                #elif puntoMME2 <= puntoMME < minimo:
                    s = i
                    _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]
                    soporte = False
                    resistencia = False

        #anade en analisisbajista, los puntos de entrada por Linea de tendencia
        if len(analisisbajista) > 0 and entradapuntoLT:
            LineaTendenciaInicio = analisisbajista[-1][3]
            LineaTendenciaFin = analisisbajista[-1][4]

            _fechaLTi , maximoLTi = LineaTendenciaInicio
            _fechaLTf , maximoLTf = LineaTendenciaFin

            if maximoLTi > 0 and maximoLTf > 0:
                #try:
                precioentradapuntoLT = round((maximoLTi * ((1 + (((1.0 + (((maximoLTf - maximoLTi) / maximoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((i - LTi) / 12.0))), 3)

                #except OverflowError:
                #    log(nombrelog='analisisBajistaAccionEntradaLT',error=OverflowError,explicacion='Accion; timming; FechaLTi; FechaLTf; Fecha de la barra donde se produce el Error',variables=('Funcion analisisBajistaAccion Buscando analisis de entrada en LT',naccion,timming,fechaLTi,fechaLTf,fecha))
                #else:
                if maximo >= precioentradapuntoLT:
                    if minimo > precioentradapuntoLT or apertura >= precioentradapuntoLT:## El precioentradapuntoLT esta por debajo del minimo, lo que significa que puede haber un split y utilizamos la apertura
                        precionentrada = apertura
                    else: #elif precioentradapuntoLT >= minimo:# El precioentradapuntoLT esta entre el maximo y el minimo
                        precionentrada = precioentradapuntoLT
                    #ultima resistencia consolidado
                    resistenciaanterior = analisisbajista[-1][1][0]
                    barraentradapuntoLT = (fecha, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, volumen)
                    analisisbajista.append((barraentradapuntoLT, (resistenciaanterior, stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming))
                    entradapuntoLT = False


        # TODO: hay un stoploss que se calcula en funcion al precio de entrada, precio objetivo, recogemos beneficios cuando el precio toque una venta limite.
        #cambia en la lista analisialcista los valores del precio de salida para cada operacion, cuando se rompe un stoploss, por la barra en la que se produce
        if maximo >= stoploss and len(analisisbajista) > 0:

            if minimo > stoploss or apertura >= stoploss:# El stoploss esta por debajo del minimo o apertura, lo que significa que puede haber un split y/o abrio por encima del stoploss, utilizamos la apertura
                salidaoperaciones = (fecha, apertura)
            else:#elif stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)

            i2 = 0
            while i2 < len(analisisbajista):
                soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis = analisisbajista[i2]
                #salidaOperacionAnalisis=analisisalcista[i2][5]
                if salidaOperacionAnalisis == False:
                    analisisbajista[i2] = soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis
                    #analisisalcista[i2][5]=datoshistoricos[i]
                i2 += 1
            entradapuntoLT = False

        if soporte and minimo < minimosoporte and not (maximo > maximoanterior and apertura > cierre):# No actualizamos el soporte, si esta es la misma barra que la crea y ademas la rompe con un movimiento de arriba hacia abajo, considerando como valida la resistencia anterior

            s = i
            _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]

        if soporte and maximo > maximoanterior:# soporte consolidada
            resistencia = True
            soporte = False
            #volvemos al indice donde esta el soporte para comprobar desde ahi las posibles resistencias
            #comparamos que el movimiento viene de abajo hacia arriba, para asi considerar el maximo del soporte como interno en el movimiento y que en tal caso pueda ser la resistencia
            if aperturasoporte < cierresoporte or i == len(datoshistoricos) - 1:#esto ultimo es porque puede que la ultima barra sea la resistencia, si le sumasemos uno nos saldriamos de rango
                i = s
            else:
                i = s + 1
            r = i
            _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[r]
            _fecha, apertura, maximo, minimo, cierre, _volumen = datoshistoricos[i]

    # resistencia bajista
        if resistencia and maximo > maximoresisten and not ((minimo < minimosoporte) and (apertura < cierre)):#No actualizamos la resistencia, si es la misma barra que rompe el soporte y ademas la apertura es menor que el cierre
#        if soporte and minimo<minimosoporte:
            r = i
            _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[r]

        if resistencia and ((minimo < minimosoporte)or i == ((len(datoshistoricos)) - 1)) and not((datoshistoricos[s] or datoshistoricos[r])  in analisisbajista):



#            if LT: # esto es porque hasta que no se produce un segundo soporte, no podemos calcular la linea de tendencia
            if s > 0:# No podremos calcular LT si no hay barras fuerra del ciclo soporte y resistencia, por eso el soporte e inicio del ciclo tiene que ser mayor que 0
                localizaLTi = True
                localizaLTf = False
                LTi = s - 1

                LTf = r
                fechaLTf, _aperturaLTf, maximoLTf, _minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[LTf]

                while localizaLTi:

                    if LTi >= 0:
                        fechaLTi, _aperturaLTi, maximoLTi, _minimoLTi, _cierreLTi, _volumenLTi = datoshistoricos[LTi]
                    else:
                        localizaLTf = True
                        localizaLTi = False
                        break

    #                    print LTi
                    for j in xrange (LTi, -1, -1):
                        fechaj, _aperturaj, maximoj, _minimoj, _cierrej, _volumenj = datoshistoricos[j]

                        if (maximoLTi < maximoLTf or maximoLTi == 0.0) and LTi > 0:# como estoy en bajista, si el maximoLTi es menor que el maximoLTf es porque esta por debajo, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por encima del LTf
                            LTi -= 1
                            break
                        try:
                            #puntoLT = round((minimoLTi*((minimoLTf/minimoLTi)**(365.0/(7.0*(LTf-LTi))))**((7.0/365)*j-(7.0/365.0)*LTi)),3)
                            puntoLT = round((maximoLTi * ((1 + (((1.0 + (((maximoLTf - maximoLTi) / maximoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        except (OverflowError, ZeroDivisionError) as e:# en el calculo de la linea de tendencia bajista hacia atras, aveces, la linea llega al infinito
    #                            puntoLTanterior=round((maximoLTi*((1+(((1.0+(((maximoLTf-maximoLTi)/maximoLTi)))**(12.0/(LTf-LTi)))-1.0))**((j-LTi-1)/12.0))),3)
    #                            maximohistorico=max([maxi[2] for maxi in datoshistoricos[0:j]])
    #                            if puntoLTanterior>maximohistorico:
                            j = 0 #El error lo da en
                            #sys.excepthook = lambda exc_type, exc_value, exc_traceback: logging.debug('UNCAUGHT EXCEPTION %r: %s' % (exc_type, traceback.format_tb(exc_traceback)))
                            logging.debug('Error: %s; Accion: %s; timming: %s; FechaLTi: %s; FechaLTf: %s; Fecha de la barra donde se produce el Error: %s' % (e, naccion.encode('UTF-8'), timming, fechaLTi, fechaLTf, fechaj))
                            #log(nombrelog = 'analisisBajistaAccion', error = OverflowError, explicacion = 'Accion; timming; FechaLTi; FechaLTf; Fecha de la barra donde se produce el Error', variables = ('Funcion analisisBajistaAccion en localizaLTi', naccion, timming, fechaLTi, fechaLTf, fechaj))
                                    #ABL(4 analisis j=2954 timming='d')
                                    #ACOM.ST (22 analisis j=357 timming='d')
                                    #ADI.L (4 analisis j=567 timming='d')
                                    #ADLS.OB(36 analisis j=148 timming='d')
                                    #AEG.L (18 analisis j=572 timming='d')
                                    #AiG (5 analisis j=1069 timming='d')aig
                                    #AIG(3 analisis j=283 timming='w')
#                        except ZeroDivisionError:
#                            j = 0
#                            #sys.excepthook = lambda exc_type, exc_value, exc_traceback: logging.debug('UNCAUGHT EXCEPTION %r: %s' % (exc_type, traceback.format_tb(exc_traceback)))
#                            logging.debug( Error: %s; Accion: %s; timming: %s; FechaLTi: %s; FechaLTf: %s; Fecha de la barra donde se produce el Error: %s' % (__name__, ZeroDivisionError, naccion, timming, fechaLTi, fechaLTf, fechaj))
#                            #log(nombrelog = 'analisisBajistaAccion', error = ZeroDivisionError, explicacion = 'Accion; timming; FechaLTi; FechaLTf; Fecha de la barra donde se produce el Error', variables = ('Funcion analisisBajistaAccion en localizaLTi', naccion, timming, fechaLTi, fechaLTf, fechaLTf))
#                        #print j,puntoLT,'localizaLTi',i

                        if puntoLT < maximoj:
                            LTi = j
                            break
                            #.....

                        if j == 0:

                            #..... las busqueda desde el ciclo resistencia y su ruptura hacia atras, ha terminado
                            # tendriamos en la variable LTi el indice de datoshitoricos de la barra de la linea de tendencia inicial donde apoyaria la LT
                            # quedaria comprobar que LTf es la mas externa
                            localizaLTi = False
                            localizaLTf = True
                            break

                LTf = s
                #LTf=r-1# Anadido el 23/01/2011
                #j=r
                while localizaLTf:

    #                print "LTf, i =", LTf, i
                    if LTf <= i:
                        _fechaLTf, _aperturaLTf, maximoLTf, _minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[LTf]
                    else:
                        localizaLTf = False
                        localizaLTi = False
                        break
    #                print "LTf, i =", LTf, i
    #                while j<=i:
                    for j in xrange (LTf, i + 1):

                        _fechaj, _aperturaj, maximoj, _minimoj, _cierrej, _volumenj = datoshistoricos[j]


                        #esto lo he anadido porque se me ha dado el caso de que cuando en los primeros ciclos alcistas, si estan demasiado proximos al inicio del historico de la accion, me toma como el mismo punto el punto de LTi y LTf
                        if LTf == LTi:
                            LTf += 1
                            break
                        try:
                            #puntoLT = round((minimoLTi*((minimoLTf/minimoLTi)**(365.0/(7.0*(LTf-LTi))))**((7.0/365)*j-(7.0/365.0)*LTi)),3)
                            puntoLT = round((maximoLTi * ((1 + (((1.0 + (((maximoLTf - maximoLTi) / maximoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        except OverflowError:
                            #sys.excepthook = lambda exc_type, exc_value, exc_traceback: logging.debug('UNCAUGHT EXCEPTION %r: %s' % (exc_type, traceback.format_tb(exc_traceback)))
                            logging.debug('Error: %s; Accion: %s; timming: %s; FechaLTi: %s; FechaLTf: %s; Fecha de la barra donde se produce el Error: %s' % (OverflowError, naccion.encode('UTF-8'), timming, fechaLTi, fechaLTf, fechaj))
                            #log(nombrelog = 'analisisBajistaAccion', error = OverflowError, explicacion = 'Accion; timming; FechaLTi; FechaLTf; Fecha de la barra donde se produce el Error', variables = ('Funcion analisisBajistaAccion en localizaLTf', naccion, timming, fechaLTi, fechaLTf, fechaj))
                            puntoLT = maximoj# asi no altero el LTf
    #                        elif timming=='semanal':
                        #else:
                        #    puntoLT=round((minimoLTi*((1+(((1.0+(((minimoLTf-minimoLTi)/minimoLTi)))**(52.0/(LTf-LTi)))-1.0))**((j-LTi)/(52.0)))),3)#365/7.0
                        #                        print j,puntoLT,'localizaLTf',i
                        if puntoLT < maximoj:
                            if (LTf == j or (puntoLT == 0.0 and LTf < i)) and not (j + 1 > i):
                                #Si la linea de tendencia llega a 0 y LTf no ha llegado a ser i, deberia comprobar hasta llegar a ser la i
                                #la primera comprobacion es porque por una falta de precision en el calculo de PuntoLT, aveces da menor que el maximo del que es precisamente el ultimo punto donde toco, es decir, ya tomamos este ultimo punto como LTf pero cuando volvemos a comprobarlo por segunda vez, vuelve a dar que es menor por un fallo de precision
                                LTf = j + 1
                            else:
                                LTf = j
                            if LTf >= i:
                                localizaLTf = False
                                localizaLTi = False
                            break

                        if j >= i:
                            localizaLTf = False
                            localizaLTi = False
                            break

                LineaTendenciaInicio = (datoshistoricos[LTi][0], datoshistoricos[LTi][2])
                LineaTendenciaFin = (datoshistoricos[LTf][0], datoshistoricos[LTf][2])

            #if not LT:
                if not (datoshistoricos[LTi][2] > datoshistoricos[LTf][2]):
                    LineaTendenciaInicio = ('0-0-0', 0.0)
                    LineaTendenciaFin = ('0-0-0', 0.0)
            else:
                LineaTendenciaInicio = ('0-0-0', 0.0)
                LineaTendenciaFin = ('0-0-0', 0.0)


            if TAR == False:
                stoploss = round((datoshistoricos[r][2] * (1 + filtro)), 3)
            else:
                stoploss = round((cierreanterior + (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

            minimosoporte = datoshistoricos[s][3]
            aperturaruptura = datoshistoricos[i][1]
            maximoruptura = datoshistoricos[i][2]

            if minimosoporte >= maximoruptura or minimosoporte >= aperturaruptura:# Si el minimo del soporte esta por encima o igual del maximo de la ruptura o apertura de la ruptura, significa que puede haber un split o abrio por debajo del soporte
                precionentrada = aperturaruptura
            else: #el maximo de la resistencia se encuetra entre la apertura y el maximo
                precionentrada = minimosoporte

            analisisbajista.append((datoshistoricos[s], (datoshistoricos[r], stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming))

            if conEntradaLT:
                entradapuntoLT = True

            #Si la misma barra que rompe el soporte abre abajo para cerrar por arriba del stoploss, esa barra nos saca del mercado
            if maximo >= stoploss and cierre > apertura and len(analisisbajista) > 0:

                #if maximo >= stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)
                #elif minimo > stoploss:# El stoploss esta por debajo del minimo, lo que significa que puede haber un split
                #    salidaoperaciones = ( fecha, minimo )

                i2 = 0
                while i2 < len(analisisbajista):
                    soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis = analisisbajista[i2]
                    #salidaOperacionAnalisis=analisisalcista[i2][5]
                    if salidaOperacionAnalisis == False:
                        analisisbajista[i2] = soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis
                        #analisisalcista[i2][5]=datoshistoricos[i]
                    i2 += 1
            s = i #como la ultima barra que ha roto la resistencia es mas alta que la resistencia, la considero como nueva resistencia
            _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]
#            if i<> len (datoshistoricos)-1:# esto esta porque si hemos llegado al final del analisis de los datos historicos, hacemos el analisis como si hubiese roto la resistencia, y ya no nos interesa volver atras una barra, ya que esto no meteria en un bucle infinito
#            if i<len (datoshistoricos)-1 and (minimo < minimoanterior and apertura>cierre):# esto esta porque si hemos llegado al final del analisis de los datos historicos, hacemos el analisis como si hubiese roto la resistencia, y ya no nos interesa volver atras una barra, ya que esto no meteria en un bucle infinito
#            if i<len (datoshistoricos)-1 and apertura>cierre:
#                i-=1 # vuelvo un dato atras porque es posible que la misma barra que rompe la resistencia lo sea en el siguiente ciclo, y asi comparo si el maximo de esa barra es el mayor dejado hasta el momento
            #print resitenciaalcista

            resistencia = False
            soporte = True

        i += 1

    if desdefecha:
        i = 0
        while i < len(analisisbajista):
            soporte, resistencia, ruptura, LTi, LTf, salida, timming = analisisbajista[i]
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = soporte
            if fecha >= desdefecha:
                analisisbajista = analisisbajista[i:]
                del resistencia, soporte, ruptura, LTi, LTf, salida, fecha, _apertura, _maximo, _minimo, _cierre, _volumen
                break
            if i == (len(analisisbajista) - 1) and fecha < desdefecha:#Ha llegado al final de analisisbajista sin encontrar una fecha de analisis mayor a desdefecha
                analisisbajista = []
            i += 1
    #grabaDatos(naccion,datoshistoricos,correcciones,cotizaciones,analisis,analisisbajista,analisisbajista)


##    codificado = pickle.dumps(analisisbajista)
##
##    f = open(archivo+".analisisbajista.pck", "w")
##    f.write(codificado)
##    f.close()
    ###mostramos en pantalla y creamos otro archivo no codificado con la tupla
    if len(analisisbajista) > 0 and txt:
        tickets = obtenTicketsBBDD(naccion)
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), carpetas["Analisis"], nombre + "." + timming + ".analisisbajista.txt")
        j = open(archivo, "w")
        j.write(str(config) + '\n')
        for n in analisisbajista:
            #~ j.write(str(n)+'\n')
            soporte, resistencia, ruptura, LTi, LTf, salida, timming = n
            j.write("Soporte     " + str(soporte) + '\n')
            j.write("Resistencia " + str(resistencia) + '\n')
            j.write("Ruptura     " + str(ruptura) + '\n')
            j.write("LT Inicio   " + str(LTi) + '\n')
            j.write("LT Final    " + str(LTf) + '\n')
            j.write("Salida      " + str(salida) + '\n')
            j.write("Timming     " + str(timming) + '\n')
            j.write('\n')

        for n in xrange (5):
            j.write('\n')

        for n in listastoploss:
            j.write(str(n) + '\n')


        j.close()

    # formato de salida, ultimo analisis alcista, soporte anterior, todo el analisis alcista
    # hay que anadir cuando el len de analisisbajista sea mayor que 2, para cada analisis alcista hay un soporte que es el precio de salida en Lt para este.
    if len(analisisbajista) == 1: #esto esta porque puede que en el analisisbajista en el timming actual no produzca resultado al no existir resistencia alcista en el timming actual
        return ((analisisbajista[-1]), 0, analisisbajista)
    elif len (analisisbajista) > 1:
        return ((analisisbajista[-1]), (analisisbajista[-2][1][1]), analisisbajista)#[-2][1][1]=penultimo analisis, resistencia, stoploss
    else:
        #habria que comprobar un timming inferirior al obtener como resultado 0
        return None

def indicadorMME(datos, **config):
    """
    devuelve de la lista, datos, el indicadorMME calculado
    indice, si es True devueve una tupla completa que corresponde al indicadorMME con el formato (Fecha, indicadorMME) para la lista de datos completa
    indice, si es un valor en concreto, nos devuelve el valor del indicadorMME para ese indice en concreto

    indicedatos, es el valor del indice de las tuplas de datos al que se utiliza para calcular el indicador, por defecto 4 que corresponde al precio de cierre.
    """
    # para los indicadores como la Media Movil 30 en la que en los primeros 29 periodos no se puede calcular, hay que asignarles valor 0
    resultado = []
    MME = config.get('MME', 30)
    indice = config.get('indice', True)
    indicedatos = config.get('indicedatos', 'cierre')

    indicedatos = ('fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'volumen').index(indicedatos)

    if indice == True:
        fin = len(datos)
    else:
        fin = indice + 1

    k = (2.0 / (1.0 + MME))
    for iMME in xrange (0, fin):
        if iMME == 0:
            puntoMME = datos[iMME][indicedatos]# Este es el pirmer cierre de los datos historicos
            fechaMME = datos[iMME][0]
        else:
            cierreMME = datos[iMME][indicedatos]
            fechaMME = datos[iMME][0]
            puntoMME = (cierreMME * k) + (puntoMME * (1 - k))

        if indicedatos == 5:
            resultado.append((fechaMME, int(puntoMME)))
        else:
            resultado.append((fechaMME, round(puntoMME, 3)))
    if not indice == True:#devuelve el valor del indicadorMME para ese indice en concreto
        resultado = round(puntoMME, 3)

    return resultado

def indicadorTAR(datos, **config):
    """
    Indicador True Averange xrange
    TAR = False/Entero
    Si TAR es false devuelve una lista de los rangos, si es un entero devuelve la media de los rangos de los periodos especificados

    """

    listaTR = []
    TR = []
    listaTAR = []
    TAR = config.get('TAR', 10)

    for i in xrange (0, len(datos)):
        inicio = (i + 1) - TAR
        if inicio < 0:
            inicio = 0

        fecha, _apertura, maximo, minimo, _cierre, _volumen = datos[i]
        if i == 0:
            valorTR = 0.0
        else:
            ant = i - 1
            _fechaanterior, _aperturaanterior, _maximoanterior, _minimoanterior, cierreanterior, _volumenanterior = datos[ant]
            valorTR = max((abs(maximo - minimo), abs(maximo - cierreanterior), abs(minimo - cierreanterior)))

        listaTR.append((fecha, valorTR))
        TR.append(valorTR)

        valorTAR = (sum(TR[inicio:])) / (len(TR[inicio:]))
        listaTAR.append((fecha, valorTAR))

    if TAR == False:
        return listaTR
    else:
        return listaTAR


def cruceconindicador(naccion):
    #TODO: funcion que compare el indicadorMME con el precio de cotizacion actual de la accion para comprobar si esta por arriba, centrado o abajo de la ultima barra y con esta informacion, realizar el analisis alcista o bajista
    """
    configurar el resultado que buscamos:
        Solo buscamos en el ultimo periodo mas actual almacenado, compare el indicadorMME con el precio de cotizacion actual y la ultima barra del historico de la accion para comprobar si esta por arriba, centrado o abajo y distacia porcentual al precio y con esta informacion, realizar el analisis alcista o bajista y busquedas de valores de su situacion y cercania en concreto
        Buscamos en todo el historico de la accion haciendo que nos devuelva una lista con las fechas de las barras en las que cruza y nos indique si esta arriba, abajo o si esta en medio en que direccion esta cruzando

    """
    return


def creaMenu(sep, lmenu):
    """Le damos el separador de la opcion y una lista con las opciones del menu,
    nos devuelve una lista de tuplas con la cola de opciones y descripciones elegidas,
    añade al final de la lista una tupla mas que contiene (None,None)
    
    
    
    
    """
    control = []
    respdescp = []

    for n in lmenu:
        print(n)
        control.append(n[0:n.find(sep)].lower())

    while True:
        resp = ((raw_input('Opcion?')).lower()).strip()

        if len(resp) == 1:
            if resp in control:
                descp = lmenu[control.index(resp)]
                respdescp = [(resp, descp), ]
                break
        elif len(resp) > 1:
            for n in resp:
                if n in control:
                    respdescp.append((n, lmenu[control.index(n)]))
            break

    respdescp.append((None, None))

    return (respdescp)

#def actualizardescargaranalizarticket(naccion,timmingdescarga):
#    datosaccion=os.path.join(os.getcwd(),"Datos\\"+naccion+".pck")
#    if (naccion in tickets.keys()) and (os.path.exists(datosaccion)) :
#        print 'Ticket %s ya descargado, comprobando la actualizacion de los datos'%naccion
#        fechaactualizar,timmingnaccion,actualicion=actualizacionDatosHisAccion(naccion)
#        if actualicion:
#            accioninvalida=descargaHistoricoAccion(naccion,fechaini=fechaactualizar,timming=timmingnaccion,actualizar=actualicion)
#            if accioninvalida=='URL invalida':
#                borraTicket (naccion, BBDD=False)
#                return 'Accion invalida'
#            duerme()
#    else:
#
#        print 'Ticket %s nuevo, descarga completa del historico de la accion' %naccion
#        accioninvalida=descargaHistoricoAccion (naccion,timming=timmingdescarga)
#        if accioninvalida=='URL invalida':
#            borraTicket (naccion, BBDD=False)
#            return 'Accion invalida'
#
#        duerme()
#
#
#    print 'Analizando ticket'
#
#    analisisalcista=analisisAlcistaAccion(naccion)
#    while analisisalcista==None:
##    if alcista==None:#si no hay analisis, bajamos el timmin
#        fechaactualizar,timmingnaccion,actualicion=actualizacionDatosHisAccion(naccion)
#
#        if timmingnaccion=='m':
#            timmingnaccion='w'
#        elif timmingnaccion=='w':
#            timmingnaccion='d'
#
#        accioninvalida=descargaHistoricoAccion(naccion,timming=timmingnaccion)
#        if accioninvalida=='URL invalida':
#            borraTicket (naccion, BBDD=False)
#            return 'Accion invalida'
#
#        analisisalcista=analisisAlcistaAccion(naccion)
#
#    alcista,soporteanterior=analisisalcista
#    resistencia,soporte,ruptura,LTi,LTf,timming=alcista
#
#    print alcista

def borraTicket (ticket, **config):
    """
    
    """
    tickets = obtenTicketsBBDD(ticket)
    cursor, db = conexionBBDD()
    ticket = ticket.upper()
    BBDD = config.get('BBDD', True)
    archivos = config.get('archivos', True)
    codigo = config.get('codigo', True)
    #cursor,db=conexionBBDD()

    if ticket != '' or ticket != ' ' or ticket != None:
        if BBDD:
            print('Borrando de la BBDD el ticket %s' % ticket)

            sql = "SELECT `componentes`.`codigo` FROM `componentes` WHERE (`componentes`.`tiket` = '" + ticket + "')"
            cursor.execute(sql)
            codigo = cursor.fetchall()
            numeroResultado = len(codigo)
            if numeroResultado == 1:
                codigo = str(codigo[0][0])
                sql = "SELECT `params_operaciones`.`id` FROM `params_operaciones` WHERE (`params_operaciones`.`codigo`=" + codigo + ")"
                cursor.execute(sql)
                numeroResultado = len(cursor.fetchall())
                if numeroResultado == 1:
                    sql = "DELETE FROM `params_operaciones` WHERE `params_operaciones`.`codigo`= " + codigo
                    cursor.execute(sql)
                sql = "DELETE FROM `componentes` WHERE `componentes`.`tiket` = '" + ticket + "'"
                cursor.execute(sql)

            sql = "SELECT `maximini`.`nombre` FROM `maximini` WHERE (`maximini`.`nombre` = '" + ticket + "')"
            cursor.execute(sql)
            numeroResultado = len(cursor.fetchall())
            if numeroResultado == 1:
                sql = "DELETE FROM `maximini` WHERE `maximini`.`nombre`='" + ticket + "' "
                cursor.execute(sql)
            sql = "DELETE FROM `nombreticket` WHERE `nombreticket`.`nombre`='" + ticket + "' "
            cursor.execute(sql)
            db.commit()

        if archivos:
            print('Borrando los Archivos de Registro del ticket %s' % ticket)
            if ticket in tickets:
                nombre = (str(ticket) + str(tickets[ticket])).replace('.', '_')
                for carpeta in carpetas.keys():
                    archivosticket = glob.glob(os.path.join(os.getcwd(), carpetas[carpeta], nombre + ".*"))
                    for archivo in archivosticket:
                        os.remove(archivo)
                #archivosticket = glob.glob(os.path.join(os.getcwd(), "Analisis\\" + nombre + ".*"))
                #for archivo in archivosticket:
                #    os.remove(archivo)
                #archivosticket = glob.glob(os.path.join(os.getcwd(), "Historicos\\" + nombre + ".*"))
                #for archivo in archivosticket:
                #    os.remove(archivo)
                if codigo:
                    del tickets[ticket]

        print('')
        return True
    else:
        return False

def cambiaTicket (ticketviejo, ticketnuevo):
    """
    
    """
    ticketviejo = ticketviejo.upper()
    cursor, db = conexionBBDD()
    ticketnuevo = (ticketnuevo.upper()).strip('"')
    #cursor,db=conexionBBDD()

    sql = "SELECT * FROM `nombreticket` WHERE (`nombreticket`.`nombre`='" + ticketnuevo + "') "
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if numeroResultado == 0:
        sql = "INSERT INTO `nombreticket` (`nombre`,`fechaRegistro`,`fechaError`,`fechaActualizacion`) VALUES ('%s','%s',NULL, NULL)" % (ticketnuevo, date.today())
        cursor.execute(sql)

    sql = "SELECT * FROM `componentes` WHERE (`componentes`.`tiket`='" + ticketnuevo + "') "
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if numeroResultado == 0:
        sql = "UPDATE `componentes` SET `tiket`='" + ticketnuevo + "' WHERE `componentes`.`tiket` = '" + ticketviejo + "'"
        cursor.execute(sql)
    elif numeroResultado == 1:
        sql = "SELECT `componentes`.`codigo` FROM `componentes` WHERE (`componentes`.`tiket` = '" + ticketviejo + "')"
        cursor.execute(sql)
        codigo = cursor.fetchall()
        numeroResultado = len(codigo)
        if numeroResultado == 1:
            codigo = str(codigo[0][0])
            sql = "SELECT `params_operaciones`.`id` FROM `params_operaciones` WHERE (`params_operaciones`.`codigo`=" + codigo + ")"
            cursor.execute(sql)
            numeroResultado = len(cursor.fetchall())
            if numeroResultado == 1:
                sql = "DELETE FROM `params_operaciones` WHERE `params_operaciones`.`codigo`= " + codigo
                cursor.execute(sql)
            sql = "DELETE FROM `componentes` WHERE `componentes`.`tiket`='" + ticketviejo + "'"
            cursor.execute(sql)


    sql = "SELECT * FROM `maximini` WHERE (`maximini`.`nombre`='" + ticketnuevo + "') "
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if numeroResultado == 0:
        sql = "SELECT `maximini`.`id` FROM `maximini` WHERE (`maximini`.`nombre`='" + ticketviejo + "')"
        cursor.execute(sql)
        codigo = cursor.fetchall()
        numeroResultado = len(codigo)
        if numeroResultado == 1:
            codigo = str(codigo[0][0])
            sql = "UPDATE `maximini` SET `nombre` = '%s', `fechaRegistro` = '%s' WHERE `maximini`.`id` =%s" % (ticketnuevo, ((datetime.now()).strftime("%Y-%m-%d %H:%M:%S")), codigo)
            cursor.execute(sql)
    elif numeroResultado == 1:
        sql = "SELECT * FROM `maximini` WHERE (`maximini`.`nombre` = '" + ticketviejo + "')"
        cursor.execute(sql)
        numeroResultado = len(cursor.fetchall())
        if numeroResultado == 1:
            sql = "DELETE FROM `maximini` WHERE `maximini`.`nombre`='" + ticketviejo + "' "
            cursor.execute(sql)


    sql = "DELETE FROM `nombreticket` WHERE `nombreticket`.`nombre`='" + ticketviejo + "'"
    cursor.execute(sql)
    db.commit()

    print('El ticket %s ha cambiado a %s. Cambiandolo en BBDD' % (ticketviejo, ticketnuevo))
    print('')
    errorenTicket(ticketnuevo)
    borraTicket(ticketviejo)
    #borraTicket(ticketviejo, BBDD=False)# Se supone que esta funcion ya lo ha borrado, solo queremos borrar los archivos

def errorenTicket (ticket):
    """
    
    """
    ticket = ticket.upper()
    cursor, db = conexionBBDD()
    sql = "SELECT `nombreticket`.`fechaError` FROM `nombreticket` WHERE `nombreticket`.`nombre` = '" + ticket + "'"
    cursor.execute(sql)
    hayerror = cursor.fetchall()
    print('')
    print('Error en el proceso del Ticket %s, error almacenado en BBDD para darle prioridad en proximas actualizaciones' % ticket)
    print('')
    if hayerror[0][0] == None:#Solo almacenamos error si no habia otro error
        sql = "UPDATE `nombreticket` SET `fechaError` ='" + ((datetime.now()).strftime("%Y-%m-%d %H:%M:%S")) + "' WHERE `nombreticket`.`nombre`='" + ticket + "' "
        cursor.execute(sql)
        db.commit()

def actualizadoTicket(ticket):
    """
    
    """
    ticket = ticket.upper()
    cursor, db = conexionBBDD()
    sql = "UPDATE `nombreticket` SET `fechaActualizacion`='" + (datetime.now()).strftime("%Y-%m-%d %H:%M:%S") + "', `fechaError` = NULL  WHERE `nombreticket`.`nombre`='" + ticket + "' "
    cursor.execute(sql)
    db.commit()

def cotizacionesTicket(nombreticket):
    """
    
    """
    #global webheaders
    cursor, db = conexionBBDD()

    nombreticket = nombreticket.upper()
    # habilitar en la funcion la posibilidad de descargar multiples tickets, tienen que ir separados o unidos por '+'
    # Tendriamos que separar nombreticket con un split y obtener una lista, comprobar la longitud de la misma, hacer la descarga, leer las lineas, comparar la lista inicial con la lista obtenida, crear un bucle en el else despues del try de la conxion en el que actualiza la BBDD

    urldatos = "http://download.finance.yahoo.com/d/quotes.csv?s=" + nombreticket + "&f=nsxkhjgl1a2ve1&e=.csv"
    r = urllib2.Request(urldatos, headers = webheaders)
    datosurl = None
    while datosurl == None:
        try:
            #r = urllib2.Request(urldatos, headers = webheaders)
            f = urllib2.urlopen(r)
            #f= urllib.urlopen (urldatos)
            # TODO: mirar que pasa con espacios en blanco y en la 1 posicion
            datosurl = ((f.read().strip()).replace(',N/A', ',NULL')).decode('UTF-8')#UTF-16le
            f.close()
        except urllib2.HTTPError as e:
            print('Conexion Perdida')
            print(e.code)
            datosurl = None
            raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
        except (urllib2.URLError, IOError, urllib2.httplib.BadStatusLine) as e:
            print('Conexion Erronea')
            #print(e.reason)
            print(e)
            datosurl = None
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, nombreticket.encode('UTF-8'), urldatos.encode('UTF-8')))
            print ('Pausa de %d segundos' % pausareconexion)
            sleep (pausareconexion)
            #raw_input( 'Pulsa una tecla cuando este reestablecida la conexion para continuar' )
#        except IOError as e:
#            print('Conexion Erronea')
#            print(e)
#            datosurl = None
#            sleep (pausareconexion)
#            print ('Pausa de %d segundos' % pausareconexion)
#            #raw_input( 'Pulsa una tecla cuando este reestablecida la conexion para continuar' )

    datosurl2 = datosurl.rsplit(',', 10)
    datonombre , datoticket , datomercado , datomax52, datomaxDia, datomin52, datominDia, datoValorActual , datovolumenMedio , datovolumen , datoerror = datosurl2
    datoticket = datoticket.strip('"')

    #comillas = datosurl[1:].find('"')#Esto es porque en ocasiones el nombre lleva una coma
    #datonombre = datosurl[:(comillas + 2)]
    #datosurl2 = datosurl.split(',')
    #datomax52, datomaxDia, datomin52, datominDia, datoValorActual = datosurl2[-8], datosurl2[-7], datosurl2[-6], datosurl2[-5], datosurl2[-4]
    #datoticket = datosurl2[-10].strip('"')

        # hay que prevenir esto
    #"Fuel Tech, Inc.","FTEK","NasdaqNM",11.20,NULL,3.77,NULL,5.82,135258,0,"N/A"   coma en el nombre
    #"MI Developments I","MIM","NYSE",33.35,30.75,16.07,30.33,30.45,238848,136519,"N/A"

        #el ticket ha cambiado, comprobar que no existe ya y en tal caso sustuirlo
    if '"No such ticker symbol.' in datosurl or 'Missing Symbols List.' in datosurl:#".DJA",".DJA",N/A,0,"N/A",N/A,N/A,N/A,N/A,0.00,"No such ticker symbol. <a href="/l">Try Symbol Lookup</a> (Look up: <a href="/l?s=.DJA">.DJA</a>)"
        borraTicket(nombreticket)

    elif ('Ticker symbol has changed to: <a href="/q?s=' in datosurl):
        print (datosurl)
        ticketinicio = datosurl.find('<a href="/q?s=') + len ('<a href="/q?s=')
        ticketfin = datosurl.find('">', ticketinicio)
        ticketnuevo = (datosurl[ticketinicio:ticketfin]).strip('"')
        cambiaTicket(nombreticket, ticketnuevo)

    # hay casos en los que nos descargamos la informacion de nombreticket pero en la informacion descargada el ticket ha cambiado
    elif datoticket != nombreticket :
        print (datosurl)
        #ticketnuevo = ( datosurl2[-10].strip( '"' ) )
        cambiaTicket(nombreticket, datoticket)

    else:
        sql = "SELECT * FROM `componentes` WHERE `tiket` = '" + nombreticket + "'"
        cursor.execute(sql)
        datosBBDDcomponentes = cursor.fetchall()
        numeroResultado = len(datosBBDDcomponentes)
        if numeroResultado == 0:
            sql = "INSERT INTO `componentes` (`codigo` ,`nombre` ,`tiket` ,`mercado` ,`max52` ,`maxDia` ,`min52` ,`minDia` ,`valorActual` ,`volumenMedio` ,`volumen` ,`error` ,`fechaRegistro`) VALUES (NULL , " + datosurl + ",'" + str(date.today()) + "')"
            cursor.execute(sql)

        elif numeroResultado == 1:
            codigo = datosBBDDcomponentes[0][0]
            sql = "UPDATE `componentes` SET `nombre`= %s, `mercado`=%s ,`max52`=%s ,`maxDia`=%s ,`min52`=%s ,`minDia`=%s ,`valorActual`=%s ,`volumenMedio`=%s ,`volumen`=%s ,`error`=%s ,`fechaRegistro`='%s'  WHERE `componentes`.`tiket` = '%s'" % (datonombre, datomercado , datomax52, datomaxDia, datomin52, datominDia, datoValorActual , datovolumenMedio , datovolumen , datoerror, date.today(), nombreticket)
            #sql = "UPDATE `componentes` SET `nombre`= %s, `mercado`=%s ,`max52`=%s ,`maxDia`=%s ,`min52`=%s ,`minDia`=%s ,`valorActual`=%s ,`volumenMedio`=%s ,`volumen`=%s ,`error`=%s ,`fechaRegistro`='%s'  WHERE `componentes`.`tiket` = '%s'" % (datonombre, datosurl2[-9], datosurl2[-8], datosurl2[-7], datosurl2[-6], datosurl2[-5], datosurl2[-4], datosurl2[-3], datosurl2[-2], datosurl2[-1], date.today(), nombreticket)
            cursor.execute(sql)
            sql = "SELECT * FROM `params_operaciones` WHERE `params_operaciones`.`codigo` = %s" % codigo
            cursor.execute(sql)
            datosBBDDoperaciones = cursor.fetchall()
            numeroResultado = len(datosBBDDoperaciones)
            if numeroResultado == 1:
                ident, precio_ini, precio_fin, _fecha_ini, _fecha_fin, _timing, _precio_salida, salida, entrada, _rentab, _codigoBBDD = datosBBDDoperaciones[0]

                if salida == None or salida == '':
                    salida = 0.0
                if entrada == None or salida == '':
                    entrada = 0.0

                if precio_ini <= precio_fin:# datos de una accion alcista
                    if (datomax52 != 'NULL' and datomax52 > entrada) or (datomaxDia != 'NULL' and datomaxDia > entrada) or (datoValorActual != 'NULL' and datoValorActual > entrada):# si true, analisis ya cumplido, obsoleto y lo actualizamos
                        sql = "UPDATE `params_operaciones` SET `entrada` = NULL, `salida` = NULL, `precio_salida` = %.3f WHERE `params_operaciones`.`id` =%s" % (salida, ident)
                        cursor.execute(sql)

                if precio_ini > precio_fin:# datos de una accion bajista
                    if (datomin52 != 'NULL' and datomin52 < entrada) or (datominDia != 'NULL' and datominDia < entrada) or (datoValorActual != 'NULL' and datoValorActual < entrada):
                        sql = "UPDATE `params_operaciones` SET `entrada` = NULL, `salida` = NULL, `precio_salida` = %.3f WHERE `params_operaciones`.`id` =%s" % (salida, ident)
                        cursor.execute(sql)
            #en este update, habra que comprobar la table params_operaciones para hacer que borre los analisis obsoletos

        print('Actualizando cotizaciones de : %s' % nombreticket)
        print('Actualizando %s con datos %s' % (nombreticket , datosurl))
        db.commit()
        actualizadoTicket(nombreticket)

def cotizacionesMoneda(nombreticket):
    """
    
    """
    #global webheaders
    cursor, db = conexionBBDD()
    nombreticket = nombreticket.upper()

    #http://download.finance.yahoo.com/d/quotes.csv?s=EURUSD=X&f=sl1d1t1c1ohgv&e=.csv
    urldatos = "http://download.finance.yahoo.com/d/quotes.csv?s=" + nombreticket + "&f=sl1e1&e=.csv"

    datosurl = None
    while datosurl == None:
        try:
            r = urllib2.Request(urldatos, headers = webheaders)
            f = urllib2.urlopen(r)
            #f= urllib.urlopen (urldatos)
            datosurl = ((f.read().strip()).replace(',N/A', ',NULL')).decode('UTF-8')#UTF-16le
            f.close()
        except urllib2.HTTPError as e:
            print('Conexion Perdida')
            print(e.code)
            datosurl = None
            raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
        except (urllib2.URLError, IOError, urllib2.httplib.BadStatusLine) as e:
            print('Conexion Erronea')
            #print(e.reason)
            print(e)
            datosurl = None
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, nombreticket.encode('UTF-8'), urldatos.encode('UTF-8')))
            print ('Pausa de %d segundos' % pausareconexion)
            sleep (pausareconexion)
            #raw_input( 'Pulsa una tecla cuando este reestablecida la conexion para continuar' )
#        except IOError as e:
#            print('Conexion Erronea')
#            print(e)
#            datosurl = None
#            sleep (pausareconexion)
#            print ('Pausa de %d segundos' % pausareconexion)
#            #raw_input( 'Pulsa una tecla cuando este reestablecida la conexion para continuar' )

    datosurl2 = datosurl.split(',')
    datoticket = datosurl2[0].strip('"')
    datoprecio = datosurl2[1]
    if nombreticket == 'EURGBP=X':
        print ('Caso especial, libra Esterlina convertida en peniques')
        datoprecio = str(float(datoprecio) * 100)

    if '"No such ticker symbol.' in datosurl or 'Missing Symbols List.' in datosurl:#".DJA",".DJA",N/A,0,"N/A",N/A,N/A,N/A,N/A,0.00,"No such ticker symbol. <a href="/l">Try Symbol Lookup</a> (Look up: <a href="/l?s=.DJA">.DJA</a>)"
        print(('La Moneda %s no existe' % nombreticket))

    elif ('Ticker symbol has changed to: <a href="/q?s=' in datosurl) or datoticket != nombreticket:
        print (datosurl)
        print(('La Moneda %s ha cambiado a %s' % (nombreticket, datoticket)))

    else:

        sql = "SELECT `codigo` FROM `monedas` WHERE `url_Inet` = '" + nombreticket + "'"
        cursor.execute(sql)
        datosBBDDcomponentes = cursor.fetchall()
        codigo = datosBBDDcomponentes[0][0]
        #sql = "UPDATE `lomiologes_cobodb`.`monedas` SET `valor` = '%s', `fechaRegistro` = '%s' WHERE `monedas`.`codigo` = '%s'" % (datoprecio , (datetime.now()).strftime("%Y-%m-%d %H:%M:%S") , codigo)
        sql = "UPDATE `monedas` SET `valor` = '%s', `fechaRegistro` = '%s' WHERE `monedas`.`codigo` = '%s'" % (datoprecio , (datetime.now()).strftime("%Y-%m-%d %H:%M:%S") , codigo)
        cursor.execute(sql)
        db.commit()

        print('Actualizando cotizaciones de : %s' % nombreticket)
        print('Actualizando %s con datos %s' % (nombreticket , datosurl))



def pidedato(texto, tipodato):
    """
    salida de texto,
    tipo de dato correcto (int/float/str) comprobando que es valido y si no lo es, bucle que no nos permite meter no valido
    valor por defecto
    """
    entrada = raw_input(texto)

    # falta o bien comprobar que el dato introducido es correcto y si no, bucle para volver a introducirlo, o hacer un try para controlar el error en la conversiones
    if tipodato == 'int':
        entrada = int(entrada)
    elif tipodato == 'float':
        entrada = float(entrada)
    elif tipodato == 'str':
        entrada = str(entrada)

    return entrada


def pidefecha():
    """

    """
    while True:
        fecha = raw_input('Backtest a analizar desde la fecha AAAA-MM-DD (sin fecha inicio): ')

        if fecha == '':
            return False

        for digito in fecha:
            if digito in '01234567890-':
                digito = True
            else:
                digito = False
                break

        if fecha[4] == '-' and fecha[7] == '-':
            separadores = True
        else:
            separadores = False

        Mes = int(fecha[5:7])
        Dia = int(fecha[8:10])
        Longitud = len(fecha)

        if separadores and digito and Longitud == 10 and Mes < 13 and Dia < 32:
            return fecha

        print('Formato de fecha mal introducido. Vuelve a intentarlo')

def obtenTicketsBBDD(ticket = None):
    """
    
    """
    cursor, _db = conexionBBDD()
    if ticket == None:
        sql = "SELECT `componentes`.`tiket`, `componentes`.`codigo` FROM `componentes` ORDER BY `componentes`.`tiket` ASC"
    else:
        sql = ("SELECT `componentes`.`tiket`, `componentes`.`codigo` FROM `componentes` WHERE (`componentes`.`tiket` = '%s') ORDER BY `componentes`.`tiket` ASC" % ticket)
#        sql="SELECT `componentes`.`tiket`, `componentes`.`codigo` FROM `componentes` WHERE `componentes`.`error` = 'N/A' ORDER BY `componentes`.`tiket` ASC"
    tickets = {}
    cursor.execute(sql)
    resultado = cursor.fetchall()
    if resultado != None:


        for registro in resultado:
            #if not tickets.has_key(registro[0]):
    #                if registro[0][0]=='.':
    #                    ticket='^'+registro[0][1:].upper()
    #                else:
    #                    ticket=registro[0].upper()
            tickets[registro[0]] = (registro[1])

        return tickets
    else:
        return False

def obtenMercadosBBDD():
    """
    
    """
    cursor, _db = conexionBBDD()
    sql = "SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo` ='MERCADOS_OBTENER_COMPONENTES')"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    resultado = (resultado[0][0].strip("'")).split(',')
    mercados = []
    for m in resultado:
        sql = "SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo` ='" + m + "')"
        cursor.execute(sql)
        resultadoM = cursor.fetchall()
        resultadoM = resultadoM[0][0].strip("'").split(',')

        for mercado in resultadoM:
            mercado = mercado.replace('@%5E', '^')
            mercado = mercado.replace('@%5e', '^')
            if not (mercado in mercados):
                mercados.append(mercado)

    return mercados

def conexionBBDD():
    """
    
    """
    try:
        db = sqlite3.connect(os.path.join(os.getcwd(), "Cobo.dat"))
        #db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '0000', db = 'lomiologes_cobodb')
        cursor = db.cursor()
	#TODO: Crear excepcion especifica para cuando no se encuentra el archivo
	#Crear el archivo Cobo.dat, y ejecutar Cobo.sql para "rellenar" la Base de datos desde "cero"
    except:
        raw_input ('Base de datos no habilitada. Para que el programa funcione necesitas conexion a la base de datos')
        quit()
    else:
        return cursor, db



#def log(**config):
#    """
#    la ubicacion deberia ser igual a __name__ de la funcion donde viene
#    nombrelog=archivo dondes queremos guardar el registro, normalmente nombre da la funcion donde queremos ubicar la funcion
#    error = Mensaje del error o causa del mismo, normalmente capturamos el error o le asignamos el nombre de la excepcion
#    explicacion = ubicacion y explicacion de las variables, son constantes ('Fecha; Tipo Error; Ubicacion; ')
#    variables = lista con breve explicacion y variables que nos interesa registrar
#    """
#    nombrelog = config.get('nombrelog', 'Cobo')
#    error = str(config.get('error', ''))
#    explicacion = 'Fecha; Tipo Error; Ubicacion; ' + (config.get('explicacion', '')) + '\n'
#    variables = ((((str(config.get('variables', dir()))).strip('(')).strip(')')).strip()).replace(',', ';')
#
#
#    if nombrelog == '':
#        nombrelog = 'Cobo'
#
#    archivo = os.path.join(os.getcwd(), carpetas['Log'], nombrelog + ".log")
#    linea = (((datetime.now()).strftime("%Y-%m-%d %H:%M")) + ';' + error + ';' + variables + '\n')
#
#    if not os.path.exists(archivo):
#
#        f = open(archivo, "w")
#        f.write(explicacion)
#        f.write(linea)
#        f.close()
#
#    else:
#        f = open(archivo, "a")
#        f.write(linea)
#        f.close()
#
#    return

#def compruebaactualizaticket(naccion):
#def actualizartickets():

# verificacion de la funcion para casos tipo

############################################################
# programa principal

# Valor inicial de las estructuras de datos

#bonito.empieza()


# he supuesto que haciendo que esto se ejecute no siendo el programa principal, podre import cobo externamente y poder utilizar sus funciones
#tickets = {}
#mercados = []

#archivoslogs = glob.glob( os.path.join( os.getcwd(), "log\\*.log" ) )
#for archivo in archivoslogs:
#    os.remove( archivo )

if __name__ == '__main__':

    for carpeta in carpetas.keys():
        nombrecarpeta = os.path.join(os.getcwd(), carpetas[carpeta])
        if not os.path.exists(nombrecarpeta):
            os.mkdir(nombrecarpeta)
            #os.path.dirname

    #os.spawnl( os.P_NOWAIT, 'C:\\xampp\\mysql\\bin\mysqld.exe --defaults-file=C:\\xampp\\mysql\\bin\\my.ini --standalone --console' )

    cursor, db = conexionBBDD()

    # Elimina los Tickets de los mercados que no nos interesan
    for n in sufijosexcluidos:
        sql = "SELECT `nombre` FROM `nombreticket` WHERE `nombre` LIKE '%" + n + "'"
        #sql = ("DELETE FROM `lomiologes_cobodb`.`nombreticket` WHERE `nombreticket`.`nombre` = '%" + n + "'")
        cursor.execute(sql)
        listatickets = cursor.fetchall()
        numeroResultado = len(listatickets)
        if numeroResultado > 0:
            listatickets = ((ticket[0]) for ticket in listatickets)
            listatickets = deque(list(listatickets))
            #for ticket in listatickets:
            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                print ('Quedan por borrar %d tickets' % len(listatickets))
                borraTicket(ticket)
    #db.commit()
    # Con esta consulta podemos comprobar los tickets que no existen en componentes y si en nombreticket, despues de hacer una insercion masiva,....
    # SELECT * FROM `nombreticket` WHERE `nombre` not in (SELECT `tiket` FROM `componentes`)


#    ficheroDatos=os.path.join(os.getcwd(),"\\Cobo.pck")
#    if not os.path.exists(ficheroDatos):
#        tickets = {}
#        mercados = []
#
#        datos = {'tickets':tickets, 'mercados':mercados}
#        codificado=pickle.dumps(datos)
#        f=open(ficheroDatos,"w")
#        f.write(codificado)
#        f.close()
#    else:
#        f=open(ficheroDatos,"r")
#        datos=f.read()
#        f.close()
#        datos = pickle.loads(datos)
#        tickets = datos['tickets']
#        mercados = datos['mercados']
#
#    print
#    if basedatos:
#        sql="SELECT `componentes`.`tiket`, `componentes`.`codigo` FROM `componentes` ORDER BY `componentes`.`tiket` ASC"
##        sql="SELECT `componentes`.`tiket`, `componentes`.`codigo` FROM `componentes` WHERE `componentes`.`error` = 'N/A' ORDER BY `componentes`.`tiket` ASC"
#
#        cursor.execute(sql)
#        resultado=cursor.fetchall()
#        for registro in resultado:
#            #if not tickets.has_key(registro[0]):
#            if registro[0][0]=='.':
#                ticket=('^'+registro[0][1:]).upper()
#            else:
#                ticket=registro[0].upper()
#            tickets[ticket]=(registro[1])
## elimino estos tickets porque son nombres de archivos no permitidos y no podiramos crear los archivos de datos de estas acciones
## problema a resolver en el futuro
#
##        try:
##            del tickets['CON.DE']
##            del tickets['AUX.V']
##            del tickets['PRN']
##            del tickets['CON.L']
##        except KeyError:
##            print 'Los tickets problematicos CON.DE, AUX.V ,PRN y CON.L no existen en la base de datos'
#
#
#        sql="SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo` ='MERCADOS_OBTENER_COMPONENTES')"
#        cursor.execute(sql)
#        resultado=cursor.fetchall()
#        resultado=(resultado[0][0].strip("'")).split(',')
#        for m in resultado:
#            sql="SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo` ='"+m+"')"
#            cursor.execute(sql)
#            resultadoM=cursor.fetchall()
#            resultadoM=resultadoM[0][0].strip("'").split(',')
#
#            for mercado in resultadoM:
#                mercado=mercado.replace('@%5E','^')
#                mercado=mercado.replace('@%5e','^')
#                if not (mercado in mercados):
#                    mercados.append(mercado)
#
#    print 'Total de mercados %d'%(len(mercados))
#    print 'Total de tickets %d'%(len(tickets.keys()))


    opcion = None
    while True:

        cursor, db = conexionBBDD()
        tickets = obtenTicketsBBDD()
        mercados = obtenMercadosBBDD()


        print('')
        if opcion == None:

            print('Total de mercados : %d' % (len(mercados)))
            print('Total de tickets : %d' % (len(tickets.keys())))

            sql = "SELECT `nombre` FROM `nombreticket` WHERE `fechaError` is not null"
            cursor.execute(sql)
            numeroResultado = len(cursor.fetchall())
            print('Tickets con errores : %d' % numeroResultado)

            diaspasados = (datetime.now() - timedelta(days = difregactualizar['w'])).strftime("%Y-%m-%d %H:%M:%S")
            diasfuturos = (datetime.now() + timedelta(days = 1)).strftime("%Y-%m-%d %H:%M:%S")
            sql = "SELECT `nombre` FROM `nombreticket` WHERE (`fechaActualizacion`<'" + diaspasados + "' or `fechaActualizacion`>'" + diasfuturos + "' or `fechaActualizacion` IS NULL or `fechaError` IS NOT NULL) ORDER BY `nombreticket`.`fechaError` DESC, `nombreticket`.`fechaActualizacion` ASC"
            cursor.execute(sql)
            numeroResultado = len(cursor.fetchall())
            print('Tickets pendientes de realiar una actualizacion : %d' % numeroResultado)
            sql = "SELECT * FROM `nombreticket` WHERE `nombre` not in (SELECT `tiket` FROM `componentes`)"
            cursor.execute(sql)
            numeroResultado = len(cursor.fetchall())
            print('Tickets necesitan de actualizar completamente : %d' % numeroResultado)

            iopciones = 0
            opciones = creaMenu(')', (
            'Acciones para un solo ticket',
            '------------------------------',
            'A) Alta/Actualizar/Descargar Datos de 1 Ticket',
            'B) Corregir Datos de 1 Ticket',
            'C) Analizar Datos de 1 Ticket',
            'D) Eliminar 1 Ticket',
            'E) Generar Archivos Grafico',
            '',
            'Acciones para los mercados',
            '------------------------------',
            'F) Listar Tickets Mercados',
            'G) Anadir Ticket Mercado',
            'H) Eliminar Ticket Mercado',
            '',
            'Acciones para las monedas',
            '-------------------------------',
            'I) Actualizar cotizaciones de las Monedas',
            '',
            'Acciones para todos los tickets en BBDD',
            '------------------------------',
            'L) Listar Tickets',
            'M) Actualizar Tickets componentes de Mercados',
            'N) Actualizar cotizaciones de todos los Tickets',
            'O) Actualizar/Descargar Datos Cotizaciones Historicas todos los Tickets',
            'P) Actualizar Max/Min Historicos de todos los Tickets',
            'Q) Analizar Datos de todos los Tickets',
            '------------------------------',
            '',
            'S) BackTest',
            '',
            '------------------------------',
            'Acciones Masivas',
            '------------------------------',
            'V) Exportar datos a arhivos csv',
            'W) Dar de alta acciones desde archivo',
            '------------------------------',
            '',
            'X) Guardar Datos',
            'Z) Salir'))
            print('')
        opcion, seleccion = opciones[iopciones]
        iopciones += 1


#'A) Alta/Actualizar/Descargar Datos de 1 Ticket'
        if opcion == 'a':
            print(seleccion)

            naccion = raw_input('Introduce ticket de la accion : ').upper()
            naccion = (naccion,)
            cursor.execute("SELECT *  FROM `nombreticket` WHERE (`nombreticket`.`nombre` = ?)", naccion)
            numeroResultado = len(cursor.fetchall())
            if numeroResultado == 0:
                cursor.execute("INSERT INTO `nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES (?, '" + str(date.today()) + "', NULL, NULL)", naccion)
                db.commit()
                print(naccion[0] + ' anadido a la base de datos')

            if not ExistenDatos(naccion[0]):
                print('Ticket %s nuevo, descarga completa del historico de la accion' % naccion[0])
                cotizacionesTicket(naccion[0])

                for timmingdescargado in 'dwm':

                    accioninvalida = descargaHistoricoAccion (naccion[0], timming = timmingdescargado)
                    duerme()

            else:
                print('Ticket %s ya descargado, comprobando la actualizacion de los datos' % naccion[0])
                for timmingdescargado in 'dwm':

                    fechaactualizar, timmingactualizar, actualizaractualizar = actualizacionDatosHisAccion(naccion[0], timming = timmingdescargado)

                    if actualizaractualizar:# and (desdefechamodificacionarchivo(datosaccion)):

                        accioninvalida = descargaHistoricoAccion(naccion[0], fechaini = fechaactualizar, timming = timmingactualizar, actualizar = actualizaractualizar)
                        duerme()
                    else:
                        accioninvalida = None

                    if accioninvalida == 'Pago Dividendos':
                        borraTicket (naccion[0], BBDD = False)# no los borramos de la BBDD porque cuando tienen muy poco historico a veces no se puede descargar
                        print('Reintento de la descarga, el error viene de un pago de Dividendos')
                        for timmingdescargado in 'dwm':

                            accioninvalida = descargaHistoricoAccion (naccion[0], timming = timmingdescargado)
                            duerme()

                    if accioninvalida == 'URL invalida':
                        borraTicket (naccion[0])

#        'B) Corregir Datos de 1 Ticket',
        elif opcion == 'b':
            print(seleccion)
            naccion = raw_input('Introduce nombre de la accion : ').upper()

            if ExistenDatos(naccion):
                corregirDatosHistoricosAccion(naccion)
            else:
                print('Ticket no descargado, hay que hacer la descarga previa de los datos historicos del ticket')


#        'C) Analizar Datos de 1 Ticket',
        elif opcion == 'c':
            print(seleccion)
            while True:
                naccion = raw_input('Introduce ticket de la accion : ').upper()
                if ExistenDatos(naccion):
                    break
                else:
                    print('Accion no descargada o no figura entre la lista de acciones')
                    errorenTicket(naccion)

            analizardesde = pidefecha()
            MMe = raw_input('Media Movil Exponencial (Sin MME): ')
            if MMe == '':
                MMe = False
            else:
                MMe = int(MMe)
            EntradaLT = raw_input('Entradas en Linea de Tendencia (Sin Entradas): ')
            if EntradaLT == '':
                EntradaLT = False
            else:
                EntradaLT = True
            filtrosalidamensual = raw_input('Filtro de salida Mensual por operacion, % (0.03): ')
            if filtrosalidamensual == '':
                filtrosalidamensual = 0.03
            else:
                filtrosalidamensual = float(filtrosalidamensual)
            filtrosalidasemanal = raw_input('Filtro de salida Semanal por operacion, % (0.02): ')
            if filtrosalidasemanal == '':
                filtrosalidasemanal = 0.02
            else:
                filtrosalidasemanal = float(filtrosalidasemanal)
            filtrosalidadiario = raw_input('Filtro de salida Diario por operacion, % (0.01): ')
            if filtrosalidadiario == '':
                filtrosalidadiario = 0.01
            else:
                filtrosalidadiario = float(filtrosalidadiario)

            if ExistenDatos(naccion):
                for timminganalisis in 'dwm':
                    print('Timming del analisis: ', timminganalisis)
                    if timminganalisis == 'w':
                        filtrosalida = filtrosalidasemanal
                    elif timminganalisis == 'm':
                        filtrosalida = filtrosalidamensual
                    elif timminganalisis == 'd':
                        filtrosalida = filtrosalidamensual
                    else:
                        filtrosalida = 0.0

                    analisisAlcistaAccion(naccion, timming = timminganalisis, desdefecha = analizardesde, MME = MMe, conEntradaLT = EntradaLT, filtro = filtrosalida)#,txt=False)
                    analisisBajistaAccion(naccion, timming = timminganalisis, desdefecha = analizardesde, MME = MMe, conEntradaLT = EntradaLT, filtro = filtrosalida)#,txt=False)


#        'D) Eliminar 1 Ticket',
        elif opcion == 'd':
            print(seleccion)
            naccion = raw_input('Introduce nombre de la accion : ').upper()

            borraTicket(naccion)


#        'E) Generar Archivos Grafico'
        elif opcion == 'e':
            print(seleccion)

            while True:
                ticket = raw_input('Introduce ticket de la accion : ').upper()
                if ExistenDatos(ticket):
                    break
            historicoMensual, historicoSemanal, historicoDiario, correcciones = LeeDatos(ticket)
            ticket = (ticket,)
            cursor.execute("SELECT `nombre` FROM `componentes` WHERE `componentes`.`tiket` LIKE ?", ticket)
            nombre = cursor.fetchall()
            nombre = (nombre[0][0].strip('"')).replace(',', '')

            print(' 1 - Diario')
            print(' 2 - Semanal')
            print(' 3 - Mensual')
            timming = 'None'
            while timming not in ('123 '):
                timming = raw_input('Introduce Timming de los Datos a Generar (Mensual):')

            if timming == '1':
                datos = historicoDiario
            elif timming == '2':
                datos = historicoSemanal
            elif timming == '3' or timming == '' or timming == ' ':
                datos = historicoMensual

            archivo = os.path.join(os.getcwd(), carpetas['Graficos'], "data.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter = ';', lineterminator = '\n', doublequote = True)
            for n in datos:
                writercsv.writerow(n)
                #j.write(str(n)+'\n')
            j.close()

            archivo = os.path.join(os.getcwd(), carpetas['Graficos'], "metatrader.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter = ',', lineterminator = '\n', doublequote = True)
            j.write('<TICKER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>\n')
            for n in datos:
                fecha, apertura, maximo, minimo, cierre, volumen = n
                fecha = fecha.replace('-', '')

                writercsv.writerow((ticket, fecha, '000000', apertura, maximo, minimo, cierre, volumen))
                #j.write(str(n)+'\n')
            j.close()

            archivo = os.path.join(os.getcwd(), carpetas['Graficos'], 'metastock.csv')
            j = open(archivo, 'w')
            j.write('<TICKER>,<NAME>,<PER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>\n')
            writercsv = csv.writer(j, delimiter = ',', lineterminator = '\n', doublequote = True)
            for n in datos:

                fecha, apertura, maximo, minimo, cierre, volumen = n
                fecha = fecha.replace('-', '')

                writercsv.writerow ((ticket, nombre, timming, fecha, '000000', apertura, maximo, minimo, cierre, volumen, '0'))
            j.close()

            MMEdatos = raw_input('Introduce Catidad de periodos para el indicadorMME (30):')

            if MMEdatos == '30' or MMEdatos == '' or MMEdatos == ' ':
                MMEdatos = 30
            else:
                MMEdatos = int(MMEdatos)

            datosMME = indicadorMME(datos, MME = MMEdatos)

            archivo = os.path.join(os.getcwd(), carpetas['Graficos'], "MME.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter = ';', lineterminator = '\n', doublequote = True)
            for n in datosMME:
                writercsv.writerow(n)
            j.close()

            TARdatos = raw_input('Introduce Catidad de periodos para el indicadorTAR (10):')

            if TARdatos == '10' or TARdatos == '' or TARdatos == ' ':
                TARdatos = 10
            else:
                TARdatos = int(TARdatos)

            datosTAR = indicadorTAR(datos, TAR = TARdatos)

            archivo = os.path.join(os.getcwd(), carpetas['Graficos'], "TAR.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter = ';', lineterminator = '\n', doublequote = True)
            for n in datosTAR:
                writercsv.writerow(n)
            j.close()


#        'F) Listar Tickets Mercados',
        elif opcion == 'f':
            print(seleccion)
            for mercado in mercados:
                print (mercado)
            print('Total de mercados %d' % (len(mercados)))

        #G) Anadir Ticket Mercado',
        elif opcion == 'g':
            print(seleccion)
            mercado = raw_input('Introduce ticket del mercado a anadir : ').upper()
            mercado = mercado.replace('@%5E', '^')
            mercado = (mercado,)
            if not (mercado[0] in mercados):
                sql = "SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo` ='MERCADOS_OBTENER_COMPONENTES')"
                cursor.execute(sql)
                resultadoM = cursor.fetchall()
                print(resultadoM)
                m = None
                while m in resultadoM:
                    m = raw_input ('Del los conjuntos anteriores, Introduce donde quieres anadir el mercado :').upper()
                m = (m,)
                cursor.execute("SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo`  = ?)", m)
                mercadosvalidos = cursor.fetchall()
                numeroResultado = len(mercadosvalidos)
                if numeroResultado == 1:
                    mercadosvalidos = list(mercadosvalidos[0])
                    mercadosvalidos.append(mercado)
                    mercadosvalidos = str(mercadosvalidos)
                    mercadosvalidos = mercadosvalidos.strip('[')
                    mercadosvalidos = mercadosvalidos.strip(']')
                    mercadosvalidos = mercadosvalidos.replace("'", "")
                    mercadosvalidos = mercadosvalidos.replace('"', '')
                    mercadosvalidos = mercadosvalidos.replace(' ', '')

                    cursor.execute("UPDATE `configuracion` SET valor = '" + mercadosvalidos + "' WHERE (`configuracion`.`codigo` =?)", m)
                    db.commit()
                    mercados.append(mercado)

            else:
                print(('El mercado %s ya esta en la lista de mercados' % mercado))
            print('Total de mercados %d' % (len(mercados)))

#        'H) Eliminar Ticket Mercado',
        elif opcion == 'h':
            print(seleccion)
            mercado = raw_input('Introduce ticket del mercado a borrar : ').upper()
            mercado = mercado.replace('@%5E', '^')
            if not (mercado in mercados):
                print(('El mercado %s no existe en la lista de mercados' % mercado))
            else:
                mercados.remove(mercado)
            print('Total de mercados %d' % (len(mercados)))

#        'I) Actualizar cotizaciones monedas
        elif opcion == 'i':
            print(seleccion)
            sql = "SELECT `url_Inet` FROM `monedas`"
            cursor.execute(sql)
            urlmonedas = cursor.fetchall()
            urlmonedas = ((moneda[0]) for moneda in urlmonedas)
            urlmonedas = deque(list(urlmonedas))

            while len(urlmonedas) > 0:
                moneda = urlmonedas.popleft()
                cotizacionesMoneda(moneda)
                duerme()
                print('Quedan por actualizar un total de : %d' % len(urlmonedas))


#        'L) Listar Tickets',
        elif opcion == 'l':
            listatickets = tickets.keys()
            listatickets.sort()
            ticketsnoBBDD = 0
            for ticket in listatickets:
                print(ticket , tickets[ticket])
                if tickets[ticket] == '' or tickets[ticket] == 0:
                    ticketsnoBBDD = +1
            print(('Total de tickets %d' % (len(tickets))))
            print('Tickets que no estan en la BBDD : %s' % ticketsnoBBDD)

            del listatickets, ticketsnoBBDD

#        'M) Actualizar Tickets componentes de Mercados',
        elif opcion == 'm':
            print(seleccion)
            sql = "SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo` ='MERCADOS_OBTENER_COMPONENTES')"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            resultado = (resultado[0][0].strip("'")).split(',')
            for m in resultado:
                sql = "SELECT `configuracion`.`valor` FROM `configuracion` WHERE (`configuracion`.`codigo` ='" + m + "')"
                cursor.execute(sql)
                resultadoM = cursor.fetchall()
                resultadoM = resultadoM[0][0].strip("'").split(',')
                ticketsanadidos = 0
                mercadosvalidos = []
                for mercado in resultadoM:
                    mercado = mercado.replace('@%5E', '^')
                    mercado = mercado.replace('@%5e', '^')
                    mercado = mercado.upper()
                    ticketscomponentesmercados = ticketsdeMercado(mercado)
                    for ticket in ticketscomponentesmercados:
                        sql = "SELECT * FROM `nombreticket` WHERE `nombre` = '" + ticket + "'"
                        cursor.execute(sql)
                        numeroResultado = len(cursor.fetchall())
                        if numeroResultado == 0:
                            sql = "INSERT INTO `nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES ('" + ticket + "', '" + str(date.today()) + "', NULL, NULL)"
                            cursor.execute(sql)
                            print(ticket + ' anadido a la base de datos')
                            ticketsanadidos += 1

                    if len(ticketscomponentesmercados) > 0:
                        mercadosvalidos.append(mercado)

                    del ticketscomponentesmercados

                mercadosvalidos2 = ''
                for mer in mercadosvalidos:
                    mercadosvalidos2 = mercadosvalidos2 + ',' + mer
                mercadosvalidos = mercadosvalidos2.strip(',')

                sql = "UPDATE `configuracion` SET valor = '" + mercadosvalidos + "' WHERE (`configuracion`.`codigo` ='" + m + "')"
                cursor.execute(sql)
                db.commit()
                print("Total tickets anadidos %s" % ticketsanadidos)
                del ticketsanadidos, mercadosvalidos


#        'N) Actualizar cotizaciones de todos los Tickets',
        elif opcion == 'n':
            print(seleccion)
            diaspasados = (datetime.now() - timedelta(days = difregactualizar['w'])).strftime("%Y-%m-%d %H:%M:%S")
            diasfuturos = (datetime.now() + timedelta(days = 1)).strftime("%Y-%m-%d %H:%M:%S")
            # si en este select hacemos una comparacion de la fecha actual con la fecha de actualizacion, obtendremos directamente la lista a actualizar, comparando las fechas por haber pasado mas de una cantidad de tiempo desde la ultima actualizacion o las que esten supuestamente actualizadas mas alla de la fecha actual
            sql = "SELECT `nombre` FROM `nombreticket` WHERE (`fechaActualizacion`<'" + diaspasados + "' or `fechaActualizacion`>'" + diasfuturos + "' or `fechaActualizacion` IS NULL or `fechaError` IS NOT NULL) ORDER BY `nombreticket`.`fechaError` DESC, `nombreticket`.`fechaActualizacion` ASC"
            cursor.execute(sql)
            listatickets = cursor.fetchall()
            listatickets = ((ticket[0]) for ticket in listatickets)
            listatickets = deque(list(listatickets))

            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                cotizacionesTicket(ticket)

                print('Quedan por actualizar un total de : %d' % len(listatickets))
                duerme()

#        'O) Actualizar/Descargar Datos Cotizaciones Historicos todos los Tickets',
        elif opcion == 'o':
            print(seleccion)
            ticketsborrados = []
            sql = "SELECT `tiket` FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' ORDER BY `componentes`.`tiket` ASC"
            cursor.execute(sql)
            listatickets = cursor.fetchall()
            listatickets = ((ticket[0]) for ticket in listatickets)
            listatickets = deque(list(listatickets))

            #cuentaatras = len ( listatickets )
            borranoactualizados = raw_input('Despues de una actualizacion del historico de una accion que ya existia, se vuelve a comprobar si se ha actualizado, si no es asi normalmente es porque la accion dejo de cotizar. Quieres borrar estas acciones? (No)')
            if borranoactualizados == '':
                borranoactualizados = False
            else:
                borranoactualizados = True

            #for ticket in listatickets:
            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                #accioninvalida=''
                print ('')
                print('Tickets pendientes de comprobar %d' % len(listatickets))

                #if naccion in tickets:

                if not ExistenDatos(ticket):
                    print('Ticket %s nuevo, descarga completa del historico de la accion' % ticket)

                    for timmingdescargado in 'dwm':

                        accioninvalida = descargaHistoricoAccion (ticket, timming = timmingdescargado, txt = False)
                        duerme()
                        if accioninvalida == 'Pago Dividendos' or accioninvalida == 'URL invalida':
                            break

                else:
                    print('Ticket %s ya descargado, comprobando la actualizacion de los datos' % ticket)
                    for timmingdescargado in 'dwm':

                        fechaactualizar, timmingactualizar, actualizaractualizar = actualizacionDatosHisAccion(ticket, timming = timmingdescargado)

                        if actualizaractualizar:# and (desdefechamodificacionarchivo(datosaccion)):

                            accioninvalida = descargaHistoricoAccion(ticket, fechaini = fechaactualizar, timming = timmingactualizar, actualizar = actualizaractualizar, txt = False)
                            duerme()

                            if accioninvalida == 'Pago Dividendos' or accioninvalida == 'URL invalida':
                                break
                            # despues de haber actualizado, volvemos a comprobarlo, si se da que si, la accion dejo de cotizar hace mucho.
                            # existe un caso especifico que es cuando comprobamos la actualizacion de datos de una accion y esta tiene menos de 3 periodos en el timming en que estemos trabajando, la funcion actualizacionDatosHisAccion la trata de forma especial, devolviendo (None, timming, True), para que con estos parametros la funcion descargaHistoricosAccion descarge todo el historico otra vez
                            # por esta razon en el siguiente if comprobamos con fechaactualizar2!=None que no sea este caso.
                            # FIXME : al hacer la comprobacion en mensual, casi siempre me da que no ha actualizado correctamente, ejemplo EGL.SW
                            fechaactualizar2, timmingactualizar2, actualizaractualizar2 = actualizacionDatosHisAccion(ticket, timming = timmingdescargado)
                            if fechaactualizar2 != None and actualizaractualizar == actualizaractualizar2 and fechaactualizar == fechaactualizar2:
                                fechahoy = ((date.today().timetuple()))
                                fechaactualizar2 = map(int, ((fechaactualizar2).split('-')))
                                desdeultimaactualizacion = (date(fechahoy[0], fechahoy[1], fechahoy[2]) - date(fechaactualizar2[0], fechaactualizar2[1], fechaactualizar2[2])).days

                                if borranoactualizados and desdeultimaactualizacion > difregactualizar['noActualizados']:
                                    accioninvalida = 'URL invalida'
                                    break
                                else:
                                    print ('No se ha actualizado correctamente. Funcion de borrado para estos casos deshabilitada')
                                    errorenTicket(ticket)
                                    break

                        else:
                            accioninvalida = None

                if accioninvalida == 'Pago Dividendos':
                    borraTicket (ticket, BBDD = False)# no los borramos de la BBDD porque cuando tienen muy poco historico a veces no se puede descargar

                    print('Reintento de la descarga, el error puede venir de un pago de Dividendos')
                    # errorenTicket(ticket)
                    for timmingdescargado in 'dwm':

                        accioninvalida = descargaHistoricoAccion (ticket, timming = timmingdescargado, txt = False)
                        duerme()

                if accioninvalida == 'URL invalida':
                    borraTicket (ticket)# Borramos completamente, de que nos sirve si no tenemos historico o despues de haber actualizado, aun no lo esta porque dejo de cotizar hace mucho
                    ticketsborrados.append(ticket)

                #cuentaatras -= 1

            print('Lista de tickets borrados por no contener historicos')
            for ticketborrado in ticketsborrados:
                print(ticketborrado)
            print('Un total de : ', len (ticketsborrados))

            del ticketsborrados


        elif opcion == 'p':
            #P) Actualizar Max/Min Historicos de todos los Tickets',
            print(seleccion)
            ticketsnodescargados = []
            sql = "SELECT `tiket` FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' ORDER BY `componentes`.`tiket` ASC"
            cursor.execute(sql)
            listatickets = cursor.fetchall()
            listatickets = ((ticket[0]) for ticket in listatickets)
            listatickets = deque(list(listatickets))
            #for ticket in listatickets:
            while len(listatickets) > 0:
                ticket = listatickets.popleft()

                print('')
                print('Tickets pendientes de comprobar %d' % len(listatickets))
                print('Actualizando ticket %s' % ticket)

                if ExistenDatos(ticket):
                    #funcion maximo minimo historico
                    datos = LeeDatos(ticket)
                    datosaccion = datos[2]#cogemos el historico diario

                    if len(datosaccion) > 0:

                        maximohistorico = max([maxi[2] for maxi in datosaccion])
                        minimohistorico = min([mini[3] for mini in datosaccion])

                        # fin de funcion
                        sql = "SELECT `maximini`.`nombre` FROM `maximini` WHERE (`maximini`.`nombre` = '" + ticket + "')"

                        print('Actualizando el ticket %s con un Maximo Historico de %s y un Minimo Historico de %s' % (ticket, maximohistorico, minimohistorico))
                        cursor.execute(sql)
                        numeroResultado = len(cursor.fetchall())
                        if numeroResultado == 1:
                            #codigo=cursor.fetchall()
                            #codigo=str(codigo[0][0])
                            #sql="UPDATE `maximini` SET `maximo` = %.2f, `minimo` = %.2f, `fechaRegistro` = `%s` WHERE `maximini`.`id` = '%s'"%(maximohistorico,minimohistorico,((datetime.now()).strftime("%Y-%m-%d %H:%M:%S")),codigo)
                            sql = "UPDATE `maximini` SET `maximo` = " + str(maximohistorico) + ", `minimo` = " + str(minimohistorico) + ", `fechaRegistro` = '" + str((datetime.now()).strftime("%Y-%m-%d %H:%M:%S")) + "' WHERE `maximini`.`nombre` = '" + ticket + "'"
                            cursor.execute(sql)
                        elif numeroResultado == 0:
                            sql = "INSERT INTO `maximini` (`id` ,`nombre` ,`maximo` ,`minimo` ,`fechaRegistro`) VALUES (NULL ,'%s',%.3f,%.3f,'%s')" % (ticket, maximohistorico, minimohistorico, (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))
                            cursor.execute(sql)
                        #print 'Ticket %s con cotizaciones historicas, actualizando max/min historicos'%naccion
                        db.commit()
                    else:# No existe suficiente historico
                        borraTicket (ticket, BBDD = False)
                        errorenTicket(ticket)
                        ticketsnodescargados.append(ticket)
                else: #no existe el archivo
                    #cotizacionesTicket(naccion)
                    errorenTicket(ticket)
                    ticketsnodescargados.append(ticket)

                print('')

            print('Tickets para los que no hay cotizaciones historicas')
            for ticket in ticketsnodescargados:
                print(ticket)
            print('Un total de : ', len (ticketsnodescargados))

        elif opcion == 'q':
            #Q) Analizar Datos de todos los Tickets',
            print(seleccion)
            sql = "SELECT * FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' ORDER BY `componentes`.`tiket` ASC"

            cursor.execute(sql)
            listadetickets = cursor.fetchall()
            cuentaatras = len(listadetickets)
            for registro in listadetickets:
                #resultado=(28141L, 'LVL MEDICAL GROUP', '-LVL.NX', 'ENX', 18.4, 14.89, 12.46, 14.56, 14.89, 12396.0, 7371.0, 'N/A', datetime.date(2011, 2, 24)
                codigo, nombre, ticket, mercado, max52, maxDia, min52, minDia, valorActual, volumenMedio, volumen, error, fechaRegistro = registro
                print('')
                print('Quedan por analizar un total de %d' % cuentaatras)
                print('Analizando ticket %s' % ticket)
                proximidadalcista, proximidadbajista = 0, 0
                if ExistenDatos(ticket):

                    #al final si utilizamos indicadorMME, el indicadorMME sera la decision de si es alcista o bajista
                    for timminganalisis in 'mwd':
                        print('Timming del analisis alcista: %s' % timminganalisis)
                        analisisalcista = analisisAlcistaAccion(ticket, timming = timminganalisis, conEntradaLT = False, txt = False)
                        if analisisalcista != None:
                            alcista, soporteanterioralcista, analisisalcistatotal = analisisalcista
                            resistencia, soporte, ruptura, LTi, LTf, salida, timming = alcista
                            soporte, stoploss = soporte
                            ruptura, entrada = ruptura
                            if maxDia == None or maxDia == 0.0:
                                maxDia = ruptura[4]
                            if valorActual == None or valorActual == 0.0:
                                valorActual = ruptura[4]
                            proximidadalcista = (abs((resistencia[2] / max(ruptura[4], maxDia, valorActual)) - 1))
#                            for precio in (ruptura[4], maxDia, valorActual):
#                                proximidadalcista.append(abs((resistencia[2] / precio) - 1))
#                            proximidadalcista = min(proximidadalcista)
                            break

                    for timminganalisis in 'mwd':
                        print('Timming del analisis bajista: %s' % timminganalisis)
                        analisisbajista = analisisBajistaAccion(ticket, timming = timminganalisis, conEntradaLT = False, txt = False)
                        if analisisbajista != None:
                            bajista, soporteanteriorbajista, analisisbajistatotal = analisisbajista
                            soporte, resistencia, ruptura, LTi, LTf, salida, timming = bajista
                            resistencia, stoploss = resistencia
                            ruptura, entrada = ruptura
                            if minDia == None or minDia == 0.0:
                                minDia = ruptura[4]
                            if valorActual == None or valorActual == 0.0:
                                valorActual = ruptura[4]
                            proximidadbajista = (abs(1 - (soporte[3] / min(ruptura[4], minDia, valorActual))))
#                            for precio in (ruptura[4], minDia, valorActual):
#                                proximidadbajista.append(abs(1 - (soporte[3] / precio)))
#                            proximidadbajista = min(proximidadbajista)
                            break

                    # TODO: falla logica, puede ser que en mensual el analisis sea bajista, pero en semanal alcista. Hay que dar preferencia al alcista semanal, la resistencia o fecha de entrada seria posterior al soporte o entrada en bajista mensual

                    #Existen ambos analisis, comparamos proximidada a ruptura
                    #la minima proximidadbajista es mayor o igual a la proximidadalcista, alcista
                    if analisisalcista != None and analisisbajista != None and proximidadbajista >= proximidadalcista:
                        resistencia, soporte, ruptura, LTi, LTf, salida, timming = alcista
                        soporte, stoploss = soporte
                        ruptura, entrada = ruptura
                        soporteanterior = soporteanterioralcista
                    #la minima proximidadbajista es menor a la proximidadalcista, bajista
                    elif analisisalcista != None and analisisbajista != None and proximidadbajista < proximidadalcista:
                        soporte, resistencia, ruptura, LTi, LTf, salida, timming = bajista
                        resistencia, stoploss = resistencia
                        ruptura, entrada = ruptura
                        soporteanterior = soporteanteriorbajista
                    # Uno de los analisis no existe, asignamos el contrario
                    elif analisisalcista == None and analisisbajista != None:
                        soporte, resistencia, ruptura, LTi, LTf, salida, timming = bajista
                        resistencia, stoploss = resistencia
                        ruptura, entrada = ruptura
                        soporteanterior = soporteanteriorbajista
                    elif analisisbajista == None and analisisalcista != None:
                        resistencia, soporte, ruptura, LTi, LTf, salida, timming = alcista
                        soporte, stoploss = soporte
                        ruptura, entrada = ruptura
                        soporteanterior = soporteanterioralcista
                    else:# Por defecto lo consideramos alcista, aunque aqui deberia entrar solo en el caso se que no se de la 3 condicion del if anterior
                        resistencia, soporte, ruptura, LTi, LTf, salida, timming = alcista
                        soporte, stoploss = soporte
                        ruptura, entrada = ruptura
                        soporteanterior = soporteanterioralcista

                    sql = "SELECT * FROM `params_operaciones` WHERE `params_operaciones`.`codigo` = %s" % codigo
                    cursor.execute(sql)
                    numeroResultado = len(cursor.fetchall())

                    if LTi == ('0-0-0', 0.0) and LTf == ('0-0-0', 0.0):
                        rentabilidad = 0.00
                    else:
                        fechainicial, precioinicial = LTi
                        fechafinal, preciofinal = LTf
                        fechainicial = map(int, (fechainicial.split('-')))
                        fechafinal = map(int, (fechafinal.split('-')))
                        diffechas = (date(fechafinal[0], fechafinal[1], fechafinal[2]) - date(fechainicial[0], fechainicial[1], fechainicial[2])).days

#                        if entrada > stoploss:#Alcista
                        rentabilidad = ((((1 + ((preciofinal - precioinicial) / precioinicial)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0
#                        elif entrada < stoploss:#Bajista
                            #TODO: la rentabilidad en bajista tiene que ser negativa, pero el equivalente en positiva
#                            rentabilidad = ((((1 + ((precioinicial - preciofinal) / preciofinal)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0

                    # no nos interesan los datos almacenados de analisis anteriores
                    #comprobamos que el analisis obtenido y que vamos a almacenar en la BBDD es o
                    #alcista o bajista
                    #comprobamos se es actual o esta obsoleto

                    #Alcista obsoleto
                    # Alcista, maximo52, maximo del dia, valoractual, precio de entrada (split) > Resitencia

                    #Bajista obsoleto
                    # Bajista, minimo52, minimo del dia, valoractual, precio de entrada (split) < soporte

                    if ((entrada > stoploss) and \
                    \
                    ((max52 != 'NULL' and max52 > resistencia[2]) or \
                    (maxDia != 'NULL' and maxDia > resistencia[2]) or \
                    (valorActual != 'NULL' and valorActual > resistencia[2]) or \
                    (entrada > resistencia[2])))\
                    \
                    or\
                    \
                    ((entrada < stoploss) and \
                    \
                    ((min52 != 'NULL' and min52 < soporte[3]) or \
                    (minDia != 'NULL' and minDia < soporte[3]) or \
                    (valorActual != 'NULL' and valorActual < soporte[3]) or \
                    (entrada < soporte[3]))):

                        # si true, analisis ya cumplido, obsoleto y lo actualizamos
                        if numeroResultado == 1:
                            sql = "UPDATE `params_operaciones` SET `precio_ini` = %.3f, `precio_fin` = %.3f, `fecha_ini` = '%s', `fecha_fin` = '%s', `salida` = NULL, `entrada` = NULL, `timing` = '%s', `precio_salida` = %.3f, `rentabilidad` = %.3f WHERE `params_operaciones`.`codigo` = %s" % (LTi[1], LTf[1], LTi[0], LTf[0], timming, soporteanterior, rentabilidad, codigo)
                        elif numeroResultado == 0:
                            sql = "INSERT INTO params_operaciones (id,precio_ini,precio_fin,fecha_ini,fecha_fin,salida,entrada,codigo,timing,precio_salida,rentabilidad) VALUES (NULL, %.3f, %.3f,'%s' ,'%s' , NULL, NULL, %d,'%s', %.3f, %.3f)" % (LTi[1], LTf[1], LTi[0], LTf[0], codigo, timming, soporteanterior, rentabilidad)

                    #Alcista/Bajista Validos
                    else:#anali
                        #si false, analisis valido, sin cumplir
                        if numeroResultado == 1:
                            sql = "UPDATE `params_operaciones` SET `precio_ini` = %.3f, `precio_fin` = %.3f, `fecha_ini` = '%s', `fecha_fin` = '%s', `salida` = %.3f, `entrada` = %.3f, `timing` = '%s', `precio_salida` = %.3f, `rentabilidad` = %.3f WHERE `params_operaciones`.`codigo` = %s" % (LTi[1], LTf[1], LTi[0], LTf[0], stoploss, entrada, timming, soporteanterior, rentabilidad, codigo)
                        elif numeroResultado == 0:
                            sql = "INSERT INTO params_operaciones (id,precio_ini,precio_fin,fecha_ini,fecha_fin,salida,entrada,codigo,timing,precio_salida,rentabilidad) VALUES (NULL, %.3f, %.3f,'%s','%s',%.3f , %.3f, %d,'%s', %.3f, %.3f)" % (LTi[1], LTf[1], LTi[0], LTf[0], stoploss, entrada, codigo, timming, soporteanterior, rentabilidad)

                    cursor.execute(sql)

                cuentaatras -= 1
                db.commit()


#        'S) BackTest

        elif opcion == 's':
            #ticket='AAPL'
            print(seleccion)
            backtest = []
            monedas = []

            print('Parametros del backtest, entre parentesis valor por defecto: ')

#            analizardesde=raw_input('Backtest a analizar desde la fecha AAAA-MM-DD (sin fecha inicio): ')
#            if analizardesde=='':
#                analizardesde=False
            estrategia = raw_input('Estrategia del backtest (Alcista): ')
            if estrategia == '':
                estrategia = 'Alcista'
            else:
                estrategia = 'Bajista'

            analizardesde = pidefecha()

            riesgo = raw_input('Riesgo por operacion (200): ')
            if riesgo == '':
                riesgo = 200
            else:
                riesgo = int(riesgo)

            volumenminimo = raw_input('Volumen Minimo por operacion (20000000): ')
            if volumenminimo == '':
                volumenminimo = 20000000
            else:
                volumenminimo = int(volumenminimo)

            filtrosalidamensual = raw_input('Filtro de salida Mensual por operacion, % (0.03): ')
            if filtrosalidamensual == '':
                filtrosalidamensual = 0.03
            else:
                filtrosalidamensual = float(filtrosalidamensual)

            filtrosalidasemanal = raw_input('Filtro de salida Semanal por operacion, % (0.02): ')
            if filtrosalidasemanal == '':
                filtrosalidasemanal = 0.02
            else:
                filtrosalidasemanal = float(filtrosalidasemanal)

            filtrosalidadiario = raw_input('Filtro de salida Diario por operacion, % (0.01): ')
            if filtrosalidadiario == '':
                filtrosalidadiario = 0.01
            else:
                filtrosalidadiario = float(filtrosalidadiario)

            rentabilidadminima = raw_input('Rentabilidad minima por operacion, % (0.35): ')
            if rentabilidadminima == '':
                rentabilidadminima = 0.35
            else:
                rentabilidadminima = float(rentabilidadminima)

            rentabilidad0 = raw_input('Consideramos Rentabilidad 0 igual a la rentabilidad minima, (Si): ')
            if rentabilidad0 == '':
                rentabilidad0 = True
            else:
                rentabilidad0 = False

            inversionminima = raw_input('Inversion minima por operacion (800): ')
            if inversionminima == '':
                inversionminima = 800
            else:
                inversionminima = int(inversionminima)

            inversionmaxima = raw_input('Inversion maxima por operacion (Sin limite): ')
            if inversionmaxima == '':
                inversionmaxima = False
            else:
                inversionmaxima = int(inversionmaxima)

            if raw_input('Media Movil Exponencial (Sin MME en todos los timmings): ') == '':
                MMediario = False
                MMesemanal = False
                MMemensual = False
                MMe2diario = False
                MMe2semanal = False
                MMe2mensual = False
            else:

                MMediario = raw_input('Media Movil Exponencial diario (Sin MME): ')
                if MMediario == '':
                    MMediario = False
                    MMe2diario = False
                else:
                    MMediario = int(MMediario)
                    MMe2diario = raw_input('2Âª Media Movil Exponencial diario para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): ')
                    if MMe2diario == '':
                        MMe2diario = False
                    else:
                        MMe2diario = int(MMe2diario)

                MMesemanal = raw_input('Media Movil Exponencial semanal (Sin MME): ')
                if MMesemanal == '':
                    MMesemanal = False
                    MMe2semanal = False
                else:
                    MMesemanal = int(MMesemanal)
                    MMe2semanal = raw_input('2Âª Media Movil Exponencial semanal para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): ')
                    if MMe2semanal == '':
                        MMe2semanal = False
                    else:
                        MMe2semanal = int(MMe2semanal)

                MMemensual = raw_input('Media Movil Exponencial mensual (Sin MME): ')
                if MMemensual == '':
                    MMemensual = False
                    MMe2mensual = False
                else:
                    MMemensual = int(MMemensual)
                    MMe2mensual = raw_input('2Âª Media Movil Exponencial semanal para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): ')
                    if MMe2mensual == '':
                        MMe2mensual = False
                    else:
                        MMe2mensual = int(MMe2mensual)


            if raw_input('True Avenrange xrange (Sin TAR en todos los timmings): ') == '':
                TARmensual = False
                TARsemanal = False
                TARdiario = False
            else:
                TARmensual = raw_input('True Avenrange xrange Mensual (Sin TAR): ')
                if TARmensual == '':
                    TARmensual = False
                else:
                    TARmensual = int(TARmensual)
                TARsemanal = raw_input('True Avenrange xrange Semanal (Sin TAR): ')
                if TARsemanal == '':
                    TARsemanal = False
                else:
                    TARsemanal = int(TARsemanal)
                TARdiario = raw_input('True Avenrange xrange Diario (Sin TAR): ')
                if TARdiario == '':
                    TARdiario = False
                else:
                    TARdiario = int(TARdiario)

            EntradaLT = raw_input('Entradas en Linea de Tendencia (Sin Entradas): ')
            if EntradaLT == '':
                EntradaLT = False
            else:
                EntradaLT = True


            opcionbacktest, seleccionbacktest = creaMenu(')', (
            'Timmin para el que hacemos el backtest',
            '1) Todo Diario',
            '2) Diario con transicion a Semanal',
            '3) Todo Semanal',
            '4) Semanal con transicion a Mensual',
            '5) Todo Mensual',
            '6) Diario con transicion a Semanal y Mensual'))


# En el caso de hacer un solo ticket, comentar desde aqui hasta print 'Analizando ticket %s' % ticket incluido, desdentar desde este comentario hasta el siguiente parecedo
            #obtenemos la lista de las monedas
            sql = "SELECT `codigo` FROM `monedas`"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            #lo mostramos en una lista
            #nos pide la moneda a buscar y la convertimos en la variable de la siguiente consulta con la que obtenemos la lista de tickes para hacer el backtest
            for mon in resultado:
                print((mon)[0])
                monedas.append(mon[0])

            while True:
                moneda = raw_input('Lista de monedas. Introduce moneda en la que se hace el backtest : ')
                if moneda == '' or moneda == None:
                    moneda = ((raw_input('Introduce sufijo de tickets del mercado en la que se hace el backtest : ')).upper(),)
                    cursor.execute ("SELECT * FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' and `componentes`.`tiket` NOT LIKE '^%' and `componentes`.`tiket` LIKE ? ORDER BY `componentes`.`tiket` ASC", moneda)
                    break
                if moneda in monedas:
                    cursor.execute ("SELECT * FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' and `componentes`.`tiket` NOT LIKE '^%' and`componentes`.`mercado` IN (SELECT `nombreUrl` FROM `mercado_moneda` WHERE `abrevMoneda` LIKE '" + moneda + "') ORDER BY `componentes`.`tiket` ASC")
                    break


            #consulta en la tabla componentes que pertenecen a los mercados de una moneda
            #sql = "SELECT * FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' and `componentes`.`tiket` NOT LIKE '^%' and`componentes`.`mercado` IN (SELECT `nombreUrl` FROM `mercado_moneda` WHERE `abrevMoneda` LIKE '" + moneda + "') ORDER BY `componentes`.`tiket` ASC"

            resultado = cursor.fetchall()
            cuentaatras = len(resultado)
            for registro in resultado:
                #resultado=(28141L, 'LVL MEDICAL GROUP', '-LVL.NX', 'ENX', 18.4, 14.89, 12.46, 14.56, 14.89, 12396.0, 7371.0, 'N/A', datetime.date(2011, 2, 24)
                codigo, nombre, ticket, mercado, max52, maxDia, min52, minDia, valorActual, volumenMedio, volumen, error, fechaRegistro = registro
                print('Quedan por analizar un total de %d' % cuentaatras)
                print('Analizando ticket %s' % ticket)


                if ExistenDatos(ticket):
                    backtestaccion = []
                    if estrategia == 'Alcista':
                        diario = analisisAlcistaAccion(ticket, timming = 'd', desdefecha = analizardesde, MME = MMediario, MME2 = MMe2diario, conEntradaLT = EntradaLT, filtro = filtrosalidadiario, TAR = TARdiario, txt = True)
                        semanal = analisisAlcistaAccion(ticket, timming = 'w', desdefecha = analizardesde, MME = MMesemanal, MME2 = MMe2semanal, conEntradaLT = EntradaLT, filtro = filtrosalidasemanal, TAR = TARsemanal, txt = True)
                        mensual = analisisAlcistaAccion(ticket, timming = 'm', desdefecha = analizardesde, MME = MMemensual, MME2 = MMe2mensual, conEntradaLT = EntradaLT, filtro = filtrosalidamensual, TAR = TARmensual, txt = True)
                    elif estrategia == 'Bajista':
                        diario = analisisBajistaAccion(ticket, timming = 'd', desdefecha = analizardesde, MME = MMediario, MME2 = MMe2diario, conEntradaLT = EntradaLT, filtro = filtrosalidadiario, TAR = TARdiario, txt = True)
                        semanal = analisisBajistaAccion(ticket, timming = 'w', desdefecha = analizardesde, MME = MMesemanal, MME2 = MMe2semanal, conEntradaLT = EntradaLT, filtro = filtrosalidasemanal, TAR = TARsemanal, txt = True)
                        mensual = analisisBajistaAccion(ticket, timming = 'm', desdefecha = analizardesde, MME = MMemensual, MME2 = MMe2mensual, conEntradaLT = EntradaLT, filtro = filtrosalidamensual, TAR = TARmensual, txt = True)

                    fecharesistenciadiario = 0
                    fecharesistenciasemanal = 0

                    if not diario == None:
                        diario = diario[2]
                        fechasentradasdiario = ([operacion[0][0] for operacion in diario])
                        i2 = len(diario)#por si alcistamensual==None, tenemos que asignarle todo el historico de semanal a backtestaccion
                    else:
                        i2 = 0
                        diario = []

# puede que no exista o analisis semanal o mensual, en estos casos hay que darle algun valor a esos casos para que backtest sea coherente
                    if not semanal == None:
                        semanal = semanal[2]
                        fechasentradassemanal = ([operacion[0][0] for operacion in semanal])
                        fecha1entradasemanal = semanal[0][0][0]
                        i = len(semanal)#por si alcistamensual==None, tenemos que asignarle todo el historico de semanal a backtestaccion

                        if not diario == []:
                            i2 = 0
                            while i2 < len(fechasentradasdiario):
                                if fecha1entradasemanal <= fechasentradasdiario[i2]:
                                    break
                                i2 += 1
                    else:
                        i = 0
                        semanal = []


                    if not mensual == None:
                        mensual = mensual[2]
                        fecha1entradamensual = mensual[0][0][0]

                        if not semanal == []:
                            i = 0
                            while i < len(fechasentradassemanal):
                                if fecha1entradamensual <= fechasentradassemanal[i]:
                                    break
                                i += 1

                    else:
                        mensual = []

#                    '1) Todo Diario',
                    if opcionbacktest == '1':
                        backtestaccion = diario
#                    '2) Diario con transicion a Semanal',
                    elif opcionbacktest == '2':
                        backtestaccion = diario[:i2] + semanal
#                    '3) Todo Semanal',
                    elif opcionbacktest == '3':
                        backtestaccion = semanal
#                    '4) Semanal con transicion a Mensual',
                    elif opcionbacktest == '4':
                        backtestaccion = semanal[:i] + mensual
#                    '5) Todo Mensual',
                    elif opcionbacktest == '5':
                        backtestaccion = mensual
#                    '6) Diario con transicion a Semanal y Mensual'))
                    elif opcionbacktest == '6':
                        backtestaccion = diario[:i2] + semanal[:i] + mensual

                    #precionentrada = 0
                    #preciosalida = 0
                    invertido = False
                    p = 0
                    while p < len(backtestaccion):
                    #for operacion in backtestaccion:

                        if estrategia == 'Alcista':
                            resistencia, soporte, ruptura, LTi, LTf, salida, timming = backtestaccion[p]
                            soporte, stoploss = soporte
                            ruptura, precionentrada = ruptura
                        elif estrategia == 'Bajista':
                            soporte, resistencia, ruptura, LTi, LTf, salida, timming = backtestaccion[p]
                            resistencia, stoploss = resistencia
                            ruptura, precionentrada = ruptura
                        #Calculamos rentabilidad

                        if LTi == ('0-0-0', 0.0) and LTf == ('0-0-0', 0.0):
                            if rentabilidad0:
                                rentabilidad = rentabilidadminima
                            else:
                                rentabilidad = 0.00
                        else:
                            fechainicial, precioinicial = LTi
                            fechafinal, preciofinal = LTf
                            fechainicial = map(int, (fechainicial.split('-')))
                            fechafinal = map(int, (fechafinal.split('-')))
                            diffechas = (date(fechafinal[0], fechafinal[1], fechafinal[2]) - date(fechainicial[0], fechainicial[1], fechainicial[2])).days

                            if estrategia == 'Alcista':
                                rentabilidad = ((((1 + ((preciofinal - precioinicial) / precioinicial)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0
                            elif estrategia == 'Bajista':
                                rentabilidad = ((((1 + ((precioinicial - preciofinal) / preciofinal)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0

                        #calculamos el volumen
                        volumenoperacion = 0
#                        for barra in resistencia, soporte, ruptura:
#                            if len(barra) == 2:
#                                barra, _barra2 = barra
#                            fecha, apertura, maximo, minimo, cierre, volumen = barra
#                            volumenoperacion = (cierre * volumen * 22) + volumenoperacion
#                        volumenoperacion = int (volumenoperacion / 3)
                        # Como utilizamos la MME (5) sobre el volumen, solo comprobamos el volumen de la barra de ruptura
                        fecha, apertura, maximo, minimo, cierre, volumen = ruptura
                        volumenoperacion = int((cierre * volumen * 22))

                        if (resistencia[2] == stoploss) or (soporte[3] == stoploss):# comprobamos que no dividomos entre 0
                            numeroacciones = 0
                        else:
                            # las siguientes comprobaciones son necesarias, porque nosotros ponemos la orden para la ruptura y calculamos el numero de acciones en relacion a ello
                            # pero eso no quiere decir que se ejecute al precionentrada
                            if estrategia == 'Alcista':
                                numeroacciones = int(riesgo / (resistencia[2] - stoploss))
                            elif estrategia == 'Bajista':
                                numeroacciones = int(riesgo / (soporte[3] - stoploss))



                        #inversion moneda
                        if estrategia == 'Alcista':
                            inversion = numeroacciones * resistencia[2]
                        elif estrategia == 'Bajista':
                            inversion = numeroacciones * soporte[3]

                        if not(inversionmaxima == False) and abs(inversion) > inversionmaxima:
                            if estrategia == 'Alcista':
                                numeroacciones = int(inversionmaxima / resistencia[2])
                                inversion = numeroacciones * resistencia[2]
                            elif estrategia == 'Bajista':
                                #la inversion maxima es en negativo, arriba comparamos el valor absoluto pero en el numero de acciones tiene que ser negativo
                                numeroacciones = (int(inversionmaxima / soporte[3])) * (-1)
                                inversion = numeroacciones * soporte[3]

                        if invertido == False and rentabilidad >= rentabilidadminima and volumenoperacion >= volumenminimo and abs(inversion) >= inversionminima:

                            if salida == False:#analisis de que no hay salida, le asignamos la fecha y cotizacion actual
                                fechasalida = str(fechaRegistro)
                                # Se da el caso que el historico o el ajuste del mismo no esta actualizado y la cotizacion si, de manera que si el analisis no nos ha dado salida y al buscar un precio de salida
                                # Si somo alcistas o bajista y no nos ha salta el stoploss con el valor actual, al precio de salida le asignamos el valor actual
                                if (estrategia == 'Alcista' and stoploss <= valorActual) or (estrategia == 'Bajista' and stoploss >= valorActual):
                                    preciosalida = valorActual
                                else:
                                    preciosalida = stoploss
                            else:
                                fechasalida, preciosalida = salida

                            #aqui en algunos casos recalculamos debido a que la orden se da con la informacion del momento, pero se puede ejecutar de manera distinta referente a los precios
                            numeroaccionesoperacion = numeroacciones
                            timmingentrada = timming
                            timmingtransicion = timming
                            inversionoperacion = numeroaccionesoperacion * precionentrada
                            inversionrecuperada = numeroaccionesoperacion * preciosalida
                            soporteentrada = soporte[3]
                            resistenciaentrada = resistencia[2]
                            fechaentrada = ruptura[0]
                            precionentrada2 = precionentrada
                            if estrategia == 'Alcista' and resistencia[2] <= ruptura[2]:# La ultima comprobacion es para el caso de que en el ultimo analisis en el que la ruptura es la ultima barra que aun no rompiendo la resistencia la consideramos que si, en el caso de que no estemos comprados esta ultima condicion no nos consideraria como tal
                                invertido = True

                                balance = inversionrecuperada - inversionoperacion

                            elif estrategia == 'Bajista' and soporte[3] >= ruptura[3]:
                                invertido = True

                                balance = inversionoperacion - inversionrecuperada

                        elif invertido == True:

                            fecharuptura = ruptura[0]
                            #fecharesistencia = resistencia[0]
                            if timmingtransicion != timming and fechasalida > fecharuptura:
                                #Si hay transicion y Si la fecha de salida es posteior al de ruptura, actualizamos en nuevo precio de salida y la fecha, en los casos de las transiciones esto indipensable para que el precio de salida se adapte a los cambios de timming
                                timmingtransicion = timming # Actualizamos el nuevo timmng de transiciones

                                if salida == False:#analisis de que no hay salida, le asignamos la fecha y cotizacion actual
                                    fechasalida = str(fechaRegistro)
                                    # Se da el caso que el historico o el ajuste del mismo no esta actualizado y la cotizacion si, de manera que si el analisis no nos ha dado salida y al buscar un precio de salida
                                    # Si somo alcistas o bajista y no nos ha salta el stoploss con el valor actual, al precio de salida le asignamos el valor actual
                                    if (estrategia == 'Alcista' and stoploss < valorActual) or (estrategia == 'Bajista' and stoploss > valorActual):
                                        preciosalida = valorActual
                                    else:
                                        preciosalida = stoploss
                                else:
                                    fechasalida, preciosalida = salida
                                inversionrecuperada = numeroaccionesoperacion * preciosalida
                                if estrategia == 'Alcista':
                                    balance = inversionrecuperada - inversion
                                elif estrategia == 'Bajista':
                                    balance = inversion - inversionrecuperada

                            elif fechasalida <= fecharuptura:
                            #elif fechasalida <= fecharuptura:
#                                if -(riesgo) * backtestoperacionessospechosas > balance:
#                                    if estrategia == 'Alcista':
#                                        print('ticket  fechaentrada  precionentrada  soporte  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
#                                        print(('%6s %13s %15.3f %8.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, soporteentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))
#
#                                    elif estrategia == 'Bajista':
#                                        print('ticket  fechaentrada  precionentrada  resistencia  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
#                                        print(('%6s %13s %15.3f %12.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, resistenciaentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))
#                                        #print ( '   %s,           %s,           %.3f,    %.3f,             %s,                      %d,          %s,         %.3f,      %s,               %.3f,                %.3f,    %.3f' % ( ticket, fechaentrada, precionentrada, ( soporte[3] ), timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance ) )
#
#                                    raw_input('Operacion Dudosa, compruebala y pulsa una tecla')
                                if fechasalida != fecharuptura:#Eliminada la posibilidad porque en el caso de que fechasalida == fecharuptura sea en una LT, nos saca y volvemos a entrar en la LT
                                    p -= 1#Puede que el ciclo que me saca, no impida que vuelva a entrar
                                # almaceno aqui la informacion del backtes porque puede que entre en un timming pero salga en otro
                                backtest.append((ticket, mercado, fechaentrada, precionentrada2, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timmingtransicion, inversionoperacion, inversionrecuperada, balance))
                                invertido = False

                        p += 1

                    # si me ha sacado invertido en la ultima analisis
                    if invertido == True:
                        #if ( resistencia[2] <= ruptura[2] ) or ( salida == False ):#si en el ultimo analisis no hay un soporte consolidado, porque no esta rota la resistencia o no hay salida del la accion
                            #  (resistencia[2]> ruptura[2])
                            # realmente no nos hemos salido de la operacion pero como no sabemos si nos sacara o no, valoramos la operacion a lo que valdria en ese momento
                        #fechasalida=ruptura[0]
#                            if -(riesgo) * backtestoperacionessospechosas > balance:
#                                if estrategia == 'Alcista':
#                                    print('ticket  fechaentrada  precionentrada  soporte  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
#                                    print(('%6s %13s %15.3f %8.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, soporteentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))
#
#                                elif estrategia == 'Bajista':
#                                    print('ticket  fechaentrada  precionentrada  resistencia  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
#                                    print(('%6s %13s %15.3f %12.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, resistenciaentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))
#                                    #print ( '   %s,           %s,           %.3f,    %.3f,             %s,                      %d,          %s,         %.3f,      %s,               %.3f,                %.3f,    %.3f' % ( ticket, fechaentrada, precionentrada, ( soporte[3] ), timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance ) )
#
#                                raw_input('Operacion Dudosa, compruebala y pulsa una tecla')
                            backtest.append((ticket, mercado, fechaentrada, precionentrada2, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timmingtransicion, inversionoperacion, inversionrecuperada, balance))
                            invertido = False

# En el caso de hacer un solo ticket, comentar desde aqui hasta cuentraatras incluido


                cuentaatras -= 1

            if len(backtest) > 0:
                positivas = 0
                negativas = 0
                inversionTotal = 0
                inversionrecuperadaTotal = 0

                archivobacktest = os.path.join(os.getcwd(), carpetas['Backtest'] , ((datetime.now()).strftime("%Y-%m-%d %H%M")) + '.csv')
                j = open(archivobacktest, 'w')
                j.write('ticket;mercado;AnoE;MesE;DiaE;PrecioE;TimmingE;Nacciones;AnoS;MesS;DiaS;PrecioS;TimmingS;InversionE;InversionS;resultado\n')
                #writercsv = csv.writer(j, delimiter=';', lineterminator = '\n', doublequote = True)


                for n in backtest:
                    ticket, mercado, fechaentrada, precionentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversion, inversionrecuperada, balance = n
                    texto = (("%s;%s;%s;%.3f;%s;%d;%s;%.3f;%s;%.3f;%.3f;%.3f\n") % (ticket, mercado, fechaentrada.replace('-', ';'), precionentrada, timmingentrada, numeroaccionesoperacion, fechasalida.replace('-', ';'), preciosalida, timming, inversion, inversionrecuperada, balance)).replace('.', ',')
                    j.write(texto)

                    #writercsv.writerow(n)


                    if balance >= 0:
                        positivas += 1
                    elif balance < 0:
                        negativas += 1

                    inversionTotal = inversionTotal + inversion
                    inversionrecuperadaTotal = inversionrecuperadaTotal + inversionrecuperada

                for n in xrange(0, 4):
                    j.write('\n')

                j.write('Parametros : \n')
                j.write('Estrategia : %s\n' % estrategia)
                j.write('Backtest desde la fecha : %s\n' % analizardesde)
                j.write('Riesgo : %d\n' % riesgo)
                j.write('Volumen Minimo : %d\n' % volumenminimo)
                j.write(('Filtro Mensual : %.2f\n' % (filtrosalidamensual)).replace('.', ','))
                j.write(('Filtro Semanal : %.2f\n' % (filtrosalidasemanal)).replace('.', ','))
                j.write(('Filtro Diario : %.2f\n' % (filtrosalidadiario)).replace('.', ','))
                j.write(('Rentabilidad Minima : %.2f\n' % (rentabilidadminima)).replace('.', ','))
                j.write('Rentabilidad 0 igual a rentabilidad minima : %s\n' % rentabilidad0)
                j.write(('Inversion Minima : %.2f\n' % inversionminima).replace('.', ','))
                j.write('Inversion Maxima : %s\n' % inversionmaxima)
                j.write(('Media Movil Exponencial diario  : %s\n' % MMediario))
                j.write(('Media Movil Exponencial semanal : %s\n' % MMesemanal))
                j.write(('Media Movil Exponencial mensual : %s\n' % MMemensual))
                j.write(('Media Movil Exponencial 2Â para cruce de medias diario  : %s\n' % MMe2diario))
                j.write(('Media Movil Exponencial 2Â para cruce de medias semanal : %s\n' % MMe2semanal))
                j.write(('Media Movil Exponencial 2Â para cruce de medias mensual : %s\n' % MMe2mensual))
                j.write(('True Averange xrange Mensual: %s\n' % TARmensual))
                j.write(('True Averange xrange Samanal: %s\n' % TARsemanal))
                j.write(('True Averange xrange Diario : %s\n' % TARdiario))
                j.write(('Con entradas en Linea de tendencia : %s\n' % EntradaLT))
                j.write('Timming de las operaciones : %s\n' % seleccionbacktest)
                j.write('Moneda del Backtest : %s\n' % moneda)


                for n in xrange(0, 4):
                    j.write('\n')

                j.write('Resultado: \n')
                j.write('Numero de operaciones totales: %d\n' % (len(backtest)))
                j.write(('Numero de operaciones positivas: %d   Representa un porcetaje de %.2f\n' % (positivas, (((positivas * 1.0) / (len(backtest))) * 100))).replace('.', ','))
                j.write(('Numero de operaciones negativas: %d   Representa un porcetaje de %.2f\n' % (negativas, (((negativas * 1.0) / (len(backtest))) * 100))).replace('.', ','))
                j.write(('Inversion Total : %.2f\n' % inversionTotal).replace('.', ','))
                j.write(('Inversion Recuperada : %.2f\n' % inversionrecuperadaTotal).replace('.', ','))
                if estrategia == 'Alcista':
                    j.write(('Rentabilidad (Porcentaje): %.2f\n' % (((inversionrecuperadaTotal / inversionTotal) - 1) * 100)).replace('.', ','))
                elif estrategia == 'Bajista':
                    j.write(('Rentabilidad (Porcentaje): %.2f\n' % (((inversionTotal / inversionrecuperadaTotal) - 1) * 100)).replace('.', ','))

                j.close()

                print('')
                print('Resultado: ')
                print(('Numero de operaciones totales: %d' % (len(backtest))))
                print(('Numero de operaciones positivas: %d   Representa un porcetaje de %.2f' % (positivas, (((positivas * 1.0) / (len(backtest))) * 100))))
                print(('Numero de operaciones negativas: %d   Representa un porcetaje de %.2f' % (negativas, (((negativas * 1.0) / (len(backtest))) * 100))))
                print(('Inversion Total : %.2f' % inversionTotal))
                print(('Inversion Recuperada : %.2f' % inversionrecuperadaTotal))
                if estrategia == 'Alcista':
                    print(('Rentabilidad (Porcentaje): %.2f' % (((inversionrecuperadaTotal / inversionTotal) - 1) * 100)))
                elif estrategia == 'Bajista':
                    print(('Rentabilidad (Porcentaje): %.2f' % (((inversionTotal / inversionrecuperadaTotal) - 1) * 100)))
                print('')
            else:
                raw_input('Backtest no realizado')

            #import bigben
            #bigben

#        'V) Exportar datos a arhivos csv',
        elif opcion == 'v':
            print (seleccion)
            print ('Limpiando Directorio')
            os.remove(glob.glob(os.path.join(os.getcwd(), carpetas['Historicos'], nombre + "*.*")))
            #archivosticket = glob.glob(os.path.join(os.getcwd(), carpetas['Historicos'], nombre + "*.*"))
            #for archivo in archivosticket:
            #    os.remove(archivo)

            moneda = (raw_input('Introduce sufijo de tickets del mercado a exportar (Todas): ')).upper()
            if moneda == '' or moneda == None:
                cursor.execute("SELECT `tiket`, `codigo`, `nombre` FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' ORDER BY `componentes`.`tiket` ASC")
            else:
                moneda = (moneda,)
                cursor.execute ("SELECT `tiket`, `codigo`, `nombre` FROM `componentes` WHERE `componentes`.`error` LIKE 'N/A' `componentes`.`tiket` LIKE ? ORDER BY `componentes`.`tiket` ASC", moneda)

            listatickets = cursor.fetchall()
            listatickets = ((ticket[0], ticket[1], ticket[2]) for ticket in listatickets)
            listatickets = deque(list(listatickets))
            ticketsnodescargados = []
            #for ticket in listatickets:
            while len(listatickets) > 0:
                ticket, codigo, naccion = listatickets.popleft()
                naccion = (naccion.strip('"')).replace(',', '')

                print('')
                print('Tickets pendientes de exportar %d' % len(listatickets))
                print('Exportando ticket %s' % ticket)

                if ExistenDatos(ticket):
                    #funcion maximo minimo historico
                    datos = LeeDatos(ticket)

                    for timming in 'MWD':
                        if timming == 'M':
                            datosaccion = datos[0]
                        elif timming == 'W':
                            datosaccion = datos[1]
                        elif timming == 'D':
                            datosaccion = datos[2]

                        if len(datosaccion) > 0:

                            nombre = (str(ticket) + str(codigo)).replace('.', '_')
                            archivo = os.path.join(os.getcwd(), carpetas['Historicos'], nombre + '.' + timming + '.csv')
                            j = open(archivo, 'w')
                            j.write('<TICKER>,<NAME>,<PER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>\n')
                            writercsv = csv.writer(j, delimiter = ',', lineterminator = '\n', doublequote = True)
                            for n in datosaccion:

                                fecha, apertura, maximo, minimo, cierre, volumen = n
                                fecha = fecha.replace('-', '')

                                n = (ticket, naccion, timming, fecha, '000000', apertura, maximo, minimo, cierre, volumen, '0')

                                writercsv.writerow(n)
                                #j.write(str(n)+'\n')
                            j.close()


                        else:# No existe suficiente historico
                            errorenTicket(ticket)
                            ticketsnodescargados.append(ticket)
                else: #no existe el archivo
                    #cotizacionesTicket(naccion)
                    errorenTicket(ticket)
                    ticketsnodescargados.append(ticket)

                print('')

            print('Tickets para los que no hay cotizaciones historicas')
            for ticket in ticketsnodescargados:
                print(ticket)
            print('Un total de : ', len (ticketsnodescargados))


#        'W) Dar de alta acciones desde archivo',
        elif opcion == 'w':
            print(seleccion)

            incluidos = 0

            archivowtickers = os.path.join('C:\\xampp\\htdocs\\jstock' , 'wtickers.dat')

            if not os.path.exists(archivowtickers):
                """
                print ('Indica la ruta del archivo wtickers.dat')
                application = (wx()).wx.PySimpleApp()
                dialog = (wx()).wx.DirDialog (None, 'Archivo wtickers.dat',
                                       style = (wx()).wx.DD_CHANGE_DIR ,
                                       defaultPath = 'C:\\xampp\\htdocs\\jstock')
                if dialog.ShowModal() == (wx()).wx.ID_OK:
                    print 'Directory:', dialog.GetPath()
                    archivowtickers = os.path.join(dialog.GetPath(), 'wtickers.dat')
                else:
                    print 'No directory.'
                dialog.Destroy()
                application.Destroy()
                """
            f = open(archivowtickers, "r")
            lineas = f.readlines()
            f.close()

            for naccion in lineas:
                naccion = ((naccion.upper()).replace('@%5E', '^')).strip()
                #incluir = True

                punto = naccion.find('.')
                if punto != -1 and not (naccion[punto:] in str(sufijosexcluidos)):# encontramos el punto en la accion y utilizamos su posicion para extraer de la accion su sufijo y si no se encuentra en la lista de excluidas, lo incluimos
                    naccion = (naccion,)
                    cursor.execute ("SELECT *  FROM `nombreticket` WHERE (`nombreticket`.`nombre` = ?)", naccion)
                    numeroResultado = len(cursor.fetchall())
                    if numeroResultado == 0:
                        cursor.execute ("INSERT INTO `nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES (?, '" + str(date.today()) + "', NULL, NULL)", naccion)
                        print(naccion[0] + ' anadido a la base de datos')
                        incluidos += 1

                #for suf in sufijosexcluidos:# Todas las comparaciones con los sufijosexcluidos tienen que ser -1(no existe) para que lo anadamos, si hay uno, no se anade
                #    existe = naccion.find(suf)
                #    if existe != -1:
                #        incluir = False

                #if incluir:
                #    sql = "SELECT *  FROM `nombreticket` WHERE (`nombreticket`.`nombre` = '" + naccion + "')"
                #

                #    if len(cursor.execute(sql).fetchall()) == 0:
                #        sql = "INSERT INTO `nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES ('" + naccion + "', '" + str(date.today()) + "', NULL, NULL)"
                #        cursor.execute(sql)
                #        print(naccion + ' anadido a la base de datos')
                #        incluidos += 1
            db.commit()
            print ('Tickets Anadidos a la BBDD : %d' % incluidos)




        elif opcion == 'x':
            print(seleccion)
            print('Funcion desabilitada')
#            ficheroDatos=os.path.join(os.getcwd(),"\\Cobo.pck")
#            datos = {'tickets':tickets, 'mercados':mercados}
#            codificado=pickle.dumps(datos)
#            f=open(ficheroDatos,"w")
#            f.write(codificado)
#            f.close()
#        
#
#    ficheroDatos=os.path.join(os.getcwd(),"\\Cobo.pck")
#    datos = {'tickets':tickets, 'mercados':mercados}
#    datos=pickle.dumps(datos)
#    f=open(ficheroDatos,"w")
#    f.write(datos)
#    f.close()
    #os.spawnl( os.P_NOWAIT, 'C:\\xampp\\apache\\bin\pv.exe -f -k mysqld.exe -q' )
        elif opcion == 'z':

            cursor.close()
            db.close()
            break
