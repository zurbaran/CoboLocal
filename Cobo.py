#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Cobo.py - v0.05 2017-07-16 Antonio Caballero, Paco Corbi.

Este modulo proporciona las herramientas necesarias para el analisis, gestion y backtest de acciones

License: http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode

"""

__version__ = '0.06'
__date__ = '2020-03-09'
__author__ = ('Antonio Caballero', 'Paco Corbi')
__mail__ = ('zurbaran79@hotmail.com', 'pacocorbi@hotmail.com')
__license__ = 'http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode'

# License
#
# THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.
#
# BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.
#
# 1. Definitions
#
#     "Adaptation" means a work based upon the Work, or upon the Work and other pre-existing works, such as a translation, adaptation, derivative work, arrangement of music or other alterations of a literary or artistic work, or phonogram or performance and includes cinematographic adaptations or any other form in which the Work may be recast, transformed, or adapted including in any form recognizably derived from the original, except that a work that constitutes a Collection will not be considered an Adaptation for the purpose of this License. For the avoidance of doubt, where the Work is a musical work, performance or phonogram, the synchronization of the Work in timed-relation with a moving image ("synching") will be considered an Adaptation for the purpose of this License.
#     "Collection" means a collection of literary or artistic works, such as encyclopedias and anthologies, or performances, phonograms or broadcasts, or other works or subject matter other than works listed in Section 1(g) below, which, by reason of the selection and arrangement of their contents, constitute intellectual creations, in which the Work is included in its entirety in unmodified form along with one or more other contributions, each constituting separate and independent works in themselves, which together are assembled into a collective whole. A work that constitutes a Collection will not be considered an Adaptation (as defined above) for the purposes of this License.
#     "Distribute" means to make available to the public the original and copies of the Work or Adaptation, as appropriate, through sale or other transfer of ownership.
#     "License Elements" means the following high-level license attributes as selected by Licensor and indicated in the title of this License: Attribution, Noncommercial, ShareAlike.
#     "Licensor" means the individual, individuals, entity or entities that offer(s) the Work under the terms of this License.
#     "Original Author" means, in the case of a literary or artistic work, the individual, individuals, entity or entities who created the Work or if no individual or entity can be identified, the publisher; and in addition (i) in the case of a performance the actors, singers, musicians, dancers, and other persons who act, sing, deliver, declaim, play in, interpret or otherwise perform literary or artistic works or expressions of folklore; (ii) in the case of a phonogram the producer being the person or legal entity who first fixes the sounds of a performance or other sounds; and, (iii) in the case of broadcasts, the organization that transmits the broadcast.
#     "Work" means the literary and/or artistic work offered under the terms of this License including without limitation any production in the literary, scientific and artistic domain, whatever may be the mode or form of its expression including digital form, such as a book, pamphlet and other writing; a lecture, address, sermon or other work of the same nature; a dramatic or dramatico-musical work; a choreographic work or entertainment in dumb show; a musical composition with or without words; a cinematographic work to which are assimilated works expressed by a process analogous to cinematography; a work of drawing, painting, architecture, sculpture, engraving or lithography; a photographic work to which are assimilated works expressed by a process analogous to photography; a work of applied art; an illustration, map, plan, sketch or three-dimensional work relative to geography, topography, architecture or science; a performance; a broadcast; a phonogram; a compilation of data to the extent it is protected as a copyrightable work; or a work performed by a variety or circus performer to the extent it is not otherwise considered a literary or artistic work.
#     "You" means an individual or entity exercising rights under this License who has not previously violated the terms of this License with respect to the Work, or who has received express permission from the Licensor to exercise rights under this License despite a previous violation.
#     "Publicly Perform" means to perform public recitations of the Work and to communicate to the public those public recitations, by any means or process, including by wire or wireless means or public digital performances; to make available to the public Works in such a way that members of the public may access these Works from a place and at a place individually chosen by them; to perform the Work to the public by any means or process and the communication to the public of the performances of the Work, including by public digital performance; to broadcast and rebroadcast the Work by any means including signs, sounds or images.
#     "Reproduce" means to make copies of the Work by any means including without limitation by sound or visual recordings and the right of fixation and reproducing fixations of the Work, including storage of a protected performance or phonogram in digital form or other electronic medium.
#
# 2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit, or restrict any uses free from copyright or rights arising from limitations or exceptions that are provided for in connection with the copyright protection under copyright law or other applicable laws.
#
# 3. License Grant. Subject to the terms and conditions of this License, Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the duration of the applicable copyright) license to exercise the rights in the Work as stated below:
#
#     to Reproduce the Work, to incorporate the Work into one or more Collections, and to Reproduce the Work as incorporated in the Collections;
#     to create and Reproduce Adaptations provided that any such Adaptation, including any translation in any medium, takes reasonable steps to clearly label, demarcate or otherwise identify that changes were made to the original Work. For example, a translation could be marked "The original work was translated from English to Spanish," or a modification could indicate "The original work has been modified.";
#     to Distribute and Publicly Perform the Work including as incorporated in Collections; and,
#     to Distribute and Publicly Perform Adaptations.
#
# The above rights may be exercised in all media and formats whether now known or hereafter devised. The above rights include the right to make such modifications as are technically necessary to exercise the rights in other media and formats. Subject to Section 8(f), all rights not expressly granted by Licensor are hereby reserved, including but not limited to the rights described in Section 4(e).
#
# 4. Restrictions. The license granted in Section 3 above is expressly made subject to and limited by the following restrictions:
#
#     You may Distribute or Publicly Perform the Work only under the terms of this License. You must include a copy of, or the Uniform Resource Identifier (URI) for, this License with every copy of the Work You Distribute or Publicly Perform. You may not offer or impose any terms on the Work that restrict the terms of this License or the ability of the recipient of the Work to exercise the rights granted to that recipient under the terms of the License. You may not sublicense the Work. You must keep intact all notices that refer to this License and to the disclaimer of warranties with every copy of the Work You Distribute or Publicly Perform. When You Distribute or Publicly Perform the Work, You may not impose any effective technological measures on the Work that restrict the ability of a recipient of the Work from You to exercise the rights granted to that recipient under the terms of the License. This Section 4(a) applies to the Work as incorporated in a Collection, but this does not require the Collection apart from the Work itself to be made subject to the terms of this License. If You create a Collection, upon notice from any Licensor You must, to the extent practicable, remove from the Collection any credit as required by Section 4(d), as requested. If You create an Adaptation, upon notice from any Licensor You must, to the extent practicable, remove from the Adaptation any credit as required by Section 4(d), as requested.
#     You may Distribute or Publicly Perform an Adaptation only under: (i) the terms of this License; (ii) a later version of this License with the same License Elements as this License; (iii) a Creative Commons jurisdiction license (either this or a later license version) that contains the same License Elements as this License (e.g., Attribution-NonCommercial-ShareAlike 3.0 US) ("Applicable License"). You must include a copy of, or the URI, for Applicable License with every copy of each Adaptation You Distribute or Publicly Perform. You may not offer or impose any terms on the Adaptation that restrict the terms of the Applicable License or the ability of the recipient of the Adaptation to exercise the rights granted to that recipient under the terms of the Applicable License. You must keep intact all notices that refer to the Applicable License and to the disclaimer of warranties with every copy of the Work as included in the Adaptation You Distribute or Publicly Perform. When You Distribute or Publicly Perform the Adaptation, You may not impose any effective technological measures on the Adaptation that restrict the ability of a recipient of the Adaptation from You to exercise the rights granted to that recipient under the terms of the Applicable License. This Section 4(b) applies to the Adaptation as incorporated in a Collection, but this does not require the Collection apart from the Adaptation itself to be made subject to the terms of the Applicable License.
#     You may not exercise any of the rights granted to You in Section 3 above in any manner that is primarily intended for or directed toward commercial advantage or private monetary compensation. The exchange of the Work for other copyrighted works by means of digital file-sharing or otherwise shall not be considered to be intended for or directed toward commercial advantage or private monetary compensation, provided there is no payment of any monetary compensation in con-nection with the exchange of copyrighted works.
#     If You Distribute, or Publicly Perform the Work or any Adaptations or Collections, You must, unless a request has been made pursuant to Section 4(a), keep intact all copyright notices for the Work and provide, reasonable to the medium or means You are utilizing: (i) the name of the Original Author (or pseudonym, if applicable) if supplied, and/or if the Original Author and/or Licensor designate another party or parties (e.g., a sponsor institute, publishing entity, journal) for attribution ("Attribution Parties") in Licensor's copyright notice, terms of service or by other reasonable means, the name of such party or parties; (ii) the title of the Work if supplied; (iii) to the extent reasonably practicable, the URI, if any, that Licensor specifies to be associated with the Work, unless such URI does not refer to the copyright notice or licensing information for the Work; and, (iv) consistent with Section 3(b), in the case of an Adaptation, a credit identifying the use of the Work in the Adaptation (e.g., "French translation of the Work by Original Author," or "Screenplay based on original Work by Original Author"). The credit required by this Section 4(d) may be implemented in any reasonable manner; provided, however, that in the case of a Adaptation or Collection, at a minimum such credit will appear, if a credit for all contributing authors of the Adaptation or Collection appears, then as part of these credits and in a manner at least as prominent as the credits for the other contributing authors. For the avoidance of doubt, You may only use the credit required by this Section for the purpose of attribution in the manner set out above and, by exercising Your rights under this License, You may not implicitly or explicitly assert or imply any connection with, sponsorship or endorsement by the Original Author, Licensor and/or Attribution Parties, as appropriate, of You or Your use of the Work, without the separate, express prior written permission of the Original Author, Licensor and/or Attribution Parties.
#
#     For the avoidance of doubt:
#         Non-waivable Compulsory License Schemes. In those jurisdictions in which the right to collect royalties through any statutory or compulsory licensing scheme cannot be waived, the Licensor reserves the exclusive right to collect such royalties for any exercise by You of the rights granted under this License;
#         Waivable Compulsory License Schemes. In those jurisdictions in which the right to collect royalties through any statutory or compulsory licensing scheme can be waived, the Licensor reserves the exclusive right to collect such royalties for any exercise by You of the rights granted under this License if Your exercise of such rights is for a purpose or use which is otherwise than noncommercial as permitted under Section 4(c) and otherwise waives the right to collect royalties through any statutory or compulsory licensing scheme; and,
#         Voluntary License Schemes. The Licensor reserves the right to collect royalties, whether individually or, in the event that the Licensor is a member of a collecting society that administers voluntary licensing schemes, via that society, from any exercise by You of the rights granted under this License that is for a purpose or use which is otherwise than noncommercial as permitted under Section 4(c).
#     Except as otherwise agreed in writing by the Licensor or as may be otherwise permitted by applicable law, if You Reproduce, Distribute or Publicly Perform the Work either by itself or as part of any Adaptations or Collections, You must not distort, mutilate, modify or take other derogatory action in relation to the Work which would be prejudicial to the Original Author's honor or reputation. Licensor agrees that in those jurisdictions (e.g. Japan), in which any exercise of the right granted in Section 3(b) of this License (the right to make Adaptations) would be deemed to be a distortion, mutilation, modification or other derogatory action prejudicial to the Original Author's honor and reputation, the Licensor will waive or not assert, as appropriate, this Section, to the fullest extent permitted by the applicable national law, to enable You to reasonably exercise Your right under Section 3(b) of this License (right to make Adaptations) but not otherwise.
#
# 5. Representations, Warranties and Disclaimer
#
# UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING AND TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, LICENSOR OFFERS THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO THIS EXCLUSION MAY NOT APPLY TO YOU.
#
# 6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW, IN NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT OF THIS LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
#
# 7. Termination
#
#     This License and the rights granted hereunder will terminate automatically upon any breach by You of the terms of this License. Individuals or entities who have received Adaptations or Collections from You under this License, however, will not have their licenses terminated provided such individuals or entities remain in full compliance with those licenses. Sections 1, 2, 5, 6, 7, and 8 will survive any termination of this License.
#     Subject to the above terms and conditions, the license granted here is perpetual (for the duration of the applicable copyright in the Work). Notwithstanding the above, Licensor reserves the right to release the Work under different license terms or to stop distributing the Work at any time; provided, however that any such election will not serve to withdraw this License (or any other license that has been, or is required to be, granted under the terms of this License), and this License will continue in full force and effect unless terminated as stated above.
#
# 8. Miscellaneous
#
#     Each time You Distribute or Publicly Perform the Work or a Collection, the Licensor offers to the recipient a license to the Work on the same terms and conditions as the license granted to You under this License.
#     Each time You Distribute or Publicly Perform an Adaptation, Licensor offers to the recipient a license to the original Work on the same terms and conditions as the license granted to You under this License.
#     If any provision of this License is invalid or unenforceable under applicable law, it shall not affect the validity or enforceability of the remainder of the terms of this License, and without further action by the parties to this agreement, such provision shall be reformed to the minimum extent necessary to make such provision valid and enforceable.
#     No term or provision of this License shall be deemed waived and no breach consented to unless such waiver or consent shall be in writing and signed by the party to be charged with such waiver or consent.
#     This License constitutes the entire agreement between the parties with respect to the Work licensed here. There are no understandings, agreements or representations with respect to the Work not specified here. Licensor shall not be bound by any additional provisions that may appear in any communication from You. This License may not be modified without the mutual written agreement of the Licensor and You.
#     The rights granted under, and the subject matter referenced, in this License were drafted utilizing the terminology of the Berne Convention for the Protection of Literary and Artistic Works (as amended on September 28, 1979), the Rome Convention of 1961, the WIPO Copyright Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996 and the Universal Copyright Convention (as revised on July 24, 1971). These rights and subject matter take effect in the relevant jurisdiction in which the License terms are sought to be enforced according to the corresponding provisions of the implementation of those treaty provisions in the applicable national law. If the standard suite of rights granted under applicable copyright law includes additional rights not granted under this License, such additional rights are deemed to be included in the License; this License is not intended to restrict the license of any rights under applicable law.
#
#     Creative Commons Notice
#
#     Creative Commons is not a party to this License, and makes no warranty whatsoever in connection with the Work. Creative Commons will not be liable to You or any party on any legal theory for any damages whatsoever, including without limitation any general, special, incidental or consequential damages arising in connection to this license. Notwithstanding the foregoing two (2) sentences, if Creative Commons has expressly identified itself as the Licensor hereunder, it shall have all rights and obligations of Licensor.
#
#     Except for the limited purpose of indicating to the public that the Work is licensed under the CCPL, Creative Commons does not authorize the use by either party of the trademark "Creative Commons" or any related trademark or logo of Creative Commons without the prior written consent of Creative Commons. Any permitted use will be in compliance with Creative Commons' then-current trademark usage guidelines, as may be published on its website or otherwise made available upon request from time to time. For the avoidance of doubt, this trademark restriction does not form part of this License.
#
#     Creative Commons may be contacted at http://creativecommons.org/.

####################################################
# modulos estandar importados

# import urllib
from collections import deque
from datetime import date, datetime
# , timedelta
import csv
import glob
import logging
from logging.handlers import RotatingFileHandler
import os
import ast
import sys
import math
# import dropbox

# import logging.config
# ARCHIVOCONFIGBACKTEST = os.path.join(os.getcwd(), 'Cobo.backtest.config')
# logging.config.fileConfig(ARCHIVO_LOG)
# logging.basicConfig(filename = ARCHIVO_LOG)
# logging.captureWarnings(True)
# basic setup with ISO 8601 time format

####################################################
# modulos no estandar o propios
import indicador
import BBDD
import yahoofinance
from jstock import ticketsJstock
from yahooticket import ticketsYahooD
import HTML

from settings import ARCHIVO_LOG, SUFIJOSEXCLUIDOS, MERCADOSEXCLUIDOS, CARPETAS, DIFREGACTUALIZAR, FILTROS, FILTROSTOPLOSS, ARCHIVOCONFIGBACKTEST

#try:
#    if os.path.getsize(ARCHIVO_LOG) >= (100*1024*1024):#524288000: #Si el archivo log ocupa mas de 500 MB*1024*1024 lo borra
#        os.remove(ARCHIVO_LOG)
#except:
#    pass

borranoactualizados = False
# 2018-02-02 15:45:52
# Crear un logger personalizado
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Establecer el nivel global de logging

# Configurar el RotatingFileHandler
handler = RotatingFileHandler(
    ARCHIVO_LOG, maxBytes=10 * 1024 * 1024,
    backupCount=5)  # Máximo de 100 MB por archivo, 5 archivos de respaldo
handler.setLevel(logging.DEBUG)

# Mantener el formato actual de log
formatter = logging.Formatter(
    '%(asctime)s : %(processName)s : %(levelname)s : %(module)s : %(funcName)s: %(lineno)d :%(message)s'
)
handler.setFormatter(formatter)

# Añadir el manejador (handler) al logger
logger.addHandler(handler)

# Ejemplo de uso (manteniendo la sintaxis actual)
logging.debug(os.linesep)
logging.debug('Inicio de Aplicacion')

############################################################
# comprobaciones especiales

# assert

############################################################
# definicion de funciones


def _test():
    """."""
    import doctest
    doctest.testmod()
    # TODO: implementar pruebas doctest
    # ejemplos en : http://mundogeek.net/archivos/2008/09/17/pruebas-en-python/  http://magmax9.blogspot.com.es/2011/09/python-como-hacer-pruebas-1.html
    # Externalizar los test
    # doctest.testfile('example2.txt')


def analisisAlcistaAccion(naccion, **config):
    """
    Analisis alcista
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
    if MME is False:
        MME2 = False
    else:
        MME2 = config.get('MME2', False)
    TAR = config.get('TAR', False)
    ADX = config.get('ADX', False)
    filtro = config.get('filtro', 0.0)
    timming = config.get('timming', "m")
    desdefecha = config.get('desdefecha', False)
    txt = config.get(
        'txt', True
    )  # Parametro para hacer que la funcion cree el archvo del analisis

    if desdefecha == '' or desdefecha == ' ' or desdefecha is None:
        desdefecha = False
    elif desdefecha is not False:
        todohistorico, desdefecha = desdefecha

    if timming == 'd':
        datoshistoricos = historico
        if filtro == 0.0:
            if TAR is False:
                filtro = FILTROSTOPLOSS[timming]
            else:
                filtro = 3.7
    elif timming == 'w':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='w')
        if filtro == 0.0:
            if TAR is False:
                filtro = FILTROSTOPLOSS[timming]
            else:
                filtro = 3.0
    elif timming == 'm':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='m')
        if filtro == 0.0:
            if TAR is False:
                filtro = FILTROSTOPLOSS[timming]
            else:
                filtro = 2.5

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

    if desdefecha is not False and todohistorico is False:  # Borramos el historico anterior a la fecha
        i = 0
        while i < len(datoshistoricos):
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = datoshistoricos[
                i]
            if fecha >= desdefecha:
                datoshistoricos = datoshistoricos[i:]
                break
            if i == (
                    len(datoshistoricos) - 1
            ) and fecha < desdefecha:  # Ha llegado al final de sin encontrar una fecha de analisis mayor a desdefecha
                datoshistoricos = []
            i += 1
        del fecha, _apertura, _maximo, _minimo, _cierre, _volumen

    i = 0

    if not (MME is False):
        puntosMME = indicador.MME(datoshistoricos, MME=MME)
        if not (MME2 is False):
            puntosMME2 = indicador.MME(datoshistoricos, MME=MME2)
    if not (TAR is False):
        puntosTAR = indicador.TAR(datoshistoricos, TAR=TAR)

    if not (ADX is False):
        puntosADX = indicador.ADX(datoshistoricos, ADX=ADX)
        puntosDI = indicador.DI(datoshistoricos, DI=ADX)

    while i < len(datoshistoricos):
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos[i]

        if i == 0:
            ant = 0
        else:
            ant = i - 1
        fechaanterior, _aperturaanterior, _maximoanterior, minimoanterior, cierreanterior, _volumenanterior = datoshistoricos[
            ant]
        _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[
            r]
        _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[
            s]

        if not (ADX is False):
            fechaADX, puntoADX = puntosADX[ant]
            fechaDI, puntoDIplus, puntoDIminus = puntosDI[ant]
            assert (fechaADX == fechaanterior or fechaDI == fechaanterior)
        else:
            puntoADX = False
            puntoDIplus = False
            puntoDIminus = False
        indicadores = (puntoADX, puntoDIplus, puntoDIminus)

        if not (TAR is False):
            fechaTAR, puntoTAR = puntosTAR[ant]

            assert (fechaTAR == fechaanterior)

            if len(analisisalcista) > 0 and stoploss < (round(
                (cierreanterior - (puntoTAR * filtro)), 3)):
                stoploss = round((cierreanterior - (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

        if not (MME is False):  # and len( datoshistoricos ) >= MME:

            fechaMME, puntoMME = puntosMME[i]
            if not (MME2 is False):
                fechaMME2, puntoMME2 = puntosMME2[i]
                assert (fechaMME == fecha and fechaMME == fechaMME2)

            assert (fechaMME == fecha)

            # if i >= ( MME - 1 ):# Empieza a utilizar el indicador.MME en una barra en concreto, para la MME30 lo utiliza apartir de la barra 30(cuyo indice es 29)
            if puntoMME > 0:
                if resistencia is False and soporte is False and puntoMME < minimo:  # Si no buscamos ni resistencias ni soportes es porque venimos de debajo de la MME
                    # la grafica esta completamente por encima de la MME,  y empezamos a buscar resistencias sobre la MMe
                    r = i
                    _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[
                        r]
                    resistencia = True
                    soporte = False
                # elif maximo < puntoMME:# Grafica completamente bajo Media Movil Exponencial, no buscamos resistencias ni soportes, y consideramos la barra actual como resistencia
                elif maximo < puntoMME and (MME2 is False or
                                            (MME2 is not False
                                             and puntoMME <= puntoMME2)):
                    # con esta logica, si hemos creado una resistencia y en algun momento bajamos una MME muy cercana a la grafica, habremos "borrado" esa resistencia anterior asignandole la barra actual como resistencia
                    r = i
                    _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[
                        r]
                    resistencia = False
                    soporte = False

        # anade en analisisalcista, los puntos de entrada por Linea de tendencia
        if len(analisisalcista) > 0 and entradapuntoLT:

            LineaTendenciaInicio = analisisalcista[-1][3]
            LineaTendenciaFin = analisisalcista[-1][4]

            _fechaLTi, minimoLTi = LineaTendenciaInicio
            _fechaLTf, minimoLTf = LineaTendenciaFin

            if minimoLTi > 0 and minimoLTf > 0:
                # TODO :  comprobar con un asser si el precioentradapuntoLT es igual al calculado con la siguiente funcion
                # entrada = puntocurvaexponencial(ltdateini, ltpriceini, ltdatefin, ltpricefin, timming, incremperiod=incremperiod)
                precioentradapuntoLT = round(
                    (minimoLTi *
                     ((1 + (((1.0 + (((minimoLTf - minimoLTi) / minimoLTi)))**
                             (12.0 /
                              (LTf - LTi))) - 1.0))**((i - LTi) / 12.0))), 3)

                if precioentradapuntoLT >= minimo:
                    if precioentradapuntoLT >= apertura or precioentradapuntoLT > maximo:  # El precioentradapuntoLT esta por encima del maximo o abrio directamente por debajo, lo que significa que puede haber un split y utilizamos la apertura
                        precionentrada = apertura
                    else:  # elif maximo>=precioentradapuntoLT:# El precioentradapuntoLT esta entre el maximo y el minimo y la paertura no la hizo por debajo
                        precionentrada = precioentradapuntoLT
                    # ultimo soporte consolidado
                    soporteanterior = analisisalcista[-1][1][0]
                    barraentradapuntoLT = (fecha, precioentradapuntoLT,
                                           precioentradapuntoLT,
                                           precioentradapuntoLT,
                                           precioentradapuntoLT, volumen)
                    analisisalcista.append(
                        (barraentradapuntoLT, (soporteanterior, stoploss),
                         (datoshistoricos[i], precionentrada),
                         LineaTendenciaInicio, LineaTendenciaFin,
                         salidaOperacion, timming, indicadores))
                    entradapuntoLT = False

        # cambia en la lista analisialcista los valores del precio de salida para cada operacion, cuando se rompe un stoploss, por la barra en la que se produce
        if stoploss >= minimo and len(analisisalcista) > 0:

            if stoploss > maximo or stoploss >= apertura:  # El stoploss esta por encima del maximo o apertura, lo que significa que puede haber un split o abrio por debajo del stoploss
                salidaoperaciones = (fecha, apertura)
            else:  # elif maximo >= stoploss:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)

            i2 = 0
            while i2 < len(analisisalcista):
                resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisalcista[
                    i2]
                if salidaOperacionAnalisis is False:
                    analisisalcista[
                        i2] = resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                    # analisisalcista[i2][5]=datoshistoricos[i]
                i2 += 1
            entradapuntoLT = False

        if resistencia and maximo > maximoresisten and not (
                minimo < minimoanterior and apertura < cierre):
            # No actualizamos la resistencia, si esta es la misma barra que la crea y ademas la rompe con un movimiento de abajo hacia arriba, considerando como valida la resistencia anterior

            r = i  # le damos a r el indice de los datoshistoricos donde se encuentra la informacion de la resistencia y volvemos a leer los datos
            _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[
                r]

        if resistencia and minimo < minimoanterior:  # resistencia consolidada
            resistencia = False
            soporte = True
            # volvemos al indice donde esta la resistencia para comprobar desde ahi los posibles soportes
            # comparamos que el movimiento viene de abajo hacia arriba, para asi considerar el minimo de la resistencia como externo en el movimiento y que en tal caso no pueda ser el soporte
            if aperturaresisten < cierreresisten and (
                    i + 1) < len(datoshistoricos):
                # esto ultimo es porque puede que la ultima barra sea la resistencia, si le sumasemos uno nos saldriamos de rango
                i = r + 1
            else:
                i = r
            s = i
            _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[
                s]
            _fecha, apertura, maximo, minimo, cierre, _volumen = datoshistoricos[
                i]

    # Soporte alcista
        if soporte and minimo < minimosoporte and not (
            (maximo > maximoresisten) and (apertura > cierre)
        ):  # No actualizamos el soporte, si es la misma barra que rompe la resistencia y ademas la apertura es mayor que el cierre
            # el soporte no tiene que ser la propia resistencia si el minimo dejado lo ha hecho abriendo abajo y cerrando arriba
            s = i
            _fechasoporte, _aperturasoporte, _maximosoporte, minimosoporte, _cierresoporte, _volumensoporte = datoshistoricos[
                s]

        if soporte and ((maximo > maximoresisten) or i == (
            (len(datoshistoricos)) - 1)) and not (
                (datoshistoricos[r] or datoshistoricos[s]) in analisisalcista):

            if r > 0:  # No podremos calcular LT si no hay barras fuerra del ciclo resistencia y soporte, por eso la resistencia e inicio del ciclo tiene que ser mayor que 0
                localizaLTi = True
                localizaLTf = False
                LTi = r - 1

                LTf = s
                _fechaLTf, _aperturaLTf, _maximoLTf, minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[
                    LTf]

                while localizaLTi:

                    if LTi >= 0:
                        fechaLTi, _aperturaLTi, _maximoLTi, minimoLTi, _cierreLTi, _volumenLTi = datoshistoricos[
                            LTi]
                    else:
                        localizaLTf = True
                        localizaLTi = False
                        break

                        #print (LTi)
                    for j in range(LTi, -1, -1):
                        fechaj, _aperturaj, _maximoj, minimoj, _cierrej, _volumenj = datoshistoricos[
                            j]
                        # logging.debug(f"Iteración {j}: Valores de entrada: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTi={LTi}, LTf={LTf}")

                        # if (minimoLTi>minimoLTf or minimoLTi==0.0) and LTi>0:# Anadido el 23/01/2011 como estoy en alcista, si el minimodeLTi es mayor que el minimoLTf es porque esta por encima, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por debajo del LTf
                        if minimoLTi > minimoLTf and LTi > 0:  # Anadido el 23/01/2011 como estoy en alcista, si el minimodeLTi es mayor que el minimoLTf es porque esta por encima, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por debajo del LTf
                            LTi -= 1
                            break
                        try:
                            # Realizamos el cálculo de puntoLT
                            puntoLT = (minimoLTi * ((1 + (
                                ((1.0 +
                                  (((minimoLTf - minimoLTi) / minimoLTi)))**
                                 (12.0 /
                                  (LTf - LTi))) - 1.0))**((j - LTi) / 12.0)))

                            # Comprobamos si puntoLT es un número complejo
                            if isinstance(puntoLT, complex):
                                logging.debug(
                                    f"Se detectó un número complejo en el cálculo de puntoLT. Buscando LTi; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                # Aplicar abs() para obtener el valor absoluto, si es necesario, o solo usar la parte real
                                puntoLT = abs(puntoLT) if abs(
                                    puntoLT.imag) > 0 else puntoLT.real

                            # Verificamos si puntoLT es infinito o NaN antes de redondearlo
                            if not math.isfinite(puntoLT):
                                logging.debug(
                                    f"Valor no finito detectado en puntoLT, asignando valor de fallback.Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                puntoLT = minimoj  # Valor de fallback

                            # Redondeamos puntoLT solo si no es complejo
                            puntoLT = round(puntoLT, 3)

                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug(
                                f"Error en cálculo: {e}. Buscando LTi; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )
                            puntoLT = minimoj
                            j = 0

                        except TypeError as e:
                            logging.debug(
                                f"TypeError en el cálculo de puntoLT, se aplicará abs(): Error en cálculo: {e}. Buscando LTi; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )
                            # Aplicamos abs() y recalculamos puntoLT
                            puntoLT = round(
                                abs(minimoLTi * ((1 + ((
                                    (1.0 +
                                     (((minimoLTf - minimoLTi) / minimoLTi)))**
                                    (12.0 / (LTf - LTi))) - 1.0))**(
                                        (j - LTi) / 12.0))), 3)

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
                    # print "LTf, i =", LTf, i
                    if LTf <= i:
                        fechaLTf, _aperturaLTf, _maximoLTf, minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[
                            LTf]
                    else:
                        localizaLTf = False
                        localizaLTi = False
                        break
#                     print "LTf, i =", LTf, i
#                     while j<=i:
                    for j in range(LTf, i + 1):
                        fechaj, _aperturaj, _maximoj, minimoj, _cierrej, _volumenj = datoshistoricos[
                            j]
                        # logging.debug(f"Iteración {j}: Valores de entrada: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTi={LTi}, LTf={LTf}")
                        # se me ha dado el caso de que cuando en los primeros ciclos alcistas, si estan demasiado proximos al inicio del historico de la accion, me toma como el mismo punto el punto de LTi y LTf
                        if LTf == LTi:
                            LTf += 1
                            break
                        try:
                            # Realizamos el cálculo de puntoLT
                            puntoLT = (minimoLTi * ((1 + (
                                ((1.0 +
                                  (((minimoLTf - minimoLTi) / minimoLTi)))**
                                 (12.0 /
                                  (LTf - LTi))) - 1.0))**((j - LTi) / 12.0)))

                            # Comprobamos si puntoLT es un número complejo
                            if isinstance(puntoLT, complex):
                                logging.debug(
                                    f"Se detectó un número complejo en el cálculo de puntoLT. Buscando LTf; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                # Aplicamos abs() para obtener el valor absoluto, si es necesario, o usamos solo la parte real
                                puntoLT = abs(puntoLT) if abs(
                                    puntoLT.imag) > 0 else puntoLT.real

                            # Verificamos si puntoLT es infinito o NaN antes de redondearlo
                            if not math.isfinite(puntoLT):
                                logging.debug(
                                    f"Valor no finito detectado en puntoLT, asignando valor de fallback.Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                puntoLT = minimoj  # Valor de fallback

                            # Redondeamos puntoLT solo si no es complejo
                            #print (puntoLT)
                            puntoLT = round(puntoLT, 3)

                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug(
                                f"Error en cálculo: {e}. Buscando LTf; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )
                            # En caso de error, asignamos minimoj a puntoLT como valor de fallback
                            puntoLT = minimoj

                        except TypeError as e:
                            logging.debug(
                                f"TypeError en el cálculo de puntoLT, se aplicará abs(): Error en cálculo: {e}. Buscando LTf; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: minimoLTi={minimoLTi}, minimoLTf={minimoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )
                            # Aplicamos abs() y recalculamos puntoLT
                            puntoLT = round(
                                abs(minimoLTi * ((1 + ((
                                    (1.0 +
                                     (((minimoLTf - minimoLTi) / minimoLTi)))**
                                    (12.0 / (LTf - LTi))) - 1.0))**(
                                        (j - LTi) / 12.0))), 3)

                        # Aveces por falta de precision en el calculo del puntoLT creamos un bucle infinito que siempre impacta en la misma barra una y otra vez
                        # Esto sirve para evitar eso no comprobando una y otra vez un LTf que siempre es la misma
                        if puntoLT > minimoj:
                            if (LTf == j or (puntoLT == 0.0
                                             and LTf < i)) and not (j + 1 > i):
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
# #                            elif LTf == j and LTfrepetido is False:
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

                LineaTendenciaInicio = (datoshistoricos[LTi][0],
                                        datoshistoricos[LTi][3])
                LineaTendenciaFin = (datoshistoricos[LTf][0],
                                     datoshistoricos[LTf][3])

                if not (datoshistoricos[LTi][3] < datoshistoricos[LTf][3]
                        ):  # comprobamos que no nos de rentabilidad negativa
                    LineaTendenciaInicio = ('0-0-0', 0.0)
                    LineaTendenciaFin = ('0-0-0', 0.0)
            else:
                LineaTendenciaInicio = ('0-0-0', 0.0)
                LineaTendenciaFin = ('0-0-0', 0.0)

            if TAR is False:
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

            analisisalcista.append(
                (datoshistoricos[r], (datoshistoricos[s], stoploss),
                 (datoshistoricos[i], precionentrada), LineaTendenciaInicio,
                 LineaTendenciaFin, salidaOperacion, timming, indicadores))
            if conEntradaLT:
                entradapuntoLT = True

            # LT=True # esto es porque hasta que no se produce un segundo soporte, no podemos calcular la linea de tendencia

            # Si la misma barra que rompe la resistencia abre arriba para cerrar por abajo del stoploss, esa barra nos saca del mercado
            if stoploss >= minimo and apertura > cierre and len(
                    analisisalcista) > 0:
                # if maximo >= stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)
                #                elif maximo < stoploss:# El stoploss esta por encima del maximo, lo que significa que puede haber un split
                #                    salidaoperaciones = ( fecha, maximo )

                i2 = 0
                while i2 < len(analisisalcista):
                    resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisalcista[
                        i2]
                    # salidaOperacionAnalisis=analisisalcista[i2][5]
                    if salidaOperacionAnalisis is False:
                        analisisalcista[
                            i2] = resistenciaAnalisis, soporteAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                        # analisisalcista[i2][5]=datoshistoricos[i]
                    i2 += 1

            r = i  # como la ultima barra que ha roto la resistencia es mas alta que la resistencia, la considero como nueva resistencia
            _fecharesisten, aperturaresisten, maximoresisten, _minimoresisten, cierreresisten, _volumenresisten = datoshistoricos[
                r]

            resistencia = True
            soporte = False

        i += 1

    if desdefecha is not False and todohistorico is True:
        i = 0
        while i < len(analisisalcista):
            resistencia, soporte, ruptura, LTi, LTf, salida, timming, indicadores = analisisalcista[
                i]
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = resistencia
            if fecha >= desdefecha:
                analisisalcista = analisisalcista[i:]
                i = 0
                break
            if i == (
                    len(analisisalcista) - 1
            ) and fecha < desdefecha:  # Ha llegado al final de analisisbajista sin encontrar una fecha de analisis mayor a desdefecha
                analisisalcista = []
            i += 1
        try:
            del resistencia, soporte, ruptura, LTi, LTf, salida, fecha, _apertura, _maximo, _minimo, _cierre, _volumen
        except UnboundLocalError as err:
            logging.debug('Error: %s al borrar bariables; Accion: %s;' %
                          (err, naccion.encode('UTF-8')))

    # ##mostramos en pantalla y creamos otro archivo no codificado con la tupla
    if len(analisisalcista) > 0 and txt:
        tickets = BBDD.ticketlistacodigo(naccion)
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), CARPETAS["Analisis"],
                               nombre + "." + timming + ".analisisalcista.txt")
        j = open(archivo, "w")
        j.write(str(config) + os.linesep)
        for n in analisisalcista:
            # ~ j.write(str(n)+os.linesep)
            resistencia, soporte, ruptura, LTi, LTf, salida, timming, indicadores = n
            j.write("Resistencia " + str(resistencia) + os.linesep)
            j.write("Soporte     " + str(soporte) + os.linesep)
            j.write("Ruptura     " + str(ruptura) + os.linesep)
            j.write("LT Inicio   " + str(LTi) + os.linesep)
            j.write("LT Final    " + str(LTf) + os.linesep)
            j.write("Salida      " + str(salida) + os.linesep)
            j.write("Timming     " + str(timming) + os.linesep)
            j.write("Indicadores ADX, DI+, DI- " + str(indicadores) +
                    os.linesep)
            j.write(os.linesep)

        for n in range(5):
            j.write(os.linesep)

        for n in listastoploss:
            j.write(str(n) + os.linesep)

        j.close()

    # formato de salida, ultimo analisis alcista, soporte anterior, todo el analisis alcista
    # hay que anadir cuando el len de analisisalcista sea mayor que 2, para cada analisis alcista hay un soporte que es el precio de salida en Lt para este.
    if len(
            analisisalcista
    ) == 1:  # esto esta porque puede que en el analisisalcista en el timming actual no produzca resultado al no existir resistencia alcista en el timming actual
        return (analisisalcista[-1], 0, analisisalcista)
    elif len(analisisalcista) > 1:
        # TODO:  es posible que haya que cambiar analisisalcista[-2][1][1] por analisisalcista[-2][1][0][3]
        return (analisisalcista[-1], (analisisalcista[-2][1][0][3]),
                analisisalcista
                )  # [-2][1][1]=penultimo analisis, Soporte, stoploss
    else:
        # habria que comprobar un timming inferirior al obtener como resultado 0
        return None


def analisisBajistaAccion(naccion, **config):
    """
    Analisis bajista.

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
    if MME is False:
        MME2 = False
    else:
        MME2 = config.get('MME2', False)
    TAR = config.get('TAR', False)
    ADX = config.get('ADX', False)
    filtro = config.get('filtro', 0.0)
    timming = config.get('timming', "m")
    desdefecha = config.get('desdefecha', False)
    txt = config.get('txt', True)

    if desdefecha == '' or desdefecha == ' ' or desdefecha is None:
        desdefecha = False
    elif desdefecha is not False:
        todohistorico, desdefecha = desdefecha

    if timming == 'd':
        datoshistoricos = historico
        if filtro == 0.0:
            if TAR is False:
                filtro = FILTROSTOPLOSS[timming]
            else:
                filtro = 3.7
    elif timming == 'w':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='w')
        if filtro == 0.0:
            if TAR is False:
                filtro = FILTROSTOPLOSS[timming]
            else:
                filtro = 3.0
    elif timming == 'm':
        datoshistoricos = yahoofinance.subirtimming(historico, timming='m')
        if filtro == 0.0:
            if TAR is False:
                filtro = FILTROSTOPLOSS[timming]
            else:
                filtro = 2.5

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

    if desdefecha is not False and todohistorico is False:
        i = 0
        while i < len(datoshistoricos):
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = datoshistoricos[
                i]
            if fecha >= desdefecha:
                datoshistoricos = datoshistoricos[i:]
                break
            if i == (
                    len(datoshistoricos) - 1
            ) and fecha < desdefecha:  # Ha llegado al final de sin encontrar una fecha de analisis mayor a desdefecha
                datoshistoricos = []
            i += 1
        del fecha, _apertura, _maximo, _minimo, _cierre, _volumen
    i = 0

    if not (MME is False):
        puntosMME = indicador.MME(datoshistoricos, MME=MME)
        if not (MME2 is False):
            puntosMME2 = indicador.MME(datoshistoricos, MME=MME2)
    if not (TAR is False):
        puntosTAR = indicador.TAR(datoshistoricos, TAR=TAR)

    if not (ADX is False):
        puntosADX = indicador.ADX(datoshistoricos, ADX=ADX)
        puntosDI = indicador.DI(datoshistoricos, DI=ADX)

    while i < len(datoshistoricos):
        fecha, apertura, maximo, minimo, cierre, volumen = datoshistoricos[i]

        if i == 0:
            ant = 0
        else:
            ant = i - 1
        fechaanterior, _aperturaanterior, maximoanterior, _minimoanterior, cierreanterior, _volumenanterior = datoshistoricos[
            ant]
        _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[
            r]
        _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[
            s]

        if not (ADX is False):
            fechaADX, puntoADX = puntosADX[ant]
            fechaDI, puntoDIplus, puntoDIminus = puntosDI[ant]
            assert (fechaADX == fechaanterior or fechaDI == fechaanterior)
        else:
            puntoADX = False
            puntoDIplus = False
            puntoDIminus = False
        indicadores = (puntoADX, puntoDIplus, puntoDIminus)

        if not (TAR is False):
            fechaTAR, puntoTAR = puntosTAR[ant]

            assert (fechaTAR == fechaanterior)

            if len(analisisbajista) > 0 and stoploss > (round(
                (cierreanterior + (puntoTAR * filtro)), 3)):
                stoploss = round((cierreanterior + (puntoTAR * filtro)), 3)
                listastoploss.append((fecha, stoploss))

        if not (MME is False):  # and len( datoshistoricos ) >= MME:

            fechaMME, puntoMME = puntosMME[i]
            if not (MME2 is False):
                fechaMME2, puntoMME2 = puntosMME2[i]
                assert (fechaMME == fecha and fechaMME == fechaMME2)

            assert (fechaMME == fecha)

            # if i >= ( MME - 1 ):# Empieza a utilizar el indicador.MME en una barra en concreto, para la MME30 lo utiliza apartir de la barra 30(cuyo indice es 29)
            if puntoMME > 0:
                if resistencia is False and soporte is False and puntoMME > maximo:  # Si no buscamos ni resistencias ni soportes y la grafica esta completamente por abajo de la MME, es porque estamos buscando soportes
                    s = i
                    _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[
                        s]
                    soporte = True
                    resistencia = False
                # if puntoMME < minimo:# Media Movil Exponencial bajo grafica, no buscamos soportes ni resistencias, y consideramos la barra actual como soporte
                elif puntoMME < minimo and (
                        MME2 is False or
                    (MME2 is not False and puntoMME2
                     <= puntoMME)):  # elif puntoMME2 <= puntoMME < minimo:
                    s = i
                    _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[
                        s]
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
                # TODO :  comprobar con un asser si el precioentradapuntoLT es igual al calculado con la siguiente funcion
                # entrada = puntocurvaexponencial(ltdateini, ltpriceini, ltdatefin, ltpricefin, timming, incremperiod=incremperiod)

                precioentradapuntoLT = round(
                    (maximoLTi *
                     ((1 + (((1.0 + (((maximoLTf - maximoLTi) / maximoLTi)))**
                             (12.0 /
                              (LTf - LTi))) - 1.0))**((i - LTi) / 12.0))), 3)

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
                    barraentradapuntoLT = (fecha, precioentradapuntoLT,
                                           precioentradapuntoLT,
                                           precioentradapuntoLT,
                                           precioentradapuntoLT, volumen)
                    analisisbajista.append(
                        (barraentradapuntoLT, (resistenciaanterior, stoploss),
                         (datoshistoricos[i], precionentrada),
                         LineaTendenciaInicio, LineaTendenciaFin,
                         salidaOperacion, timming, indicadores))
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
                soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisbajista[
                    i2]
                # salidaOperacionAnalisis=analisisalcista[i2][5]
                if salidaOperacionAnalisis is False:
                    analisisbajista[
                        i2] = soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                    # analisisalcista[i2][5]=datoshistoricos[i]
                i2 += 1
            entradapuntoLT = False

        if soporte and minimo < minimosoporte and not (
                maximo > maximoanterior and apertura > cierre
        ):  # No actualizamos el soporte, si esta es la misma barra que la crea y ademas la rompe con un movimiento de arriba hacia abajo, considerando como valida la resistencia anterior

            s = i
            _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[
                s]

        if soporte and maximo > maximoanterior:  # soporte consolidada
            resistencia = True
            soporte = False
            # volvemos al indice donde esta el soporte para comprobar desde ahi las posibles resistencias
            # comparamos que el movimiento viene de abajo hacia arriba, para asi considerar el maximo del soporte como interno en el movimiento y que en tal caso pueda ser la resistencia
            if aperturasoporte > cierresoporte and (i +
                                                    1) < len(datoshistoricos):
                # esto ultimo es porque puede que la ultima barra sea la resistencia, si le sumasemos uno nos saldriamos de rango
                i = s + 1
            else:
                i = s
            r = i
            _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[
                r]
            _fecha, apertura, maximo, minimo, cierre, _volumen = datoshistoricos[
                i]

    # resistencia bajista
        if resistencia and maximo > maximoresisten and not (
            (minimo < minimosoporte) and (apertura < cierre)
        ):  # if soporte and minimo<minimosoporte: # No actualizamos la resistencia, si es la misma barra que rompe el soporte y ademas la apertura es menor que el cierre
            r = i
            _fecharesisten, _aperturaresisten, maximoresisten, _minimoresisten, _cierreresisten, _volumenresisten = datoshistoricos[
                r]

        if resistencia and ((minimo < minimosoporte) or i == (
            (len(datoshistoricos)) - 1)) and not (
                (datoshistoricos[s] or datoshistoricos[r]) in analisisbajista):

            # if LT: # esto es porque hasta que no se produce un segundo soporte, no podemos calcular la linea de tendencia
            if s > 0:  # No podremos calcular LT si no hay barras fuerra del ciclo soporte y resistencia, por eso el soporte e inicio del ciclo tiene que ser mayor que 0
                localizaLTi = True
                localizaLTf = False
                LTi = s - 1

                LTf = r
                fechaLTf, _aperturaLTf, maximoLTf, _minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[
                    LTf]

                while localizaLTi:

                    if LTi >= 0:
                        fechaLTi, _aperturaLTi, maximoLTi, _minimoLTi, _cierreLTi, _volumenLTi = datoshistoricos[
                            LTi]
                    else:
                        localizaLTf = True
                        localizaLTi = False
                        break

                        #print LTi
                    for j in range(LTi, -1, -1):
                        fechaj, _aperturaj, maximoj, _minimoj, _cierrej, _volumenj = datoshistoricos[
                            j]
                        # logging.debug(f"Iteración {j}: Valores de entrada: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}")

                        if (
                                maximoLTi < maximoLTf or maximoLTi == 0.0
                        ) and LTi > 0:  # como estoy en bajista, si el maximoLTi es menor que el maximoLTf es porque esta por debajo, asi que muevo el punto LTi una barra menos, en busca del un LTi que este por encima del LTf
                            LTi -= 1
                            break

                        try:
                            # Realizamos el cálculo de puntoLT
                            puntoLT = (maximoLTi * ((1 + (
                                ((1.0 +
                                  (((maximoLTf - maximoLTi) / maximoLTi)))**
                                 (12.0 /
                                  (LTf - LTi))) - 1.0))**((j - LTi) / 12.0)))

                            # Comprobamos si puntoLT es un número complejo
                            if isinstance(puntoLT, complex):
                                logging.debug(
                                    f"Se detectó un número complejo en el cálculo de puntoLT. Buscando LTi; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                # Aplicamos abs() para obtener el valor absoluto, si es necesario, o usamos solo la parte real
                                puntoLT = abs(puntoLT) if abs(
                                    puntoLT.imag) > 0 else puntoLT.real

                            # Verificamos si puntoLT es infinito o NaN antes de redondearlo
                            if not math.isfinite(puntoLT):
                                logging.debug(
                                    f"Valor no finito detectado en puntoLT, asignando valor de fallback.Buscando LTi; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                puntoLT = maximoj  # Valor de fallback

                            # Redondeamos puntoLT solo si no es complejo
                            puntoLT = round(puntoLT, 3)

                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug(
                                f"Error en cálculo: {e}. Buscando LTi; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )

                            # En caso de error, asignamos maximoj a puntoLT como valor de fallback
                            puntoLT = maximoj
                            j = 0  # Reinicio de j para evitar bucles infinitos si no se controla correctamente

                        except TypeError as e:
                            logging.debug(
                                f"TypeError en el cálculo de puntoLT, se aplicará abs(): Error en cálculo: {e}. Buscando LTi; Accion: {naccion}. Timming: {timming}. FechaLTi: {fechaLTi}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )
                            # Aplicamos abs() y recalculamos puntoLT
                            puntoLT = round(
                                abs(maximoLTi * ((1 + ((
                                    (1.0 +
                                     (((maximoLTf - maximoLTi) / maximoLTi)))**
                                    (12.0 / (LTf - LTi))) - 1.0))**(
                                        (j - LTi) / 12.0))), 3)

                        # Control adicional para evitar bucles infinitos debido a la precisión en el cálculo de puntoLT
                        if puntoLT > maximoj:
                            LTi = j
                            break

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
                    # print "LTf, i =", LTf, i
                    if LTf <= i:
                        _fechaLTf, _aperturaLTf, maximoLTf, _minimoLTf, _cierreLTf, _volumenLTf = datoshistoricos[
                            LTf]
                    else:
                        localizaLTf = False
                        localizaLTi = False
                        break
    #                print "LTf, i =", LTf, i
    #                while j<=i:
                    for j in range(LTf, i + 1):

                        _fechaj, _aperturaj, maximoj, _minimoj, _cierrej, _volumenj = datoshistoricos[
                            j]

                        # esto lo he anadido porque se me ha dado el caso de que cuando en los primeros ciclos alcistas, si estan demasiado proximos al inicio del historico de la accion, me toma como el mismo punto el punto de LTi y LTf
                        if LTf == LTi:
                            LTf += 1
                            break
                        try:
                            # Realizamos el cálculo de puntoLT
                            puntoLT = (maximoLTi * ((1 + (
                                ((1.0 +
                                  (((maximoLTf - maximoLTi) / maximoLTi)))**
                                 (12.0 /
                                  (LTf - LTi))) - 1.0))**((j - LTi) / 12.0)))

                            # Comprobamos si puntoLT es un número complejo
                            if isinstance(puntoLT, complex):
                                logging.debug(
                                    f"Se detectó un número complejo en el cálculo de puntoLT. Buscando LTf; Accion: {naccion}. Timming: {timming}. FechaLTf: {fechaLTf}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                # Aplicamos abs() para obtener el valor absoluto, si es necesario, o usamos solo la parte real
                                puntoLT = abs(puntoLT) if abs(
                                    puntoLT.imag) > 0 else puntoLT.real

                            # Verificamos si puntoLT es infinito o NaN antes de redondearlo
                            if not math.isfinite(puntoLT):
                                logging.debug(
                                    f"Valor no finito detectado en puntoLT, asignando valor de fallback.Buscando LTf; Accion: {naccion}. Timming: {timming}. FechaLTf: {fechaLTf}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                                )
                                puntoLT = maximoj  # Valor de fallback

                            # Redondeamos puntoLT solo si no es complejo
                            puntoLT = round(puntoLT, 3)

                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug(
                                f"Error en cálculo: {e}. Buscando LTf; Accion: {naccion}. Timming: {timming}. FechaLTf: {fechaLTf}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )
                            # En caso de error, asignamos maximoj a puntoLT como valor de fallback, pero no alteramos LTf
                            puntoLT = maximoj

                        except TypeError as e:
                            logging.debug(
                                f"TypeError en el cálculo de puntoLT, se aplicará abs(): Error en cálculo: {e}. Buscando LTf; Accion: {naccion}. Timming: {timming}. FechaLTf: {fechaLTf}. Fecha barra del Error: {fechaj}. Valores: maximoLTi={maximoLTi}, maximoLTf={maximoLTf}, LTf={LTf}, LTi={LTi}, j={j}"
                            )
                            # Aplicamos abs() y recalculamos puntoLT
                            puntoLT = round(
                                abs(maximoLTi * ((1 + ((
                                    (1.0 +
                                     (((maximoLTf - maximoLTi) / maximoLTi)))**
                                    (12.0 / (LTf - LTi))) - 1.0))**(
                                        (j - LTi) / 12.0))), 3)

                        if puntoLT < maximoj:
                            if (LTf == j or (puntoLT == 0.0
                                             and LTf < i)) and not (j + 1 > i):
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

                LineaTendenciaInicio = (datoshistoricos[LTi][0],
                                        datoshistoricos[LTi][2])
                LineaTendenciaFin = (datoshistoricos[LTf][0],
                                     datoshistoricos[LTf][2])

                # if not LT:
                if not (datoshistoricos[LTi][2] > datoshistoricos[LTf][2]):
                    LineaTendenciaInicio = ('0-0-0', 0.0)
                    LineaTendenciaFin = ('0-0-0', 0.0)
            else:
                LineaTendenciaInicio = ('0-0-0', 0.0)
                LineaTendenciaFin = ('0-0-0', 0.0)

            if TAR is False:
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

            analisisbajista.append(
                (datoshistoricos[s], (datoshistoricos[r], stoploss),
                 (datoshistoricos[i], precionentrada), LineaTendenciaInicio,
                 LineaTendenciaFin, salidaOperacion, timming, indicadores))

            if conEntradaLT:
                entradapuntoLT = True

            # Si la misma barra que rompe el soporte abre abajo para cerrar por arriba del stoploss, esa barra nos saca del mercado
            if maximo >= stoploss and cierre > apertura and len(
                    analisisbajista) > 0:

                # if maximo >= stoploss >= minimo:# El stoploss esta entre el maximo y el minimo
                salidaoperaciones = (fecha, stoploss)
                # elif minimo > stoploss:# El stoploss esta por debajo del minimo, lo que significa que puede haber un split
                #    salidaoperaciones = ( fecha, minimo )

                i2 = 0
                while i2 < len(analisisbajista):
                    soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaOperacionAnalisis, timmingAnalisis, indicesAnalisis = analisisbajista[
                        i2]
                    # salidaOperacionAnalisis=analisisalcista[i2][5]
                    if salidaOperacionAnalisis is False:
                        analisisbajista[
                            i2] = soporteAnalisis, resistenciaAnalisis, rupturaAnalisis, LTInicioAnalisis, LTFinAnalisis, salidaoperaciones, timmingAnalisis, indicesAnalisis
                        # analisisalcista[i2][5]=datoshistoricos[i]
                    i2 += 1
            s = i  # como la ultima barra que ha roto la resistencia es mas alta que la resistencia, la considero como nueva resistencia
            _fechasoporte, aperturasoporte, _maximosoporte, minimosoporte, cierresoporte, _volumensoporte = datoshistoricos[
                s]
            #            if i<> len (datoshistoricos)-1:# esto esta porque si hemos llegado al final del analisis de los datos historicos, hacemos el analisis como si hubiese roto la resistencia, y ya no nos interesa volver atras una barra, ya que esto no meteria en un bucle infinito
            #            if i<len (datoshistoricos)-1 and (minimo < minimoanterior and apertura>cierre):# esto esta porque si hemos llegado al final del analisis de los datos historicos, hacemos el analisis como si hubiese roto la resistencia, y ya no nos interesa volver atras una barra, ya que esto no meteria en un bucle infinito
            #            if i<len (datoshistoricos)-1 and apertura>cierre:
            #                i-=1 # vuelvo un dato atras porque es posible que la misma barra que rompe la resistencia lo sea en el siguiente ciclo, y asi comparo si el maximo de esa barra es el mayor dejado hasta el momento
            # print resitenciaalcista

            resistencia = False
            soporte = True

        i += 1

    if desdefecha is not False and todohistorico is True:
        i = 0
        while i < len(analisisbajista):
            soporte, resistencia, ruptura, LTi, LTf, salida, timming, indicadores = analisisbajista[
                i]
            fecha, _apertura, _maximo, _minimo, _cierre, _volumen = soporte
            if fecha >= desdefecha:
                analisisbajista = analisisbajista[i:]
                break
            if i == (
                    len(analisisbajista) - 1
            ) and fecha < desdefecha:  # Ha llegado al final de analisisbajista sin encontrar una fecha de analisis mayor a desdefecha
                analisisbajista = []
            i += 1
        del resistencia, soporte, ruptura, LTi, LTf, salida, fecha, _apertura, _maximo, _minimo, _cierre, _volumen

    # grabaDatos(naccion,datoshistoricos,correcciones,cotizaciones,analisis,analisisbajista,analisisbajista)

    if len(analisisbajista) > 0 and txt:
        tickets = BBDD.ticketlistacodigo(naccion)
        nombre = (str(naccion) + str(tickets[naccion])).replace('.', '_')
        archivo = os.path.join(os.getcwd(), CARPETAS["Analisis"],
                               nombre + "." + timming + ".analisisbajista.txt")
        j = open(archivo, "w")
        j.write(str(config) + os.linesep)
        for n in analisisbajista:
            # ~ j.write(str(n)+os.linesep)
            soporte, resistencia, ruptura, LTi, LTf, salida, timming, indicadores = n
            j.write("Soporte     " + str(soporte) + os.linesep)
            j.write("Resistencia " + str(resistencia) + os.linesep)
            j.write("Ruptura     " + str(ruptura) + os.linesep)
            j.write("LT Inicio   " + str(LTi) + os.linesep)
            j.write("LT Final    " + str(LTf) + os.linesep)
            j.write("Salida      " + str(salida) + os.linesep)
            j.write("Timming     " + str(timming) + os.linesep)
            j.write("Indicadores ADX, DI+, DI- " + str(indicadores) +
                    os.linesep)
            j.write(os.linesep)

        for n in range(5):
            j.write(os.linesep)

        for n in listastoploss:
            j.write(str(n) + os.linesep)

        j.close()

    # formato de salida, ultimo analisis alcista, soporte anterior, todo el analisis alcista
    # hay que anadir cuando el len de analisisbajista sea mayor que 2, para cada analisis alcista hay un soporte que es el precio de salida en Lt para este.
    if len(
            analisisbajista
    ) == 1:  # esto esta porque puede que en el analisisbajista en el timming actual no produzca resultado al no existir resistencia alcista en el timming actual
        return ((analisisbajista[-1]), 0, analisisbajista)
    elif len(analisisbajista) > 1:
        # TODO:  es posible que haya que cambiar analisisbajista[-2][1][1] por analisisbajista[-2][1][0][2]
        return ((analisisbajista[-1]), (analisisbajista[-2][1][0][2]),
                analisisbajista
                )  # [-2][1][1]=penultimo analisis, resistencia, stoploss
    else:
        # habria que comprobar un timming inferirior al obtener como resultado 0
        return None


def creaMenu(sep, lmenu, cola=True):
    """
    Crea un menu de opciones.


    Le damos el separador de la opcion y una lista con las opciones del menu,
    nos devuelve una lista de tuplas con la cola de opciones y descripciones elegidas,
    anade al final de la lista una tupla mas que contiene (None,None)

    """
    control = []
    respdescp = []

    for n in lmenu:
        print(n)
        control.append(n[0:n.find(sep)].lower())

    while True:
        # print (sys.argv)
        if len(sys.argv) == 1:
            resp = (input('Opcion?').lower()).strip()
        else:
            resp = sys.argv.pop(1)
            print(('Automatico, opciones: %s ' % resp))
            # sys.argv.pop() # = ['./Cobo.py']

        if len(resp) == 1:
            if resp in control:
                descp = lmenu[control.index(resp)]
                respdescp = [
                    (resp, descp),
                ]
                break
        elif len(resp) > 1:
            for n in resp:
                if n in control:
                    respdescp.append((n, lmenu[control.index(n)]))
            break

    respdescp.append((None, None))

    if cola is False:
        respdescp = respdescp[0]

    return (respdescp)


def historicoTicket(nombreticket, **config):
    """."""
    correcto = True
    borranoactualizados = config.get('borranoactualizados', False)
    if not BBDD.datoshistoricosexisten(nombreticket):
        print(
            ('Ticket %s nuevo, descarga completa del historico de la accion' %
             nombreticket))
        #        for timmingdescargado in 'dwm':
        accioninvalida = yahoofinance.descargaHistoricoAccion(nombreticket,
                                                              timming='d',
                                                              txt=False)
        yahoofinance.duerme()
        if accioninvalida == 'URL invalida':
            BBDD.ticketborra(nombreticket)
            correcto = False

    else:
        print((
            'Ticket %s ya descargado, comprobando la actualizacion de los datos'
            % nombreticket))
        # for timmingdescargado in 'dwm':

        fechaactualizar, actualizaractualizar = BBDD.datoshistoricosactualizacion(
            nombreticket)

        if actualizaractualizar:  # and (desdefechamodificacionarchivo(datosaccion)):

            accioninvalida = yahoofinance.descargaHistoricoAccion(
                nombreticket,
                fechaini=fechaactualizar,
                timming='d',
                actualizar=actualizaractualizar,
                txt=False)
            yahoofinance.duerme()

            if accioninvalida == 'Pago Dividendos':
                BBDD.ticketborra(nombreticket, BBDD=False)
                print(
                    'Reintento de la descarga, el error puede venir de un pago de Dividendos'
                )
                accioninvalida = yahoofinance.descargaHistoricoAccion(
                    nombreticket, timming='d', txt=False)
                yahoofinance.duerme()
                # despues de haber actualizado, volvemos a comprobarlo, si se da que si, la accion dejo de cotizar hace mucho.
                # existe un caso especifico que es cuando comprobamos la actualizacion de datos de una accion y esta tiene menos de 3 periodos en el timming en que estemos trabajando, la funcion actualizacionDatosHisAccion la trata de forma especial, devolviendo (None, timming, True), para que con estos parametros la funcion descargaHistoricosAccion descarge todo el historico otra vez
                # por esta razon en el siguiente if comprobamos con fechaactualizar2!=None que no sea este caso.
                # FIXME : al hacer la comprobacion en mensual, casi siempre me da que no ha actualizado correctamente, ejemplo EGL.SW
                fechaactualizar2, actualizaractualizar2 = BBDD.datoshistoricosactualizacion(
                    nombreticket)
                if fechaactualizar2 is not None and actualizaractualizar == actualizaractualizar2 and fechaactualizar == fechaactualizar2:
                    fechahoy = ((date.today().timetuple()))
                    fechaactualizar2 = list(
                        map(int, ((fechaactualizar2).split('-'))))
                    desdeultimaactualizacion = (
                        date(fechahoy[0], fechahoy[1], fechahoy[2]) -
                        date(fechaactualizar2[0], fechaactualizar2[1],
                             fechaactualizar2[2])).days

                    if borranoactualizados and desdeultimaactualizacion > DIFREGACTUALIZAR[
                            'noActualizados']:
                        accioninvalida = 'URL invalida'
                        BBDD.ticketborra(nombreticket)
                    else:
                        print(
                            'No se ha actualizado correctamente. Funcion de borrado para estos casos deshabilitada'
                        )
                        BBDD.ticketerror(nombreticket)

            elif accioninvalida == 'URL invalida':
                BBDD.ticketborra(nombreticket)
                correcto = False
    return correcto


def analisisTicket(nombreticket):
    """."""
    cursor, db = BBDD.conexion()
    # nombreticket = (nombreticket.upper(),)
    # cursor.execute("SELECT * FROM `Cobo_componentes` WHERE `Cobo_componentes`.`tiket` = ?", nombreticket)
    # registro = cursor.fetchall()
    # # resultado=(28141L, 'LVL MEDICAL GROUP', '-LVL.NX', 'ENX', 18.4, 14.89, 12.46, 14.56, 14.89, 12396.0, 7371.0, 'N/A', datetime.date(2011, 2, 24)
    # FIXME: codigo, _nombre, ticket, _mercado, _max52, maxDia, _min52, minDia, valorActual, _volumenMedio, _volumen, _error, _fechaRegistro = BBDD.ticketobtencotizacion(nombreticket)
    # IndexError: list index out of range
    codigo, _nombre, ticket, _mercado, _max52, maxDia, _min52, minDia, valorActual, _volumenMedio, _volumen, _error, _fechaRegistro = BBDD.ticketobtencotizacion(
        nombreticket)
    proximidadalcista, proximidadbajista = 0, 0
    if BBDD.datoshistoricosexisten(ticket):

        # al final si utilizamos indicador.MME, el indicador.MME sera la decision de si es alcista o bajista
        for timminganalisis in 'mwd':
            print(('Timming del analisis alcista: %s' % timminganalisis))
            analisisalcista = analisisAlcistaAccion(
                ticket,
                timming=timminganalisis,
                conEntradaLT=False,
                txt=False,
                filtro=FILTROSTOPLOSS[timminganalisis])
            if analisisalcista is not None:
                alcista, soporteanterioralcista, _analisisalcistatotal = analisisalcista
                resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
                soporte, stoploss = soporte
                ruptura, entrada = ruptura
                # evitando que la division de mas abajo sea por 0
                if ruptura[4] == 0.0:
                    cierreruptura = 0.0001
                else:
                    cierreruptura = ruptura[4]
                if maxDia is None or maxDia == 0.0:
                    maxDia = cierreruptura
                if valorActual is None or valorActual == 0.0:
                    valorActual = cierreruptura
                # except ZeroDivisionError:
                proximidadalcista = (abs((
                    resistencia[2] / max(cierreruptura, maxDia, valorActual)) -
                                         1))
                #                            for precio in (ruptura[4], maxDia, valorActual):
                #                                proximidadalcista.append(abs((resistencia[2] / precio) - 1))
                #                            proximidadalcista = min(proximidadalcista)
                break

        for timminganalisis in 'mwd':
            print(('Timming del analisis bajista: %s' % timminganalisis))
            analisisbajista = analisisBajistaAccion(
                ticket,
                timming=timminganalisis,
                conEntradaLT=False,
                txt=False,
                filtro=FILTROSTOPLOSS[timminganalisis])
            if analisisbajista is not None:
                bajista, soporteanteriorbajista, _analisisbajistatotal = analisisbajista
                soporte, resistencia, ruptura, LTi, LTf, _salida, timming, _indices = bajista
                resistencia, stoploss = resistencia
                ruptura, entrada = ruptura
                # evitando que la division de mas abajo sea por 0
                if ruptura[4] == 0.0:
                    cierreruptura = 0.0001
                else:
                    cierreruptura = ruptura[4]
                if minDia is None or minDia == 0.0:
                    minDia = cierreruptura
                if valorActual is None or valorActual == 0.0:
                    valorActual = cierreruptura
                # except ZeroDivisionError:
                proximidadbajista = (abs(1 - (
                    soporte[3] / min(cierreruptura, minDia, valorActual))))
                #                            for precio in (ruptura[4], minDia, valorActual):
                #                                proximidadbajista.append(abs(1 - (soporte[3] / precio)))
                #                            proximidadbajista = min(proximidadbajista)
                break
        # Existen ambos analisis, comparamos proximidada a ruptura
        # la minima proximidadbajista es mayor o igual a la proximidadalcista, alcista
        if analisisalcista is not None and analisisbajista is not None and proximidadbajista >= proximidadalcista:
            resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
            soporte, stoploss = soporte
            salida = soporte[3]
            ruptura, entrada = ruptura
            soporteanterior = soporteanterioralcista
        # la minima proximidadbajista es menor a la proximidadalcista, bajista
        elif analisisalcista is not None and analisisbajista is not None and proximidadbajista < proximidadalcista:
            soporte, resistencia, ruptura, LTi, LTf, _salida, timming, _indices = bajista
            resistencia, stoploss = resistencia
            salida = resistencia[3]
            ruptura, entrada = ruptura
            soporteanterior = soporteanteriorbajista
        # Uno de los analisis no existe, asignamos el contrario
        elif analisisalcista is None and analisisbajista is not None:
            soporte, resistencia, ruptura, LTi, LTf, _salida, timming, _indices = bajista
            resistencia, stoploss = resistencia
            salida = resistencia[3]
            ruptura, entrada = ruptura
            soporteanterior = soporteanteriorbajista
        elif analisisbajista is None and analisisalcista is not None:
            resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
            soporte, stoploss = soporte
            salida = soporte[3]
            ruptura, entrada = ruptura
            soporteanterior = soporteanterioralcista
        elif analisisbajista is None and analisisalcista is None:  # No existe analisis posible
            BBDD.ticketerror(ticket)
            return

        else:  # Por defecto lo consideramos alcista, aunque aqui deberia entrar solo en el caso se que no se de la 3 condicion del if anterior
            resistencia, soporte, ruptura, LTi, LTf, _salida, timming, _indices = alcista
            soporte, stoploss = soporte
            salida = soporte[3]
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
            rentabilidad = indicador.curvexprent(fechainicial, precioinicial,
                                                 fechafinal, preciofinal)

        # no nos interesan los datos almacenados de analisis anteriores
        # comprobamos que el analisis obtenido y que vamos a almacenar en la BBDD es o
        # alcista o bajista
        # comprobamos se es actual o esta obsoleto

        if ((entrada > stoploss) and
            # Alcista obsoleto, maximo52, maximo del dia, valoractual, precio de entrada (split) > Resitencia
            # ((max52 != 'NULL' and max52 > resistencia[2]) or\ # Eliminamos la comparacion con el max52week porque en ocasiones cuando se paga un dividendo o se produce un split, este valor tardan en ajustarlo a esos cambios y queda por encima del precio de entrada, provocando esta comparacion que algunos analisis no aparezcan
            ((maxDia != 'NULL' and maxDia > resistencia[2]) or
             (valorActual != 'NULL' and valorActual > resistencia[2]) or
             (entrada > resistencia[2])))\
           or\
           ((entrada < stoploss) and
            # Bajista obsoleto, minimo52, minimo del dia, valoractual, precio de entrada (split) < soporte
            # ((min52 != 'NULL' and min52 < soporte[3]) or\ # Eliminamos la comparacion con el min52week porque en ocasiones cuando se paga un dividendo o se produce un split, este valor tardan en ajustarlo a esos cambios y queda por debajo del precio de entrada, provocando esta comparacion que algunos analisis no aparezcan
            ((minDia != 'NULL' and minDia < soporte[3]) or
             (valorActual != 'NULL' and valorActual < soporte[3]) or
             (entrada < soporte[3]))):

            # si true, analisis ya cumplido, obsoleto y lo actualizamos
            if numeroResultado == 1:
                sql = "UPDATE `Cobo_params_operaciones` SET `precio_ini` = %.3f, `precio_fin` = %.3f, `fecha_ini` = '%s', `fecha_fin` = '%s', `salida` = NULL, `entrada` = NULL, `timing` = '%s', `precio_salida` = %.3f, `rentabilidad` = %.3f WHERE `Cobo_params_operaciones`.`codigo` = %s" % (
                    LTi[1], LTf[1], LTi[0], LTf[0], timming, salida,
                    rentabilidad, codigo)
            elif numeroResultado == 0:
                sql = "INSERT INTO `Cobo_params_operaciones` (id,precio_ini,precio_fin,fecha_ini,fecha_fin,salida,entrada,codigo,timing,precio_salida,rentabilidad) VALUES (NULL, %.3f, %.3f,'%s' ,'%s' , NULL, NULL, %d,'%s', %.3f, %.3f)" % (
                    LTi[1], LTf[1], LTi[0], LTf[0], codigo, timming, salida,
                    rentabilidad)

        # Alcista/Bajista Validos
        else:  # anali
            # si false, analisis valido, sin cumplir
            if numeroResultado == 1:
                sql = "UPDATE `Cobo_params_operaciones` SET `precio_ini` = %.3f, `precio_fin` = %.3f, `fecha_ini` = '%s', `fecha_fin` = '%s', `salida` = %.3f, `entrada` = %.3f, `timing` = '%s', `precio_salida` = %.3f, `rentabilidad` = %.3f WHERE `Cobo_params_operaciones`.`codigo` = %s" % (
                    LTi[1], LTf[1], LTi[0], LTf[0], salida, entrada, timming,
                    soporteanterior, rentabilidad, codigo)
            elif numeroResultado == 0:
                sql = "INSERT INTO `Cobo_params_operaciones` (id,precio_ini,precio_fin,fecha_ini,fecha_fin,salida,entrada,codigo,timing,precio_salida,rentabilidad) VALUES (NULL, %.3f, %.3f,'%s','%s',%.3f , %.3f, %d,'%s', %.3f, %.3f)" % (
                    LTi[1], LTf[1], LTi[0], LTf[0], salida, entrada, codigo,
                    timming, soporteanterior, rentabilidad)

        cursor.execute(sql)

    db.commit()
    db.close()


def backtestMoneda(**config):
    """."""
    backtest = []
    # TODO: posiblemente interese convertirlo en una variable, en consecuencia habria que restarle esta cantidad a todas las operaciones
    # al convertirlo en una variable, habria que restarle esta cantidad a todas las operaciones
    comision = config.get('comision', 25.0)
    estrategia = config.get('estrategia', 'Alcista')  # 'Alcista'/'Bajista'
    # fecha desde la que considelamos un analisis valido
    analizardesde = config.get(
        'analizardesde', False)  # False/ string ficha con formato YYYY-MM-DD
    # consideramos todo el historico en el analisis
    # si analizardesde contiene una fecha, todohistorico True consideraria una posible entrada desde aquella fecha analizando todo el historico
    #                                      todohistorico False analizaria desde esa fecha sin tener en cuenta lo anterior
    todohistorico = config.get('todohistorico', True)  # True/False
    if analizardesde is not False:
        analizardesde = (todohistorico, analizardesde)

    riesgo = config.get('riesgo', FILTROS['riesgo'])
    volumenminimo = config.get('volumenminimo', FILTROS['volumen'])
    filtrosalidamensual = config.get('filtrosalidamensual',
                                     FILTROSTOPLOSS['m'])
    filtrosalidasemanal = config.get('filtrosalidasemanal',
                                     FILTROSTOPLOSS['w'])
    filtrosalidadiario = config.get('filtrosalidadiario', FILTROSTOPLOSS['d'])
    rentabilidadminima = config.get('rentabilidadminima',
                                    FILTROS['rentMinima'])
    rentabilidad0 = config.get(
        'rentabilidad0', True
    )  # True/False Consideramos Rentabilidad 0 igual a la rentabilidad minima,
    inversionminima = config.get('inversionminima', FILTROS['invMinima'])
    inversionmaxima = config.get('inversionmaxima', False)  # False / entero

    MMediario = config.get('MMediario', False)
    MMesemanal = config.get('MMesemanal', False)
    MMemensual = config.get('MMemensual', False)
    MMe2diario = config.get('MMe2diario', False)
    MMe2semanal = config.get('MMe2semanal', False)
    MMe2mensual = config.get('MMe2mensual', False)

    TARmensual = config.get('TARmensual', False)
    TARsemanal = config.get('TARsemanal', False)
    TARdiario = config.get('TARdiario', False)

    ADXobjetivo = config.get('ADXobjetivo', False)
    ADXmensual = config.get('ADXmensual', False)
    ADXsemanal = config.get('ADXsemanal', False)
    ADXdiario = config.get('ADXdiario', False)

    EntradaLT = config.get('EntradaLT', False)

    opcionbacktest = config.get('opcionbacktest', '4')
    opcionesbacktest = {
        '1': '1) Todo Diario',
        '2': '2) Diario con transicion a Semanal',
        '3': '3) Todo Semanal',
        '4': '4) Semanal con transicion a Mensual',
        '5': '5) Todo Mensual',
        '6': '6) Diario con transicion a Semanal y Mensual'
    }
    seleccionbacktest = opcionesbacktest[opcionbacktest]
    # En el caso de hacer un solo ticket, comentar desde aqui hasta print 'Analizando ticket %s' % ticket incluido, desdentar desde este comentario hasta el siguiente parecedo
    # obtenemos la lista de las monedas
    moneda = config.get('moneda', 'E')
    cursor, db = BBDD.conexion()

    monedas = []
    cursor.execute("SELECT Cobo_monedas.codigo FROM Cobo_monedas")
    resultado = cursor.fetchall()
    for mon in resultado:
        monedas.append(mon[0])

    # Comprobamos si la moneda es una moneda
    if moneda in monedas:  # Si es una moneda, buscamos en la base de datos los componentes que pertenezcan a esa moneda
        sql = ("""SELECT * FROM Cobo_componentes
            WHERE Cobo_componentes.tiket NOT LIKE '^%'
            AND Cobo_componentes.error IS NULL
            AND Cobo_componentes.mercado IN
            (SELECT Cobo_mercado_moneda.nombreUrl
                FROM Cobo_mercado_moneda
                WHERE Cobo_mercado_moneda.abrevMoneda LIKE ?)
            AND Cobo_componentes.mercado not IN """ + str(MERCADOSEXCLUIDOS) +
               "ORDER BY Cobo_componentes.tiket ASC")

    else:  # Si no es una moneda comprobamos si es un mercado
        cursor.execute(
            "SELECT Cobo_mercado_moneda.nombreUrl FROM Cobo_mercado_moneda ORDER BY Cobo_mercado_moneda.nombreUrl ASC"
        )
        resultado = cursor.fetchall()
        monedas = []
        for mon in resultado:
            monedas.append(mon[0])
        if moneda in monedas:
            sql = ("""SELECT * FROM Cobo_componentes
                WHERE Cobo_componentes.tiket NOT LIKE '^%'
                AND Cobo_componentes.error IS NULL
                AND Cobo_componentes.mercado LIKE ?
                ORDER BY Cobo_componentes.tiket ASC""")

    cursor.execute(sql, (moneda, ))
    # consulta en la tabla componentes que pertenecen a los mercados de una moneda
    # sql = "SELECT * FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' and `Cobo_componentes`.`tiket` NOT LIKE '^%' and`Cobo_componentes`.`mercado` IN (SELECT `nombreUrl` FROM `Cobo_mercado_moneda` WHERE `abrevMoneda` LIKE '" + moneda + "') ORDER BY `Cobo_componentes`.`tiket` ASC"
    resultado = cursor.fetchall()
    cuentaatras = len(resultado)
    db.close()
    for registro in resultado:
        # resultado=(28141L, 'LVL MEDICAL GROUP', '-LVL.NX', 'ENX', 18.4, 14.89, 12.46, 14.56, 14.89, 12396.0, 7371.0, 'N/A', datetime.date(2011, 2, 24)
        _codigo, _nombre, ticket, mercado, _max52, _maxDia, _min52, _minDia, valorActual, _volumenMedio, volumen, _error, fechaRegistro = registro
        print(('Quedan por analizar un total de %d' % cuentaatras))
        print(('Analizando ticket %s' % ticket))

        diario = None
        semanal = None
        mensual = None

        if BBDD.datoshistoricosexisten(ticket):
            backtestaccion = []
            if estrategia == 'Alcista':
                if opcionbacktest == '1' or opcionbacktest == '2' or opcionbacktest == '6':
                    diario = analisisAlcistaAccion(ticket,
                                                   timming='d',
                                                   desdefecha=analizardesde,
                                                   MME=MMediario,
                                                   MME2=MMe2diario,
                                                   conEntradaLT=EntradaLT,
                                                   filtro=filtrosalidadiario,
                                                   TAR=TARdiario,
                                                   ADX=ADXdiario,
                                                   txt=True)
                if opcionbacktest == '2' or opcionbacktest == '3' or opcionbacktest == '4' or opcionbacktest == '6':
                    semanal = analisisAlcistaAccion(ticket,
                                                    timming='w',
                                                    desdefecha=analizardesde,
                                                    MME=MMesemanal,
                                                    MME2=MMe2semanal,
                                                    conEntradaLT=EntradaLT,
                                                    filtro=filtrosalidasemanal,
                                                    TAR=TARsemanal,
                                                    ADX=ADXsemanal,
                                                    txt=True)
                if opcionbacktest == '4' or opcionbacktest == '5' or opcionbacktest == '6':
                    mensual = analisisAlcistaAccion(ticket,
                                                    timming='m',
                                                    desdefecha=analizardesde,
                                                    MME=MMemensual,
                                                    MME2=MMe2mensual,
                                                    conEntradaLT=EntradaLT,
                                                    filtro=filtrosalidamensual,
                                                    TAR=TARmensual,
                                                    ADX=ADXmensual,
                                                    txt=True)
            elif estrategia == 'Bajista':
                if opcionbacktest == '1' or opcionbacktest == '2' or opcionbacktest == '6':
                    diario = analisisBajistaAccion(ticket,
                                                   timming='d',
                                                   desdefecha=analizardesde,
                                                   MME=MMediario,
                                                   MME2=MMe2diario,
                                                   conEntradaLT=EntradaLT,
                                                   filtro=filtrosalidadiario,
                                                   TAR=TARdiario,
                                                   ADX=ADXdiario,
                                                   txt=True)
                if opcionbacktest == '2' or opcionbacktest == '3' or opcionbacktest == '4' or opcionbacktest == '6':
                    semanal = analisisBajistaAccion(ticket,
                                                    timming='w',
                                                    desdefecha=analizardesde,
                                                    MME=MMesemanal,
                                                    MME2=MMe2semanal,
                                                    conEntradaLT=EntradaLT,
                                                    filtro=filtrosalidasemanal,
                                                    TAR=TARsemanal,
                                                    ADX=ADXsemanal,
                                                    txt=True)
                if opcionbacktest == '4' or opcionbacktest == '5' or opcionbacktest == '6':
                    mensual = analisisBajistaAccion(ticket,
                                                    timming='m',
                                                    desdefecha=analizardesde,
                                                    MME=MMemensual,
                                                    MME2=MMe2mensual,
                                                    conEntradaLT=EntradaLT,
                                                    filtro=filtrosalidamensual,
                                                    TAR=TARmensual,
                                                    ADX=ADXmensual,
                                                    txt=True)

            # fecharesistenciadiario = 0
            # fecharesistenciasemanal = 0

            if diario is not None:
                diario = diario[2]
                fechasentradasdiario = ([
                    operacion[0][0] for operacion in diario
                ])
                i2 = len(
                    diario
                )  # por si alcistamensual==None, tenemos que asignarle todo el historico de semanal a backtestaccion
            else:
                i2 = 0
                diario = []

# puede que no exista o analisis semanal o mensual, en estos casos hay que darle algun valor a esos casos para que backtest sea coherente
            if semanal is not None:
                semanal = semanal[2]
                fechasentradassemanal = ([
                    operacion[0][0] for operacion in semanal
                ])
                fecha1entradasemanal = semanal[0][0][0]
                i = len(
                    semanal
                )  # por si alcistamensual==None, tenemos que asignarle todo el historico de semanal a backtestaccion

                if not diario == []:
                    i2 = 0
                    while i2 < len(fechasentradasdiario):
                        if fecha1entradasemanal <= fechasentradasdiario[i2]:
                            break
                        i2 += 1
            else:
                i = 0
                semanal = []

            if mensual is not None:
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
            while p < len(backtestaccion):  # for operacion in backtestaccion:

                if estrategia == 'Alcista':
                    resistencia, soporte, ruptura, LTi, LTf, salida, timming, indicadores = backtestaccion[
                        p]
                    soporte, stoploss = soporte
                    ruptura, precionentrada = ruptura
                elif estrategia == 'Bajista':
                    soporte, resistencia, ruptura, LTi, LTf, salida, timming, indicadores = backtestaccion[
                        p]
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
                    fechainicial = list(map(int, (fechainicial.split('-'))))
                    fechafinal = list(map(int, (fechafinal.split('-'))))
                    diffechas = (
                        date(fechafinal[0], fechafinal[1], fechafinal[2]) -
                        date(fechainicial[0], fechainicial[1],
                             fechainicial[2])).days

                    if estrategia == 'Alcista':
                        if precioinicial == 0.0:
                            precioinicial = 0.01
                        try:
                            rentabilidad = ((((1 + (
                                (preciofinal - precioinicial) / precioinicial))
                                              **(365.0 / diffechas)) - 1.0) *
                                            100.0) / 100.0
                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug(
                                'Error: %s calculando Rentabilidad Backtest; Accion: %s; timming: %s; FechaLTi: %s; PrecioLTi %s; FechaLTf: %s; PrecioLTf %s'
                                % (e, ticket.encode('UTF-8'), timming,
                                   fechainicial, precioinicial, fechafinal,
                                   preciofinal))
                            if rentabilidad0:
                                rentabilidad = rentabilidadminima
                            else:
                                rentabilidad = 0.00

                    elif estrategia == 'Bajista':
                        if preciofinal == 0.0:
                            preciofinal = 0.01
                        try:
                            rentabilidad = ((((1 + (
                                (precioinicial - preciofinal) / preciofinal))**
                                              (365.0 / diffechas)) - 1.0) *
                                            100.0) / 100.0
                        except (OverflowError, ZeroDivisionError) as e:
                            logging.debug(
                                'Error: %s calculando Rentabilidad Backtest; Accion: %s; timming: %s; FechaLTi: %s; PrecioLTi %s; FechaLTf: %s; PrecioLTf %s'
                                % (e, ticket.encode('UTF-8'), timming,
                                   fechainicial, precioinicial, fechafinal,
                                   preciofinal))
                            if rentabilidad0:
                                rentabilidad = rentabilidadminima
                            else:
                                rentabilidad = 0.00

                # calculamos el volumen
                volumenoperacion = 0
                #                        for barra in resistencia, soporte, ruptura:
                #                            if len(barra) == 2:
                #                                barra, _barra2 = barra
                #                            fecha, apertura, maximo, minimo, cierre, volumen = barra
                #                            volumenoperacion = (cierre * volumen * 22) + volumenoperacion
                #                        volumenoperacion = int (volumenoperacion / 3)
                # Como utilizamos la MME (5) sobre el volumen, solo comprobamos el volumen de la barra de ruptura
                _fecha, _apertura, _maximo, _minimo, cierre, volumen = ruptura

                volumenoperacion = int((cierre * volumen * 22))

                if (resistencia[2] == stoploss) or (
                        soporte[3]
                        == stoploss):  # comprobamos que no dividomos entre 0
                    numeroacciones = 0
                else:
                    # las siguientes comprobaciones son necesarias, porque nosotros ponemos la orden para la ruptura y calculamos el numero de acciones en relacion a ello
                    # pero eso no quiere decir que se ejecute al precionentrada
                    if estrategia == 'Alcista':
                        numeroacciones = int(riesgo /
                                             (resistencia[2] - stoploss))
                    elif estrategia == 'Bajista':
                        numeroacciones = int(riesgo / (soporte[3] - stoploss))

                # inversion moneda
                if estrategia == 'Alcista':
                    inversion = numeroacciones * resistencia[2]
                elif estrategia == 'Bajista':
                    inversion = numeroacciones * soporte[3]

                if not (inversionmaxima
                        is False) and abs(inversion) > inversionmaxima:
                    if estrategia == 'Alcista':
                        numeroacciones = int(inversionmaxima / resistencia[2])
                        inversion = numeroacciones * resistencia[2]
                    elif estrategia == 'Bajista':
                        # la inversion maxima es en negativo, arriba comparamos el valor absoluto pero en el numero de acciones tiene que ser negativo
                        numeroacciones = (int(
                            inversionmaxima / soporte[3])) * (-1)
                        inversion = numeroacciones * soporte[3]

                if invertido is False and \
                    rentabilidad >= rentabilidadminima and \
                    volumenoperacion >= volumenminimo and \
                    abs(inversion) >= inversionminima and \
                    (puntoADX is False or puntoADX == 0.0 or puntoADX >= ADXobjetivo) and \
                    ((puntoDIplus is False and puntoDIminus is False) or
                     (estrategia == 'Alcista' and puntoDIplus >= puntoDIminus) or
                     (estrategia == 'Bajista' and puntoDIminus >= puntoDIplus)):

                    if salida is False:  # analisis de que no hay salida, le asignamos la fecha y cotizacion actual
                        fechasalida = str(fechaRegistro)
                        # Se da el caso que el historico o el ajuste del mismo no esta actualizado y la cotizacion si, de manera que si el analisis no nos ha dado salida y al buscar un precio de salida
                        # Si somo alcistas o bajista y no nos ha salta el stoploss con el valor actual, al precio de salida le asignamos el valor actual
                        if (estrategia == 'Alcista' and stoploss
                                <= valorActual) or (estrategia == 'Bajista' and
                                                    stoploss >= valorActual):
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
                    #                    _soporteentrada = soporte[3]
                    #                    _resistenciaentrada = resistencia[2]
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

                elif invertido is True:

                    fecharuptura = ruptura[0]
                    # fecharesistencia = resistencia[0]
                    if timmingtransicion != timming and fechasalida > fecharuptura:
                        # Si hay transicion y Si la fecha de salida es posteior al de ruptura, actualizamos en nuevo precio de salida y la fecha, en los casos de las transiciones esto indipensable para que el precio de salida se adapte a los cambios de timming
                        timmingtransicion = timming  # Actualizamos el nuevo timmng de transiciones

                        if salida is False:  # analisis de que no hay salida, le asignamos la fecha y cotizacion actual
                            fechasalida = str(fechaRegistro)
                            # Se da el caso que el historico o el ajuste del mismo no esta actualizado y la cotizacion si, de manera que si el analisis no nos ha dado salida y al buscar un precio de salida
                            # Si somo alcistas o bajista y no nos ha salta el stoploss con el valor actual, al precio de salida le asignamos el valor actual
                            if (estrategia == 'Alcista'
                                    and stoploss < valorActual) or (
                                        estrategia == 'Bajista'
                                        and stoploss > valorActual):
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
                        # if -(riesgo) * BACKTESTOPERACIONESSOSPECHOSAS > balance:
                        #     if estrategia == 'Alcista':
                        #         print('ticket  fechaentrada  precionentrada  soporte  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
                        #         print(('%6s %13s %15.3f %8.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, soporteentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))

                        #     elif estrategia == 'Bajista':
                        #         print('ticket  fechaentrada  precionentrada  resistencia  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
                        #         print(('%6s %13s %15.3f %12.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, resistenciaentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))
                        #         #print ( '   %s,           %s,           %.3f,    %.3f,             %s,                      %d,          %s,         %.3f,      %s,               %.3f,                %.3f,    %.3f' % ( ticket, fechaentrada, precionentrada, ( soporte[3] ), timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance ) )

                        #     input('Operacion Dudosa, compruebala y pulsa una tecla')
                        if fechasalida != fecharuptura:  # Eliminada la posibilidad porque en el caso de que fechasalida == fecharuptura sea en una LT, nos saca y volvemos a entrar en la LT
                            p -= 1  # Puede que el ciclo que me saca, no impida que vuelva a entrar
                        # almaceno aqui la informacion del backtes porque puede que entre en un timming pero salga en otro

                        fechainicial = list(map(int,
                                                (fechaentrada.split('-'))))
                        fechafinal = list(map(int, (fechasalida.split('-'))))
                        diffechas = (
                            date(fechafinal[0], fechafinal[1], fechafinal[2]) -
                            date(fechainicial[0], fechainicial[1],
                                 fechainicial[2])).days
                        if estrategia == 'Alcista':
                            try:
                                rentabilidadoperacion = ((((1 + (
                                    (inversionrecuperada - inversionoperacion)
                                    / inversionoperacion))**(
                                        365.0 / diffechas)) - 1.0) * 100.0)
                            except (OverflowError, ZeroDivisionError) as e:
                                logging.debug(
                                    'Error: %s calculando Rentabilidad Backtest; Accion: %s; timming: %s; FechaLTi: %s; PrecioLTi %s; FechaLTf: %s; PrecioLTf %s'
                                    % (e, ticket.encode('UTF-8'), timming,
                                       fechainicial, precioinicial, fechafinal,
                                       preciofinal))
                                rentabilidadoperacion = 0.00

                        elif estrategia == 'Bajista':
                            try:
                                rentabilidadoperacion = ((((1 + (
                                    (inversionoperacion - inversionrecuperada)
                                    / inversionrecuperada))**(
                                        365.0 / diffechas)) - 1.0) * 100.0)
                            except (OverflowError, ZeroDivisionError) as e:
                                logging.debug(
                                    'Error: %s calculando Rentabilidad Backtest; Accion: %s; timming: %s; FechaLTi: %s; PrecioLTi %s; FechaLTf: %s; PrecioLTf %s'
                                    % (e, ticket.encode('UTF-8'), timming,
                                       fechainicial, precioinicial, fechafinal,
                                       preciofinal))
                                rentabilidadoperacion = 0.00

                        backtest.append(
                            (ticket, mercado, fechaentrada, precionentrada2,
                             timmingentrada, numeroaccionesoperacion,
                             fechasalida, preciosalida, timmingtransicion,
                             inversionoperacion, inversionrecuperada, balance,
                             rentabilidadoperacion, indicadoresentrada))
                        invertido = False

                p += 1

            # si me ha sacado invertido en la ultima analisis
            if invertido is True:
                # if ( resistencia[2] <= ruptura[2] ) or ( salida is False ):#si en el ultimo analisis no hay un soporte consolidado, porque no esta rota la resistencia o no hay salida del la accion
                #  (resistencia[2]> ruptura[2])
                # realmente no nos hemos salido de la operacion pero como no sabemos si nos sacara o no, valoramos la operacion a lo que valdria en ese momento
                # fechasalida=ruptura[0]
                #                            if -(riesgo) * BACKTESTOPERACIONESSOSPECHOSAS > balance:
                #                                if estrategia == 'Alcista':
                #                                    print('ticket  fechaentrada  precionentrada  soporte  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
                #                                    print(('%6s %13s %15.3f %8.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, soporteentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))
                #
                #                                elif estrategia == 'Bajista':
                #                                    print('ticket  fechaentrada  precionentrada  resistencia  timmingentrada  numeroaccionesoperacion  fechasalida  preciosalida  timming  inversionoperacion  inversionrecuperada  balance')
                #                                    print(('%6s %13s %15.3f %12.3f %15s %24d %12s %13.3f %8s %19.3f %20.3f %8.3f' % (ticket, fechaentrada, precionentrada, resistenciaentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance)))
                #                                    #print ( '   %s,           %s,           %.3f,    %.3f,             %s,                      %d,          %s,         %.3f,      %s,               %.3f,                %.3f,    %.3f' % ( ticket, fechaentrada, precionentrada, ( soporte[3] ), timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversionoperacion, inversionrecuperada, balance ) )
                #
                #                                input('Operacion Dudosa, compruebala y pulsa una tecla')
                fechainicial = list(map(int, (fechaentrada.split('-'))))
                fechafinal = list(map(int, (fechasalida.split('-'))))
                diffechas = (
                    date(fechafinal[0], fechafinal[1], fechafinal[2]) -
                    date(fechainicial[0], fechainicial[1],
                         fechainicial[2])).days
                if estrategia == 'Alcista':
                    try:
                        rentabilidadoperacion = ((((1 + (
                            (inversionrecuperada - inversionoperacion) /
                            inversionoperacion))**(365.0 / diffechas)) - 1.0) *
                                                 100.0)
                    except (OverflowError, ZeroDivisionError) as e:
                        logging.debug(
                            'Error: %s calculando Rentabilidad Backtest; Accion: %s; timming: %s; FechaLTi: %s; PrecioLTi %s; FechaLTf: %s; PrecioLTf %s'
                            %
                            (e, ticket.encode('UTF-8'), timming, fechainicial,
                             precioinicial, fechafinal, preciofinal))
                        rentabilidadoperacion = 0.00

                elif estrategia == 'Bajista':
                    try:
                        rentabilidadoperacion = ((((1 + (
                            (inversionoperacion - inversionrecuperada) /
                            inversionrecuperada))**(365.0 / diffechas)) - 1.0)
                                                 * 100.0)
                    except (OverflowError, ZeroDivisionError) as e:
                        logging.debug(
                            'Error: %s calculando Rentabilidad Backtest; Accion: %s; timming: %s; FechaLTi: %s; PrecioLTi %s; FechaLTf: %s; PrecioLTf %s'
                            %
                            (e, ticket.encode('UTF-8'), timming, fechainicial,
                             precioinicial, fechafinal, preciofinal))
                        rentabilidadoperacion = 0.00

                backtest.append(
                    (ticket, mercado, fechaentrada, precionentrada2,
                     timmingentrada, numeroaccionesoperacion, fechasalida,
                     preciosalida, timmingtransicion, inversionoperacion,
                     inversionrecuperada, balance, rentabilidadoperacion,
                     indicadoresentrada))
                invertido = False


# En el caso de hacer un solo ticket, comentar desde aqui hasta cuentraatras incluido
        cuentaatras -= 1

    if len(backtest) > 0:
        positivas = []
        negativas = []
        inversionTotal = 0
        inversionrecuperadaTotal = 0

        archivobacktest = os.path.join(
            os.getcwd(), CARPETAS['Backtest'],
            ((datetime.now()).strftime("%Y-%m-%d %H%M")) + '.Cobo.csv')
        j = open(archivobacktest, 'w')
        j.write(
            'ticket;mercado;AnoE;MesE;DiaE;PrecioE;TimmingE;Nacciones;AnoS;MesS;DiaS;PrecioS;TimmingS;InversionE;InversionS;resultado;rentabilidad;ADX;DI+;DI-'
            + os.linesep)
        # writercsv = csv.writer(j, delimiter=';', lineterminator = os.linesep, doublequote = True)

        for n in backtest:
            ticket, mercado, fechaentrada, precionentrada, timmingentrada, numeroaccionesoperacion, fechasalida, preciosalida, timming, inversion, inversionrecuperada, balance, rentabilidadoperacion, indicadores = n
            # si los indicadores son False, esto no funcionara
            if ADXobjetivo is False:  # la otra opcion era asignarle a los indicacores valor Falso o 0 , pero no me parecio bien y es lioso imprimir columnas inecesarias
                texto = (
                    ("%s;%s;%s;%.3f;%s;%d;%s;%.3f;%s;%.3f;%.3f;%.3f;%.3f\n") %
                    (ticket, mercado, fechaentrada.replace(
                        '-', ';'), precionentrada, timmingentrada,
                     numeroaccionesoperacion, fechasalida.replace('-', ';'),
                     preciosalida, timming, inversion, inversionrecuperada,
                     balance, rentabilidadoperacion)).replace('.', ',')
            else:

                texto = ((
                    "%s;%s;%s;%.3f;%s;%d;%s;%.3f;%s;%.3f;%.3f;%.3f;%.3f;%.3f;%.3f;%.3f\n"
                    + os.linesep) %
                         (ticket, mercado, fechaentrada.replace(
                             '-', ';'), precionentrada, timmingentrada,
                          numeroaccionesoperacion, fechasalida.replace(
                              '-', ';'), preciosalida, timming, inversion,
                          inversionrecuperada, balance, rentabilidadoperacion,
                          indicadores[0], indicadores[1],
                          indicadores[2])).replace('.', ',')
            j.write(texto)

            # writercsv.writerow(n)

            if balance > 0:
                positivas.append(balance)
            elif balance <= 0:
                negativas.append(balance)

            inversionTotal = inversionTotal + inversion
            inversionrecuperadaTotal = inversionrecuperadaTotal + inversionrecuperada

        for n in range(0, 4):
            j.write(os.linesep)

        j.write('Parametros : ' + os.linesep)
        j.write(('Estrategia : %s' + os.linesep) % estrategia)
        j.write(
            ('Backtest desde la fecha : %s' + os.linesep) % str(analizardesde))
        j.write(('Riesgo : %d' + os.linesep) % riesgo)
        j.write(('Volumen Minimo : %d' + os.linesep) % volumenminimo)
        j.write((('Filtro Mensual : %.2f' + os.linesep) %
                 (filtrosalidamensual)).replace('.', ','))
        j.write((('Filtro Semanal : %.2f' + os.linesep) %
                 (filtrosalidasemanal)).replace('.', ','))
        j.write((('Filtro Diario : %.2f' + os.linesep) %
                 (filtrosalidadiario)).replace('.', ','))
        j.write((('Rentabilidad Minima : %.2f' + os.linesep) %
                 (rentabilidadminima)).replace('.', ','))
        j.write(
            ('Rentabilidad 0 igual a rentabilidad minima : %s' + os.linesep) %
            rentabilidad0)
        j.write((('Inversion Minima : %.2f' + os.linesep) %
                 inversionminima).replace('.', ','))
        j.write(('Inversion Maxima : %s' + os.linesep) % inversionmaxima)
        j.write((('Media Movil Exponencial diario  : %s' + os.linesep) %
                 MMediario))
        j.write((('Media Movil Exponencial semanal : %s' + os.linesep) %
                 MMesemanal))
        j.write((('Media Movil Exponencial mensual : %s' + os.linesep) %
                 MMemensual))
        j.write(
            (('Media Movil Exponencial 2A para cruce de medias diario  : %s' +
              os.linesep) % MMe2diario))
        j.write(
            (('Media Movil Exponencial 2A para cruce de medias semanal : %s' +
              os.linesep) % MMe2semanal))
        j.write(
            (('Media Movil Exponencial 2A para cruce de medias mensual : %s' +
              os.linesep) % MMe2mensual))
        j.write(
            (('True Averange xrange Mensual: %s' + os.linesep) % TARmensual))
        j.write(
            (('True Averange xrange Samanal: %s' + os.linesep) % TARsemanal))
        j.write(
            (('True Averange xrange Diario : %s' + os.linesep) % TARdiario))
        j.write(
            (('Average Directional Movement Index Objetivo: %s' + os.linesep) %
             ADXobjetivo))
        j.write(
            (('Average Directional Movement Index Mensual: %s' + os.linesep) %
             ADXmensual))
        j.write(
            (('Average Directional Movement Index Samanal: %s' + os.linesep) %
             ADXsemanal))
        j.write(
            (('Average Directional Movement Index Diario: %s' + os.linesep) %
             ADXdiario))
        j.write((('Con entradas en Linea de tendencia : %s' + os.linesep) %
                 EntradaLT))
        j.write(('Timming de las operaciones : %s' + os.linesep) %
                seleccionbacktest)
        j.write(('Moneda del Backtest : %s' + os.linesep) % moneda)

        for n in range(0, 4):
            j.write(os.linesep)

        print('')
        j.write('Resultado: ' + os.linesep)
        print('Resultado: ')
        j.write(
            ('Numero de operaciones totales: %d' + os.linesep) % len(backtest))
        print(('Numero de operaciones totales: %d' % (len(backtest))))
        j.write(((
            'Numero de operaciones positivas: %d   Representa un porcetaje de %.2f'
            + os.linesep) %
                 (len(positivas),
                  (len(positivas) * 1.0 / len(backtest) * 1.0) * 100)).replace(
                      '.', ','))
        print((
            'Numero de operaciones positivas: %d   Representa un porcetaje de %.2f'
            % (len(positivas),
               (len(positivas) * 1.0 / len(backtest) * 1.0) * 100)))
        j.write(((
            'Numero de operaciones negativas: %d   Representa un porcetaje de %.2f'
            + os.linesep) %
                 (len(negativas),
                  (len(negativas) * 1.0 / len(backtest) * 1.0) * 100)).replace(
                      '.', ','))
        print((
            'Numero de operaciones negativas: %d   Representa un porcetaje de %.2f'
            % (len(negativas),
               (len(negativas) * 1.0 / len(backtest) * 1.0) * 100)))
        if len(positivas) > 0:
            j.write(
                (('Ganancia Media : %.2f' + os.linesep) %
                 (sum(positivas) / (len(positivas) * 1.0))).replace('.', ','))
            print(('Ganancia Media : %.2f' %
                   (sum(positivas) / len(positivas) * 1.0)))
        else:
            j.write('Ganancia Media : 0.00' + os.linesep)
            print(('Ganancia Media : 0.0'))
        if len(negativas) > 0:
            j.write(
                (('Perdida Media : %.2f' + os.linesep) %
                 (sum(negativas) / (len(negativas) * 1.0))).replace('.', ','))
            print(('Perdida Media : %.2f' %
                   (sum(negativas) / len(negativas) * 1.0)))
        else:
            j.write('Perdida Media : 0.00' + os.linesep)
            print(('Perdida Media : 0.00'))
        j.write(
            (('Inversion Total : %.2f' + os.linesep) % inversionTotal).replace(
                '.', ','))
        print(('Inversion Total : %.2f' % inversionTotal))
        j.write((('Inversion Recuperada : %.2f' + os.linesep) %
                 inversionrecuperadaTotal).replace('.', ','))
        print(('Inversion Recuperada : %.2f' % inversionrecuperadaTotal))
        if estrategia == 'Alcista':
            j.write((('Rentabilidad (Porcentaje): %.2f' + os.linesep) %
                     (((inversionrecuperadaTotal / inversionTotal) - 1) *
                      100)).replace('.', ','))
            print(('Rentabilidad (Porcentaje): %.2f' %
                   (((inversionrecuperadaTotal / inversionTotal) - 1) * 100)))
        elif estrategia == 'Bajista':
            j.write((('Rentabilidad (Porcentaje): %.2f' + os.linesep) %
                     (((inversionTotal / inversionrecuperadaTotal) - 1) *
                      100)).replace('.', ','))
            print(('Rentabilidad (Porcentaje): %.2f' %
                   (((inversionTotal / inversionrecuperadaTotal) - 1) * 100)))
        if len(positivas) > 0 and len(negativas) > 0:
            j.write((('Esperanza Matematica : %.2f' + os.linesep) %
                     (((len(positivas) * 1.0 / len(backtest) * 1.0) *
                       (sum(positivas) / len(positivas) * 1.0)) - abs(
                           (len(negativas) * 1.0 / len(backtest) * 1.0) *
                           (sum(negativas) / len(negativas) * 1.0)))).replace(
                               '.', ','))
            print(('Esperanza Matematica : %.2f' %
                   (((len(positivas) * 1.0 / len(backtest) * 1.0) *
                     (sum(positivas) / len(positivas) * 1.0)) - abs(
                         (len(negativas) * 1.0 / len(backtest) * 1.0) *
                         (sum(negativas) / len(negativas) * 1.0)))))
            j.write((('Ratio profit/lost : %.2f' + os.linesep) %
                     ((sum(positivas) / (len(positivas) * 1.0)) /
                      abs(sum(negativas) / (len(negativas) * 1.0)))).replace(
                          '.', ','))
            print((('Ratio profit/lost :  %.2f' + os.linesep) %
                   ((sum(positivas) / (len(positivas) * 1.0)) /
                    abs(sum(negativas) / (len(negativas) * 1.0)))))
            j.write(((
                'minimo de porcentaje aciertos para no perder con el sistema : %.2f'
                + os.linesep) % (
                    ((1.0 +
                      (comision / abs(sum(negativas) /
                                      (len(negativas) * 1.0)))) /
                     (1.0 + ((sum(positivas) / (len(positivas) * 1.0)) /
                             abs(sum(negativas) /
                                 (len(negativas) * 1.0))))) * 100)).replace(
                                     '.', ','))
            print(((
                'minimo de porcentaje aciertos para no perder con el sistema : %.2f'
                + os.linesep) %
                   (((1.0 +
                      (comision / abs(sum(negativas) /
                                      (len(negativas) * 1.0)))) /
                     (1.0 + ((sum(positivas) / (len(positivas) * 1.0)) /
                             abs(sum(negativas) /
                                 (len(negativas) * 1.0))))) * 100)))
        j.write(
            (('factor ruina : %.2f' + os.linesep) %
             (((1.0 - (len(positivas) * 1.0 / len(backtest) * 1.0)) /
               (len(positivas) * 1.0 / len(backtest) * 1.0))**2.0)).replace(
                   '.', ','))
        print((('factor ruina : %.2f' + os.linesep) %
               (((1.0 - (len(positivas) * 1.0 / len(backtest) * 1.0)) /
                 (len(positivas) * 1.0 / len(backtest) * 1.0))**2.0)))
        j.close()
        print('')
    else:
        input('Backtest no realizado')
        # winsound.PlaySound("*", winsound.SND_ALIAS)


def pidedato(texto, tipodato):
    """
    salida de texto,
    tipo de dato correcto (int/float/str) comprobando que es valido y si no lo es, bucle que no nos permite meter no valido
    valor por defecto

    """
    entrada = eval(input(texto))

    # falta o bien comprobar que el dato introducido es correcto y si no, bucle para volver a introducirlo, o hacer un try para controlar el error en la conversiones
    if tipodato == 'int':
        entrada = int(entrada)
    elif tipodato == 'float':
        entrada = float(entrada)
    elif tipodato == 'str':
        entrada = str(entrada)

    return entrada


def pidefecha():
    """."""
    while True:
        fecha = eval(
            input(
                'Backtest a analizar desde la fecha AAAA-MM-DD (sin fecha inicio): '
            ))

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


def ticketsexcluidos(SUFIJOSEXCLUIDOS):
    """Elimina los Tickets de los mercados que no nos interesan."""
    cursor, db = BBDD.conexion()
    for n in SUFIJOSEXCLUIDOS:
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
                print(('Quedan por borrar %d tickets' % len(listatickets)))
                BBDD.ticketborra(ticket)
    db.close()


def stonicks(listatikets):
    """
    Crea un enlace en la columna dada con el ticket algrafico de la pagina de stonicks.com
    <a href="http://www.stonicks.com/?s=G1A.DE" title="Grafico" target="_blank">G1A.DE</a>.
    """
    listatickets2 = []
    for ticket, nombre, mercado, moneda, timming, rentabilidad, inve, entrada, salida, numaccion, ltdateini, ltpriceini, ltdatefin, ltpricefin in listatikets:
        ticket = (
            '<a href="http://www.stonicks.com/?s=%s" title="Grafico" target="_blank">%s</a>'
            % (ticket, ticket))
        listatickets2.append((ticket, nombre, mercado, moneda, timming,
                              rentabilidad, inve, entrada, salida, numaccion,
                              ltdateini, ltpriceini, ltdatefin, ltpricefin))

    return tuple(listatickets2)


def main():
    """."""
    for carpeta in list(CARPETAS.keys()):
        nombrecarpeta = os.path.join(os.getcwd(), CARPETAS[carpeta])
        if not os.path.exists(nombrecarpeta):
            os.mkdir(nombrecarpeta)
            # os.path.dirname

    opcion = None

    while True:

        # cursor, db = BBDD.conexion()
        tickets = BBDD.ticketlistacodigo()
        mercados = BBDD.mercadoslista()

        ticketsexcluidos(SUFIJOSEXCLUIDOS)
        BBDD.comprobaciones()
        # db.close()

        print('')
        if opcion is None:

            print(('Total de mercados : %d' % (len(mercados))))
            print(('Total de tickets : %d' % (len(list(tickets.keys())))))

            iopciones = 0
            opciones = creaMenu(')', (
                'Acciones para un solo ticket',
                '------------------------------',
                'A) Alta/Actualizar/Descargar/Analizar Datos de 1 Ticket',
                'C) Analizar Datos de 1 Ticket', 'D) Eliminar 1 Ticket',
                'E) Generar Archivos Grafico', '',
                'Acciones para los mercados', '------------------------------',
                'F) Listar Tickets Mercados', 'G) Anadir Ticket Mercado',
                'H) Eliminar Ticket Mercado', '', 'Acciones para las monedas',
                '-------------------------------',
                'I) Actualizar cotizaciones de las Monedas', '',
                'Acciones para todos los tickets en BBDD',
                '------------------------------', 'L) Listar Tickets',
                'M) Actualizar Tickets componentes de Mercados',
                'N) Actualizar cotizaciones de todos los Tickets',
                'O) Actualizar/Descargar Datos Cotizaciones Historicas todos los Tickets',
                'Q) Analizar Datos de todos los Tickets',
                '------------------------------', 'S) BackTest', '', '',
                'Acciones Masivas', '------------------------------',
                'T) Bateria de Backtest', 'V) Exportar datos a arhivos csv',
                'W) Generar Bateria de Lista de acciones',
                'X) Generar Lista de acciones',
                '------------------------------', '', 'Z) Salir'))
            print('')
        opcion, seleccion = opciones[iopciones]
        iopciones += 1

        # 'A) Alta/Actualizar/Descargar/Analizar Datos de 1 Ticket'
        if opcion == 'a':
            print(seleccion)
            # cursor, db = BBDD.conexion()
            naccion = input('Introduce ticket de la accion : ').upper()
            # naccion = (naccion,)
            # Primero lo borramos
            BBDD.ticketborra(naccion, BBDD=False)

            # Lo incorporamos a la base de datos
            BBDD.ticketalta(naccion)
            # cursor.execute("SELECT *  FROM `Cobo_nombreticket` WHERE (`Cobo_nombreticket`.`nombre` = ?)", naccion)
            # numeroResultado = len(cursor.fetchall())
            # if numeroResultado == 0:
            #     cursor.execute("INSERT INTO `Cobo_nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`) VALUES (?, '" + str(date.today()) + "', NULL, NULL)", naccion)
            #     db.commit()
            #     print((naccion[0] + ' anadido a la base de datos'))

            # Actualizamos las cotizaciones
            if 'null,null,null,null,null,null,null' in yahoofinance.cotizacionesTicket(
                    naccion):
                BBDD.ticketborra(naccion)
            else:
                # Descargamos/Actualizamos el historico
                historicoTicket(naccion)

                # Analizamos la accion
                analisisTicket(naccion)
                # db.close()

#        'C) Analizar Datos de 1 Ticket',
        elif opcion == 'c':
            print(seleccion)
            while True:
                naccion = input('Introduce ticket de la accion : ').upper()
                if BBDD.datoshistoricosexisten(naccion):
                    break
                else:
                    print(
                        'Accion no descargada o no figura entre la lista de acciones'
                    )
                    BBDD.ticketerror(naccion)

            analizardesde = pidefecha()
            MMe = input('Media Movil Exponencial (Sin MME): ')
            if MMe == '':
                MMe = False
            else:
                MMe = int(MMe)
            EntradaLT = input(
                'Entradas en Linea de Tendencia (Sin Entradas): ')
            if EntradaLT == '':
                EntradaLT = False
            else:
                EntradaLT = True
            filtrosalidamensual = input(
                'Filtro de salida Mensual por operacion, (%.2f): ' %
                (FILTROSTOPLOSS['m']))
            if filtrosalidamensual == '':
                filtrosalidamensual = FILTROSTOPLOSS['m']
            else:
                filtrosalidamensual = float(filtrosalidamensual)
            filtrosalidasemanal = input(
                'Filtro de salida Semanal por operacion,(%.2f): ' %
                (FILTROSTOPLOSS['w']))
            if filtrosalidasemanal == '':
                filtrosalidasemanal = FILTROSTOPLOSS['w']
            else:
                filtrosalidasemanal = float(filtrosalidasemanal)
            filtrosalidadiario = input(
                'Filtro de salida Diario por operacion, (%.2f): ' %
                (FILTROSTOPLOSS['d']))
            if filtrosalidadiario == '':
                filtrosalidadiario = FILTROSTOPLOSS['d']
            else:
                filtrosalidadiario = float(filtrosalidadiario)

            if BBDD.datoshistoricosexisten(naccion):
                for timminganalisis in 'dwm':
                    print(('Timming del analisis: ', timminganalisis))
                    if timminganalisis == 'w':
                        filtrosalida = filtrosalidasemanal
                    elif timminganalisis == 'm':
                        filtrosalida = filtrosalidamensual
                    elif timminganalisis == 'd':
                        filtrosalida = filtrosalidamensual
                    else:
                        filtrosalida = 0.0

                    analisisAlcistaAccion(naccion,
                                          timming=timminganalisis,
                                          desdefecha=analizardesde,
                                          MME=MMe,
                                          conEntradaLT=EntradaLT,
                                          filtro=filtrosalida)  # ,txt=False)
                    analisisBajistaAccion(naccion,
                                          timming=timminganalisis,
                                          desdefecha=analizardesde,
                                          MME=MMe,
                                          conEntradaLT=EntradaLT,
                                          filtro=filtrosalida)  # ,txt=False)

#        'D) Eliminar 1 Ticket',
        elif opcion == 'd':
            print(seleccion)
            naccion = input('Introduce nombre de la accion : ').upper()
            BBDD.ticketborra(naccion)

#        'E) Generar Archivos Grafico'
        elif opcion == 'e':
            print(seleccion)
            cursor, db = BBDD.conexion()
            while True:
                ticket = input('Introduce ticket de la accion : ').upper()
                if BBDD.datoshistoricosexisten(ticket):
                    break
            datos = BBDD.datoshistoricoslee(ticket)
            ticketconsulta = (ticket, )
            cursor.execute(
                "SELECT `nombre` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`tiket` LIKE ?",
                ticketconsulta)
            nombre = cursor.fetchall()
            nombre = (nombre[0][0].strip('"')).replace(',', '')

            print(' 1 - Diario')
            print(' 2 - Semanal')
            print(' 3 - Mensual')
            timming = 'None'
            while timming not in ('123 '):
                timming = input(
                    'Introduce Timming de los Datos a Generar (Mensual):')

            if timming == '1':
                datos = datos
            elif timming == '2':
                datos = yahoofinance.subirtimming(datos, timming='w')
            elif timming == '3' or timming == '' or timming == ' ':
                datos = yahoofinance.subirtimming(datos, timming='m')

            archivo = os.path.join(os.getcwd(), CARPETAS['Graficos'],
                                   "data.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j,
                                   delimiter=';',
                                   lineterminator=os.linesep,
                                   doublequote=True)
            for n in datos:
                writercsv.writerow(n)
                # j.write(str(n)+os.linesep)
            j.close()

            archivo = os.path.join(os.getcwd(), CARPETAS['Graficos'],
                                   "metatrader.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j,
                                   delimiter=',',
                                   lineterminator=os.linesep,
                                   doublequote=True)
            j.write(
                '<TICKER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>'
                + os.linesep)
            for n in datos:
                fecha, apertura, maximo, minimo, cierre, volumen = n
                fecha = fecha.replace('-', '')

                writercsv.writerow((ticket, fecha, '000000', apertura, maximo,
                                    minimo, cierre, volumen))
                # j.write(str(n)+os.linesep)
            j.close()

            archivo = os.path.join(os.getcwd(), CARPETAS['Graficos'],
                                   'metastock.csv')
            j = open(archivo, 'w')
            j.write(
                '<TICKER>,<NAME>,<PER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>'
                + os.linesep)
            writercsv = csv.writer(j,
                                   delimiter=',',
                                   lineterminator=os.linesep,
                                   doublequote=True)
            for n in datos:

                fecha, apertura, maximo, minimo, cierre, volumen = n
                fecha = fecha.replace('-', '')

                writercsv.writerow(
                    (ticket, nombre, timming, fecha, '000000', apertura,
                     maximo, minimo, cierre, volumen, '0'))
            j.close()

            MMEdatos = eval(
                input(
                    'Introduce Catidad de periodos para el indicador.MME (30):'
                ))

            if MMEdatos == '30' or MMEdatos == '' or MMEdatos == ' ':
                MMEdatos = 30
            else:
                MMEdatos = int(MMEdatos)

            datosMME = indicador.MME(datos, MME=MMEdatos)

            archivo = os.path.join(os.getcwd(), CARPETAS['Graficos'],
                                   "MME.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j,
                                   delimiter=';',
                                   lineterminator=os.linesep,
                                   doublequote=True)
            for n in datosMME:
                writercsv.writerow(n)
            j.close()

            TARdatos = eval(
                input(
                    'Introduce Catidad de periodos para el indicador.TAR (10):'
                ))

            if TARdatos == '10' or TARdatos == '' or TARdatos == ' ':
                TARdatos = 10
            else:
                TARdatos = int(TARdatos)

            datosTAR = indicador.TAR(datos, TAR=TARdatos)

            archivo = os.path.join(os.getcwd(), CARPETAS['Graficos'],
                                   "TAR.csv")
            j = open(archivo, 'w')
            writercsv = csv.writer(j,
                                   delimiter=';',
                                   lineterminator=os.linesep,
                                   doublequote=True)
            for n in datosTAR:
                writercsv.writerow(n)
            j.close()
            db.close()

#        'F) Listar Tickets Mercados',
        elif opcion == 'f':
            print(seleccion)
            for mercado in mercados:
                print(mercado)
            print(('Total de mercados %d' % (len(mercados))))

        # G) Anadir Ticket Mercado',
        elif opcion == 'g':
            print(seleccion)
            mercado = input('Introduce ticket del mercado a anadir : ').upper()
            mercado = mercado.replace('@%5E', '^')
            mercado = (mercado, )
            # TODO : anadir un mercado o dehabilitar y hacerlo directamente en la BBDD
#            if not (mercado[0] in mercados):
#                sql = "SELECT `Cobo_configuracion`.`valor` FROM `Cobo_configuracion` WHERE (`Cobo_configuracion`.`codigo` ='MERCADOS_OBTENER_COMPONENTES')"
#                cursor.execute(sql)
#                resultadoM = cursor.fetchall()
#                print(resultadoM)
#                m = None
#                while m in resultadoM:
#                    m = input('Del los conjuntos anteriores, Introduce donde quieres anadir el mercado :').upper()
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
            mercado = input('Introduce ticket del mercado a borrar : ').upper()
            mercado = mercado.replace('@%5E', '^')
            # TODO : anadir un mercado o dehabilitar y hacerlo directamente en la BBDD
#            if not (mercado in mercados):
#                print(('El mercado %s no existe en la lista de mercados' % mercado))
#            else:
#                mercados.remove(mercado)
#            print('Total de mercados %d' % (len(mercados)))

#        'I) Actualizar cotizaciones monedas
        elif opcion == 'i':
            print(seleccion)
            cursor, db = BBDD.conexion()
            sql = "SELECT `url_Inet` FROM `Cobo_monedas`"
            cursor.execute(sql)
            urlmonedas = cursor.fetchall()
            urlmonedas = ((moneda[0]) for moneda in urlmonedas)
            urlmonedas = deque(list(urlmonedas))

            while len(urlmonedas) > 0:
                moneda = urlmonedas.popleft()
                yahoofinance.cotizacionesMoneda(moneda)
                yahoofinance.duerme()
                print(('Quedan por actualizar un total de : %d' %
                       len(urlmonedas)))
            db.close()

#        'L) Listar Tickets',
        elif opcion == 'l':
            listatickets = list(tickets.keys())
            listatickets.sort()
            ticketsnoBBDD = 0
            for ticket in listatickets:
                print((ticket, tickets[ticket]))
                if tickets[ticket] == '' or tickets[ticket] == 0:
                    ticketsnoBBDD = +1
            print(('Total de tickets %d' % (len(tickets))))
            print(('Tickets que no estan en la BBDD : %s' % ticketsnoBBDD))

            del listatickets, ticketsnoBBDD

#        'M) Actualizar Tickets componentes de Mercados',
        elif opcion == 'm':
            print(seleccion)
            #            ticketsanadidos = 0
            #            mercados = BBDD.mercadoslista()
            #            for mercado in mercados:
            #                mercado = mercado.replace('@%5E', '^')
            #                mercado = mercado.replace('@%5e', '^')
            #                mercado = mercado.upper()
            #                ticketscomponentesmercados = yahoofinance.ticketsdeMercado(mercado)
            #                for ticket in ticketscomponentesmercados:
            #                    if BBDD.ticketalta(ticket):
            #                        ticketsanadidos += 1
            #
            #                if len(ticketscomponentesmercados) == 0:
            #                    print (('Mercado sin ticket, Deshabilitando el Mercado %s' % mercado))
            #                    # BBDD.mercadosdeshabilita(mercado)
            #            print(('Se han anadido un total de : %d tickets' % ticketsanadidos))
            #            ticketscomponentesmercados = []

            print('Se estan anadiendo IPOs del mercado americano')
            ticketsanadidos = 0
            diasatras = int(
                input(
                    'Dias atras para retroceder desde hoy para buscar Ipos? '))
            tickets = yahoofinance.ticketsIPO(diasatras=diasatras)
            for ticket in tickets:
                if BBDD.ticketalta(ticket):
                    ticketsanadidos += 1
            print(
                ('Se han anadido un total de : %d IPOs del mercado americano' %
                 ticketsanadidos))
            del tickets

            print('Se estan anadiendo Criptomonedas')
            if input('Quieres anadir Criptomonedas (Y/....) ?') == 'Y':
                ticketsanadidos = 0
                tickets = yahoofinance.ticketsCriptoIPO()
                for ticket in tickets:
                    if BBDD.ticketalta(ticket):
                        ticketsanadidos += 1
                print(('Se han anadido un total de : %d Criptomonedas' %
                       ticketsanadidos))
                del tickets

            print('Se estan anadiendo acciones de JStock')
            if input('Quieres iniciar el proceso de JStock (Y/....) ?') == 'Y':
                ticketsanadidos = 0
                tickets = ticketsJstock()
                for ticket in tickets:
                    if BBDD.ticketalta(ticket):
                        ticketsanadidos += 1
                print(('Se han anadido un total de : %d acciones de JStock' %
                       ticketsanadidos))
                del tickets

            print('Se estan anadiendo acciones de yahoo-ticker-downloader ')
            if input(
                    'Quieres leer archivo generado por yahoo-downloader (Y/....) ?'
            ) == 'Y':
                ticketsanadidos = 0
                tickets = ticketsYahooD()
                for ticket in tickets:
                    if BBDD.ticketalta(ticket):
                        ticketsanadidos += 1
                print((
                    'Se han anadido un total de : %d acciones de yahoo-ticker-downloader'
                    % ticketsanadidos))
                del tickets

#        'N) Actualizar cotizaciones de todos los Tickets',
        elif opcion == 'n':
            print(seleccion)
            listatickets = BBDD.comprobaciones(cola_resultado='Cotizacion',
                                               aleatorio=True)
            listatickets = deque(listatickets)

            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                if 'null,null,null,null,null,null,null,null' in yahoofinance.cotizacionesTicket(
                        ticket):
                    BBDD.ticketborra(ticket)

                print((((datetime.now()).strftime("%m-%d %H:%M:%S")) +
                       (' - Quedan por actualizar un total de : %d' %
                        len(listatickets))))
                #                threads = list()
                #                for i in (0, MULTIHILO):
                #                    ticket = listatickets.popleft()
                #                    t = threading.Thread(target=yahoofinance.cotizacionesTicket(ticket))
                #                    threads.append(t)
                #                    print(((datetime.now()).strftime("%m-%d %H:%M:%S")) + (' - Quedan por actualizar un total de : %d' % len(listatickets)))
                #                t.setDaemon(True)
                #                t.start()
                yahoofinance.duerme()

#        'O) Actualizar/Descargar Datos Cotizaciones Historicos todos los Tickets',
        elif opcion == 'o':
            print(seleccion)
            # TODO : como ahora tenemos una columna en `Cobo_nombreticket` que contiene la fecha del historico descargado
            #            sql = "SELECT `tiket` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` LIKE 'N/A' ORDER BY `Cobo_componentes`.`tiket` ASC"
            listatickets = BBDD.comprobaciones(cola_resultado='Historico',
                                               aleatorio=True)
            listatickets = deque(listatickets)

            # #            borranoactualizados = input('Despues de una actualizacion del historico de una accion que ya existia, se vuelve a comprobar si se ha actualizado, si no es asi normalmente es porque la accion dejo de cotizar. Quieres borrar estas acciones? (No)')
            # #            if borranoactualizados == '':
            # #            borranoactualizados = False
            # #            else:
            #            borranoactualizados = True

            # for ticket in listatickets:
            while len(listatickets) > 0:
                ticket = listatickets.popleft()
                # accioninvalida=''
                print('')
                print((((datetime.now()).strftime("%m-%d %H:%M:%S")) +
                       (' - Tickets pendientes de comprobar %d' %
                        len(listatickets))))
                # if naccion in tickets:
                # TODO: cuando actualizo con multiples ventanas, a veces se encuentra que una de las ventanas borro la accion de la BBDD
                # para que no se detenga, habria que comprobar si la accion existe en la BBDD
                # con multiples ventanas borra acciones que no deberia
                # FIXME: crear una funcion que compruebe, antes de hacer estas cosas, si la accion aun existe
                if historicoTicket(ticket,
                                   borranoactualizados=borranoactualizados):
                    analisisTicket(ticket)
                # cuentaatras -= 1

        elif opcion == 'q':
            # Q) Analizar Datos de todos los Tickets',
            print(seleccion)
            cursor, db = BBDD.conexion()
            sql = "SELECT `tiket` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` IS NULL ORDER BY `Cobo_componentes`.`tiket` ASC"
            cursor.execute(sql)
            listatickets = cursor.fetchall()
            listatickets = ((ticket[0]) for ticket in listatickets)
            listatickets = deque(list(listatickets))
            db.close()
            # for ticket in listatickets:
            while len(listatickets) > 0:

                print('')
                print(
                    ('Quedan por analizar un total de %d' % len(listatickets)))
                ticket = listatickets.popleft()
                print(('Analizando ticket %s' % ticket))

                analisisTicket(ticket)

#        'S) BackTest
        elif opcion == 's':
            # ticket='AAPL'
            print(seleccion)
            config = {}
            # config['comision'] = 25.0

            print(
                'Parametros del backtest, entre parentesis valor por defecto: '
            )
            #            analizardesde=input('Backtest a analizar desde la fecha AAAA-MM-DD (sin fecha inicio): ')
            #            if analizardesde=='':
            #                analizardesde=False
            if eval(input('Estrategia del backtest (Alcista): ')) != '':
                config['estrategia'] = 'Bajista'

            analizardesde = pidefecha()
            if analizardesde is not False:
                config['analizardesde'] = analizardesde
                if eval(
                        input(
                            'Utilizamos todo el historico para el analisis, (Si): '
                        )) != '':
                    config['todohistorico'] = False

            riesgo = eval(
                input('Riesgo por operacion (%d): ' % (FILTROS['riesgo'])))
            if riesgo != '':
                config['riesgo'] = int(riesgo)

            volumenminimo = eval(
                input('Volumen Minimo por operacion (%d): ' %
                      (FILTROS['volumen'])))
            if volumenminimo != '':
                config['volumenminimo'] = int(volumenminimo)

            filtrosalidamensual = eval(
                input('Filtro de salida Mensual por operacion, (%.2f): ' %
                      (FILTROSTOPLOSS['m'])))
            if filtrosalidamensual != '':
                config['filtrosalidamensual'] = float(filtrosalidamensual)

            filtrosalidasemanal = eval(
                input('Filtro de salida Semanal por operacion, (%.2f): ' %
                      (FILTROSTOPLOSS['w'])))
            if filtrosalidasemanal != '':
                config['filtrosalidasemanal'] = float(filtrosalidasemanal)

            filtrosalidadiario = eval(
                input('Filtro de salida Diario por operacion, (%.2f): ' %
                      (FILTROSTOPLOSS['d'])))
            if filtrosalidadiario != '':
                config['filtrosalidadiario'] = float(filtrosalidadiario)

            rentabilidadminima = eval(
                input('Rentabilidad minima por operacion, (%.2f): ' %
                      (FILTROS['rentMinima'])))
            if rentabilidadminima != '':
                config['rentabilidadminima'] = float(rentabilidadminima)

            if eval(
                    input(
                        'Consideramos Rentabilidad 0 igual a la rentabilidad minima, (Si): '
                    )) != '':
                config['rentabilidad0'] = False

            inversionminima = eval(
                input('Inversion minima por operacion (%d): ' %
                      (FILTROS['invMinima'])))
            if inversionminima != '':
                config['inversionminima'] = int(inversionminima)

            inversionmaxima = eval(
                input('Inversion maxima por operacion (Sin limite): '))
            if inversionmaxima != '':
                config['inversionmaxima'] = int(inversionmaxima)

            if eval(
                    input(
                        'Media Movil Exponencial (Sin MME en todos los timmings): '
                    )) != '':

                MMediario = eval(
                    input('Media Movil Exponencial diario (Sin MME): '))
                if MMediario != '':
                    config['MMediario'] = int(MMediario)
                    MMe2diario = eval(
                        input(
                            '2A Media Movil Exponencial diario para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): '
                        ))
                    if MMe2diario != '':
                        config['MMe2diario'] = int(MMe2diario)

                MMesemanal = eval(
                    input('Media Movil Exponencial semanal (Sin MME): '))
                if MMesemanal != '':
                    config['MMesemanal'] = int(MMesemanal)
                    MMe2semanal = eval(
                        input(
                            '2A Media Movil Exponencial semanal para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): '
                        ))
                    if MMe2semanal != '':
                        config['MMe2semanal'] = int(MMe2semanal)

                MMemensual = eval(
                    input('Media Movil Exponencial mensual (Sin MME): '))
                if MMemensual != '':
                    config['MMemensual'] = int(MMemensual)
                    MMe2mensual = eval(
                        input(
                            '2A Media Movil Exponencial mensual para el cruce de medias. Mismo formato que la MME (Sin MME2, sin cruce de medias): '
                        ))
                    if MMe2mensual != '':
                        config['MMe2mensual'] = int(MMe2mensual)

            if eval(
                    input(
                        'True Avenrange xrange (Sin TAR en todos los timmings): '
                    )) != '':
                TARmensual = eval(
                    input('True Avenrange xrange Mensual (Sin TAR): '))
                if TARmensual != '':
                    config['TARmensual'] = float(TARmensual)
                TARsemanal = eval(
                    input('True Avenrange xrange Semanal (Sin TAR): '))
                if TARsemanal != '':
                    config['TARsemanal'] = float(TARsemanal)
                TARdiario = eval(
                    input('True Avenrange xrange Diario (Sin TAR): '))
                if TARdiario != '':
                    config['TARdiario'] = float(TARdiario)

            ADXobjetivo = eval(
                input(
                    'Average Directional Movement Index, introduce entero, excluir entradas que no lleguen a (deja en blanco pulsando intro para Sin ADX en todos los timmings): '
                ))
            if ADXobjetivo != '':
                config['ADXobjetivo'] = int(ADXobjetivo)
                ADXmensual = eval(
                    input(
                        'Average Directional Movement Index Mensual (deja en blanco pulsando intro para Sin ADX): '
                    ))
                if ADXmensual != '':
                    config['ADXmensual'] = int(ADXmensual)
                ADXsemanal = eval(
                    input(
                        'Average Directional Movement Index Semanal (deja en blanco pulsando intro para Sin ADX): '
                    ))
                if ADXsemanal != '':
                    config['ADXsemanal'] = int(ADXsemanal)
                ADXdiario = eval(
                    input(
                        'Average Directional Movement Index Diario (deja en blanco pulsando intro para Sin ADX): '
                    ))
                if ADXdiario != '':
                    config['ADXdiario'] = int(ADXdiario)

            if eval(input(
                    'Entradas en Linea de Tendencia (Sin Entradas): ')) != '':
                config['EntradaLT'] = True

            config['opcionbacktest'], config['seleccionbacktest'] = creaMenu(
                ')',
                ('Timmin para el que hacemos el backtest', '1) Todo Diario',
                 '2) Diario con transicion a Semanal', '3) Todo Semanal',
                 '4) Semanal con transicion a Mensual', '5) Todo Mensual',
                 '6) Diario con transicion a Semanal y Mensual'),
                cola=False)

            # En el caso de hacer un solo ticket, comentar desde aqui hasta print 'Analizando ticket %s' % ticket incluido, desdentar desde este comentario hasta el siguiente parecedo
            # obtenemos la lista de las monedas
            cursor, db = BBDD.conexion()
            monedas = []
            sql = "SELECT Cobo_monedas.codigo FROM Cobo_monedas"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            # lo mostramos en una lista
            # nos pide la moneda a buscar y la convertimos en la variable de la siguiente consulta con la que obtenemos la lista de tickes para hacer el backtest
            for mon in resultado:
                print((mon[0]))
                monedas.append(mon[0])

            while True:
                moneda = eval(
                    input(
                        'Lista de monedas. Introduce moneda en la que se hace el backtest, para hacerlo por mercado pulsa intro : '
                    ))
                if moneda == '' or moneda is None:
                    monedas = []
                    sql = "SELECT Cobo_mercado_moneda.nombreUrl FROM Cobo_mercado_moneda ORDER BY Cobo_mercado_moneda.nombreUrl ASC"
                    cursor.execute(sql)
                    resultado = cursor.fetchall()
                    # lo mostramos en una lista
                    # nos pide la moneda a buscar y la convertimos en la variable de la siguiente consulta con la que obtenemos la lista de tickes para hacer el backtest
                    for mon in resultado:
                        print((mon[0]))
                        monedas.append(mon[0])
                    while True:
                        moneda = eval(
                            input(
                                'Introduce nombre del mercado en la que se hace el backtest, recuerda escribirlo exactamente igual : '
                            ))
                        if moneda in monedas:
                            config['moneda'] = moneda
                            break
                    break
                elif moneda in monedas:
                    config['moneda'] = moneda
                    break

            backtestMoneda(**config)

            if eval(
                    input(
                        'Deseas agregar esta configuracion de Backtest a la bateria de Backtest (Si): '
                    )) == '':
                j = open(ARCHIVOCONFIGBACKTEST, 'a')
                j.write((str(config) + os.linesep))
                j.close()

        elif opcion == 't':
            print(seleccion)
            j = open(ARCHIVOCONFIGBACKTEST, 'r')
            lineas = j.readlines()
            j.close()
            for linea in lineas:
                dicc = ast.literal_eval(linea)
                backtestMoneda(**dicc)
                del dicc

#            'Cambiar sistema de analisis',
#            '------------------------------',
#            'T) Cooper',
#             print(seleccion)
#             del analisisAlcistaAccion, analisisBajistaAccion
#             from Cooper import analisisAlcistaAccion, analisisBajistaAccion
#             global analisisAlcistaAccion, analisisBajistaAccion
#             print('Cambiado todos los sistemas de analisis al sistema de Cooper')

#        'V) Exportar datos a arhivos csv',
        elif opcion == 'v':
            print(seleccion)
            print('Limpiando Directorio')
            cursor, db = BBDD.conexion()
            # os.remove(glob.glob(os.path.join(os.getcwd(), CARPETAS['Historicos'], nombre + "*.*")))
            archivosticket = glob.glob(
                os.path.join(os.getcwd(), CARPETAS['Historicos'], "*.*"))
            for archivo in archivosticket:
                os.remove(archivo)
            del archivosticket
            moneda = (eval(
                input(
                    'Introduce sufijo de tickets del mercado a exportar (Todas): '
                ))).upper()
            if moneda == '' or moneda is None:
                cursor.execute(
                    "SELECT `tiket`, `codigo`, `nombre` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` IS NULL ORDER BY `Cobo_componentes`.`tiket` ASC"
                )
            else:
                moneda = (moneda, )
                cursor.execute(
                    "SELECT `tiket`, `codigo`, `nombre` FROM `Cobo_componentes` WHERE `Cobo_componentes`.`error` IS NULL AND `Cobo_componentes`.`mercado` IN (SELECT `nombreUrl` FROM `Cobo_mercado_moneda` WHERE `abrevMoneda` LIKE ?) ORDER BY `Cobo_componentes`.`tiket` ASC",
                    moneda)
            listatickets = cursor.fetchall()
            listatickets = ((ticket[0], ticket[1], ticket[2])
                            for ticket in listatickets)
            listatickets = deque(list(listatickets))
            ticketsnodescargados = []
            db.close()
            # for ticket in listatickets:
            while len(listatickets) > 0:
                ticket, _codigo, naccion = listatickets.popleft()
                naccion = (naccion.strip('"')).replace(',', '')

                print('')
                print(
                    ('Tickets pendientes de exportar %d' % len(listatickets)))
                print(('Exportando ticket %s' % ticket))

                if BBDD.datoshistoricosexisten(ticket):
                    # funcion maximo minimo historico
                    datos = BBDD.datoshistoricoslee(ticket)

                    for timming in 'MWD':
                        if timming == 'D':
                            datosaccion = datos
                        elif timming == 'W':
                            datosaccion = yahoofinance.subirtimming(
                                datos, timming='w')
                        elif timming == 'M':
                            datosaccion = yahoofinance.subirtimming(
                                datos, timming='m')

                        if len(datosaccion) > 0:
                            nombre = (str(ticket)).replace('.', '_')
                            # nombre = (str(ticket) + str(codigo)).replace('.', '_')
                            archivo = os.path.join(
                                os.getcwd(), CARPETAS['Historicos'],
                                nombre + '.' + timming + '.csv')
                            j = open(archivo, 'w')
                            j.write(
                                '<TICKER>,<NAME>,<PER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>'
                                + os.linesep)
                            writercsv = csv.writer(j,
                                                   delimiter=',',
                                                   lineterminator=os.linesep,
                                                   doublequote=True)
                            for n in datosaccion:

                                fecha, apertura, maximo, minimo, cierre, volumen = n
                                fecha = fecha.replace('-', '')

                                n = (ticket, naccion, timming, fecha, '000000',
                                     apertura, maximo, minimo, cierre, volumen,
                                     '0')

                                writercsv.writerow(n)
                                # j.write(str(n)+os.linesep)
                            j.close()

                        else:  # No existe suficiente historico
                            BBDD.ticketerror(ticket)
                            ticketsnodescargados.append(ticket)
                else:  # no existe el archivo
                    # cotizacionesTicket(naccion)
                    BBDD.ticketerror(ticket)
                    ticketsnodescargados.append(ticket)

                print('')

            print(('Tickets para los que no hay cotizaciones historicas'))
            for ticket in ticketsnodescargados:
                print(ticket)
            print(('Un total de : ', len(ticketsnodescargados)))

#        'W) Generar Bateria lista de acciones',
        elif opcion == 'w':
            print(seleccion)

            config1 = {}
            config2 = {}

            config2['volumen'] = FILTROS['volumen']
            config1['volumen'] = FILTROS['volumen']

            config2['rentMinima'] = FILTROS['rentMinima']
            config1['rentMinima'] = FILTROS['rentMinima']

            config2['inversion'] = FILTROS['invMinima']
            config1['inversion'] = FILTROS['invMinima']

            config2['riesgo'] = FILTROS['riesgo']
            config1['riesgo'] = FILTROS['riesgo']

            config2['filtroM'] = float(0.03)
            config1['filtroM'] = FILTROSTOPLOSS['m']

            config2['filtroW'] = float(0.02)
            config1['filtroW'] = FILTROSTOPLOSS['w']

            config2['filtroD'] = float(0.01)
            config1['filtroD'] = FILTROSTOPLOSS['d']

            config2['timmings'] = ('m', 'w', 'd')
            config1['timmings'] = ('m', 'w', 'd')

            for config in (config1, config2):

                resultado = stonicks(BBDD.listacciones(**config))
                resultado2 = stonicks(BBDD.listaccionesLT(**config))
                resultado3 = stonicks(
                    BBDD.listaccionesLT(incremperiod=1, **config))

                ficheroFecha = (
                    (datetime.now()).strftime("%Y%m%d %H%M%S")) + '.html'

                ficheroDatos = os.path.join("/home/antonio/Dropbox/Analisis/",
                                            ficheroFecha)
                f = open(ficheroDatos, "w")
                f.write('<!DOCTYPE html>' + os.linesep)
                f.write('<html>' + os.linesep)
                f.write('<head>' + os.linesep)
                f.write(
                    '<meta content="text/html; charset=windows-1252" http-equiv="content-type">'
                    + os.linesep)
                for name, content in (
                    ('author', __author__[0]), ('mail', __mail__[0]),
                    ('license',
                     'http://creativecommons.org/licenses/by-sa/3.0/legalcode'
                     )):
                    f.write('<meta name="' + name + '" content="' + content +
                            '">' + os.linesep)
                f.write('</head>' + os.linesep)
                f.write('<body>' + os.linesep)
                f.write(
                    '<p>Lista Generada Automaticamente. Parametros:</p>\n\
                                        <ul>\n\
                                          <li>Volumen: %d</li>\n\
                                          <li>Rentabilidad: %.2f</li>\n\
                                          <li>InversionMinima: %d</li>\n\
                                          <li>Riesgo: %d</li>\n\
                                          <li>FiltroMensual %.2f</li>\n\
                                          <li>FiltroSemanal %.2f</li>\n\
                                          <li>FiltroDiario %.2f</li>\n\
                                </ul>\n' %
                    (config['volumen'], config['rentMinima'],
                     config['inversion'], config['riesgo'], config['filtroM'],
                     config['filtroW'], config['filtroD']))

                for res in (resultado, resultado2, resultado3):
                    htmlcode = HTML.table(
                        res,
                        header_row=[
                            'Ticket', 'Nombre', 'Mercado', 'Moneda', 'Timming',
                            'Rentabilidad', 'Inversion en Euros', 'Entrada',
                            'Salida', 'Numero Acciones', 'LT Fecha Ini',
                            'LT Precio Ini', 'LT Fecha Fin', 'LT Precio Fin'
                        ])
                    f.write(htmlcode)
                    f.write(
                        '<br>Calculos para entradas en Linea de Tendencia<br><p><br></p>'
                    )
                f.write(
                    '<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.es_CO"><img alt="Licencia Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.es_CO">Licencia Creative Commons Atribución-CompartirIgual 3.0 Unported</a>.'
                )
                f.write('</body>' + os.linesep)
                f.write('</html>' + os.linesep)
                f.close()

                yahoofinance.duerme(tiempo=20000)

        # x) Generar lista de acciones
        elif opcion == 'x':
            print(seleccion)
            config = {}

            vol = input('Volumen minimo (%d)?' % (FILTROS['volumen']))
            if vol != '':
                config['volumen'] = int(vol)
            else:
                config['volumen'] = FILTROS['volumen']

            rentMinima = input('rentabilidad minima (%.2f)?' %
                               (FILTROS['rentMinima']))
            if rentMinima != '':
                config['rentMinima'] = float(rentMinima)
            else:
                config['rentMinima'] = FILTROS['rentMinima']

            inversion = input('inversion minima (%dE)?' %
                              (FILTROS['invMinima']))
            if inversion != '':
                config['inversion'] = int(inversion)
            else:
                config['inversion'] = FILTROS['invMinima']

            riesgo = input('riesgo por operacion (%dE)?' % (FILTROS['riesgo']))
            if riesgo != '':
                config['riesgo'] = int(riesgo)
            else:
                config['riesgo'] = FILTROS['riesgo']

            filtroM = input(
                'Filtro de salida Mensual por operacion, (%.2f): ' %
                (FILTROSTOPLOSS['m']))
            if filtroM != '':
                config['filtroM'] = float(filtroM)
            else:
                config['filtroM'] = FILTROSTOPLOSS['m']

            filtroW = input(
                'Filtro de salida Semanal por operacion, (%.2f): ' %
                (FILTROSTOPLOSS['w']))
            if filtroW != '':
                config['filtroW'] = float(filtroW)
            else:
                config['filtroW'] = FILTROSTOPLOSS['w']

            filtroD = input('Filtro de salida Diario por operacion, (%.2f): ' %
                            (FILTROSTOPLOSS['d']))
            if filtroD != '':
                config['filtroD'] = float(filtroD)
            else:
                config['filtroD'] = FILTROSTOPLOSS['d']
            timmings = []
            for n in ('m', 'w', 'd'):
                if input(
                        'Anadir el timming %s (intro si/ cualquier otra tecla no) :'
                        % n) == '':
                    timmings.append(n)
            config['timmings'] = tuple(timmings)

            resultado = stonicks(BBDD.listacciones(**config))
            resultado2 = stonicks(BBDD.listaccionesLT(**config))
            resultado3 = stonicks(BBDD.listaccionesLT(incremperiod=1,
                                                      **config))

            ficheroFecha = (
                (datetime.now()).strftime("%Y%m%d %H%M%S")) + '.html'
            #ficheroDatos = os.path.join(os.getcwd(), ficheroFecha)
            ficheroDatos = os.path.join("/home/antonio/Dropbox/Analisis/",
                                        ficheroFecha)
            f = open(ficheroDatos, "w")
            f.write('<!DOCTYPE html>' + os.linesep)
            f.write('<html>' + os.linesep)
            f.write('<head>' + os.linesep)
            f.write(
                '<meta content="text/html; charset=windows-1252" http-equiv="content-type">'
                + os.linesep)
            for name, content in (
                ('author', __author__[0]), ('mail', __mail__[0]),
                ('license',
                 'http://creativecommons.org/licenses/by-sa/3.0/legalcode')):
                f.write('<meta name="' + name + '" content="' + content +
                        '">' + os.linesep)
            f.write('</head>' + os.linesep)
            f.write('<body>' + os.linesep)
            f.write('<p>Lista Generada Automaticamente. Parametros:</p>\n\
                        <ul>\n\
                          <li>Volumen: %d</li>\n\
                          <li>Rentabilidad: %.2f</li>\n\
                          <li>InversionMinima: %d</li>\n\
                          <li>Riesgo: %d</li>\n\
                          <li>FiltroMensual %.2f</li>\n\
                          <li>FiltroSemanal %.2f</li>\n\
                          <li>FiltroDiario %.2f</li>\n\
                </ul>\n' %
                    (config['volumen'], config['rentMinima'],
                     config['inversion'], config['riesgo'], config['filtroM'],
                     config['filtroW'], config['filtroD']))

            for res in (resultado, resultado2, resultado3):
                htmlcode = HTML.table(res,
                                      header_row=[
                                          'Ticket', 'Nombre', 'Mercado',
                                          'Moneda', 'Timming', 'Rentabilidad',
                                          'Inversion en Euros', 'Entrada',
                                          'Salida', 'Numero Acciones',
                                          'LT Fecha Ini', 'LT Precio Ini',
                                          'LT Fecha Fin', 'LT Precio Fin'
                                      ])
                f.write(htmlcode)
                f.write(
                    '<br>Calculos para entradas en Linea de Tendencia<br><p><br></p>'
                )
#             for n in resultado:
#                 ticket, nombre, mercado, moneda, timming, rentabilidad, inversion, entrada, salida, numeroacc, LTFIni, LTPIni, LTFFin, LTFPFin = n
#                 if rentabilidad >= 0.0:
#                     color = 'Green'
#                 else:
#                     color = 'Red'
#                 colored_n = HTML.TableCell(ticket, nombre, mercado, moneda, timming, rentabilidad, inversion, entrada, salida, numeroacc, LTFIni, LTPIni, LTFFin, LTFPFin, bgcolor=color)
#                 htmlcode.rows.append(colored_n)
#                 # table.rows.append(colored_n)
#             htmlcode = str(htmlcode)
            f.write(
                '<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.es_CO"><img alt="Licencia Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.es_CO">Licencia Creative Commons Atribución-CompartirIgual 3.0 Unported</a>.'
            )
            f.write('</body>' + os.linesep)
            f.write('</html>' + os.linesep)
            f.close()

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

            # cursor.close()
            # db.close()
            break


############################################################
# programa principal

if __name__ == '__main__':
    main()
