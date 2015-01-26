#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
BBDD.py - v0.02 2013-07-16 Antonio Caballero

Este modulo proporciona las herramientas necesarias para junto con Cobo o Cooper gestionar la Base de datos

License: http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode
"""

__version__ = '0.03'
__date__ = '2013-07-26'
__author__ = ('Antonio Caballero',)
__mail__ = ('zurbaran79@hotmail.com',)
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

#################################################
# Constantes locales

#################################################

####################################################
# modulos estandar importados

import os
import glob
from datetime import date, datetime, timedelta
from random import choice


# from sql import *
# from sql.aggregate import *
# from sql.conditionals import *
# TODO: implementar la libreria python-sql para generar el codigo sql

try:
    from pysqlite2 import dbapi2 as sqlite3
except ImportError:
    print ('Modulo de pysqlite2 deshabilitado. Cargando sqlite3 nativo')
    from setuptools.command.easy_install import main as install
    import sqlite3  # lint:ok
    install(['-v', 'pysqlite'])

####################################################
# modulos no estandar o propios
from Cobo import CARPETAS, DIFREGACTUALIZAR, FILTROSTOPLOSS, FILTROS
from indicador import puntocurvaexponencial, curvexprent


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


def comprobaciones(colaResultado=None, aleatorio=False):
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
    listatickets = cursor.fetchall()
    numeroResultado = len(listatickets)
    if colaResultado == None:
        print(('Tickets a los que les falta relacion entre mercado y moneda : %d' % numeroResultado))
        if numeroResultado >= 1:
            print listatickets

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
        if aleatorio == False:
            colaResultado = list((ticket[0]) for ticket in listatickets)
        elif aleatorio == True:
            colaResultado2 = list((ticket[0]) for ticket in listatickets)
            colaResultado = []
            while len(colaResultado2) != 0:
                ticket = choice(colaResultado2)
                colaResultado.append(ticket)
                colaResultado2.remove(ticket)

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
        if aleatorio == False:
            colaResultado = list((ticket[0]) for ticket in listatickets)
        elif aleatorio == True:
            colaResultado2 = list((ticket[0]) for ticket in listatickets)
            colaResultado = []
            while len(colaResultado2) != 0:
                ticket = choice(colaResultado2)
                colaResultado.append(ticket)
                colaResultado2.remove(ticket)

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
    ticket = (ticket,)
    anadido = False

    # Comprobamos si existe
    cursor.execute("SELECT *  FROM `Cobo_nombreticket` WHERE (`Cobo_nombreticket`.`nombre` = ?)", ticket)
    # sql = "SELECT * FROM `Cobo_nombreticket` WHERE `nombre` = '" + ticket + "'"
    # cursor.execute(sql)
    numeroResultado = len(cursor.fetchall())
    if numeroResultado == 0:
        # Si no existe, lo incorporamos
        cursor.execute("INSERT INTO `Cobo_nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`, fechahistorico) VALUES (?, '" + str(date.today()) + "', NULL, NULL, NULL)", ticket)
        # sql = "INSERT INTO `Cobo_nombreticket` (`nombre`, `fechaRegistro`, `fechaError`, `fechaActualizacion`, `fechahistorico`) VALUES ('" + ticket + "', '" + str(date.today()) + "', NULL, NULL, NULL)"
        # cursor.execute(sql)
        anadido = True
        db.commit()
        print((ticket[0] + ' anadido a la base de datos'))

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


def ticketobtencotizacion(nombreticket):
         cursor, db = conexion()
         nombreticket = (nombreticket.upper(),)
         cursor.execute("SELECT * FROM `Cobo_componentes` WHERE `Cobo_componentes`.`tiket` = ?", nombreticket)
         registro = cursor.fetchall()
         # resultado=(28141L, 'LVL MEDICAL GROUP', '-LVL.NX', 'ENX', 18.4, 14.89, 12.46, 14.56, 14.89, 12396.0, 7371.0, 'N/A', datetime.date(2011, 2, 24)
         ## TODO: FIXME: a veces, cuando esta haciendose en modo multiple, registro=[] y IndexError: list index out of range
         return registro[0]


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
    db.commit()
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
    vol = config.get('volumen', FILTROS['volumen'])
    rentMinima = config.get('rentMinima', FILTROS['rentMinima'])
    inv = config.get('inversion', FILTROS['invMinima'])
    riesgo = config.get('riesgo', FILTROS['riesgo'])
    filtroM = config.get('filtroM', FILTROSTOPLOSS['m'])
    filtroW = config.get('filtroW', FILTROSTOPLOSS['w'])
    filtroD = config.get('filtroD', FILTROSTOPLOSS['d'])
    filtro = {'m': filtroM, 'w': filtroW, 'd': filtroD}
    timmings = config.get('timmings', ('m', 'w', 'd'))

    cursor, db = conexion()
    sql = ("SELECT Cobo_componentes.tiket AS Ticket,\
       Cobo_componentes.nombre,\
       Cobo_componentes.mercado,\
       Cobo_monedas.descripcion,\
       Cobo_monedas.valor,\
       Cobo_params_operaciones.timing,\
       Cobo_params_operaciones.entrada,\
       Cobo_params_operaciones.salida,\
       Cobo_params_operaciones.fecha_ini,\
       Cobo_params_operaciones.precio_ini,\
       Cobo_params_operaciones.fecha_fin,\
       Cobo_params_operaciones.precio_fin\
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
       NOT ( Cobo_componentes.mercado = 'Other OTC'\
           OR\
           Cobo_componentes.mercado = 'PCX'\
           OR\
           Cobo_componentes.mercado = 'IOB'\
           OR\
           Cobo_componentes.mercado = 'PSX'\
           OR\
       Cobo_componentes.mercado = 'NGM' )\
 ORDER BY Cobo_monedas.descripcion DESC,\
           Cobo_params_operaciones.rentabilidad DESC" % (vol, vol, rentMinima, rentMinima, rentMinima))
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    resultado2 = []

    for ticket, nombre, mercado, moneda, divisa, timming, entrada, salida, ltdateini, ltpriceini, ltdatefin, ltpricefin in resultado:
        nombre = nombre.encode('UTF-8')
        rentabilidad = curvexprent(ltdateini, ltpriceini, ltdatefin, ltpricefin)
        if entrada == None:
            entrada = 0.0
        if salida == None:
            salida = 0.0
        if rentabilidad >= 0.0:
            entrada = entrada + 0.01
            salida = round(salida * (1.0 - filtro[timming]), 2)
        elif rentabilidad < 0.0:
            entrada = entrada - 0.01
            salida = round(salida * (1.0 + filtro[timming]), 2)
        # FIXME: entrada y salida deben ser distintos
        # [(u'ISAT.L', u'INMARSAT', u'London', u'Libra Esterlina(Peniques)', 82.95, u'm', ...), (u'RR.L', u'ROLLS-ROYCE HLDGS', u'London', u'Libra Esterlina(Peniques)', 82.95, u'm', ...), (u'AZN.L', u'ASTRAZENECA', u'London', u'Libra Esterlina(Peniques)', 82.95, u'm', ...), (u'CPG.L', u'COMPASS GROUP', u'London', u'Libra Esterlina(Peniques)', 82.95, u'm', ...), (u'RMG.L', u'ROYAL MAIL', u'London', u'Libra Esterlina(Peniques)', 82.95, u'w', ...), (u'CSR.L', u'CSR', u'London', u'Libra Esterlina(Peniques)', 82.95, u'm', ...), ...]
        # 'Kofax Limited'
        # entrada y salida son 6.51, puede ser una cohincidencia en los calculos

        if entrada != salida:
            numaccion = int((divisa * riesgo) / (entrada - salida))
        else:
            numaccion = 0
            
        inve = round(((numaccion * 1.0) * entrada) / divisa, 2)
        if not ((-1.0 * inv) <= inve <= inv) and \
           (rentabilidad >= rentMinima or \
           rentabilidad <= -(rentMinima / (1.0 + rentMinima)) or \
           rentabilidad == 0.0) and\
           timming in timmings:
            resultado2.append((ticket, nombre, mercado, moneda, timming, round(rentabilidad * 100, 2), inve, entrada, salida, numaccion, ltdateini, ltpriceini, ltdatefin, ltpricefin))
    return tuple(resultado2)


def listaccionesLT(**config):
    """
    """
    vol = config.get('volumen', FILTROS['volumen'])
    rentMinima = config.get('rentMinima', FILTROS['rentMinima'])
    inv = config.get('inversion', FILTROS['invMinima'])
    riesgo = config.get('riesgo', FILTROS['riesgo'])
    filtroM = config.get('filtroM', FILTROSTOPLOSS['m'])
    filtroW = config.get('filtroW', FILTROSTOPLOSS['w'])
    filtroD = config.get('filtroD', FILTROSTOPLOSS['d'])
    filtro = {'m': filtroM, 'w': filtroW, 'd': filtroD}
    timmings = config.get('timmings', ('m', 'w', 'd'))

    incremperiod = config.get('incremperiod', 0)

    cursor, db = conexion()
    sql = ("SELECT Cobo_componentes.tiket,\
       Cobo_componentes.nombre,\
       Cobo_componentes.mercado,\
       Cobo_monedas.descripcion,\
       Cobo_monedas.valor,\
       Cobo_params_operaciones.timing,\
       Cobo_params_operaciones.precio_salida,\
       Cobo_params_operaciones.fecha_ini,\
       Cobo_params_operaciones.precio_ini,\
       Cobo_params_operaciones.fecha_fin,\
       Cobo_params_operaciones.precio_fin,\
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
           Cobo_params_operaciones.rentabilidad DESC" % (vol, vol, rentMinima, rentMinima, rentMinima))
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    resultado2 = []

    # TODO: comprobar si al precio_salida hay que aplicarle los filtros en funcion del timming
    for ticket, nombre, mercado, moneda, divisa, timming, salida, ltdateini, ltpriceini, ltdatefin, ltpricefin, maxDia, minDia, valorActual in resultado:
        nombre = nombre.encode('UTF-8')
        rentabilidad = curvexprent(ltdateini, ltpriceini, ltdatefin, ltpricefin)
        entrada = puntocurvaexponencial(ltdateini, ltpriceini, ltdatefin, ltpricefin, timming, incremperiod=incremperiod)
        if entrada == None:
            entrada = 0.0
        if salida == None:
            salida = 0.0
        if rentabilidad >= 0.0:
            salida = round(salida * (1.0 - filtro[timming]), 2)
        elif rentabilidad < 0.0:
            salida = round(salida * (1.0 + filtro[timming]), 2)
        if entrada != salida:
            numaccion = int((divisa * riesgo) / (entrada - salida))
        else:
            numaccion = 0
        inve = round(((numaccion * 1.0) * entrada) / divisa, 2)
        # FIXME: hay que quitar la igualdad de los >= <=
        # FIXME: en los calculos de inversion en bajista, la inve es negativo
        # dependiendo de si es alcista o bajista que:
        # Comprobamos inversion minima bajista en negativo e inversion minima alcista
        # Comprobamos la rentabilidad minima
        # en alcista el precio de entrada se encuenta por debajo de los precios de maximo diario, minimo diario, cotizacion actual y la entrada esta por encima de la salida sin ser igual
        # en bajista el precio de entrada se encuenta por encima de los precios de maximo diario, minimo diario, cotizacion actual y la entrada esta por debajo de la salida sin ser igual

        if not ((-1.0 * inv) <= inve <= inv) and \
           (rentabilidad >= rentMinima or \
           rentabilidad <= -(rentMinima / (1.0 + rentMinima)) or \
           rentabilidad == 0.0) and\
            ((rentabilidad >= 0.0 and\
              (maxDia > entrada and minDia > entrada and valorActual > entrada and entrada > salida and entrada > ltpricefin)) or\
             (rentabilidad < 0.0 and\
              (maxDia < entrada and minDia < entrada and valorActual < entrada and entrada < salida and entrada < ltpricefin))) and\
           timming in timmings:
            resultado2.append((ticket, nombre, mercado, moneda, timming, round(rentabilidad * 100, 2), inve, entrada, salida, numaccion, ltdateini, ltpriceini, ltdatefin, ltpricefin))

    return tuple(resultado2)


if __name__ == '__main__':
    pass
