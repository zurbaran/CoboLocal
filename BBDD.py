# -*- coding: UTF-8 -*-
####################################################
# Name:        BBDD.py
# Purpose:
#
# Author:      Antonio
#
# Created:     23/07/2012
# Copyright:   (c) Antonio 2012
# Licence:     <your licence>
####################################################


#################################################
# Constantes locales

#################################################

####################################################
# modulos estandar importados

from setuptools.command.easy_install import main as install
import os
import glob
from datetime import date, datetime, timedelta

# from sql import *
# from sql.aggregate import *
# from sql.conditionals import *
# TODO: implementar la libreria python-sql para generar el codigo sql

try:
    from pysqlite2 import dbapi2 as sqlite3
except ImportError:
    print ('Modulo de pysqlite2 deshabilitado. Cargando sqlite3 nativo')
    import sqlite3  # lint:ok
    install(['-v', 'pysqlite'])

####################################################
# modulos no estandar o propios
from Cobo import CARPETAS, DIFREGACTUALIZAR
from yahoofinance import precioentradaLT


def conexion(archivo=None):
    """

    """
    # crearmos una conexion para cada ticket que corresponda a un archivo distinto
    # igual que cuando guardabamos los historicos en archivos
    if archivo == None:
        archivo = os.path.join(os.getcwd(), "Cobo.dat")
    else:
        ticket = archivo
        ticket = ticket.upper()
        # tickets = ticketlistacodigo(ticket)
        # nombre = ('%s%s' % (ticket, tickets[ticket])).replace('.', '_')
        nombre = ('%s' % ticket).replace('.', '_')
        archivo = os.path.join(os.getcwd(), CARPETAS['Datos'], nombre + ".dat")

    try:
        db = sqlite3.connect(os.path.join(archivo))
        # db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '0000', db = 'lomiologes_cobodb')
        cursor = db.cursor()
    # TODO: Crear contenido de la bbdd en el caso de que este vacia
    # como no se produce excepcion aunque el archivo no exista, y encima lo crea cuando no existe
    # hay que hacer una consulta dentro de la bbdd para comprobar que todo existe
# #    if archivo == os.path.join(os.getcwd(), "Cobo.dat"):
# #        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
# #        tables= cursor.fetchall()
# #        if len(tables)<7:
# #            funcion que crea la estructura completa de la bbdd, incorporandola del archivo CoboBBDDInicio.sql

    except:
        raw_input('Base de datos no habilitada. Para que el programa funcione necesitas conexion a la base de datos')
        quit()
    else:
        return cursor, db


def comprobaciones(colaResultado=None):
    """
    """
    # TODO : darle parametros a esta funciona para obtener listas de tickets pendientes de actualizar,....
    # si no tiene parametros, que imprima las comprobaciones

    # Lista de los distintos mercados a los que pertenecen los tickets y cantidad de tickets para cada uno de ellos
    cursor, db = conexion()
    sql = "SELECT `mercado`, count(*) FROM `Cobo_componentes` GROUP BY `mercado` HAVING count(*) >= 0"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    if colaResultado == None:
        for n in resultado:
            print(('%s contiene %d tickets' % (n)))
        print ('')

    # Buscar tickets duplicados en la BBDD
    sql = "SELECT `tiket`, count(*) FROM `Cobo_componentes` GROUP BY `tiket` HAVING count(*) > 1"
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if colaResultado == None:
        print(('Tickets duplicados : %d' % numeroResultado))

    # Buscar tikets a las que les falte relacion entre mercados y monedas
    sql = " SELECT `tiket`,`mercado` FROM `Cobo_componentes` where `mercado` not in (SELECT `nombreUrl` FROM `Cobo_mercado_moneda`)"
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if colaResultado == None:
        print(('Tickets a los que les falta relacion entre mercado y moneda : %d' % numeroResultado))

    # Tickets con errores
#    Cobo_nombreticket = Table('Cobo_nombreticket')
#    select = Cobo_nombreticket.select(Cobo_nombreticket.nombre)
#    select.where = Cobo_nombreticket.fechaError != 'NULL'
    sql = "SELECT `nombre` FROM `Cobo_nombreticket` WHERE `fechaError` IS NOT NULL"
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if colaResultado == None:
        print(('Tickets con errores : %d' % numeroResultado))

    # Tickets pendientes de realiar una actualizacion en la cotizacion
    diaspasados = (datetime.now() - timedelta(days=DIFREGACTUALIZAR['cotizacion'])).strftime("%Y-%m-%d %H:%M:%S")
    diasfuturos = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    sql = "SELECT `nombre` FROM `Cobo_nombreticket` WHERE (`fechaActualizacion`<'" + diaspasados + "' or `fechaActualizacion`>'" + diasfuturos + "' or `fechaActualizacion` IS NULL or `fechaError` IS NOT NULL) ORDER BY `Cobo_nombreticket`.`fechaError` DESC, `Cobo_nombreticket`.`fechaActualizacion` ASC"
    cursor.execute(sql)
    listatickets = cursor.fetchall()
    if colaResultado == None:
        print(('Tickets pendientes de realiar una actualizacion : %d' % len(listatickets)))
    if colaResultado == 'Cotizacion':
        colaResultado = ((ticket[0]) for ticket in listatickets)

    # Tickets pendientes de realiar una actualizacion en el historico
    diaspasados = (datetime.now() - timedelta(days=DIFREGACTUALIZAR['historico'])).strftime("%Y-%m-%d")
    diasfuturos = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    # La lista de acciones para actualizar historico lo debemos hacer partiendo de la tabla Cobo_componentes porque es ahi donde se genera el codigo con el que junto
    # al nombre sirve para el archivo que contendra la BBDD del historico, si no hay codigo porque el ticket no esta en esta tabla, no deberiamos poder descargar el
    # historico. Paso previo, obtener la informacion de la cotizacion y generar el codigo
    sql = "SELECT `tiket` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' AND `tiket` IN (SELECT `nombre` FROM `Cobo_nombreticket` WHERE ((`fechahistorico`<'" + diaspasados + "' or `fechahistorico`>'" + diasfuturos + "' or `fechahistorico` IS NULL) and `fechaActualizacion` IS NOT NULL) ORDER BY `Cobo_nombreticket`.`fechaError` DESC, `Cobo_nombreticket`.`fechahistorico` ASC) ORDER BY `Cobo_componentes`.`tiket` ASC"
#    sql = "SELECT `nombre` FROM `Cobo_nombreticket` WHERE ((`fechahistorico`<'" + diaspasados + "' or `fechahistorico`>'" + diasfuturos + "' or `fechahistorico` IS NULL) and `fechaActualizacion` IS NOT NULL) ORDER BY `Cobo_nombreticket`.`fechaError` DESC, `Cobo_nombreticket`.`fechahistorico` ASC"
    cursor.execute(sql)
    listatickets = cursor.fetchall()
    if colaResultado == None:
        print(('Tickets pendientes de realiar una actualizacion del historico : %d' % len(listatickets)))
    if colaResultado == 'Historico':
        colaResultado = ((ticket[0]) for ticket in listatickets)

    # Con esta consulta podemos comprobar los tickets que no existen en componentes y si en nombreticket, despues de hacer una insercion masiva,....
    sql = "SELECT * FROM `Cobo_nombreticket` WHERE `nombre` not in (SELECT `tiket` FROM `Cobo_componentes`)"
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if colaResultado == None:
        print(('Tickets necesitan de actualizar completamente : %d' % numeroResultado))

    db.close()

    return colaResultado


def ticketalta(ticket):
    """
    """
    cursor, db = conexion()
    ticket = ticket.upper()
    anadido = False
    sql = "SELECT * FROM `Cobo_nombreticket` WHERE `nombre` = '" + ticket + "'"
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if numeroResultado == 0:
        sql = "INSERT INTO `Cobo_nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`, `fechahistorico`) VALUES ('" + ticket + "', '" + str(date.today()) + "', NULL, NULL, NULL)"
        cursor.execute(sql)
        anadido = True
    db.commit()
    db.close()
    return anadido


def ticketborra(ticket, **config):
    """

    """
    cursor, db = conexion()
    ticket = ticket.upper()
    BBDD = config.get('BBDD', True)
    archivos = config.get('archivos', True)
    historico = config.get('historico', True)
    # codigo = config.get('codigo', True)
    # cursor,db=conexionBBDD()

    if ticket != '' or ticket != ' ' or ticket != None:
        if BBDD:
            print(('Borrando de la BBDD el ticket %s' % ticket))

            sql = "SELECT `Cobo_componentes`.`codigo` FROM `Cobo_componentes` WHERE (`Cobo_componentes`.`tiket` = '" + ticket + "')"
            cursor.execute(sql)
            codigo = cursor.fetchall()
            numeroResultado = len(codigo)
            if numeroResultado == 1:
                codigo = str(codigo[0][0])
                sql = "SELECT `Cobo_params_operaciones`.`id` FROM `Cobo_params_operaciones` WHERE (`Cobo_params_operaciones`.`codigo`=" + codigo + ")"
                cursor.execute(sql)
                numeroResultado = len(cursor.fetchall())
                if numeroResultado == 1:
                    sql = "DELETE FROM `Cobo_params_operaciones` WHERE `Cobo_params_operaciones`.`codigo`= " + codigo
                    cursor.execute(sql)
                sql = "DELETE FROM `Cobo_componentes` WHERE `Cobo_componentes`.`tiket` = '" + ticket + "'"
                cursor.execute(sql)

# #            sql = "SELECT `Cobo_maximini`.`nombre` FROM `Cobo_maximini` WHERE (`Cobo_maximini`.`nombre` = '" + ticket + "')"
# #            cursor.execute(sql)
# #            numeroResultado = len(cursor.fetchall())
# #            if numeroResultado == 1:
# #                sql = "DELETE FROM `Cobo_maximini` WHERE `Cobo_maximini`.`nombre`='" + ticket + "' "
# #                cursor.execute(sql)
            sql = "DELETE FROM `Cobo_nombreticket` WHERE `Cobo_nombreticket`.`nombre`='" + ticket + "' "
            cursor.execute(sql)

        if historico:
            print(('Borrando los Datos historicos de la BBDD del ticket %s' % ticket))
            ticket2 = ticket.replace('.', '_')
            ticket2 = ticket2.replace('-', '_')
            ticket2 = ticket2.replace('^', 'Indice')
            sql = "Drop Table IF EXISTS `Ticket_" + ticket2 + "`"
            cursor.execute(sql)

        if archivos:
            print(('Borrando los Archivos de Registro del ticket %s' % ticket))
            # tickets = ticketlistacodigo(ticket)
            # if ticket in tickets:
            # nombre = (str(ticket) + str(tickets[ticket])).replace('.', '_')
            nombre = ('%s' % ticket).replace('.', '_')
            for carpeta in list(CARPETAS.keys()):
                archivosticket = glob.glob(os.path.join(os.getcwd(), CARPETAS[carpeta], nombre + ".*"))
                for archivo in archivosticket:
                    os.remove(archivo)

        db.commit()
        db.close()
        print('')
        return True
    else:
        return False


def ticketcambia(ticketviejo, ticketnuevo):
    """

    """
    ticketviejo = ticketviejo.upper()
    cursor, db = conexion()
    ticketnuevo = (ticketnuevo.upper()).strip('"')
    # cursor,db=conexionBBDD()

    sql = "SELECT * FROM `Cobo_nombreticket` WHERE (`Cobo_nombreticket`.`nombre`='" + ticketnuevo + "') "
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if numeroResultado == 0:
        sql = "INSERT INTO `Cobo_nombreticket` (`nombre`,`fechaRegistro`,`fechaError`,`fechaActualizacion`) VALUES ('%s','%s',NULL, NULL)" % (ticketnuevo, date.today())
        cursor.execute(sql)

    sql = "SELECT * FROM `Cobo_componentes` WHERE (`Cobo_componentes`.`tiket`='" + ticketnuevo + "') "
    cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if numeroResultado == 0:
        sql = "UPDATE `Cobo_componentes` SET `tiket`='" + ticketnuevo + "' WHERE `Cobo_componentes`.`tiket` = '" + ticketviejo + "'"
        cursor.execute(sql)
    elif numeroResultado == 1:
        sql = "SELECT `Cobo_componentes`.`codigo` FROM `Cobo_componentes` WHERE (`Cobo_componentes`.`tiket` = '" + ticketviejo + "')"
        cursor.execute(sql)
        codigo = cursor.fetchall()
        numeroResultado = len(codigo)
        if numeroResultado == 1:
            codigo = str(codigo[0][0])
            sql = "SELECT `Cobo_params_operaciones`.`id` FROM `Cobo_params_operaciones` WHERE (`Cobo_params_operaciones`.`codigo`=" + codigo + ")"
            cursor.execute(sql)
            numeroResultado = len(cursor.fetchall())
            if numeroResultado == 1:
                sql = "DELETE FROM `Cobo_params_operaciones` WHERE `Cobo_params_operaciones`.`codigo`= " + codigo
                cursor.execute(sql)
            sql = "DELETE FROM `Cobo_componentes` WHERE `Cobo_componentes`.`tiket`='" + ticketviejo + "'"
            cursor.execute(sql)

    # sql = "SELECT * FROM `Cobo_maximini` WHERE (`Cobo_maximini`.`nombre`='" + ticketnuevo + "') "
    # cursor.execute(sql)
    # numeroResultado = len(cursor.fetchall())
    # if numeroResultado == 0:
        # sql = "SELECT `Cobo_maximini`.`id` FROM `Cobo_maximini` WHERE (`Cobo_maximini`.`nombre`='" + ticketviejo + "')"
        # cursor.execute(sql)
        # codigo = cursor.fetchall()
        # numeroResultado = len(codigo)
        # if numeroResultado == 1:
            # codigo = str(codigo[0][0])
            # sql = "UPDATE `Cobo_maximini` SET `nombre` = '%s', `fechaRegistro` = '%s' WHERE `Cobo_maximini`.`id` =%s" % (ticketnuevo, ((datetime.now()).strftime("%Y-%m-%d %H:%M:%S")), codigo)
            # cursor.execute(sql)
    # elif numeroResultado == 1:
        # sql = "SELECT * FROM `Cobo_maximini` WHERE (`Cobo_maximini`.`nombre` = '" + ticketviejo + "')"
        # cursor.execute(sql)
        # numeroResultado = len(cursor.fetchall())
        # if numeroResultado == 1:
            # sql = "DELETE FROM `Cobo_maximini` WHERE `Cobo_maximini`.`nombre`='" + ticketviejo + "' "
            # cursor.execute(sql)

    sql = "DELETE FROM `Cobo_nombreticket` WHERE `Cobo_nombreticket`.`nombre`='" + ticketviejo + "'"
    cursor.execute(sql)
    db.commit()
    db.close()

    print(('El ticket %s ha cambiado a %s. Cambiandolo en BBDD' % (ticketviejo, ticketnuevo)))
    print('')
    ticketerror(ticketnuevo)
    ticketborra(ticketviejo)


def ticketerror(ticket):
    """

    """
    ticket = ticket.upper()
    cursor, db = conexion()
    sql = "SELECT `Cobo_nombreticket`.`fechaError` FROM `Cobo_nombreticket` WHERE `Cobo_nombreticket`.`nombre` = '" + ticket + "'"
    cursor.execute(sql)
    hayerror = cursor.fetchall()
    print('')
    print(('Error en el proceso del Ticket %s, error almacenado en BBDD para darle prioridad en proximas actualizaciones' % ticket))
    print('')
    if len(hayerror) > 0 and hayerror[0][0] == None:  # Solo almacenamos error si no habia otro error
        sql = "UPDATE `Cobo_nombreticket` SET `fechaError` ='" + ((datetime.now()).strftime("%Y-%m-%d %H:%M:%S")) + "' WHERE `Cobo_nombreticket`.`nombre`='" + ticket + "' "
        cursor.execute(sql)
        db.commit()
    db.close()


def ticketactualizado(ticket):
    """

    """
    ticket = ticket.upper()
    cursor, db = conexion()
    sql = "UPDATE `Cobo_nombreticket` SET `fechaActualizacion`='" + (datetime.now()).strftime("%Y-%m-%d %H:%M:%S") + "', `fechaError` = NULL  WHERE `Cobo_nombreticket`.`nombre`='" + ticket + "' "
    cursor.execute(sql)
    db.commit()
    db.close()


def ticketactualizadohistorico(ticket, fecha):
    """

    """
    ticket = ticket.upper()
    cursor, db = conexion()
    sql = "UPDATE `Cobo_nombreticket` SET `fechahistorico`='" + fecha + "' WHERE `Cobo_nombreticket`.`nombre`='" + ticket + "' "
    cursor.execute(sql)
    db.commit()
    db.close()


def ticketcotizaciones(nombreticket, datosurl):
    """
    """
    # datosurl=datosurl.replace('ñ','n')
    cursor, db = conexion()
    datosurl2 = datosurl.rsplit(',', 10)
    datonombre, datoticket, datomercado, datomax52, datomaxDia, datomin52, datominDia, datoValorActual, datovolumenMedio, datovolumen, datoerror = datosurl2
    datoticket = datoticket.strip('"')

    # comillas = datosurl[1:].find('"')#Esto es porque en ocasiones el nombre lleva una coma
    # datonombre = datosurl[:(comillas + 2)]
    # datosurl2 = datosurl.split(',')
    # datomax52, datomaxDia, datomin52, datominDia, datoValorActual = datosurl2[-8], datosurl2[-7], datosurl2[-6], datosurl2[-5], datosurl2[-4]
    # datoticket = datosurl2[-10].strip('"')

        # hay que prevenir esto
    # "Fuel Tech, Inc.","FTEK","NasdaqNM",11.20,NULL,3.77,NULL,5.82,135258,0,"N/A"   coma en el nombre
    # "MI Developments I","MIM","NYSE",33.35,30.75,16.07,30.33,30.45,238848,136519,"N/A"

        # el ticket ha cambiado, comprobar que no existe ya y en tal caso sustuirlo
    if '"No such ticker symbol.' in datosurl or 'Missing Symbols List.' in datosurl or 'Missing Format Variable.' in datosurl:  # ".DJA",".DJA",N/A,0,"N/A",N/A,N/A,N/A,N/A,0.00,"No such ticker symbol. <a href="/l">Try Symbol Lookup</a> (Look up: <a href="/l?s=.DJA">.DJA</a>)"
        ticketborra(nombreticket)  # FIXME: los tickets con sufijo .MC estan contestando asi "GRF.MC","GRF.MC","N/A",N/A,N/A,N/A,N/A,0.00,0,N/A,"No such ticker symbol. <a href="/l">Try Symbol Lookup</a> (Look up: <a href="/l?s=GRF.MC">GRF.MC</a>)"

    elif ('Ticker symbol has changed to: <a href="/q?s=' in datosurl):
        print (datosurl)
        ticketinicio = datosurl.find('<a href="/q?s=') + len('<a href="/q?s=')
        ticketfin = datosurl.find('">', ticketinicio)
        ticketnuevo = (datosurl[ticketinicio:ticketfin]).strip('"')
        ticketcambia(nombreticket, ticketnuevo)

    # hay casos en los que nos descargamos la informacion de nombreticket pero en la informacion descargada el ticket ha cambiado
    elif datoticket != nombreticket:
        print (datosurl)
        # ticketnuevo = ( datosurl2[-10].strip( '"' ) )
        ticketcambia(nombreticket, datoticket)

    else:
        sql = "SELECT * FROM `Cobo_componentes` WHERE `tiket` = '" + nombreticket + "'"
        cursor.execute(sql)
        datosBBDDcomponentes = cursor.fetchall()
        numeroResultado = len(datosBBDDcomponentes)
        if numeroResultado == 0:
            sql = "INSERT INTO `Cobo_componentes` (`codigo` ,`nombre` ,`tiket` ,`mercado` ,`max52` ,`maxDia` ,`min52` ,`minDia` ,`valorActual` ,`volumenMedio` ,`volumen` ,`error` ,`fechaRegistro`) VALUES (NULL , " + datosurl + ",'" + str(date.today()) + "')"
            cursor.execute(sql)

        elif numeroResultado == 1:
            codigo = datosBBDDcomponentes[0][0]
            sql = "UPDATE `Cobo_componentes` SET `nombre`= %s, `mercado`=%s ,`max52`=%s ,`maxDia`=%s ,`min52`=%s ,`minDia`=%s ,`valorActual`=%s ,`volumenMedio`=%s ,`volumen`=%s ,`error`=%s ,`fechaRegistro`='%s'  WHERE `Cobo_componentes`.`tiket` = '%s'" % (datonombre, datomercado, datomax52, datomaxDia, datomin52, datominDia, datoValorActual, datovolumenMedio, datovolumen, datoerror, date.today(), nombreticket)
            # sql = "UPDATE `Cobo_componentes` SET `nombre`= %s, `mercado`=%s ,`max52`=%s ,`maxDia`=%s ,`min52`=%s ,`minDia`=%s ,`valorActual`=%s ,`volumenMedio`=%s ,`volumen`=%s ,`error`=%s ,`fechaRegistro`='%s'  WHERE `Cobo_componentes`.`tiket` = '%s'" % (datonombre, datosurl2[-9], datosurl2[-8], datosurl2[-7], datosurl2[-6], datosurl2[-5], datosurl2[-4], datosurl2[-3], datosurl2[-2], datosurl2[-1], date.today(), nombreticket)
            cursor.execute(sql)
            sql = "SELECT * FROM `Cobo_params_operaciones` WHERE `Cobo_params_operaciones`.`codigo` = %s" % codigo
            cursor.execute(sql)
            datosBBDDoperaciones = cursor.fetchall()
            numeroResultado = len(datosBBDDoperaciones)
            if numeroResultado == 1:
                ident, precio_ini, precio_fin, _fecha_ini, _fecha_fin, _timing, _precio_salida, salida, entrada, _rentab, _codigoBBDD = datosBBDDoperaciones[0]

                if salida == None or salida == '':
                    salida = 0.0
                elif type(salida) == unicode or type(salida) == str:
                    # Corregimos un posible fallo. Cuando en un analisis introducimos datos manualmente, posteriormente cuando recuperamos esa informacion
                    # lo que recuperamos es un valor unicode con con coma y no punto u'48,760'
                    salida = float(salida.replace(',', '.'))

                if entrada == None or salida == '':
                    entrada = 0.0
                elif type(entrada) == unicode or type(salida) == str:
                    entrada = float(entrada.replace(',', '.'))

                if precio_ini <= precio_fin:  # datos de una accion alcista
                    if (datomax52 != 'NULL' and datomax52 > entrada) or (datomaxDia != 'NULL' and datomaxDia > entrada) or (datoValorActual != 'NULL' and datoValorActual > entrada):  # si true, analisis ya cumplido, obsoleto y lo actualizamos
                        sql = "UPDATE `Cobo_params_operaciones` SET `entrada` = NULL, `salida` = NULL, `precio_salida` = %.3f WHERE `Cobo_params_operaciones`.`id` =%s" % (salida, ident)
                        cursor.execute(sql)

                if precio_ini > precio_fin:  # datos de una accion bajista
                    if (datomin52 != 'NULL' and datomin52 < entrada) or (datominDia != 'NULL' and datominDia < entrada) or (datoValorActual != 'NULL' and datoValorActual < entrada):
                        sql = "UPDATE `Cobo_params_operaciones` SET `entrada` = NULL, `salida` = NULL, `precio_salida` = %.3f WHERE `Cobo_params_operaciones`.`id` =%s" % (salida, ident)
                        cursor.execute(sql)
            # en este update, habra que comprobar la table params_operaciones para hacer que borre los analisis obsoletos

        print(('Actualizando cotizaciones de : %s' % nombreticket))
        print(('Actualizando %s con datos %s' % (nombreticket, datosurl)))
        db.commit()
        db.close()
        ticketactualizado(nombreticket)


def ticketlistacodigo(ticket=None):
    """

    """
    cursor, db = conexion()
    if ticket == None:
        sql = "SELECT `Cobo_componentes`.`tiket`, `Cobo_componentes`.`codigo` FROM `Cobo_componentes` ORDER BY `Cobo_componentes`.`tiket` ASC"
    else:
        sql = ("SELECT `Cobo_componentes`.`tiket`, `Cobo_componentes`.`codigo` FROM `Cobo_componentes` WHERE (`Cobo_componentes`.`tiket` = '%s') ORDER BY `Cobo_componentes`.`tiket` ASC" % ticket)
#        sql="SELECT `Cobo_componentes`.`tiket`, `Cobo_componentes`.`codigo` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` = 'N/A' ORDER BY `Cobo_componentes`.`tiket` ASC"
    tickets = {}
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    if resultado != None:

        for registro in resultado:
            # if not tickets.has_key(registro[0]):
    #                if registro[0][0]=='.':
    #                    ticket='^'+registro[0][1:].upper()
    #                else:
    #                    ticket=registro[0].upper()
            tickets[registro[0]] = (registro[1])

        return tickets
    else:
        return False


def datoshistoricosexisten(naccion):
    """

    """
    # Pero esta vez seran BBDD que contengan una tabla con su historico
    # habra que comprobar:
        # que esxiste el archivo
        # que existe la tabla dentro del archivo
    naccion = naccion.upper()
#    tickets = ticketlistacodigo(naccion)
    existe = False
#    if naccion in tickets:
    nombre = ('%s' % naccion).replace('.', '_')
#        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
    archivo = os.path.join(os.getcwd(), CARPETAS['Datos'], nombre + ".dat")

    if os.path.exists(archivo):
        # el archivo que contiene la BBDD de la cotizacion historica existe
        cursor2, db2 = conexion(naccion)
        naccion2 = naccion.replace('.', '_')
        naccion2 = naccion2.replace('-', '_')
        naccion2 = naccion2.replace('^', 'Indice')
        sql = ("SELECT name FROM sqlite_master WHERE type='table' and name = 'Ticket_%s'" % naccion2)
        cursor2.execute(sql)
        if len(cursor2.fetchall()) > 0:
            existe = True
        else:
            print ('No existe informacion historico descargado')
        db2.close()
    else:
        print ('No existe archivo historico descargado')
#    else:
#        print ('No existe informacion de cotizaciones en BBDD')
#        # borraTicket (ticket, BBDD=False)
#        # No tiene sentido que intente borrar los archivos, no exista tickets en el diccionario y no puedo componer el nombre de los archivos
#        ticketerror(naccion)

    return existe


def datoshistoricoscreatabla(naccion):
    """

    """
    naccion = naccion.upper()
    cursor2, db2 = conexion(naccion)
    naccion2 = naccion.replace('.', '_')
    naccion2 = naccion2.replace('-', '_')
    naccion2 = naccion2.replace('^', 'Indice')
    sql = ("CREATE TABLE IF NOT EXISTS Ticket_%s ( \
    `fecha` DATE PRIMARY KEY NOT NULL UNIQUE, \
    `apertura` FLOAT( 0, 0 ) NOT NULL, \
    `maximo` FLOAT( 0, 0 ) NOT NULL, \
    `minimo` FLOAT( 0, 0 ) NOT NULL, \
    `cierre` FLOAT( 0, 0 ) NOT NULL, \
    volumen INTEGER( 0, 0 ) NOT NULL)" % naccion2)
    cursor2.execute(sql)
    db2.commit()
    db2.close()
    return


def datoshistoricoslee(naccion):
    """

    """
    # hay que crear una Conexion() especifica, utilizaremos los mismo nombres de archivos
    naccion = naccion.upper()
    cursor2, db2 = conexion(naccion)
    naccion2 = naccion.replace('.', '_')
    naccion2 = naccion2.replace('-', '_')
    naccion2 = naccion2.replace('^', 'Indice')
    historico = []
    if datoshistoricosexisten(naccion):
        sql = ("SELECT * From `Ticket_%s` ORDER BY fecha ASC" % naccion2)
        cursor2.execute(sql)
        historico = cursor2.fetchall()

    else:
        datoshistoricoscreatabla(naccion)
        # ticketerror(naccion)
    db2.close()
    return historico


def datoshistoricosgraba(naccion, historico):
    """

    """
    # grabar el archivo, igual que antes, que contiene la bbdd
    # hay que crear una Conexion() especifica, utilizaremos los mismo nombres de archivos
    naccion = naccion.upper()
    datoshistoricoscreatabla(naccion)
    cursor2, db2 = conexion(naccion)
    tabla = naccion.replace('.', '_')
    tabla = tabla.replace('-', '_')
    tabla = tabla.replace('^', 'Indice')
    cursor2.execute("DELETE FROM Ticket_%s" % tabla)
    for n in historico:
        fecha, apertura, maximo, minimo, cierre, volumen = n
        sql = ("INSERT INTO Ticket_%s (`fecha`,`apertura`,`maximo`,`minimo`,`cierre`,`volumen`) VALUES ('%s',%f,%f,%f,%f,%d)" % (tabla, fecha, apertura, maximo, minimo, cierre, volumen))
        cursor2.execute(sql)
    db2.commit()
    db2.close()
    if len(historico) > 0:
        ticketactualizadohistorico(naccion, fecha)
    else:
        ticketactualizadohistorico(naccion, 'NULL')


def datoshistoricosactualizacion(naccion):
    """

    """
    # TODO: Podemos intentar integrar la funcion actualizacionDatosHisAccion dentro de la propia funcion descargaHistoricoAccion, nos ahorrariamos una funcion y seguramente procesos duplicados
    # Con esta consulta nos devuelve la ultima fecha acumulada
    # sql = (SELECT MAX(fecha) FROM 'Ticket_%s'%naccion
    # compararla como lo hacemos ahora fechaultimoregistro con la fechahoy y restarle 2 dias en vez de utilizar el historico[-3],
    # el problema puede ser que al restarle 2 podemos pillar un fin de semana por enmedio
    historico = datoshistoricoslee(naccion)

    if len(historico) < 3:  # al devolverno true=actualizar pero sin fecha, en la funcion descargaHistoricoAccion entiende que tiene que descargar todo el historico
        print('Registro insuficiente. Actualizacion completa')
        return (None, True)

    fechahoy = ((date.today().timetuple()))

    fechaultimoregistro = list(map(int, ((historico[-1][0]).split('-'))))

    desdeultimaactualizacion = (date(fechahoy[0], fechahoy[1], fechahoy[2]) - date(fechaultimoregistro[0], fechaultimoregistro[1], fechaultimoregistro[2])).days
# Comparar fecha de hoy con la del archivo he incluirla en el if con un and
# en esta funcion hay que hacer que cuando el len de datosaccion no es sufieciente, menor de 3 registros, que automaticamente responda para que la funcion de descarga descarge con un timming inferior
#    desdeultimaactualizacionarchivo=(date(fechahoy[0],fechahoy[1],fechahoy[2])-date(fechaarchivo[0],fechaarchivo[1],fechaarchivo[2])).days

    if (desdeultimaactualizacion > DIFREGACTUALIZAR['historico']):  # and (desdeultimaactualizacionarchivo>difregistros):
        print(('Registro pendiente de una actualizacion desde %s' % (historico[-2][0])))
        return (str(historico[-3][0]), True)
    else:
        print('Registro actualizado')
        print('')
        return ((historico[-1][0]), False)


def mercadoslista():
    """

    """
    cursor, db = conexion()
    sql = "SELECT `Cobo_mercados`.`mercado` FROM `Cobo_mercados` WHERE `Cobo_mercados`.`habilitado` = 'True'"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    mercados = []
    for m in resultado:
        mercado = m[0]
        mercado = mercado.replace('@%5E', '^')
        mercado = mercado.replace('@%5e', '^')
        mercados.append(mercado)
    db.close()
    return mercados


def mercadosdeshabilita(mercado):
    """

    """
    cursor, db = conexion()
    mercado = mercado.upper()
    sql = "UPDATE `Cobo_mercados` SET `habilitado` = 'False' WHERE `mercado` = '%s'" % mercado
    cursor.execute(sql)
    db.close()


def monedacotizaciones(nombreticket, datosurl):
    """
    """
    cursor, db = conexion()
    datosurl2 = datosurl.split(',')
    datoticket = datosurl2[0].strip('"')
    datoprecio = datosurl2[1]
    if nombreticket == 'EURGBP=X':
        print ('Caso especial, libra Esterlina convertida en peniques')
        datoprecio = str(float(datoprecio) * 100)

    if '"No such ticker symbol.' in datosurl or 'Missing Symbols List.' in datosurl:  # ".DJA",".DJA",N/A,0,"N/A",N/A,N/A,N/A,N/A,0.00,"No such ticker symbol. <a href="/l">Try Symbol Lookup</a> (Look up: <a href="/l?s=.DJA">.DJA</a>)"
        print(('La Moneda %s no existe' % nombreticket))

    elif ('Ticker symbol has changed to: <a href="/q?s=' in datosurl) or datoticket != nombreticket:
        print (datosurl)
        print(('La Moneda %s ha cambiado a %s' % (nombreticket, datoticket)))

    else:

        sql = "SELECT `codigo` FROM `Cobo_monedas` WHERE `url_Inet` = '" + nombreticket + "'"
        cursor.execute(sql)
        datosBBDDcomponentes = cursor.fetchall()
        codigo = datosBBDDcomponentes[0][0]
        # sql = "UPDATE `lomiologes_cobodb`.`Cobo_monedas` SET `valor` = '%s', `fechaRegistro` = '%s' WHERE `Cobo_monedas`.`codigo` = '%s'" % (datoprecio , (datetime.now()).strftime("%Y-%m-%d %H:%M:%S") , codigo)
        sql = "UPDATE `Cobo_monedas` SET `valor` = '%s', `fechaRegistro` = '%s' WHERE `Cobo_monedas`.`codigo` = '%s'" % (datoprecio, (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"), codigo)
        cursor.execute(sql)
        db.commit()
        db.close()

        print(('Actualizando cotizaciones de : %s' % nombreticket))
        print(('Actualizando %s con datos %s' % (nombreticket, datosurl)))


def listacciones(**config):
    """
    """
    vol = config.get('volumen', 20000000)
    rent = config.get('rentabilidad', 0.35)
    inv = config.get('inversion', 900)
    riesgo = config.get('riesgo', 200)

    cursor, db = conexion()
    sql = ("SELECT Cobo_componentes.tiket AS Ticket,\
       Cobo_componentes.nombre AS Nombre,\
       Cobo_componentes.mercado AS Mercado,\
       Cobo_monedas.descripcion AS Moneda,\
       Cobo_params_operaciones.timing AS Timing,\
       round( Cobo_params_operaciones.rentabilidad * 100, 2 ) AS Rentabilidad,\
       round( (  (  (  ( round( ( Cobo_monedas.valor * %d ) / ( Cobo_params_operaciones.entrada - Cobo_params_operaciones.salida ) , 0 )  ) * Cobo_params_operaciones.entrada )  ) / Cobo_monedas.valor ) , 2 ) AS InversionEnEuros,\
       Cobo_params_operaciones.entrada AS Entrada,\
       Cobo_params_operaciones.salida AS Salida,\
       round( ( Cobo_monedas.valor * %d ) / ( Cobo_params_operaciones.entrada - Cobo_params_operaciones.salida ) , 0 ) AS NumeroAcciones,\
       Cobo_params_operaciones.fecha_ini AS [LT Fecha Ini],\
       Cobo_params_operaciones.precio_ini AS [LT Precio Ini],\
       Cobo_params_operaciones.fecha_fin AS [LT Fecha Fin],\
       Cobo_params_operaciones.precio_fin AS [LT Precio Fin]\
  FROM Cobo_componentes,\
       Cobo_mercado_moneda,\
       Cobo_monedas,\
       Cobo_params_operaciones\
 WHERE Cobo_componentes.mercado = Cobo_mercado_moneda.nombreUrl\
       AND\
       Cobo_mercado_moneda.abrevMoneda = Cobo_monedas.codigo\
       AND\
       Cobo_componentes.codigo = Cobo_params_operaciones.codigo\
       AND\
        (  (  ( Cobo_componentes.valorActual / Cobo_monedas.valor ) * Cobo_componentes.volumenMedio * 21 >= %d )\
           OR\
        (  ( Cobo_componentes.valorActual / Cobo_monedas.valor ) * Cobo_componentes.volumen * 21 >= %d )  )\
       AND\
        ( Cobo_params_operaciones.rentabilidad >= %f\
           OR\
       Cobo_params_operaciones.rentabilidad <= -(%f/(1+%f) )\
           OR\
       Cobo_params_operaciones.rentabilidad = 0.0 )\
       AND\
        ( InversionEnEuros >= %d\
           OR\
       InversionEnEuros <= -(%d) )\
       AND\
       NOT ( Cobo_componentes.mercado = 'Other OTC'\
           OR\
           Cobo_componentes.mercado = 'PCX'\
           OR\
           Cobo_componentes.mercado = 'IOB'\
           OR\
           Cobo_componentes.mercado = 'PSX'\
           OR\
       Cobo_componentes.mercado = 'NGM' )\
 ORDER BY Moneda DESC, Cobo_params_operaciones.rentabilidad DESC, InversionEnEuros DESC" % (riesgo, riesgo, vol, vol, rent, rent, rent, inv, inv))
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    resultado2 = []
    for ticket, nombre, mercado, moneda, timming, rent, inve, entrada, salida, numaccion, ltdateini, ltpriceini, ltdatefin, ltpricefin in resultado:
        numaccion = int(numaccion)
        nombre = nombre.encode('UTF-8')
        resultado2.append((ticket, nombre, mercado, moneda, timming, rent, inve, entrada, salida, numaccion, ltdateini, ltpriceini, ltdatefin, ltpricefin))
    return tuple(resultado2)


def listaccionesLT(**config):
    """
    """
    vol = config.get('volumen', 20000000)
    rent = config.get('rentabilidad', 0.35)
    inv = config.get('inversion', 900)
    riesgo = config.get('riesgo', 200)
    incremperiod = config.get('incremperiod', 0)

    cursor, db = conexion()
    sql = ("SELECT Cobo_componentes.tiket AS Ticket,\
       Cobo_componentes.nombre AS Nombre,\
       Cobo_componentes.mercado AS Mercado,\
       Cobo_monedas.descripcion AS Moneda,\
       Cobo_monedas.valor As divisa,\
       Cobo_params_operaciones.timing AS Timing,\
       round( Cobo_params_operaciones.rentabilidad * 100, 2 ) AS Rentabilidad,\
       Cobo_params_operaciones.precio_salida AS Salida,\
       Cobo_params_operaciones.fecha_ini AS [LT Fecha Ini],\
       Cobo_params_operaciones.precio_ini AS [LT Precio Ini],\
       Cobo_params_operaciones.fecha_fin AS [LT Fecha Fin],\
       Cobo_params_operaciones.precio_fin AS [LT Precio Fin],\
       Cobo_componentes.maxDia AS MaxDia,\
       Cobo_componentes.minDia AS MinDia,\
       Cobo_componentes.valorActual AS ValorActual\
  FROM Cobo_componentes,\
       Cobo_mercado_moneda,\
       Cobo_monedas,\
       Cobo_params_operaciones\
 WHERE Cobo_componentes.mercado = Cobo_mercado_moneda.nombreUrl\
       AND\
       Cobo_mercado_moneda.abrevMoneda = Cobo_monedas.codigo \
       AND\
       Cobo_componentes.codigo = Cobo_params_operaciones.codigo\
       AND\
       ( ( ( Cobo_componentes.valorActual / Cobo_monedas.valor ) * Cobo_componentes.volumenMedio * 21 >= %d )\
           OR\
       ( ( Cobo_componentes.valorActual / Cobo_monedas.valor ) * Cobo_componentes.volumen * 21 >= %d )  )\
       AND\
       ( Cobo_params_operaciones.rentabilidad >= %f\
           OR\
           Cobo_params_operaciones.rentabilidad <=-( %f /( 1 + %f )  )\
           OR\
       Cobo_params_operaciones.rentabilidad = 0.0 )\
       AND\
           (Cobo_params_operaciones.precio_ini > 0.0\
           AND\
           Cobo_params_operaciones.precio_fin > 0.0)\
       AND\
       NOT( Cobo_componentes.mercado = 'Other OTC'\
           OR\
           Cobo_componentes.mercado = 'PCX'\
           OR\
           Cobo_componentes.mercado = 'IOB'\
           OR\
           Cobo_componentes.mercado = 'PSX'\
           OR\
           Cobo_componentes.mercado = 'NGM' )\
 ORDER BY Cobo_monedas.descripcion DESC,\
           Cobo_params_operaciones.rentabilidad DESC" % (vol, vol, rent, rent, rent))
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    resultado2 = []
    # TODO: comprobar si al precio_salida hay que aplicarle los filtros en funcion del timming

    for ticket, nombre, mercado, moneda, divisa, timming, rent, salida, ltdateini, ltpriceini, ltdatefin, ltpricefin, maxDia, minDia, valorActual in resultado:
        nombre = nombre.encode('UTF-8')
        entrada = precioentradaLT(ltdateini, ltpriceini, ltdatefin, ltpricefin, timming, incremperiod=incremperiod)
        if entrada!=salida:
            numaccion = int((divisa * riesgo) / (entrada - salida))
        else:
            numaccion = 0
        inve = round((numaccion * entrada) / divisa, 2)

        # dependiendo de si es alcista o bajista que:
        # Comprobamos inversion minima
        # en alcista el precio de entrada se encuenta por debajo de los precios de maximo diario, minimo diario, cotizacion actual y la entrada esta por encima de la salida
        # en bajista el precio de entrada se encuenta por encima de los precios de maximo diario, minimo diario, cotizacion actual y la entrada esta por debajo de la salida
        if inve >= inv and\
            ((rent >= 0.0 and\
              (maxDia >= entrada and minDia >= entrada and valorActual >= entrada and entrada >= salida)) or\
             (rent < 0.0 and \
              (maxDia <= entrada and minDia <= entrada and valorActual <= entrada and entrada <= salida))):  # Bajista
            resultado2.append((ticket, nombre, mercado, moneda, timming, rent, inve, entrada, salida, numaccion, ltdateini, ltpriceini, ltdatefin, ltpricefin))

    return tuple(resultado2)


if __name__ == '__main__':
    pass
