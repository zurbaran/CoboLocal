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


####################################################
# modulos estandar importados

# import urllib

from collections import deque
from datetime import date, datetime  # , timedelta
from random import randint
from time import sleep
import csv
import glob
import logging
import os

import indicador
import BBDD
import yahoofinance

import HTML
# TODO: implementar la libreria HTML para generar archivos en formato html de las consultas/resultados de la BBDD

# from adodbapi.adodbapi import type
# import traceback
# from decimal import Decimal
# import sys
# import locale

#################################################
setdefaultencoding = ('UTF-8')
# sys.setdefaultencoding('UTF-8')
# locale.setlocale(locale.LC_ALL, "")


#################################################
# Constantes locales

sufijosexcluidos = ('.BA', '.BC', '.BE', '.BI', '.BM', '.BO', '.CBT', '.CME',
    '.CMX', '.DU', '.EX', '.F', '.HA', '.HM', '.JK', '.KL', '.KQ', '.KS',
    '.MA', '.MF', '.MU', '.MX', '.NS', '.NYB', '.NYM', '.NZ', '.SA', '.SG',
    '.SI', '.SN', '.SS', '.SZ', '.TA', '.TW', '.TWO', '.VA',)
__carpetas__ = {'Analisis': 'Analisis', 'Backtest': 'Backtest', 'Datos': 'Datos',
    'Historicos': 'Historicos', 'Log': 'Log', 'Graficos': 'amstock'}
# Expresa la diferencia entre los registros para hacer una actualizacion
__difregactualizar__ = {'d': 10, 'w': 15, 'm': 33, 'noActualizados': 120}
backtestoperacionessospechosas = 1.50

# import logging.config
__ARCHIVO_LOG__ = os.path.join(os.getcwd(), __carpetas__['Log'], "general.log")
# logging.config.fileConfig(ARCHIVO_LOG)
# logging.basicConfig(filename = ARCHIVO_LOG)
# logging.captureWarnings(True)
# basic setup with ISO 8601 time format
logging.basicConfig(filename=__ARCHIVO_LOG__,
    format='%(asctime)sZ; nivel: %(levelname)s; modulo: %(module)s; Funcion : %(funcName)s; %(message)s',
    level=logging.DEBUG)
logging.debug('\n')
logging.debug('Inicio de Aplicacion')


############################################################
# comprobaciones especiales

# assert

# Buscar tickets duplicados en la BBDD
# SELECT `tiket`, count(*)
# FROM `Cobo_componentes`
# GROUP BY `tiket` HAVING count(*) > 1

# Lista de los distintos mercados a los que pertenecen los tickets y cantidad de tickets para cada uno de ellos
# SELECT `mercado`, count(*) FROM `Cobo_componentes` GROUP BY `mercado` HAVING count(*) > 0

# Buscar tikets a las que les falte relacion entre mercados y monedas
# SELECT `tiket`,`mercado` FROM `Cobo_componentes` where `mercado` not in (SELECT `nombreUrl` FROM `Cobo_mercado_moneda`)

# Con esta consulta podemos comprobar los tickets que no existen en componentes y si en nombreticket, despues de hacer una insercion masiva,....
# SELECT * FROM `Cobo_nombreticket` WHERE `nombre` not in (SELECT `tiket` FROM `Cobo_componentes`)


# Cualquier rentabilidad positiva dividido por 1, esa rentabilidad te dara la negativa y al reves 1- la rentabilidad negativa dividido por esa negativa te da la positiva
# 35 dividido por 1,35 te da 25,925 y al reves 1- 0,25925 =0,7407. Que si lo dividimos por el nos da 35.       25,925/0.7407=35
# rentabilidadnegativa= - (rentabilidadpositiva / (1+rentabilidadpositiva))
# rentabilidadpositiva= 1-(rentabilidadnegativa / (1-rentabilidadnegativa))


############################################################
# definicion de funciones


def _test():
    import doctest
    doctest.testmod()
    # TODO: implementar pruebas doctest
    # ejemplos en : http://mundogeek.net/archivos/2008/09/17/pruebas-en-python/  http://magmax9.blogspot.com.es/2011/09/python-como-hacer-pruebas-1.html
    # Externalizar los test
    # doctest.testfile('example2.txt')


def duerme(tiempo=1500):
    """

    """
    x = (randint(0, tiempo)) / 1000.0
    print('Pausa de %.3f segundos' % x)
    sleep(x)
    print('')


def analisisAlcistaAccion(naccion, **config):
    """ Analisis alcista
    timming=d/w/m, timming a analizar
    desdefecha=False o tupla (true/false,AAAA-MM-DD), fecha desde la que queremos recuperar analisis, fecha incluida, devuelbe todos los analisis cuya resistencia sea desde esta fecha
    txt=True/False, configuracion para hacer que genere archivos txt del analisis
    conEntradaLT = True/False, si queremos que nos incluya los analisis de LT, posibles entradas en LT
    MME = False/entero, Si queremos que se trace una Media Movil Exponencial, no utilizando el concepto de Maximo historico como tal
    filtro = 0.00, flotante filtro aplicado al soporte como precio de salida
    ADX=False/entero

    Resultado es: Resistencia,Soporte,Ruptura Resistencia,Punto LineaTendenciaInicio,Punto LineaTendenciaFin,timming del analisis, indicadores
                    el formato obtenido es:
                                Resistencia , soporte , Salida Lt = fecha,apertura, maximo, minimo, cierre, volumen
                                punto LT = fecha inicio, precio inicio
                                salida Lt = Soporte anterior
                                indicadores=(ADX, DI+, DI-)

    """

    # TODO: separar la funcion en la lectura, analisis y grabar datos, creando una funcion interna que nos sirva para darle la lista que contiene los datos y devuelva el analisis. De esta manera podre esternalizar la funcion y llamarla desde un programa
    # anadido un nuevo dato dando como resultado: Resistencia,Soporte,Ruptura Resistencia,Punto LineaTendenciaInicio,Punto LineaTendenciaFin, Punto de salida,timming del analisis
        # Anadiendo el Punto de Salida futuro, dandolo como valor inicial False y si en mitad del analisis el precio esta por debajo del Soporte menos el filtro cambiar todos los falses de la lista analisisalcista donde el valor es false asignandole la barra en la que ha roto el soporte-filtro=stoploss
        # anadido un nuevo parametro para hacer lo anterior, filtro de la resistencia = Stoploss

    naccion = naccion.upper()

    historico = BBDD.datoshistoricoslee(naccion)

    conEntradaLT = config.get('conEntradaLT', True)
    MME = config.get('MME', False)
    if MME == False:
        MME2 = False
    else:
        MME2 = config.get('MME2', False)
    TAR = config.get('TAR', False)
    ADX = config.get('ADX', False)
    filtro = config.get('filtro', 0.0)
    timming = config.get('timming', "m")
    desdefecha = config.get('desdefecha', False)
    txt = config.get('txt', True)  # Parametro para hacer que la funcion cree el archvo del analisis

    if desdefecha == '' or desdefecha == ' ' or desdefecha == None:
        desdefecha = False
    elif desdefecha != False:
        todohistorico, desdefecha = desdefecha

    if timming == 'd':
        datoshistoricos = historico
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.01
            else:
                filtro = 3.5
    elif timming == 'w':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='w')
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.02
            else:
                filtro = 2.5
    elif timming == 'm':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='m')
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.03
            else:
                filtro = 1.5

    analisisalcista = []
    listastoploss = []

    i, r, s, LTi, LTf = 0, 0, 0, 0, 0
    resistencia = True
    soporte = False
    stoploss = 0.0
    salidaOperacion = False
    entradapuntoLT = False

#    datoshistoricos = []
#    volumenMME = indicador.MME(datoshistoricos2, MME=5, indicedatos='volumen')
#    while i < len(datoshistoricos2):
#        assert (datoshistoricos2[i][0] == volumenMME[i][0])
#        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos2[i]
#        datoshistoricos.append((fecha, apertura, maximo, minimo, cierre, volumenMME[i][1]))
#        i += 1
#    del datoshistoricos2

    if desdefecha != False and todohistorico == False:  # Borramos el historico anterior a la fecha
        i = 0
        while i < len(datoshistoricos):
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = datoshistoricos[i]
            if fecha >= desdefecha:
                datoshistoricos = datoshistoricos[i:]
                del fecha, _apertura, _maximo, _minimo, _cierre, _volumen
                break
            if i == (len(datoshistoricos) - 1) and fecha < desdefecha:  # Ha llegado al final de sin encontrar una fecha de analisis mayor a desdefecha
                datoshistoricos = []
            i += 1

    i = 0

    if not(MME == False):
        puntosMME = indicador.MME(datoshistoricos, MME=MME)
        if not(MME2 == False):
            puntosMME2 = indicador.MME(datoshistoricos, MME=MME2)
    if not (TAR == False):
        puntosTAR = indicador.TAR(datoshistoricos, TAR=TAR)

    if not (ADX == False):
        puntosADX = indicador.ADX(datoshistoricos, ADX=ADX)
        puntosDI = indicador.DI(datoshistoricos, DI=ADX)

    while i < len(datoshistoricos):
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos[i]

        if i == 0:
            ant = 0
        else:
            ant = i - 1
        fechaanterior, _aperturaanterior, _maximoanterior, minimoanterior, cierreanterior, _volumenanterior = datoshistoricos[ant]
        _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]
        _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[s]

        if not (ADX == False):
            fechaADX, puntoADX = puntosADX[ant]
            fechaDI, puntoDIplus, puntoDIminus = puntosDI[ant]
            assert (fechaADX == fechaanterior or fechaDI == fechaanterior)
        else:
            puntoADX = False
            puntoDIplus = False
            puntoDIminus = False
        indicadores = (puntoADX, puntoDIplus, puntoDIminus)

        if not (TAR == False):
            fechaTAR, puntoTAR = puntosTAR[ant]

            assert (fechaTAR == fechaanterior)

            if len(analisisalcista) > 0 and stoploss < (round((cierreanterior - (puntoTAR * filtro)), 3)):
                stoploss = round((cierreanterior - (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

        if not (MME == False):  # and len( datoshistoricos ) >= MME:

            fechaMME, puntoMME = puntosMME[i]
            if not (MME2 == False):
                fechaMME2, puntoMME2 = puntosMME2[i]
                assert (fechaMME == fecha and fechaMME == fechaMME2)

            assert (fechaMME == fecha)

            # if i >= ( MME - 1 ):# Empieza a utilizar el indicador.MME en una barra en concreto, para la MME30 lo utiliza apartir de la barra 30(cuyo indice es 29)
            if puntoMME > 0:
                if resistencia == False and soporte == False and puntoMME < minimo:  # Si no buscamos ni resistencias ni soportes es porque venimos de debajo de la MME
                    # la grafica esta completamente por encima de la MME,  y empezamos a buscar resistencias sobre la MMe
                    r = i
                    _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]
                    resistencia = True
                    soporte = False
                # elif maximo < puntoMME:# Grafica completamente bajo Media Movil Exponencial, no buscamos resistencias ni soportes, y consideramos la barra actual como resistencia
                elif maximo < puntoMME and (MME2 == False or (MME2 != False and puntoMME <= puntoMME2)):
                    # con esta logica, si hemos creado una resistencia y en algun momento bajamos una MME muy cercana a la grafica, habremos "borrado" esa resistencia anterior asignandole la barra actual como resistencia
                    r = i
                    _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]
                    resistencia = False
                    soporte = False

        # anade en analisisalcista, los puntos de entrada por Linea de tendencia
        if len(analisisalcista) > 0 and entradapuntoLT:

            LineaTendenciaInicio = analisisalcista[-1][3]
            LineaTendenciaFin = analisisalcista[-1][4]

            _fechaLTi, minimoLTi = LineaTendenciaInicio
            _fechaLTf, minimoLTf = LineaTendenciaFin

            if minimoLTi > 0 and minimoLTf > 0:

                precioentradapuntoLT = round((minimoLTi * ((1 + (((1.0 + (((minimoLTf - minimoLTi) / minimoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((i - LTi) / 12.0))), 3)

                if precioentradapuntoLT >= minimo:
                    if precioentradapuntoLT >= apertura or precioentradapuntoLT > maximo:  # El precioentradapuntoLT esta por encima del maximo o abrio directamente por debajo, lo que significa que puede haber un split y utilizamos la apertura
                        precionentrada = apertura
                    else:  # elif maximo>=precioentradapuntoLT:# El precioentradapuntoLT esta entre el maximo y el minimo y la paertura no la hizo por debajo
                        precionentrada = precioentradapuntoLT
                    # ultimo soporte consolidado
                    soporteanterior = analisisalcista[-1][1][0]
                    barraentradapuntoLT = (fecha, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, volumen)
                    analisisalcista.append((barraentradapuntoLT, (soporteanterior, stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming, indicadores))
                    entradapuntoLT = False

        # cambia en la lista analisialcista los valores del precio de salida para cada operacion, cuando se rompe un stoploss, por la barra en la que se produce
        if stoploss >= minimo and len(analisisalcista) > 0:

            if stoploss > maximo or stoploss >= apertura:  # El stoploss esta por encima del maximo o apertura, lo que significa que puede haber un split o abrio por debajo del stoploss
                salidaoperaciones = (fecha, apertura)
            else:  # elif maximo >= stoploss:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)

            i2 = 0
            while i2 < len(analisisalcista):
                resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisalcista[i2]
                if salidaOperacionAnalisis == False:
                    analisisalcista[i2] = resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                    # analisisalcista[i2][5]=datoshistoricos[i]
                i2 += 1
            entradapuntoLT = False

        if resistencia and maximo > maximoresisten and not (minimo < minimoanterior and apertura < cierre):
            # No actualizamos la resistencia, si esta es la misma barra que la crea y ademas la rompe con un movimiento de abajo hacia arriba, considerando como valida la resistencia anterior

            r = i  # le damos a r el indice de los datoshistoricos donde se encuentra la informacion de la resistencia y volvemos a leer los datos
            _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]

        if resistencia and minimo < minimoanterior:  # resistencia consolidada
            resistencia = False
            soporte = True
            # volvemos al indice donde esta la resistencia para comprobar desde ahi los posibles soportes
            # comparamos que el movimiento viene de abajo hacia arriba, para asi considerar el minimo de la resistencia como externo en el movimiento y que en tal caso no pueda ser el soporte
            if aperturaresisten < cierreresisten and (i + 1) < len(datoshistoricos):
                # esto ultimo es porque puede que la ultima barra sea la resistencia, si le sumasemos uno nos saldriamos de rango
                i = r + 1
            else:
                i = r
            s = i
            _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[s]
            _fecha, apertura, maximo, minimo, cierre, _volumen = datoshistoricos[i]

    # Soporte alcista
        if soporte and minimo < minimosoporte and not ((maximo > maximoresisten) and (apertura > cierre)):  # No actualizamos el soporte, si es la misma barra que rompe la resistencia y ademas la apertura es mayor que el cierre
            # el soporte no tiene que ser la propia resistencia si el minimo dejado lo ha hecho abriendo abajo y cerrando arriba
            s = i
            _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[s]

        if soporte and ((maximo > maximoresisten)or i == ((len(datoshistoricos)) - 1)) and not((datoshistoricos[r] or datoshistoricos[s])  in analisisalcista):

            if r > 0:  # No podremos calcular LT si no hay barras fuerra del ciclo resistencia y soporte, por eso la resistencia e inicio del ciclo tiene que ser mayor que 0
                localizaLTi = True
                localizaLTf = False
                LTi = r - 1

                LTf = s
                _fechaLTf, _aperturaLTf, _maximoLTf, minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[LTf]

                while localizaLTi:

                    if LTi >= 0:
                        fechaLTi, _aperturaLTi, _maximoLTi, minimoLTi, _cierreLTi, _volumenLTi = datoshistoricos[LTi]
                    else:
                        localizaLTf = True
                        localizaLTi = False
                        break

    #                    print LTi
                    for j in xrange(LTi, -1, -1):
                        fechaj, _aperturaj, _maximoj, minimoj, _cierrej, _volumenj = datoshistoricos[j]

                        # if (minimoLTi>minimoLTf or minimoLTi==0.0) and LTi>0:# Anadido el 23/01/2011 como estoy en alcista, si el minimodeLTi es mayor que el minimoLTf es porque esta por encima, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por debajo del LTf
                        if minimoLTi > minimoLTf and LTi > 0:  # Anadido el 23/01/2011 como estoy en alcista, si el minimodeLTi es mayor que el minimoLTf es porque esta por encima, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por debajo del LTf
                            LTi -= 1
                            break
                        try:
                            puntoLT = round((minimoLTi * ((1 + (((1.0 + (((minimoLTf - minimoLTi) / minimoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug('Error: %s buscando LTi en analisisAlcistaAccion; Accion: %s; timming: %s; FechaLTi: %s; Fecha de la barra donde se produce el Error: %s; con un valor de minimoLTi: %s' \
                                          % (e, naccion.encode('UTF-8'), timming, fechaLTi, fechaj, minimoLTi))
#                            LineaTendenciaInicio = ('0-0-0', 0.0)
#                            LineaTendenciaFin = ('0-0-0', 0.0)
#                            localizaLTi = False
#                            localizaLTf = False
#                            break
                            puntoLT = minimoj
                            j = 0

                        if puntoLT > minimoj:
                            LTi = j
                            break
                            # .....

                        if j == 0:

                            # ..... las busqueda desde el ciclo resistencia y su ruptura hacia atras, ha terminado
                            # tendriamos en la variable LTi el indice de datoshitoricos de la barra de la linea de tendencia inicial donde apoyaria la LT
                            # quedaria comprobar que LTf es la mas externa
                            localizaLTi = False
                            localizaLTf = True
                            break

                LTf = r
                # LTfrepetido = False
                while localizaLTf:

    #                print "LTf, i =", LTf, i
                    if LTf <= i:
                        fechaLTf, _aperturaLTf, _maximoLTf, minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[LTf]
                    else:
                        localizaLTf = False
                        localizaLTi = False
                        break
    #                print "LTf, i =", LTf, i
    #                while j<=i:
                    for j in xrange(LTf, i + 1):

                        fechaj, _aperturaj, _maximoj, minimoj, _cierrej, _volumenj = datoshistoricos[j]

                        # esto lo he anadido porque se me ha dado el caso de que cuando en los primeros ciclos alcistas, si estan demasiado proximos al inicio del historico de la accion, me toma como el mismo punto el punto de LTi y LTf
                        if LTf == LTi:
                            LTf += 1
                            break
                        try:
                            puntoLT = round((minimoLTi * ((1 + (((1.0 + (((minimoLTf - minimoLTi) / minimoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug('Error: %s buscando LTf en analisisAlcistaAccion; Accion: %s; timming: %s; FechaLTi: %s; Fecha de la barra donde se produce el Error: %s; con un valor de minimoLTi: %s' \
                                          % (e, naccion.encode('UTF-8'), timming, fechaLTf, fechaj, minimoLTi))
#                            LineaTendenciaInicio = ('0-0-0', 0.0)
#                            LineaTendenciaFin = ('0-0-0', 0.0)
#                            localizaLTi = False
#                            localizaLTf = False
#                            break
                            puntoLT = minimoj
                        # puntoLT = round((minimoLTi*((minimoLTf/minimoLTi)**(365.0/(7.0*(LTf-LTi))))**((7.0/365)*j-(7.0/365.0)*LTi)),3)

                        # Aveces por falta de precision en el calculo del puntoLT creamos un bucle infinito que siempre impacta en la misma barra una y otra vez
                        # Esto sirve para evitar eso no comprobando una y otra vez un LTf que siempre es la misma
                        if puntoLT > minimoj:
                            if (LTf == j or (puntoLT == 0.0 and LTf < i)) and not (j + 1 > i):
                                # Si la linea de tendencia llega a 0 y LTf no ha llegado a ser i, deberia comprobar hasta llegar a ser la i
                                # la primera comprobacion es porque por una falta de precision en el calculo de PuntoLT, aveces da menor que el maximo del que es precisamente el ultimo punto donde toco, es decir, ya tomamos este ultimo punto como LTf pero cuando volvemos a comprobarlo por segunda vez, vuelve a dar que es menor por un fallo de precision
                                localizaLTf = False
                                localizaLTi = False
                            else:
                                LTf = j
# #                            if LTfrepetido or LTfrepetido == LTf:
# #                                LTfrepetido = False
# #                                localizaLTf = False
# #                                localizaLTi = False
# #                                break
# #                            elif LTf == j and LTfrepetido == False:
# #                                LTfrepetido = LTf
# #                            LTf = j
                            break
                            # .....

                        if j >= i:
                            localizaLTf = False
                            localizaLTi = False
                            break

            # quiero anadir aqui una ultima comprobacion de la LT desde 0 hasta i comprobandola entera, en el caso de que el
            # puntoLT sea igual al dato del indice de la tupla datoshistoricos no cambia o no lo damos por malo, pero si
            # si el puntoLT sea mayor al punto, y entonces habria que volver a calcular la LT pero esta vez tomando este nuevo punto
            # como LTi o LTf dependiendo de si esta entre '0' y 'r' o 'r' y 'i'.

                LineaTendenciaInicio = (datoshistoricos[LTi][0], datoshistoricos[LTi][3])
                LineaTendenciaFin = (datoshistoricos[LTf][0], datoshistoricos[LTf][3])

                if not (datoshistoricos[LTi][3] < datoshistoricos[LTf][3]):  # comprobamos que no nos de rentabilidad negativa
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

            if maximoresistencia <= minimoruptura or maximoresistencia <= aperturaruptura:  # Si el Maximo de la resistecia esta por debajo o igual del minimo de la ruptura o apertura de la ruptura, significa que puede haber un split o abrio por encima de la resistenca
                precionentrada = aperturaruptura
            else:  # el maximo de la resistencia se encuetra entre la apertura y el maximo
                precionentrada = maximoresistencia

            analisisalcista.append((datoshistoricos[r], (datoshistoricos[s], stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming, indicadores))
            if conEntradaLT:
                entradapuntoLT = True

            # LT=True # esto es porque hasta que no se produce un segundo soporte, no podemos calcular la linea de tendencia

            # Si la misma barra que rompe la resistencia abre arriba para cerrar por abajo del stoploss, esa barra nos saca del mercado
            if stoploss >= minimo and apertura > cierre and len(analisisalcista) > 0:

#                if maximo >= stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)
#                elif maximo < stoploss:# El stoploss esta por encima del maximo, lo que significa que puede haber un split
#                    salidaoperaciones = ( fecha, maximo )

                i2 = 0
                while i2 < len(analisisalcista):
                    resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisalcista[i2]
                    # salidaOperacionAnalisis=analisisalcista[i2][5]
                    if salidaOperacionAnalisis == False:
                        analisisalcista[i2] = resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                        # analisisalcista[i2][5]=datoshistoricos[i]
                    i2 += 1

            r = i  # como la ultima barra que ha roto la resistencia es mas alta que la resistencia, la considero como nueva resistencia
            _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[r]

            resistencia = True
            soporte = False

        i += 1

    if desdefecha != False and todohistorico == True:
        i = 0
        while i < len(analisisalcista):
            resistencia, soporte, ruptura, LTi, LTf, salida, timming, indicadores = analisisalcista[i]
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = resistencia
            if fecha >= desdefecha:
                analisisalcista = analisisalcista[i:]
                i = 0
                del resistencia, soporte, ruptura, LTi, LTf, salida, fecha, _apertura, _maximo, _minimo, _cierre, _volumen
                break
            if i == (len(analisisalcista) - 1) and fecha < desdefecha:  # Ha llegado al final de analisisbajista sin encontrar una fecha de analisis mayor a desdefecha
                analisisalcista = []
            i += 1

    # ##mostramos en pantalla y creamos otro archivo no codificado con la tupla
    if len(analisisalcista) > 0 and txt:
        tickets = BBDD.ticketlistacodigo(naccion)
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), __carpetas__["Analisis"], nombre + "." + timming + ".analisisalcista.txt")
        j = open(archivo, "w")
        j.write(str(config) + '\n')
        for n in analisisalcista:
            # ~ j.write(str(n)+'\n')
            resistencia, soporte, ruptura, LTi, LTf, salida, timming, indicadores = n
            j.write("Resistencia " + str(resistencia) + '\n')
            j.write("Soporte     " + str(soporte) + '\n')
            j.write("Ruptura     " + str(ruptura) + '\n')
            j.write("LT Inicio   " + str(LTi) + '\n')
            j.write("LT Final    " + str(LTf) + '\n')
            j.write("Salida      " + str(salida) + '\n')
            j.write("Timming     " + str(timming) + '\n')
            j.write("Indicadores ADX, DI+, DI- " + str(indicadores) + '\n')
            j.write('\n')

        for n in xrange(5):
            j.write('\n')

        for n in listastoploss:
            j.write(str(n) + '\n')

        j.close()

    # formato de salida, ultimo analisis alcista, soporte anterior, todo el analisis alcista
    # hay que anadir cuando el len de analisisalcista sea mayor que 2, para cada analisis alcista hay un soporte que es el precio de salida en Lt para este.
    if len(analisisalcista) == 1:  # esto esta porque puede que en el analisisalcista en el timming actual no produzca resultado al no existir resistencia alcista en el timming actual
        return (analisisalcista[-1], 0, analisisalcista)
    elif len(analisisalcista) > 1:
        return (analisisalcista[-1], (analisisalcista[-2][1][1]), analisisalcista)  # [-2][1][1]=penultimo analisis, Soporte, stoploss
    else:
        # habria que comprobar un timming inferirior al obtener como resultado 0
        return None


def analisisBajistaAccion(naccion, **config):
    """ Analisis bajista

     timming=d/w/m, timming a analizar
    desdefecha=False/AAAA-MM-DD, fecha desde la que queremos recuperar analisis, fecha incluida, devuelbe todos los analisis cuya resistencia sea desde esta fecha
    txt=True/False, configuracion para hacer que genere archivos txt del analisis
    conEntradaLT = True/False, si queremos que nos incluya los analisis de LT, posibles entradas en LT
    MME = False/entero, Si queremos que se trace una Media Movil Exponencial, no utilizando el concepto de Maximo historico como tal
    filtro = 0.00, flotante filtro aplicado al soporte como precio de salida
    ADX=False/entero

    Resultado es: Resistencia,Soporte,Ruptura Resistencia,Punto LineaTendenciaInicio,Punto LineaTendenciaFin,timming del analisis,indicadores
                    el formato obtenido es:
                                Resistencia , soporte , Salida Lt = fecha,apertura, maximo, minimo, cierre, volumen
                                punto LT = fecha inicio, precio inicio
                                salida Lt = Soporte anterior
                                indicadores=(ADX, DI+, DI-)

    """
    naccion = naccion.upper()

    historico = BBDD.datoshistoricoslee(naccion)

    conEntradaLT = config.get('conEntradaLT', True)
    MME = config.get('MME', False)
    if MME == False:
        MME2 = False
    else:
        MME2 = config.get('MME2', False)
    TAR = config.get('TAR', False)
    ADX = config.get('ADX', False)
    filtro = config.get('filtro', 0.0)
    timming = config.get('timming', "m")
    desdefecha = config.get('desdefecha', False)
    txt = config.get('txt', True)

    if desdefecha == '' or desdefecha == ' ' or desdefecha == None:
        desdefecha = False
    elif desdefecha != False:
        todohistorico, desdefecha = desdefecha

    if timming == 'd':
        datoshistoricos = historico
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.01
            else:
                filtro = 3.5
    elif timming == 'w':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='w')
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.02
            else:
                filtro = 2.5
    elif timming == 'm':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='m')
        if filtro == 0.0:
            if TAR == False:
                filtro = 0.03
            else:
                filtro = 1.5

    analisisbajista = []
    listastoploss = []

    i, r, s, LTi, LTf = 0, 0, 0, 0, 0
    resistencia = False
    soporte = True
    stoploss = 0.0
    salidaOperacion = False
    entradapuntoLT = False

#    datoshistoricos = []
#    volumenMME = indicador.MME(datoshistoricos2, MME=5, indicedatos='volumen')
#    while i < len(datoshistoricos2):
#        assert (datoshistoricos2[i][0] == volumenMME[i][0])
#        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos2[i]
#        datoshistoricos.append((fecha, apertura, maximo, minimo, cierre, volumenMME[i][1]))
#        i += 1
#    del datoshistoricos2

    if desdefecha != False and todohistorico == False:
        i = 0
        while i < len(datoshistoricos):
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = datoshistoricos[i]
            if fecha >= desdefecha:
                datoshistoricos = datoshistoricos[i:]
                del fecha, _apertura, _maximo, _minimo, _cierre, _volumen
                break
            if i == (len(datoshistoricos) - 1) and fecha < desdefecha:  # Ha llegado al final de sin encontrar una fecha de analisis mayor a desdefecha
                datoshistoricos = []
            i += 1

    i = 0

    if not(MME == False):
        puntosMME = indicador.MME(datoshistoricos, MME=MME)
        if not(MME2 == False):
            puntosMME2 = indicador.MME(datoshistoricos, MME=MME2)
    if not (TAR == False):
        puntosTAR = indicador.TAR(datoshistoricos, TAR=TAR)

    if not (ADX == False):
        puntosADX = indicador.ADX(datoshistoricos, ADX=ADX)
        puntosDI = indicador.DI(datoshistoricos, DI=ADX)

    while i < len(datoshistoricos):
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos[i]

        if i == 0:
            ant = 0
        else:
            ant = i - 1
        fechaanterior, _aperturaanterior, maximoanterior, _minimoanterior, cierreanterior, _volumenanterior = datoshistoricos[ant]
        _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[r]
        _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]

        if not (ADX == False):
            fechaADX, puntoADX = puntosADX[ant]
            fechaDI, puntoDIplus, puntoDIminus = puntosDI[ant]
            assert (fechaADX == fechaanterior or fechaDI == fechaanterior)
        else:
            puntoADX = False
            puntoDIplus = False
            puntoDIminus = False
        indicadores = (puntoADX, puntoDIplus, puntoDIminus)

        if not (TAR == False):
            fechaTAR, puntoTAR = puntosTAR[ant]

            assert (fechaTAR == fechaanterior)

            if len(analisisbajista) > 0 and stoploss > (round((cierreanterior + (puntoTAR * filtro)), 3)):
                stoploss = round((cierreanterior + (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

        if not (MME == False):  # and len( datoshistoricos ) >= MME:

            fechaMME, puntoMME = puntosMME[i]
            if not (MME2 == False):
                fechaMME2, puntoMME2 = puntosMME2[i]
                assert (fechaMME == fecha and fechaMME == fechaMME2)

            assert (fechaMME == fecha)

            # if i >= ( MME - 1 ):# Empieza a utilizar el indicador.MME en una barra en concreto, para la MME30 lo utiliza apartir de la barra 30(cuyo indice es 29)
            if puntoMME > 0:
                if resistencia == False and soporte == False and puntoMME > maximo:  # Si no buscamos ni resistencias ni soportes y la grafica esta completamente por abajo de la MME, es porque estamos buscando soportes
                    s = i
                    _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]
                    soporte = True
                    resistencia = False
                # if puntoMME < minimo:# Media Movil Exponencial bajo grafica, no buscamos soportes ni resistencias, y consideramos la barra actual como soporte
                elif puntoMME < minimo and (MME2 == False or (MME2 != False and puntoMME2 <= puntoMME)):
                # elif puntoMME2 <= puntoMME < minimo:
                    s = i
                    _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]
                    soporte = False
                    resistencia = False

        # anade en analisisbajista, los puntos de entrada por Linea de tendencia
        if len(analisisbajista) > 0 and entradapuntoLT:
            LineaTendenciaInicio = analisisbajista[-1][3]
            LineaTendenciaFin = analisisbajista[-1][4]

            _fechaLTi, maximoLTi = LineaTendenciaInicio
            _fechaLTf, maximoLTf = LineaTendenciaFin

            if maximoLTi > 0 and maximoLTf > 0:
                # try:
                precioentradapuntoLT = round((maximoLTi * ((1 + (((1.0 + (((maximoLTf - maximoLTi) / maximoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((i - LTi) / 12.0))), 3)

                # except OverflowError:
                #    log(nombrelog='analisisBajistaAccionEntradaLT',error=OverflowError,explicacion='Accion; timming; FechaLTi; FechaLTf; Fecha de la barra donde se produce el Error',variables=('Funcion analisisBajistaAccion Buscando analisis de entrada en LT',naccion,timming,fechaLTi,fechaLTf,fecha))
                # else:
                if maximo >= precioentradapuntoLT:
                    if minimo > precioentradapuntoLT or apertura >= precioentradapuntoLT:  # # El precioentradapuntoLT esta por debajo del minimo, lo que significa que puede haber un split y utilizamos la apertura
                        precionentrada = apertura
                    else:  # elif precioentradapuntoLT >= minimo:# El precioentradapuntoLT esta entre el maximo y el minimo
                        precionentrada = precioentradapuntoLT
                    # ultima resistencia consolidado
                    resistenciaanterior = analisisbajista[-1][1][0]
                    barraentradapuntoLT = (fecha, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, precioentradapuntoLT, volumen)
                    analisisbajista.append((barraentradapuntoLT, (resistenciaanterior, stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming, indicadores))
                    entradapuntoLT = False

        # TODO: hay un stoploss que se calcula en funcion al precio de entrada, precio objetivo, recogemos beneficios cuando el precio toque una venta limite.
        # cambia en la lista analisialcista los valores del precio de salida para cada operacion, cuando se rompe un stoploss, por la barra en la que se produce
        if maximo >= stoploss and len(analisisbajista) > 0:

            if minimo > stoploss or apertura >= stoploss:  # El stoploss esta por debajo del minimo o apertura, lo que significa que puede haber un split y/o abrio por encima del stoploss, utilizamos la apertura
                salidaoperaciones = (fecha, apertura)
            else:  # elif stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)

            i2 = 0
            while i2 < len(analisisbajista):
                soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisbajista[i2]
                # salidaOperacionAnalisis=analisisalcista[i2][5]
                if salidaOperacionAnalisis == False:
                    analisisbajista[i2] = soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                    # analisisalcista[i2][5]=datoshistoricos[i]
                i2 += 1
            entradapuntoLT = False

        if soporte and minimo < minimosoporte and not (maximo > maximoanterior and apertura > cierre):  # No actualizamos el soporte, si esta es la misma barra que la crea y ademas la rompe con un movimiento de arriba hacia abajo, considerando como valida la resistencia anterior

            s = i
            _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]

        if soporte and maximo > maximoanterior:  # soporte consolidada
            resistencia = True
            soporte = False
            # volvemos al indice donde esta el soporte para comprobar desde ahi las posibles resistencias
            # comparamos que el movimiento viene de abajo hacia arriba, para asi considerar el maximo del soporte como interno en el movimiento y que en tal caso pueda ser la resistencia
            if aperturasoporte > cierresoporte and (i + 1) < len(datoshistoricos):
                # esto ultimo es porque puede que la ultima barra sea la resistencia, si le sumasemos uno nos saldriamos de rango
                i = s + 1
            else:
                i = s
            r = i
            _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[r]
            _fecha, apertura, maximo, minimo, cierre, _volumen = datoshistoricos[i]

    # resistencia bajista
        if resistencia and maximo > maximoresisten and not ((minimo < minimosoporte) and (apertura < cierre)):  # No actualizamos la resistencia, si es la misma barra que rompe el soporte y ademas la apertura es menor que el cierre
#        if soporte and minimo<minimosoporte:
            r = i
            _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[r]

        if resistencia and ((minimo < minimosoporte)or i == ((len(datoshistoricos)) - 1)) and not((datoshistoricos[s] or datoshistoricos[r])  in analisisbajista):

#            if LT: # esto es porque hasta que no se produce un segundo soporte, no podemos calcular la linea de tendencia
            if s > 0:  # No podremos calcular LT si no hay barras fuerra del ciclo soporte y resistencia, por eso el soporte e inicio del ciclo tiene que ser mayor que 0
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
                    for j in xrange(LTi, -1, -1):
                        fechaj, _aperturaj, maximoj, _minimoj, _cierrej, _volumenj = datoshistoricos[j]

                        if (maximoLTi < maximoLTf or maximoLTi == 0.0) and LTi > 0:  # como estoy en bajista, si el maximoLTi es menor que el maximoLTf es porque esta por debajo, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por encima del LTf
                            LTi -= 1
                            break
                        try:
                            puntoLT = round((maximoLTi * ((1 + (((1.0 + (((maximoLTf - maximoLTi) / maximoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug('Error: %s buscando LTi en analisisBajistaAccion; Accion: %s; timming: %s; FechaLTi: %s; Fecha de la barra donde se produce el Error: %s; con un valor de maximoLTi: %s' \
                                          % (e, naccion.encode('UTF-8'), timming, fechaLTi, fechaj, maximoLTi))
#                            LineaTendenciaInicio = ('0-0-0', 0.0)
#                            LineaTendenciaFin = ('0-0-0', 0.0)
#                            localizaLTi = False
#                            localizaLTf = False
#                            break
                            puntoLT = maximoj
                            j = 0

                        if puntoLT < maximoj:
                            LTi = j
                            break
                            # .....

                        if j == 0:

                            # ..... las busqueda desde el ciclo resistencia y su ruptura hacia atras, ha terminado
                            # tendriamos en la variable LTi el indice de datoshitoricos de la barra de la linea de tendencia inicial donde apoyaria la LT
                            # quedaria comprobar que LTf es la mas externa
                            localizaLTi = False
                            localizaLTf = True
                            break

                LTf = s
                # LTf=r-1# Anadido el 23/01/2011
                # j=r
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
                    for j in xrange(LTf, i + 1):

                        _fechaj, _aperturaj, maximoj, _minimoj, _cierrej, _volumenj = datoshistoricos[j]

                        # esto lo he anadido porque se me ha dado el caso de que cuando en los primeros ciclos alcistas, si estan demasiado proximos al inicio del historico de la accion, me toma como el mismo punto el punto de LTi y LTf
                        if LTf == LTi:
                            LTf += 1
                            break
                        try:
                            # puntoLT = round((minimoLTi*((minimoLTf/minimoLTi)**(365.0/(7.0*(LTf-LTi))))**((7.0/365)*j-(7.0/365.0)*LTi)),3)
                            puntoLT = round((maximoLTi * ((1 + (((1.0 + (((maximoLTf - maximoLTi) / maximoLTi))) ** (12.0 / (LTf - LTi))) - 1.0)) ** ((j - LTi) / 12.0))), 3)
                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug('Error: %s buscando LTf en analisisBajistaAccion; Accion: %s; timming: %s; FechaLTi: %s; Fecha de la barra donde se produce el Error: %s; con un valor de maximoLTi: %s' \
                                          % (e, naccion.encode('UTF-8'), timming, fechaLTf, fechaj, maximoLTi))
#                            LineaTendenciaInicio = ('0-0-0', 0.0)
#                            LineaTendenciaFin = ('0-0-0', 0.0)
#                            localizaLTi = False
#                            localizaLTf = False
#                            break
                            puntoLT = maximoj  # asi no altero el LTf

                        if puntoLT < maximoj:
                            if (LTf == j or (puntoLT == 0.0 and LTf < i)) and not (j + 1 > i):
                                # Si la linea de tendencia llega a 0 y LTf no ha llegado a ser i, deberia comprobar hasta llegar a ser la i
                                # la primera comprobacion es porque por una falta de precision en el calculo de PuntoLT, aveces da menor que el maximo del que es precisamente el ultimo punto donde toco, es decir, ya tomamos este ultimo punto como LTf pero cuando volvemos a comprobarlo por segunda vez, vuelve a dar que es menor por un fallo de precision
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

            # if not LT:
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

            if minimosoporte >= maximoruptura or minimosoporte >= aperturaruptura:  # Si el minimo del soporte esta por encima o igual del maximo de la ruptura o apertura de la ruptura, significa que puede haber un split o abrio por debajo del soporte
                precionentrada = aperturaruptura
            else:  # el maximo de la resistencia se encuetra entre la apertura y el maximo
                precionentrada = minimosoporte

            analisisbajista.append((datoshistoricos[s], (datoshistoricos[r], stoploss), (datoshistoricos[i], precionentrada), LineaTendenciaInicio, LineaTendenciaFin, salidaOperacion, timming, indicadores))

            if conEntradaLT:
                entradapuntoLT = True

            # Si la misma barra que rompe el soporte abre abajo para cerrar por arriba del stoploss, esa barra nos saca del mercado
            if maximo >= stoploss and cierre > apertura and len(analisisbajista) > 0:

                # if maximo >= stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)
                # elif minimo > stoploss:# El stoploss esta por debajo del minimo, lo que significa que puede haber un split
                #    salidaoperaciones = ( fecha, minimo )

                i2 = 0
                while i2 < len(analisisbajista):
                    soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisbajista[i2]
                    # salidaOperacionAnalisis=analisisalcista[i2][5]
                    if salidaOperacionAnalisis == False:
                        analisisbajista[i2] = soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                        # analisisalcista[i2][5]=datoshistoricos[i]
                    i2 += 1
            s = i  # como la ultima barra que ha roto la resistencia es mas alta que la resistencia, la considero como nueva resistencia
            _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[s]
#            if i<> len (datoshistoricos)-1:# esto esta porque si hemos llegado al final del analisis de los datos historicos, hacemos el analisis como si hubiese roto la resistencia, y ya no nos interesa volver atras una barra, ya que esto no meteria en un bucle infinito
#            if i<len (datoshistoricos)-1 and (minimo < minimoanterior and apertura>cierre):# esto esta porque si hemos llegado al final del analisis de los datos historicos, hacemos el analisis como si hubiese roto la resistencia, y ya no nos interesa volver atras una barra, ya que esto no meteria en un bucle infinito
#            if i<len (datoshistoricos)-1 and apertura>cierre:
#                i-=1 # vuelvo un dato atras porque es posible que la misma barra que rompe la resistencia lo sea en el siguiente ciclo, y asi comparo si el maximo de esa barra es el mayor dejado hasta el momento
            # print resitenciaalcista

            resistencia = False
            soporte = True

        i += 1

    if desdefecha != False and todohistorico == True:
        i = 0
        while i < len(analisisbajista):
            soporte, resistencia, ruptura, LTi, LTf, salida, timming, indicadores = analisisbajista[i]
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = soporte
            if fecha >= desdefecha:
                analisisbajista = analisisbajista[i:]
                del resistencia, soporte, ruptura, LTi, LTf, salida, fecha, _apertura, _maximo, _minimo, _cierre, _volumen
                break
            if i == (len(analisisbajista) - 1) and fecha < desdefecha:  # Ha llegado al final de analisisbajista sin encontrar una fecha de analisis mayor a desdefecha
                analisisbajista = []
            i += 1
    # grabaDatos(naccion,datoshistoricos,correcciones,cotizaciones,analisis,analisisbajista,analisisbajista)

# #    codificado = pickle.dumps(analisisbajista)
# #
# #    f = open(archivo+".analisisbajista.pck", "w")
# #    f.write(codificado)
# #    f.close()
    # ##mostramos en pantalla y creamos otro archivo no codificado con la tupla
    if len(analisisbajista) > 0 and txt:
        tickets = BBDD.ticketlistacodigo(naccion)
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), __carpetas__["Analisis"], nombre + "." + timming + ".analisisbajista.txt")
        j = open(archivo, "w")
        j.write(str(config) + '\n')
        for n in analisisbajista:
            # ~ j.write(str(n)+'\n')
            soporte, resistencia, ruptura, LTi, LTf, salida, timming, indicadores = n
            j.write("Soporte     " + str(soporte) + '\n')
            j.write("Resistencia " + str(resistencia) + '\n')
            j.write("Ruptura     " + str(ruptura) + '\n')
            j.write("LT Inicio   " + str(LTi) + '\n')
            j.write("LT Final    " + str(LTf) + '\n')
            j.write("Salida      " + str(salida) + '\n')
            j.write("Timming     " + str(timming) + '\n')
            j.write("Indicadores ADX, DI+, DI- " + str(indicadores) + '\n')
            j.write('\n')

        for n in xrange(5):
            j.write('\n')

        for n in listastoploss:
            j.write(str(n) + '\n')

        j.close()

    # formato de salida, ultimo analisis alcista, soporte anterior, todo el analisis alcista
    # hay que anadir cuando el len de analisisbajista sea mayor que 2, para cada analisis alcista hay un soporte que es el precio de salida en Lt para este.
    if len(analisisbajista) == 1:  # esto esta porque puede que en el analisisbajista en el timming actual no produzca resultado al no existir resistencia alcista en el timming actual
        return ((analisisbajista[-1]), 0, analisisbajista)
    elif len(analisisbajista) > 1:
        return ((analisisbajista[-1]), (analisisbajista[-2][1][1]), analisisbajista)  # [-2][1][1]=penultimo analisis, resistencia, stoploss
    else:
        # habria que comprobar un timming inferirior al obtener como resultado 0
        return None


def creaMenu(sep, lmenu, cola=True):
    """Le damos el separador de la opcion y una lista con las opciones del menu,
    nos devuelve una lista de tuplas con la cola de opciones y descripciones elegidas,
    anade al final de la lista una tupla mas que contiene (None,None)

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

    if cola == False:
        respdescp = respdescp[0]

    return (respdescp)


def historicoTicket(nombreticket, **config):
    """
    """
    borranoactualizados = config.get('borranoactualizados', False)
    if not BBDD.datoshistoricosexisten(nombreticket):
        print('Ticket %s nuevo, descarga completa del historico de la accion' % nombreticket)
#        for timmingdescargado in 'dwm':
        accioninvalida = yahoofinance.descargaHistoricoAccion(nombreticket, timming='d', txt=False)
        duerme()
        if accioninvalida == 'URL invalida':
            BBDD.ticketborra(nombreticket)

    else:
        print('Ticket %s ya descargado, comprobando la actualizacion de los datos' % nombreticket)
        # for timmingdescargado in 'dwm':

        fechaactualizar, actualizaractualizar = BBDD.datoshistoricosactualizacion(nombreticket)

        if actualizaractualizar:  # and (desdefechamodificacionarchivo(datosaccion)):

            accioninvalida = yahoofinance.descargaHistoricoAccion(nombreticket, fechaini=fechaactualizar, timming='d', actualizar=actualizaractualizar, txt=False)
            duerme()

            if accioninvalida == 'Pago Dividendos':
                BBDD.ticketborra(nombreticket, BBDD=False)
                print('Reintento de la descarga, el error puede venir de un pago de Dividendos')
                accioninvalida = yahoofinance.descargaHistoricoAccion(nombreticket, timming='d', txt=False)
                duerme()
                # despues de haber actualizado, volvemos a comprobarlo, si se da que si, la accion dejo de cotizar hace mucho.
                # existe un caso especifico que es cuando comprobamos la actualizacion de datos de una accion y esta tiene menos de 3 periodos en el timming en que estemos trabajando, la funcion actualizacionDatosHisAccion la trata de forma especial, devolviendo (None, timming, True), para que con estos parametros la funcion descargaHistoricosAccion descarge todo el historico otra vez
                # por esta razon en el siguiente if comprobamos con fechaactualizar2!=None que no sea este caso.
                # FIXME : al hacer la comprobacion en mensual, casi siempre me da que no ha actualizado correctamente, ejemplo EGL.SW
                fechaactualizar2, actualizaractualizar2 = BBDD.datoshistoricosactualizacion(nombreticket)
                if fechaactualizar2 != None and actualizaractualizar == actualizaractualizar2 and fechaactualizar == fechaactualizar2:
                    fechahoy = ((date.today().timetuple()))
                    fechaactualizar2 = map(int, ((fechaactualizar2).split('-')))
                    desdeultimaactualizacion = (date(fechahoy[0], fechahoy[1], fechahoy[2]) - date(fechaactualizar2[0], fechaactualizar2[1], fechaactualizar2[2])).days

                    if borranoactualizados and desdeultimaactualizacion > __difregactualizar__['noActualizados']:
                        accioninvalida = 'URL invalida'
                        BBDD.ticketborra(nombreticket)
                    else:
                        print ('No se ha actualizado correctamente. Funcion de borrado para estos casos deshabilitada')
                        BBDD.ticketerror(nombreticket)

            elif  accioninvalida == 'URL invalida':
                BBDD.ticketborra(nombreticket)


def analisisTicket(nombreticket):
    """
    """

    nombreticket = (nombreticket.upper(),)
    cursor.execute("SELECT * FROM `Cobo_componentes` WHERE `Cobo_componentes`.`tiket` = ?", nombreticket)
    registro = cursor.fetchall()
    # resultado=(28141L, 'LVL MEDICAL GROUP', '-LVL.NX', 'ENX', 18.4, 14.89, 12.46, 14.56, 14.89, 12396.0, 7371.0, 'N/A', datetime.date(2011, 2, 24)
    codigo, _nombre, ticket, _mercado, max52, maxDia, min52, minDia, valorActual, _volumenMedio, _volumen, _error, _fechaRegistro = registro[0]
    proximidadalcista, proximidadbajista = 0, 0
    if BBDD.datoshistoricosexisten(ticket):

        # al final si utilizamos indicador.MME, el indicador.MME sera la decision de si es alcista o bajista
        for timminganalisis in 'mwd':
            print('Timming del analisis alcista: %s' % timminganalisis)
            analisisalcista = analisisAlcistaAccion(ticket, timming=timminganalisis, conEntradaLT=False, txt=False)
            if analisisalcista != None:
                alcista, soporteanterioralcista, _analisisalcistatotal = analisisalcista
                resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
                soporte, stoploss = soporte
                ruptura, entrada = ruptura
                # evitando que la division de mas abajo sea por 0
                if ruptura[4] == 0.0:
                    cierreruptura = 0.0001
                else:
                    cierreruptura = ruptura[4]
                if maxDia == None or maxDia == 0.0:
                    maxDia = cierreruptura
                if valorActual == None or valorActual == 0.0:
                    valorActual = cierreruptura
                # except ZeroDivisionError:
                proximidadalcista = (abs((resistencia[2] / max(cierreruptura, maxDia, valorActual)) - 1))
#                            for precio in (ruptura[4], maxDia, valorActual):
#                                proximidadalcista.append(abs((resistencia[2] / precio) - 1))
#                            proximidadalcista = min(proximidadalcista)
                break

        for timminganalisis in 'mwd':
            print('Timming del analisis bajista: %s' % timminganalisis)
            analisisbajista = analisisBajistaAccion(ticket, timming=timminganalisis, conEntradaLT=False, txt=False)
            if analisisbajista != None:
                bajista, soporteanteriorbajista, _analisisbajistatotal = analisisbajista
                soporte, resistencia, ruptura, LTi, LTf, _salida, timming, _indices = bajista
                resistencia, stoploss = resistencia
                ruptura, entrada = ruptura
                # evitando que la division de mas abajo sea por 0
                if ruptura[4] == 0.0:
                    cierreruptura = 0.0001
                else:
                    cierreruptura = ruptura[4]
                if minDia == None or minDia == 0.0:
                    minDia = cierreruptura
                if valorActual == None or valorActual == 0.0:
                    valorActual = cierreruptura
                # except ZeroDivisionError:
                proximidadbajista = (abs(1 - (soporte[3] / min(cierreruptura, minDia, valorActual))))
#                            for precio in (ruptura[4], minDia, valorActual):
#                                proximidadbajista.append(abs(1 - (soporte[3] / precio)))
#                            proximidadbajista = min(proximidadbajista)
                break

        # TODO: falla logica, puede ser que en mensual el analisis sea bajista, pero en semanal alcista. Hay que dar preferencia al alcista semanal, la resistencia o fecha de entrada seria posterior al soporte o entrada en bajista mensual

        # Existen ambos analisis, comparamos proximidada a ruptura
        # la minima proximidadbajista es mayor o igual a la proximidadalcista, alcista
        if analisisalcista != None and analisisbajista != None and proximidadbajista >= proximidadalcista:
            resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
            soporte, stoploss = soporte
            ruptura, entrada = ruptura
            soporteanterior = soporteanterioralcista
        # la minima proximidadbajista es menor a la proximidadalcista, bajista
        elif analisisalcista != None and analisisbajista != None and proximidadbajista < proximidadalcista:
            soporte, resistencia, ruptura, LTi, LTf, _salida, timming, _indices = bajista
            resistencia, stoploss = resistencia
            ruptura, entrada = ruptura
            soporteanterior = soporteanteriorbajista
        # Uno de los analisis no existe, asignamos el contrario
        elif analisisalcista == None and analisisbajista != None:
            soporte, resistencia, ruptura, LTi, LTf, _salida, timming, _indices = bajista
            resistencia, stoploss = resistencia
            ruptura, entrada = ruptura
            soporteanterior = soporteanteriorbajista
        elif analisisbajista == None and analisisalcista != None:
            resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
            soporte, stoploss = soporte
            ruptura, entrada = ruptura
            soporteanterior = soporteanterioralcista
        elif analisisbajista == None and analisisalcista == None:  # No existe analisis posible
            BBDD.ticketerror(ticket)
            return

        else:  # Por defecto lo consideramos alcista, aunque aqui deberia entrar solo en el caso se que no se de la 3 condicion del if anterior
            resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
            soporte, stoploss = soporte
            ruptura, entrada = ruptura
            soporteanterior = soporteanterioralcista

        sql = "SELECT * FROM `Cobo_params_operaciones` WHERE `Cobo_params_operaciones`.`codigo` = %s" % codigo
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
            # evitando que la division de mas abajo sea por 0
            if precioinicial == 0.0:
                precioinicial = 0.001
#                        if entrada > stoploss:#Alcista
            rentabilidad = ((((1 + ((preciofinal - precioinicial) / precioinicial)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0
#                        elif entrada < stoploss:#Bajista
                # TODO: la rentabilidad en bajista tiene que ser negativa, pero el equivalente en positiva
#                            rentabilidad = ((((1 + ((precioinicial - preciofinal) / preciofinal)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0

        # no nos interesan los datos almacenados de analisis anteriores
        # comprobamos que el analisis obtenido y que vamos a almacenar en la BBDD es o
        # alcista o bajista
        # comprobamos se es actual o esta obsoleto

        if ((entrada > stoploss) and\
            # Alcista obsoleto, maximo52, maximo del dia, valoractual, precio de entrada (split) > Resitencia
            ((max52 != 'NULL' and max52 > resistencia[2]) or\
             (maxDia != 'NULL' and maxDia > resistencia[2]) or\
             (valorActual != 'NULL' and valorActual > resistencia[2]) or\
             (entrada > resistencia[2])))\
             or\
             ((entrada < stoploss) and\
              # Bajista obsoleto, minimo52, minimo del dia, valoractual, precio de entrada (split) < soporte
              ((min52 != 'NULL' and min52 < soporte[3]) or\
               (minDia != 'NULL' and minDia < soporte[3]) or\
               (valorActual != 'NULL' and valorActual < soporte[3]) or\
               (entrada < soporte[3]))):

            # si true, analisis ya cumplido, obsoleto y lo actualizamos
            if numeroResultado == 1:
                sql = "UPDATE `Cobo_params_operaciones` SET `precio_ini` = %.3f, `precio_fin` = %.3f, `fecha_ini` = '%s', `fecha_fin` = '%s', `salida` = NULL, `entrada` = NULL, `timing` = '%s', `precio_salida` = %.3f, `rentabilidad` = %.3f WHERE `Cobo_params_operaciones`.`codigo` = %s" % (LTi[1], LTf[1], LTi[0], LTf[0], timming, soporteanterior, rentabilidad, codigo)
            elif numeroResultado == 0:
                sql = "INSERT INTO `Cobo_params_operaciones` (id,precio_ini,precio_fin,fecha_ini,fecha_fin,salida,entrada,codigo,timing,precio_salida,rentabilidad) VALUES (NULL, %.3f, %.3f,'%s' ,'%s' , NULL, NULL, %d,'%s', %.3f, %.3f)" % (LTi[1], LTf[1], LTi[0], LTf[0], codigo, timming, soporteanterior, rentabilidad)

        # Alcista/Bajista Validos
        else:  # anali
            # si false, analisis valido, sin cumplir
            if numeroResultado == 1:
                sql = "UPDATE `Cobo_params_operaciones` SET `precio_ini` = %.3f, `precio_fin` = %.3f, `fecha_ini` = '%s', `fecha_fin` = '%s', `salida` = %.3f, `entrada` = %.3f, `timing` = '%s', `precio_salida` = %.3f, `rentabilidad` = %.3f WHERE `Cobo_params_operaciones`.`codigo` = %s" % (LTi[1], LTf[1], LTi[0], LTf[0], stoploss, entrada, timming, soporteanterior, rentabilidad, codigo)
            elif numeroResultado == 0:
                sql = "INSERT INTO `Cobo_params_operaciones` (id,precio_ini,precio_fin,fecha_ini,fecha_fin,salida,entrada,codigo,timing,precio_salida,rentabilidad) VALUES (NULL, %.3f, %.3f,'%s','%s',%.3f , %.3f, %d,'%s', %.3f, %.3f)" % (LTi[1], LTf[1], LTi[0], LTf[0], stoploss, entrada, codigo, timming, soporteanterior, rentabilidad)

        cursor.execute(sql)

    db.commit()


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


def ticketsexcluidos(sufijosexcluidos):
    """
    Elimina los Tickets de los mercados que no nos interesan
    """
    for n in sufijosexcluidos:
        sql = "SELECT `nombre` FROM `Cobo_nombreticket` WHERE `nombre` LIKE '%" + n + "'"
        cursor.execute(sql)
        listatickets = cursor.fetchall()
        numeroResultado = len(listatickets)
        if numeroResultado > 0:
            listatickets = ((ticket[0]) for ticket in listatickets)
            listatickets = deque(list(listatickets))
            # for ticket in listatickets:
            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                print ('Quedan por borrar %d tickets' % len(listatickets))
                BBDD.ticketborra(ticket)


def main():

    for carpeta in __carpetas__.keys():
        nombrecarpeta = os.path.join(os.getcwd(), __carpetas__[carpeta])
        if not os.path.exists(nombrecarpeta):
            os.mkdir(nombrecarpeta)
            # os.path.dirname

    opcion = None
    while True:

        cursor, db = BBDD.conexion()
        tickets = BBDD.ticketlistacodigo()
        mercados = BBDD.mercadoslista()

        ticketsexcluidos(sufijosexcluidos)
        BBDD.comprobaciones()

        print('')
        if opcion == None:

            print('Total de mercados : %d' % (len(mercados)))
            print('Total de tickets : %d' % (len(tickets.keys())))

            iopciones = 0
            opciones = creaMenu(')', (
            'Acciones para un solo ticket',
            '------------------------------',
            'A) Alta/Actualizar/Descargar/Analizar Datos de 1 Ticket',
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
            'Q) Analizar Datos de todos los Tickets',
            '------------------------------',
            'S) BackTest',
            '',
            'Cambiar sistema de analisis',
            '------------------------------',
            'T) Cooper',
            '',
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

# 'A) Alta/Actualizar/Descargar/Analizar Datos de 1 Ticket'
        if opcion == 'a':
            print(seleccion)

            naccion = raw_input('Introduce ticket de la accion : ').upper()
            naccion = (naccion,)
            # Primero lo borramos
            BBDD.ticketborra(naccion[0], BBDD=False)

            cursor.execute("SELECT *  FROM `Cobo_nombreticket` WHERE (`Cobo_nombreticket`.`nombre` = ?)", naccion)
            numeroResultado = len(cursor.fetchall())

            # Lo incorporamos a la base de datos
            if numeroResultado == 0:
                cursor.execute("INSERT INTO `Cobo_nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES (?, '" + str(date.today()) + "', NULL, NULL)", naccion)
                db.commit()
                print(naccion[0] + ' anadido a la base de datos')

            # Actualizamos las cotizaciones
            yahoofinance.cotizacionesTicket(naccion[0])

            # Descargamos/Actualizamos el historico
            historicoTicket(naccion[0])

            # Analizamos la accion
            analisisTicket(naccion[0])

#        'C) Analizar Datos de 1 Ticket',
        elif opcion == 'c':
            print(seleccion)
            while True:
                naccion = raw_input('Introduce ticket de la accion : ').upper()
                if BBDD.datoshistoricosexisten(naccion):
                    break
                else:
                    print('Accion no descargada o no figura entre la lista de acciones')
                    BBDD.ticketerror(naccion)

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

            if BBDD.datoshistoricosexisten(naccion):
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

                    analisisAlcistaAccion(naccion, timming=timminganalisis, desdefecha=analizardesde, MME=MMe, conEntradaLT=EntradaLT, filtro=filtrosalida)  # ,txt=False)
                    analisisBajistaAccion(naccion, timming=timminganalisis, desdefecha=analizardesde, MME=MMe, conEntradaLT=EntradaLT, filtro=filtrosalida)  # ,txt=False)

#        'D) Eliminar 1 Ticket',
        elif opcion == 'd':
            print(seleccion)
            naccion = raw_input('Introduce nombre de la accion : ').upper()
            BBDD.ticketborra(naccion)

#        'E) Generar Archivos Grafico'
        elif opcion == 'e':
            print(seleccion)

            while True:
                ticket = raw_input('Introduce ticket de la accion : ').upper()
                if BBDD.datoshistoricosexisten(ticket):
                    break
            datos = BBDD.datoshistoricoslee(ticket)
            ticketconsulta = (ticket,)
            cursor.execute("SELECT `nombre` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`tiket` LIKE ?", ticketconsulta)
            nombre = cursor.fetchall()
            nombre = (nombre[0][0].strip('"')).replace(',', '')

            print(' 1 - Diario')
            print(' 2 - Semanal')
            print(' 3 - Mensual')
            timming = 'None'
            while timming not in ('123 '):
                timming = raw_input('Introduce Timming de los Datos a Generar (Mensual):')

            if timming == '1':
                datos = datos
            elif timming == '2':
                datos = yahoofinance.subirtimming(datos, timming='w')
            elif timming == '3' or timming == '' or timming == ' ':
                datos = yahoofinance.subirtimming(datos, timming='m')

            archivo = os.path.join(os.getcwd(), __carpetas__['Graficos'], "data.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter=';', lineterminator='\n', doublequote=True)
            for n in datos:
                writercsv.writerow(n)
                # j.write(str(n)+'\n')
            j.close()

            archivo = os.path.join(os.getcwd(), __carpetas__['Graficos'], "metatrader.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter=',', lineterminator='\n', doublequote=True)
            j.write('<TICKER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>\n')
            for n in datos:
                fecha, apertura, maximo, minimo, cierre, volumen = n
                fecha = fecha.replace('-', '')

                writercsv.writerow((ticket, fecha, '000000', apertura, maximo, minimo, cierre, volumen))
                # j.write(str(n)+'\n')
            j.close()

            archivo = os.path.join(os.getcwd(), __carpetas__['Graficos'], 'metastock.csv')
            j = open(archivo, 'w')
            j.write('<TICKER>,<NAME>,<PER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>\n')
            writercsv = csv.writer(j, delimiter=',', lineterminator='\n', doublequote=True)
            for n in datos:

                fecha, apertura, maximo, minimo, cierre, volumen = n
                fecha = fecha.replace('-', '')

                writercsv.writerow((ticket, nombre, timming, fecha, '000000', apertura, maximo, minimo, cierre, volumen, '0'))
            j.close()

            MMEdatos = raw_input('Introduce Catidad de periodos para el indicador.MME (30):')

            if MMEdatos == '30' or MMEdatos == '' or MMEdatos == ' ':
                MMEdatos = 30
            else:
                MMEdatos = int(MMEdatos)

            datosMME = indicador.MME(datos, MME=MMEdatos)

            archivo = os.path.join(os.getcwd(), __carpetas__['Graficos'], "MME.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter=';', lineterminator='\n', doublequote=True)
            for n in datosMME:
                writercsv.writerow(n)
            j.close()

            TARdatos = raw_input('Introduce Catidad de periodos para el indicador.TAR (10):')

            if TARdatos == '10' or TARdatos == '' or TARdatos == ' ':
                TARdatos = 10
            else:
                TARdatos = int(TARdatos)

            datosTAR = indicador.TAR(datos, TAR=TARdatos)

            archivo = os.path.join(os.getcwd(), __carpetas__['Graficos'], "TAR.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j, delimiter=';', lineterminator='\n', doublequote=True)
            for n in datosTAR:
                writercsv.writerow(n)
            j.close()

#        'F) Listar Tickets Mercados',
        elif opcion == 'f':
            print(seleccion)
            for mercado in mercados:
                print (mercado)
            print('Total de mercados %d' % (len(mercados)))

        # G) Anadir Ticket Mercado',
        elif opcion == 'g':
            print(seleccion)
            mercado = raw_input('Introduce ticket del mercado a anadir : ').upper()
            mercado = mercado.replace('@%5E', '^')
            mercado = (mercado,)
            # TODO : añadir un mercado o dehabilitar y hacerlo directamente en la BBDD
#            if not (mercado[0] in mercados):
#                sql = "SELECT `Cobo_configuracion`.`valor` FROM `Cobo_configuracion` WHERE (`Cobo_configuracion`.`codigo` ='MERCADOS_OBTENER_COMPONENTES')"
#                cursor.execute(sql)
#                resultadoM = cursor.fetchall()
#                print(resultadoM)
#                m = None
#                while m in resultadoM:
#                    m = raw_input('Del los conjuntos anteriores, Introduce donde quieres anadir el mercado :').upper()
#                m = (m,)
#                cursor.execute("SELECT `Cobo_configuracion`.`valor` FROM `Cobo_configuracion` WHERE (`Cobo_configuracion`.`codigo`  = ?)", m)
#                mercadosvalidos = cursor.fetchall()
#                numeroResultado = len(mercadosvalidos)
#                if numeroResultado == 1:
#                    mercadosvalidos = list(mercadosvalidos[0])
#                    mercadosvalidos.append(mercado)
#                    mercadosvalidos = str(mercadosvalidos)
#                    mercadosvalidos = mercadosvalidos.strip('[')
#                    mercadosvalidos = mercadosvalidos.strip(']')
#                    mercadosvalidos = mercadosvalidos.replace("'", "")
#                    mercadosvalidos = mercadosvalidos.replace('"', '')
#                    mercadosvalidos = mercadosvalidos.replace(' ', '')
#
#                    cursor.execute("UPDATE `Cobo_configuracion` SET valor = '" + mercadosvalidos + "' WHERE (`Cobo_configuracion`.`codigo` =?)", m)
#                    db.commit()
#                    mercados.append(mercado)
#
#            else:
#                print(('El mercado %s ya esta en la lista de mercados' % mercado))
#            print('Total de mercados %d' % (len(mercados)))

#        'H) Eliminar Ticket Mercado',
        elif opcion == 'h':
            print(seleccion)
            mercado = raw_input('Introduce ticket del mercado a borrar : ').upper()
            mercado = mercado.replace('@%5E', '^')
            # TODO : añadir un mercado o dehabilitar y hacerlo directamente en la BBDD
#            if not (mercado in mercados):
#                print(('El mercado %s no existe en la lista de mercados' % mercado))
#            else:
#                mercados.remove(mercado)
#            print('Total de mercados %d' % (len(mercados)))

#        'I) Actualizar cotizaciones monedas
        elif opcion == 'i':
            print(seleccion)
            sql = "SELECT `url_Inet` FROM `Cobo_monedas`"
            cursor.execute(sql)
            urlmonedas = cursor.fetchall()
            urlmonedas = ((moneda[0]) for moneda in urlmonedas)
            urlmonedas = deque(list(urlmonedas))

            while len(urlmonedas) > 0:
                moneda = urlmonedas.popleft()
                yahoofinance.cotizacionesMoneda(moneda)
                duerme()
                print('Quedan por actualizar un total de : %d' % len(urlmonedas))

#        'L) Listar Tickets',
        elif opcion == 'l':
            listatickets = tickets.keys()
            listatickets.sort()
            ticketsnoBBDD = 0
            for ticket in listatickets:
                print(ticket, tickets[ticket])
                if tickets[ticket] == '' or tickets[ticket] == 0:
                    ticketsnoBBDD = +1
            print(('Total de tickets %d' % (len(tickets))))
            print('Tickets que no estan en la BBDD : %s' % ticketsnoBBDD)

            del listatickets, ticketsnoBBDD

#        'M) Actualizar Tickets componentes de Mercados',
        elif opcion == 'm':
            print(seleccion)
            ticketsanadidos = 0
            mercados = BBDD.mercadoslista()
            for mercado in mercados:
                mercado = mercado.replace('@%5E', '^')
                mercado = mercado.replace('@%5e', '^')
                mercado = mercado.upper()
                ticketscomponentesmercados = yahoofinance.ticketsdeMercado(mercado)
                for ticket in ticketscomponentesmercados:
                    if BBDD.ticketalta(ticket):
                        ticketsanadidos += 1

                if len(ticketscomponentesmercados) == 0:
                    print ('Mercado sin ticket, Deshabilitando el Mercado %s' % mercado)
                    BBDD.mercadosdeshabilita(mercado)
            print('Se han anadido un total de : %d tickets' % ticketsanadidos)
            del ticketscomponentesmercados

#        'N) Actualizar cotizaciones de todos los Tickets',
        elif opcion == 'n':
            print(seleccion)
            listatickets = BBDD.comprobaciones(colaResultado='Cotizacion')
            listatickets = deque(list(listatickets))

            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                yahoofinance.cotizacionesTicket(ticket)

                print('Quedan por actualizar un total de : %d' % len(listatickets))
                duerme()

#        'O) Actualizar/Descargar Datos Cotizaciones Historicos todos los Tickets',
        elif opcion == 'o':
            print(seleccion)
            # TODO : como ahora tenemos una columna en `Cobo_nombreticket` que contiene la fecha del historico descargado
#            sql = "SELECT `tiket` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' ORDER BY `Cobo_componentes`.`tiket` ASC"
            listatickets = BBDD.comprobaciones(colaResultado='Historico')
            listatickets = deque(list(listatickets))

# #            borranoactualizados = raw_input('Despues de una actualizacion del historico de una accion que ya existia, se vuelve a comprobar si se ha actualizado, si no es asi normalmente es porque la accion dejo de cotizar. Quieres borrar estas acciones? (No)')
# #            if borranoactualizados == '':
# #                borranoactualizados = False
# #            else:
            borranoactualizados = True

            # for ticket in listatickets:
            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                # accioninvalida=''
                print ('')
                print('Tickets pendientes de comprobar %d' % len(listatickets))

                # if naccion in tickets:

                historicoTicket(ticket, borranoactualizados=borranoactualizados)

                # cuentaatras -= 1

        elif opcion == 'q':
            # Q) Analizar Datos de todos los Tickets',
            print(seleccion)

            sql = "SELECT `tiket` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' ORDER BY `Cobo_componentes`.`tiket` ASC"
            cursor.execute(sql)
            listatickets = cursor.fetchall()
            listatickets = ((ticket[0]) for ticket in listatickets)
            listatickets = deque(list(listatickets))
            # for ticket in listatickets:
            while len(listatickets) > 0:

                print('')
                print('Quedan por analizar un total de %d' % len(listatickets))
                ticket = listatickets.popleft()
                print('Analizando ticket %s' % ticket)

                analisisTicket(ticket)

#        'S) BackTest
        elif opcion == 's':
            # ticket='AAPL'
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
            if analizardesde != False:
                todohistorico = raw_input('Utilizamos todo el historico para el analisis, (Si): ')
                if todohistorico == '':
                    todohistorico = True
                else:
                    todohistorico = False
                analizardesde = (todohistorico, analizardesde)

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
                    MMe2diario = raw_input('2A Media Movil Exponencial diario para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): ')
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
                    MMe2semanal = raw_input('2A Media Movil Exponencial semanal para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): ')
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
                    MMe2mensual = raw_input('2A Media Movil Exponencial semanal para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): ')
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

            ADXobjetivo = raw_input('Average Directional Movement Index, introduce entero, excluir entradas que no lleguen a (deja en blanco pulsando intro para Sin ADX en todos los timmings): ')
            if ADXobjetivo == '':
                ADXmensual = False
                ADXsemanal = False
                ADXdiario = False
                ADXobjetivo = False
            else:
                ADXobjetivo = float(ADXobjetivo)
                ADXmensual = raw_input('Average Directional Movement Index Mensual (deja en blanco pulsando intro para Sin ADX): ')
                if ADXmensual == '':
                    ADXmensual = False
                else:
                    ADXmensual = int(ADXmensual)
                ADXsemanal = raw_input('Average Directional Movement Index Semanal (deja en blanco pulsando intro para Sin ADX): ')
                if ADXsemanal == '':
                    ADXsemanal = False
                else:
                    ADXsemanal = int(ADXsemanal)
                ADXdiario = raw_input('Average Directional Movement Index Diario (deja en blanco pulsando intro para Sin ADX): ')
                if ADXdiario == '':
                    ADXdiario = False
                else:
                    ADXdiario = int(ADXdiario)

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
            '6) Diario con transicion a Semanal y Mensual'), cola=False)

# En el caso de hacer un solo ticket, comentar desde aqui hasta print 'Analizando ticket %s' % ticket incluido, desdentar desde este comentario hasta el siguiente parecedo
            # obtenemos la lista de las monedas
            sql = "SELECT `codigo` FROM `Cobo_monedas`"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            # lo mostramos en una lista
            # nos pide la moneda a buscar y la convertimos en la variable de la siguiente consulta con la que obtenemos la lista de tickes para hacer el backtest
            for mon in resultado:
                print((mon)[0])
                monedas.append(mon[0])

            while True:
                moneda = raw_input('Lista de monedas. Introduce moneda en la que se hace el backtest : ')
                if moneda == '' or moneda == None:
                    moneda = ((raw_input('Introduce sufijo de tickets del mercado en la que se hace el backtest : ')).upper(),)
                    cursor.execute("SELECT * FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' and `Cobo_componentes`.`tiket` NOT LIKE '^%' and `Cobo_componentes`.`tiket` LIKE ? ORDER BY `Cobo_componentes`.`tiket` ASC", moneda)
                    break
                if moneda in monedas:
                    cursor.execute("SELECT * FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' and `Cobo_componentes`.`tiket` NOT LIKE '^%' and`Cobo_componentes`.`mercado` IN (SELECT `nombreUrl` FROM `Cobo_mercado_moneda` WHERE `abrevMoneda` LIKE ?) ORDER BY `Cobo_componentes`.`tiket` ASC", moneda)
                    break

            # consulta en la tabla componentes que pertenecen a los mercados de una moneda
            # sql = "SELECT * FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' and `Cobo_componentes`.`tiket` NOT LIKE '^%' and`Cobo_componentes`.`mercado` IN (SELECT `nombreUrl` FROM `Cobo_mercado_moneda` WHERE `abrevMoneda` LIKE '" + moneda + "') ORDER BY `Cobo_componentes`.`tiket` ASC"
            resultado = cursor.fetchall()
            cuentaatras = len(resultado)
            for registro in resultado:
                # resultado=(28141L, 'LVL MEDICAL GROUP', '-LVL.NX', 'ENX', 18.4, 14.89, 12.46, 14.56, 14.89, 12396.0, 7371.0, 'N/A', datetime.date(2011, 2, 24)
                _codigo, nombre, ticket, mercado, _max52, _maxDia, _min52, _minDia, valorActual, _volumenMedio, volumen, _error, fechaRegistro = registro
                print('Quedan por analizar un total de %d' % cuentaatras)
                print('Analizando ticket %s' % ticket)

                diario = None
                semanal = None
                mensual = None

                if BBDD.datoshistoricosexisten(ticket):
                    backtestaccion = []
                    if estrategia == 'Alcista':
                        if opcionbacktest == '1' or opcionbacktest == '2' or opcionbacktest == '6':
                            diario = analisisAlcistaAccion(ticket, timming='d', desdefecha=analizardesde, MME=MMediario, MME2=MMe2diario, conEntradaLT=EntradaLT, filtro=filtrosalidadiario, TAR=TARdiario, ADX=ADXdiario, txt=True)
                        if opcionbacktest == '2' or opcionbacktest == '3' or opcionbacktest == '4' or opcionbacktest == '6':
                            semanal = analisisAlcistaAccion(ticket, timming='w', desdefecha=analizardesde, MME=MMesemanal, MME2=MMe2semanal, conEntradaLT=EntradaLT, filtro=filtrosalidasemanal, TAR=TARsemanal, ADX=ADXsemanal, txt=True)
                        if opcionbacktest == '4' or opcionbacktest == '5' or opcionbacktest == '6':
                            mensual = analisisAlcistaAccion(ticket, timming='m', desdefecha=analizardesde, MME=MMemensual, MME2=MMe2mensual, conEntradaLT=EntradaLT, filtro=filtrosalidamensual, TAR=TARmensual, ADX=ADXmensual, txt=True)
                    elif estrategia == 'Bajista':
                        if opcionbacktest == '1' or opcionbacktest == '2' or opcionbacktest == '6':
                            diario = analisisBajistaAccion(ticket, timming='d', desdefecha=analizardesde, MME=MMediario, MME2=MMe2diario, conEntradaLT=EntradaLT, filtro=filtrosalidadiario, TAR=TARdiario, ADX=ADXdiario, txt=True)
                        if opcionbacktest == '2' or opcionbacktest == '3' or opcionbacktest == '4' or opcionbacktest == '6':
                            semanal = analisisBajistaAccion(ticket, timming='w', desdefecha=analizardesde, MME=MMesemanal, MME2=MMe2semanal, conEntradaLT=EntradaLT, filtro=filtrosalidasemanal, TAR=TARsemanal, ADX=ADXsemanal, txt=True)
                        if opcionbacktest == '4' or opcionbacktest == '5' or opcionbacktest == '6':
                            mensual = analisisBajistaAccion(ticket, timming='m', desdefecha=analizardesde, MME=MMemensual, MME2=MMe2mensual, conEntradaLT=EntradaLT, filtro=filtrosalidamensual, TAR=TARmensual, ADX=ADXmensual, txt=True)

                    # fecharesistenciadiario = 0
                    # fecharesistenciasemanal = 0

                    if not diario == None:
                        diario = diario[2]
                        fechasentradasdiario = ([operacion[0][0] for operacion in diario])
                        i2 = len(diario)  # por si alcistamensual==None, tenemos que asignarle todo el historico de semanal a backtestaccion
                    else:
                        i2 = 0
                        diario = []

# puede que no exista o analisis semanal o mensual, en estos casos hay que darle algun valor a esos casos para que backtest sea coherente
                    if not semanal == None:
                        semanal = semanal[2]
                        fechasentradassemanal = ([operacion[0][0] for operacion in semanal])
                        fecha1entradasemanal = semanal[0][0][0]
                        i = len(semanal)  # por si alcistamensual==None, tenemos que asignarle todo el historico de semanal a backtestaccion

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

                    # precionentrada = 0
                    # preciosalida = 0
                    invertido = False
                    p = 0
                    while p < len(backtestaccion):
                    # for operacion in backtestaccion:

                        if estrategia == 'Alcista':
                            resistencia, soporte, ruptura, LTi, LTf, salida, timming, indicadores = backtestaccion[p]
                            soporte, stoploss = soporte
                            ruptura, precionentrada = ruptura
                        elif estrategia == 'Bajista':
                            soporte, resistencia, ruptura, LTi, LTf, salida, timming, indicadores = backtestaccion[p]
                            resistencia, stoploss = resistencia
                            ruptura, precionentrada = ruptura
                        # Calculamos rentabilidad

                        if len(indicadores) == 3:
                            puntoADX, puntoDIplus, puntoDIminus = indicadores
                        else:
                            puntoADX, puntoDIplus, puntoDIminus, _puntoTAR, _puntoMME, _puntoMME2, _puntoHL = indicadores

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
                                if precioinicial == 0.0:
                                    precioinicial = 0.000001
                                rentabilidad = ((((1 + ((preciofinal - precioinicial) / precioinicial)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0
                            elif estrategia == 'Bajista':
                                if preciofinal == 0.0:
                                    preciofinal = 0.000001
                                rentabilidad = ((((1 + ((precioinicial - preciofinal) / preciofinal)) ** (365.0 / diffechas)) - 1.0) * 100.0) / 100.0

                        # calculamos el volumen
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

                        if (resistencia[2] == stoploss) or (soporte[3] == stoploss):  # comprobamos que no dividomos entre 0
                            numeroacciones = 0
                        else:
                            # las siguientes comprobaciones son necesarias, porque nosotros ponemos la orden para la ruptura y calculamos el numero de acciones en relacion a ello
                            # pero eso no quiere decir que se ejecute al precionentrada
                            if estrategia == 'Alcista':
                                numeroacciones = int(riesgo / (resistencia[2] - stoploss))
                            elif estrategia == 'Bajista':
                                numeroacciones = int(riesgo / (soporte[3] - stoploss))

                        # inversion moneda
                        if estrategia == 'Alcista':
                            inversion = numeroacciones * resistencia[2]
                        elif estrategia == 'Bajista':
                            inversion = numeroacciones * soporte[3]

                        if not(inversionmaxima == False) and abs(inversion) > inversionmaxima:
                            if estrategia == 'Alcista':
                                numeroacciones = int(inversionmaxima / resistencia[2])
                                inversion = numeroacciones * resistencia[2]
                            elif estrategia == 'Bajista':
                                # la inversion maxima es en negativo, arriba comparamos el valor absoluto pero en el numero de acciones tiene que ser negativo
                                numeroacciones = (int(inversionmaxima / soporte[3])) * (-1)
                                inversion = numeroacciones * soporte[3]

                        if invertido == False and \
                        rentabilidad >= rentabilidadminima and \
                        volumenoperacion >= volumenminimo and \
                        abs(inversion) >= inversionminima and \
                        (puntoADX == False or puntoADX == 0.0 or puntoADX >= ADXobjetivo) and \
                        (
                         (puntoDIplus == False and puntoDIminus == False) or
                         (estrategia == 'Alcista' and puntoDIplus >= puntoDIminus) or
                         (estrategia == 'Bajista' and puntoDIminus >= puntoDIplus)
                        ):

                            if salida == False:  # analisis de que no hay salida, le asignamos la fecha y cotizacion actual
                                fechasalida = str(fechaRegistro)
                                # Se da el caso que el historico o el ajuste del mismo no esta actualizado y la cotizacion si, de manera que si el analisis no nos ha dado salida y al buscar un precio de salida
                                # Si somo alcistas o bajista y no nos ha salta el stoploss con el valor actual, al precio de salida le asignamos el valor actual
                                if (estrategia == 'Alcista' and stoploss <= valorActual) or (estrategia == 'Bajista' and stoploss >= valorActual):
                                    preciosalida = valorActual
                                else:
                                    preciosalida = stoploss
                            else:
                                fechasalida, preciosalida = salida

                            # aqui en algunos casos recalculamos debido a que la orden se da con la informacion del momento, pero se puede ejecutar de manera distinta referente a los precios
                            numeroaccionesoperacion = numeroacciones
                            timmingentrada = timming
                            timmingtransicion = timming
                            inversionoperacion = numeroaccionesoperacion * precionentrada
                            inversionrecuperada = numeroaccionesoperacion * preciosalida
                            _soporteentrada = soporte[3]
                            _resistenciaentrada = resistencia[2]
                            fechaentrada = ruptura[0]
                            precionentrada2 = precionentrada
                            indicadoresentrada = indicadores
                            if (estrategia == 'Alcista' and resistencia[2] <= ruptura[2])\
                               or (estrategia == 'Bajista' and soporte[3] >= ruptura[3]):  # La ultima comprobacion es para el caso de que en el ultimo analisis en el que la ruptura es la ultima barra que aun no rompiendo la resistencia la consideramos que si, en el caso de que no estemos comprados esta ultima condicion no nos consideraria como tal
                                invertido = True
                                balance = inversionrecuperada - inversionoperacion

                            # elif estrategia == 'Bajista' and soporte[3] >= ruptura[3]:
                            #    invertido = True
                            #    balance = inversionoperacion - inversionrecuperada

                        elif invertido == True:

                            fecharuptura = ruptura[0]
                            # fecharesistencia = resistencia[0]
                            if timmingtransicion != timming and fechasalida > fecharuptura:
                                # Si hay transicion y Si la fecha de salida es posteior al de ruptura, actualizamos en nuevo precio de salida y la fecha, en los casos de las transiciones esto indipensable para que el precio de salida se adapte a los cambios de timming
                                timmingtransicion = timming  # Actualizamos el nuevo timmng de transiciones

                                if salida == False:  # analisis de que no hay salida, le asignamos la fecha y cotizacion actual
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
                                # if estrategia == 'Alcista':
                                balance = inversionrecuperada - inversionoperacion
                                # elif estrategia == 'Bajista':
                                #    balance = inversion - inversionrecuperada

                            elif fechasalida <= fecharuptura:
                            # elif fechasalida <= fecharuptura:
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
                                if fechasalida != fecharuptura:  # Eliminada la posibilidad porque en el caso de que fechasalida == fecharuptura sea en una LT, nos saca y volvemos a entrar en la LT
                                    p -= 1  # Puede que el ciclo que me saca, no impida que vuelva a entrar
                                # almaceno aqui la informacion del backtes porque puede que entre en un timming pero salga en otro
                                backtest.append((ticket, mercado, fechaentrada, precionentrada2, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timmingtransicion, inversionoperacion, inversionrecuperada, balance, indicadoresentrada))
                                invertido = False

                        p += 1

                    # si me ha sacado invertido en la ultima analisis
                    if invertido == True:
                        # if ( resistencia[2] <= ruptura[2] ) or ( salida == False ):#si en el ultimo analisis no hay un soporte consolidado, porque no esta rota la resistencia o no hay salida del la accion
                            #  (resistencia[2]> ruptura[2])
                            # realmente no nos hemos salido de la operacion pero como no sabemos si nos sacara o no, valoramos la operacion a lo que valdria en ese momento
                        # fechasalida=ruptura[0]
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
                            backtest.append((ticket, mercado, fechaentrada, precionentrada2, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timmingtransicion, inversionoperacion, inversionrecuperada, balance, indicadoresentrada))
                            invertido = False

# En el caso de hacer un solo ticket, comentar desde aqui hasta cuentraatras incluido
                cuentaatras -= 1

            if len(backtest) > 0:
                positivas = 0
                negativas = 0
                inversionTotal = 0
                inversionrecuperadaTotal = 0

                archivobacktest = os.path.join(os.getcwd(), __carpetas__['Backtest'], ((datetime.now()).strftime("%Y-%m-%d %H%M")) + '.csv')
                j = open(archivobacktest, 'w')
                j.write('ticket;mercado;AnoE;MesE;DiaE;PrecioE;TimmingE;Nacciones;AnoS;MesS;DiaS;PrecioS;TimmingS;InversionE;InversionS;resultado;ADX;DI+;DI-\n')
                # writercsv = csv.writer(j, delimiter=';', lineterminator = '\n', doublequote = True)

                for n in backtest:
                    ticket, mercado, fechaentrada, precionentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversion, inversionrecuperada, balance, indicadores = n
                    # si los indicadores son False, esto no funcionara
                    if ADXobjetivo == False:  # la otra opcion era asignarle a los indicacores valor Falso o 0 , pero no me parecio bien y es lioso imprimir columnas inecesarias
                        texto = (("%s;%s;%s;%.3f;%s;%d;%s;%.3f;%s;%.3f;%.3f;%.3f\n") \
                                 % (
                                    ticket,
                                    mercado,
                                    fechaentrada.replace('-', ';'),
                                    precionentrada,
                                    timmingentrada,
                                    numeroaccionesoperacion,
                                    fechasalida.replace('-', ';'),
                                    preciosalida,
                                    timming,
                                    inversion,
                                    inversionrecuperada,
                                    balance
                                    )).replace('.', ',')
                    else:

                        texto = (("%s;%s;%s;%.3f;%s;%d;%s;%.3f;%s;%.3f;%.3f;%.3f;%.3f;%.3f;%.3f\n") \
                                 % (
                                    ticket,
                                    mercado,
                                    fechaentrada.replace('-', ';'),
                                    precionentrada,
                                    timmingentrada,
                                    numeroaccionesoperacion,
                                    fechasalida.replace('-', ';'),
                                    preciosalida,
                                    timming,
                                    inversion,
                                    inversionrecuperada,
                                    balance,
                                    indicadores[0],
                                    indicadores[1],
                                    indicadores[2]
                                    )).replace('.', ',')
                    j.write(texto)

                    # writercsv.writerow(n)

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
                j.write('Backtest desde la fecha : %s\n' % str(analizardesde))
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
                j.write(('Media Movil Exponencial 2A para cruce de medias diario  : %s\n' % MMe2diario))
                j.write(('Media Movil Exponencial 2A para cruce de medias semanal : %s\n' % MMe2semanal))
                j.write(('Media Movil Exponencial 2A para cruce de medias mensual : %s\n' % MMe2mensual))
                j.write(('True Averange xrange Mensual: %s\n' % TARmensual))
                j.write(('True Averange xrange Samanal: %s\n' % TARsemanal))
                j.write(('True Averange xrange Diario : %s\n' % TARdiario))
                j.write(('Average Directional Movement Index Objetivo: %s\n' % ADXobjetivo))
                j.write(('Average Directional Movement Index Mensual: %s\n' % ADXmensual))
                j.write(('Average Directional Movement Index Samanal: %s\n' % ADXsemanal))
                j.write(('Average Directional Movement Index Diario: %s\n' % ADXdiario))
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

#            'Cambiar sistema de analisis',
#            '------------------------------',
#            'T) Cooper',
        elif opcion == 't':
            print(seleccion)
            # del analisisAlcistaAccion, analisisBajistaAccion
            # from Cooper import analisisAlcistaAccion, analisisBajistaAccion
            print('Cambiado todos los sistemas de analisis al sistema de Cooper')

#        'V) Exportar datos a arhivos csv',
        elif opcion == 'v':
            print (seleccion)
            print ('Limpiando Directorio')
            # os.remove(glob.glob(os.path.join(os.getcwd(), __carpetas__['Historicos'], nombre + "*.*")))
            archivosticket = glob.glob(os.path.join(os.getcwd(), __carpetas__['Historicos'], "*.*"))
            for archivo in archivosticket:
                os.remove(archivo)
            del archivosticket
            moneda = (raw_input('Introduce sufijo de tickets del mercado a exportar (Todas): ')).upper()
            if moneda == '' or moneda == None:
                cursor.execute("SELECT `tiket`, `codigo`, `nombre` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` = 'N/A' ORDER BY `Cobo_componentes`.`tiket` ASC")
            else:
                moneda = (moneda,)
                cursor.execute("SELECT `tiket`, `codigo`, `nombre` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` = 'N/A' AND `Cobo_componentes`.`mercado` IN (SELECT `nombreUrl` FROM `Cobo_mercado_moneda` WHERE `abrevMoneda` LIKE ?) ORDER BY `Cobo_componentes`.`tiket` ASC", moneda)
            listatickets = cursor.fetchall()
            listatickets = ((ticket[0], ticket[1], ticket[2]) for ticket in listatickets)
            listatickets = deque(list(listatickets))
            ticketsnodescargados = []
            # for ticket in listatickets:
            while len(listatickets) > 0:
                ticket, _codigo, naccion = listatickets.popleft()
                naccion = (naccion.strip('"')).replace(',', '')

                print('')
                print('Tickets pendientes de exportar %d' % len(listatickets))
                print('Exportando ticket %s' % ticket)

                if BBDD.datoshistoricosexisten(ticket):
                    # funcion maximo minimo historico
                    datos = BBDD.datoshistoricoslee(ticket)

                    for timming in 'MWD':
                        if timming == 'D':
                            datosaccion = datos
                        elif timming == 'W':
                            datosaccion = yahoofinance.subirtimming(datos, timming='w')
                        elif timming == 'M':
                            datosaccion = yahoofinance.subirtimming(datos, timming='m')

                        if len(datosaccion) > 0:
                            nombre = (str(ticket)).replace('.', '_')
                            # nombre = (str(ticket) + str(codigo)).replace('.', '_')
                            archivo = os.path.join(os.getcwd(), __carpetas__['Historicos'], nombre + '.' + timming + '.csv')
                            j = open(archivo, 'w')
                            j.write('<TICKER>,<NAME>,<PER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>\n')
                            writercsv = csv.writer(j, delimiter=',', lineterminator='\n', doublequote=True)
                            for n in datosaccion:

                                fecha, apertura, maximo, minimo, cierre, volumen = n
                                fecha = fecha.replace('-', '')

                                n = (ticket, naccion, timming, fecha, '000000', apertura, maximo, minimo, cierre, volumen, '0')

                                writercsv.writerow(n)
                                # j.write(str(n)+'\n')
                            j.close()

                        else:  # No existe suficiente historico
                            BBDD.ticketerror(ticket)
                            ticketsnodescargados.append(ticket)
                else:  # no existe el archivo
                    # cotizacionesTicket(naccion)
                    BBDD.ticketerror(ticket)
                    ticketsnodescargados.append(ticket)

                print('')

            print('Tickets para los que no hay cotizaciones historicas')
            for ticket in ticketsnodescargados:
                print(ticket)
            print('Un total de : ', len(ticketsnodescargados))

#        'W) Dar de alta acciones desde archivo',
        elif opcion == 'w':
            print(seleccion)

            incluidos = 0

            archivowtickers = os.path.join('C:\\xampp\\htdocs\\jstock', 'wtickers.dat')

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
                # incluir = True

                punto = naccion.find('.')
                if punto != -1 and not (naccion[punto:] in str(sufijosexcluidos)):  # encontramos el punto en la accion y utilizamos su posicion para extraer de la accion su sufijo y si no se encuentra en la lista de excluidas, lo incluimos
                    naccion = (naccion,)
                    cursor.execute("SELECT *  FROM `Cobo_nombreticket` WHERE (`Cobo_nombreticket`.`nombre` = ?)", naccion)
                    numeroResultado = len(cursor.fetchall())
                    if numeroResultado == 0:
                        cursor.execute("INSERT INTO `Cobo_nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES (?, '" + str(date.today()) + "', NULL, NULL)", naccion)
                        print(naccion[0] + ' anadido a la base de datos')
                        incluidos += 1

                # for suf in sufijosexcluidos:# Todas las comparaciones con los sufijosexcluidos tienen que ser -1(no existe) para que lo anadamos, si hay uno, no se anade
                #    existe = naccion.find(suf)
                #    if existe != -1:
                #        incluir = False

                # if incluir:
                #    sql = "SELECT *  FROM `Cobo_nombreticket` WHERE (`Cobo_nombreticket`.`nombre` = '" + naccion + "')"
                #

                #    if len(cursor.execute(sql).fetchall()) == 0:
                #        sql = "INSERT INTO `Cobo_nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES ('" + naccion + "', '" + str(date.today()) + "', NULL, NULL)"
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
    # os.spawnl( os.P_NOWAIT, 'C:\\xampp\\apache\\bin\pv.exe -f -k mysqld.exe -q' )
        elif opcion == 'z':

            cursor.close()
            db.close()
            break

############################################################
# programa principal
if __name__ == '__main__':
    cursor, db = BBDD.conexion()
    main()
