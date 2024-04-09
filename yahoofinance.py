#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
yahoofinance.py - v0.05 2017-07-16 Antonio Caballero.

Este modulo proporciona las herramientas necesarias la descarga de datos de yahoo finance

License: http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode
"""

__version__ = '0.06'
__date__    = '2020-03-09'
__author__  = ('Antonio Caballero',)
__mail__    = ('zurbaran79@hotmail.com',)
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


# paginas de interes
# http://finance.yahoo.com/international


#################################################
# Constantes locales

webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
pausareconexion = 35
prefijo = {'': '',
           '.AS': '',
           '.AT': 'gr.',
           '.AX': '',
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
           '.CO': '',
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
           '.OL': '',
           '.PA': 'fr.',
           '.PK': '',
           '.SA': 'br.',
           '.SG': 'de.',
           '.SI': 'sg.',
           '.SN': 'cl.',
           '.SS': '',
           '.ST': '',
           '.SW': '',
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
# mercadosfail = ('.MC',)

####################################################
# modulos estandar importados

from time import sleep, strftime, strptime
from datetime import date, timedelta, datetime
from calendar import timegm
from random import randint
import random
import logging
import os
import http.client
import urllib.request
import urllib.error
import socket
import csv
import concurrent.futures

####################################################
# modulos no estandar o propios
from yahoofinancials import YahooFinancials
import yfinance as yf

from settings import CARPETAS, ARCHIVO_LOG
# from BBDD import datoshistoricoslee, datoshistoricosgraba, ticketcotizaciones, monedacotizaciones
import BBDD


logging.basicConfig(filename=ARCHIVO_LOG,
                    format='%(asctime)s : %(processName)s : %(levelname)s : %(module)s : %(funcName)s: %(lineno)d :%(message)s',
                    level=logging.DEBUG)

socket.setdefaulttimeout(pausareconexion)


# TODO: Utilizando la red TOR para descargar la informacion de yahoo

cookier = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(cookier)
urllib.request.install_opener(opener)

# Cookie and corresponding crumb
_cookie = None
#_crumb = True #None


def _test():
    """."""
    import doctest
    doctest.testmod()


def duerme(tiempo=1500):
    """."""
    x = (randint(0, tiempo)) / 1000.0
    print(('Pausa de %.3f segundos' % x))
    sleep(x)


def ticketsdeMercado(mercado):
    """."""
    # global webheaders
    # habra que buscar los ticket y utilizar como fin de pagina el texto en la primera
    # <a href="/q/cp?s=%5EDJA&amp;c=1">Last< donde c=1 indica el final de la pagina
    # en los casos donde solo hay una pagina, no encontrariamos cadena dando valor -1
    # los tickets se encuentan en detras de la cadena <b><a href="/q?s= y como final ">

    # TODO: utilizar la libreria yahoo-ticker-downloader
    # arhcivo resultante stocks.pickle
    # ./ YahooTickerDownloader.py stocks - e
    # exportado a un csv con la cabecera
    # Ticker, Name, Exchange, categoryName

    ticketsanadidos = []
    ultimapagina = 0
    pagina = 0
    mercado = mercado.strip()
    while pagina <= ultimapagina:
        print('')
        url = 'https://es.finance.yahoo.com/q/cp?s=' + mercado + '&c=' + str(pagina)
        print(url)

        web = None
        while web is None:
            try:
                r = urllib.request.Request(url, headers=webheaders)
                f = urllib.request.urlopen(r, timeout=pausareconexion)
                web = (f.read()).decode('utf-8')
                f.close()
            except urllib.error.HTTPError as e:
                print('Conexion Perdida')
                print(e.code)
                if e.code == 500:
                    return ticketsanadidos
                else:
                    web = None
                    sleep(pausareconexion)
                    # raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
            except (urllib.error.URLError, IOError, http.client.BadStatusLine, socket.timeout) as e:
                print('Conexion Erronea')
                # print(e.reason)
                print(url, e)
                web = None
                logging.debug('Error: %s; Mercado: %s; Url: %s' % (e, mercado.encode('utf-8'), url.encode('utf-8')))
                print('Pausa de %d segundos' % pausareconexion)
                sleep(pausareconexion)

        if ultimapagina == 0:
            busqueda = 'Siguiente</a> | <a href="/q/cp?s=' + (mercado.upper().replace('^', '%5E')) + '&amp;c='
            ultimapaginainicio = web.find(busqueda)
            if ultimapaginainicio == -1:
                ultimapagina = 0
            else:
                ultimapaginainicio = ultimapaginainicio + len(busqueda)
                ultimapaginafinal = web.find('">', ultimapaginainicio)
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


def ticketsIPO(diasatras=6):
    """."""
    
    ticketsanadidos = []
    hoy = datetime.today()
    fechas=[]
    for n in range(diasatras):
        fechas.append((hoy - timedelta(days=n)).strftime('%Y-%m-%d'))
    
    for fecha in fechas:
        url = 'https://finance.yahoo.com/calendar/ipo?day=' + fecha
        print(url)

        web = None
        while web is None:
            try:
                r = urllib.request.Request(url, headers=webheaders)
                f = urllib.request.urlopen(r, timeout=pausareconexion)
                web = (f.read()).decode('utf-8')
                f.close()
            except urllib.error.HTTPError as e:
                print('Conexion Perdida')
                print(e.code)
                if e.code == 500:
                    return ticketsanadidos
                else:
                    web = None
                    sleep(pausareconexion)
                    # raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
            except (urllib.error.URLError, IOError, http.client.BadStatusLine, socket.timeout) as e:
                print('Conexion Erronea')
                # print(e.reason)
                print(url, e)
                web = None
                # logging.debug('Error: %s; Mercado: %s; Url: %s' % (e, mercado.encode('utf-8'), url.encode('utf-8')))
                print('Pausa de %d segundos' % pausareconexion)
                sleep(pausareconexion)

            ticketfin = 0

            while True:
                try:
                    ticketinicio = web.find('data-test="quoteLink" href="/quote/', ticketfin)
                except AttributeError:
                    break
                if ticketinicio == -1:
                    break
                else:
                    ticketinicio = ticketinicio + len('data-test="quoteLink" href="/quote/')

                ticketfin = web.find('?p=', ticketinicio)
                if ticketfin == -1:
                    break

                ticket = (web[ticketinicio:ticketfin].strip())

##                # En ocasiones la cerda ticket contiene el ticket y un enlace, comprobamos que no existe este enlace:
##                if '<a href="http://finance.yahoo.com/q?s=' in ticket:  # Si que existe este enlace
##                    ticketinicio = web.find('<a href="http://finance.yahoo.com/q?s=', ticketinicio) + len('<a href="http://finance.yahoo.com/q?s=')
##                    ticketinicio = web.find('&d=t">', ticketinicio) + len('&d=t">')
##                    ticket = (web[ticketinicio:ticketfin].strip())
                ticket = ticket.upper()

                if (ticket not in ticketsanadidos) and ('%20' not in ticket):
                    ticketsanadidos.append(ticket)

        print(("%8d Tickets IPO añadidas" % (len(ticketsanadidos))))
        duerme()
    print('')
    print(("Total %8d Tickets IPO añadidas" % (len(ticketsanadidos))))
    print('')

    return ticketsanadidos


def ticketsCriptoIPO():
    """."""
    ticketsanadidos = []

    print('')
    n = 0
    for n in range (97):
        url = 'https://finance.yahoo.com/cryptocurrencies?count=100&offset=' + str(100*n)
        print(url)

        web = None
        while web is None:
            try:
                r = urllib.request.Request(url, headers=webheaders)
                f = urllib.request.urlopen(r, timeout=pausareconexion)
                web = (f.read()).decode('utf-8')
                f.close()
            except urllib.error.HTTPError as e:
                print('Conexion Perdida')
                print(e.code)
                if e.code == 500:
                    return ticketsanadidos
                else:
                    web = None
                    sleep(pausareconexion)
                    # raw_input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
            except (urllib.error.URLError, IOError, http.client.BadStatusLine, socket.timeout) as e:
                print('Conexion Erronea')
                # print(e.reason)
                print(url, e)
                web = None
                # logging.debug('Error: %s; Mercado: %s; Url: %s' % (e, mercado.encode('utf-8'), url.encode('utf-8')))
                print('Pausa de %d segundos' % pausareconexion)
                sleep(pausareconexion)

            ticketinicio = 0
            ticketfin = 0
        while True:
            ticketinicio = web.find('data-test="quoteLink" href="/quote/', ticketfin)
            if ticketinicio == -1:
                break
            else:
                ticketinicio = ticketinicio + len('data-test="quoteLink" href="/quote/')

            ticketfin = web.find('?p=', ticketinicio)
            if ticketfin == -1:
                break

            ticket = (web[ticketinicio:ticketfin].strip())
            ticket = ticket.upper()

            if (ticket not in ticketsanadidos) and ('%20' not in ticket):
                ticketsanadidos.append(ticket)

    print('')
    print("%d CriptoMonedas añadidas" % (len(ticketsanadidos)))
    print('')

    return ticketsanadidos


def descargaHistoricoAccion(naccion, **config):
    """
    Funcion para la descarga de las cotizaciones historicas de una accion.

    Parametros : naccion - nombre de la accion
                fechaini - fecha de inicio
                fechafin - fecha fin
                timming - timming
                actualizar - False/True
    el formato del las fecha debe ser AAAA-MM-DD
    Modificado desde Mayo 2017
    el formato de las fechas es en segundos, considerando la fecha 1 de enero de 1970 como el punto 0,
    apartir de ahi en segundos desde esa fecha en adelante

    las posiblidades del timming son:   d - 1 -diario
                                        w - 2 - semanal
                                        m - 3 - mensual
                                        v - 4 - muestra dividendos

    el return devuelve o:
        los datos
        que ha habido pago de dividendos 'Pago Dividendos'
        o que la url no es valida 'URL invalida'
    """

    global _cookie, webheaders#, _crumb

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

    if fechafin is None:
        fechafin = int(timegm((date.today().timetuple())))
        #fechafin = int(mktime((date.today().timetuple())))
        # anofin = str(fechafin[0])
        # mesfin = str(fechafin[1])
        # diafin = str(fechafin[2])

    else:
        fechafin = int(timegm((strptime(fechafin, "%Y-%m-%d"))))
        #fechafin = int(mktime((strptime(fechafin, "%Y-%m-%d"))))
        # anofin = (fechafin[0])
        # mesfin = (fechafin[1])
        # diafin = (fechafin[2])

    # la funcion necesaria para convertir en segundos es time.mktime

#    convertir un string de fecha en un formato determinado en una time.timetuple manejable por time.mktime para convertirla en segundos
#
#    >>> time.strptime("2017-05-25", "%Y-%m-%d")
#    time.struct_time(tm_year=2017, tm_mon=5, tm_mday=25, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=145, tm_isdst=-1)
#    >>> hoy = time.strptime("2017-05-25", "%Y-%m-%d")
#
#    >>> time.mktime(hoy)
#    1495663200.0
#    >>> hoy = time.strptime("2017-05-26", "%Y-%m-%d")
#    >>> time.mktime(hoy)
#    1495749600.0

    # mesfin = str(int(mesfin) - 1)
    # La barra de hoy no puede estar "acabada" por eso no se descarga.
    # Si la guardamos y efectivamente no esta acabada, cuando vuelva a descargar los datos
    # y al comprobar la ultima guardada con la primera descargada, no coincidiran y pensara que hay un pago de dividendos
    # diafin = str(int(diafin) - 1)
    # le restamos un dia completo
    fechafin = str(fechafin - 86400)
    # comprobandodividendo=False

    if fechaini is not None:
        fechaini = str(int(timegm((strptime(fechaini, "%Y-%m-%d")))))
        #fechaini = str(int(mktime((strptime(fechaini, "%Y-%m-%d")))))
    
    preurl = "https://query1.finance.yahoo.com/v7/finance/download/" + naccion + "?period1=0&period2=" + fechafin + "&interval=1d&events=history&includeAdjustedClose=true"

    # abrimos la pagina donde esta la informacion de las cotizaciones historicos del pais al que le corresponde la accion
    # la abrimos para hacerle creer que venimos de aqui
    # hemos observado casos donde hasta que no entrabamos en esta pagina no actualizaba correctamente la informacion en el archivo que nos descargamos posteriormente
    #if _crumb is None:  # or _cookie is None:
    #    yahoocrumb(naccion, fechaini=config.get('fechaini', None), fechafin=config.get('fechafin', None))

    if fechaini is None:  # hay un caso en el que nos puede interesar que la funcion cambie el estado de actualizar en el caso de que venga de 'actualizacionDatosHisAccion' con actualizar=True pero con fechaini=None
        actualizar = False
        url = "https://query1.finance.yahoo.com/v7/finance/download/" + naccion + "?period1=0&period2=" + fechafin + "&interval=1d&events=history&includeAdjustedClose=true" #&crumb=" + _crumb  # .decode('utf-8')
    else:
        actualizar = True
        #resto un dia a la fecha inicial porque esta descargando los datos en la actualizacion de un dia posterior al que queremos actualizar
        fechaini = str(int(fechaini) - 86400)
        url = "https://query1.finance.yahoo.com/v7/finance/download/" + naccion + "?period1=" + fechaini + "&period2=" + fechafin + "&interval=1d&events=history&includeAdjustedClose=true" #&crumb=" + _crumb  # .decode('utf-8')
    f = None
    r = urllib.request.Request(url, headers=webheaders)

    r.add_header('Referer', preurl)

    reintento = False

    while f is None:
        try:
            f = urllib.request.urlopen(r, timeout=pausareconexion)
            print(url)
            lineas = f.readlines()  # .decode('utf-8')
            f.close()
        except urllib.error.HTTPError as e:
            print((e.code))
            print('Url invalida, accion no disponible')
            print(url)
            f = None
            #_crumb = None
            #yahoocrumb(naccion, renew=True, fechaini=config.get('fechaini', None), fechafin=config.get('fechafin', None))
            # si ha reintentado y error http 401, sin autorizacion, o error 404, no encontrado, o error 301, movido
            if (reintento and not (e.code == 401)) or (e.code == 404) or (e.code == 301):
                return 'URL invalida'
            elif e.code == 401:
                logging.debug('Error: %s; Ticket: %s' % (e, naccion.encode('utf-8'), ))
                sleep(pausareconexion)
                #logging.debug('Error: %s; Ticket: %s; crumb: %s' % (e, naccion.encode('utf-8'), _crumb))
            reintento = True
        except (urllib.error.URLError, IOError, http.client.BadStatusLine, socket.timeout, http.client.IncompleteRead) as e:
            print('Conexion Perdida')
            # print(e.reason)
            print(url, e)
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, naccion.encode('utf-8'), url.encode('utf-8')))
            f = None
            print('Pausa de %d segundos' % pausareconexion)
            sleep(pausareconexion)

    if not (lineas[0] == b"Date,Open,High,Low,Close,Adj Close,Volume\n"):
        # print (lineas[0])
        print('Informacion invalida, accion no disponible')
        return 'URL invalida'
# en la mayoria de los casos, en la web el historico existe, pero la descarga del archivo no, la accion ha desaparecido y yahoo elimina el archivo sin eliminar en la web el historico

    datosaccion = BBDD.datoshistoricoslee(naccion)

    if actualizar:
        penultimoregistro = len(datosaccion) - 2
        del datosaccion[penultimoregistro:]
    else:
        datosaccion = []

    i = 1
    print('%d Registros de la accion' % (len(lineas) - 1))
    while i < len(lineas):
        linea_datos = lineas[i].decode('utf-8')
        columnas = linea_datos.split(",")
        # tengo que probar a sustituir los float por la funcion Decimal
        fecha = str(columnas[0])

        try:
            apertura = float(columnas[1])
        except ValueError:
            apertura = 0.0

        try:
            maximo = float(columnas[2])
        except ValueError:
            maximo = 0.0

        try:
            minimo = float(columnas[3])
        except ValueError:
            minimo = 0.0

        try:
            cierre = float(columnas[4])
        except ValueError:
            cierre = 0.0

        try:  # en ocasiones los datos vienen con todos los valores en 0 y el volumen null
            volumen = int(columnas[6])
        except ValueError:
            # if 'null' in columnas[6]
            volumen = 0

        try:
            cierreajustado = float(columnas[5])
        except ValueError:
            cierreajustado = 0.0

        if cierre == 0.0 or apertura == 0.0 or cierreajustado == 0.0:  # tenemos en cuenta que cierre sea 0 en ese caso no podriamos hacer la division de ajuste
            aperturaajustado = 0.0
        else:
            aperturaajustado = round(apertura * (cierreajustado / cierre), 3)
            if aperturaajustado < 0.0:
                aperturaajustado = 0.0

        if cierre == 0.0 or maximo == 0.0 or cierreajustado == 0.0:
            maximoajustado = 0.0
        else:
            maximoajustado = round(maximo * (cierreajustado / cierre), 3)
            if maximoajustado < 0.0:
                maximoajustado = 0.0

        if cierre == 0.0 or minimo == 0.0 or cierreajustado == 0.0:
            minimoajustado = 0.0
        else:
            minimoajustado = round(minimo * (cierreajustado / cierre), 3)
            if minimoajustado < 0.0:
                minimoajustado = 0.0

        cierreajustado = round(cierreajustado, 3)
        if cierreajustado < 0.0:
            cierreajustado = 0.0

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
            if (registroalmacenadoultimo != registrodescargadoprimero):  # and (registroalmacenadoultimo[0] == registrodescargadoprimero[0]):
                print('El historico ha cambiado por el pago de un dividendo, hay que hacer una descarga completa nueva')
                logging.debug('Error: Cambio historico; Ticket: %s; Parametros funcion: %s; Ultimo registro almacenado: %s; Primer registro descargado: %s ' % (naccion, str(config), str(registroalmacenadoultimo), str(registrodescargadoprimero)))
                print ('Ultimo registro almacenado: %s ' % str(registroalmacenadoultimo))
                print ('Primer registro descargado: %s ' % str(registrodescargadoprimero))
                # print 'Borrando todos los datos almacenados'
                # borraTicket(naccion, BBDD=False)
                return 'Pago Dividendos'

        else:
            datosaccion.append((fecha, aperturaajustado, maximoajustado, minimoajustado, cierreajustado, volumen))

        i += 1

    BBDD.datoshistoricosgraba(naccion, datosaccion)

    if txt:
        nombre = (str(naccion)).replace('.', '_')
        archivo = os.path.join(os.getcwd(), CARPETAS['Historicos'], nombre + '.' + timming + '.csv')
        j = open(archivo, 'w')
        writercsv = csv.writer(j, delimiter=';', lineterminator=os.linesep, doublequote=True)
        for n in datosaccion:

            fecha, apertura, maximo, minimo, cierre, volumen = n
            apertura = str(apertura).replace('.', ',')
            maximo = str(maximo).replace('.', ',')
            minimo = str(minimo).replace('.', ',')
            cierre = str(cierre).replace('.', ',')
            volumen = str(volumen).replace('.', ',')

            n = (fecha, apertura, maximo, minimo, cierre, volumen)

            writercsv.writerow(n)
            # j.write(str(n)+os.linesep)
        j.close()
    return datosaccion


def cotizacionesTicket(nombreticket):
    """."""
    nombreticket = nombreticket.upper()

    # Lista de funciones que obtienen datos
    funciones_obtencion_datos = [
        cotizacionesTicketWeb,
        cotizacionesTicketyfinance,
        # Puedes agregar cotizacionesTicketYahooFinancials u otras funciones aquí
    ]

    # Seleccionar aleatoriamente una función de la lista
    funcion_seleccionada = random.choice(funciones_obtencion_datos)

    # Obtener datos de la función seleccionada
    datosurl = funcion_seleccionada(nombreticket)

    #resultado_final = None

    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    # Ejecutar las funciones en paralelo
    #    resultado1 = executor.submit(cotizacionesTicketWeb, nombreticket)
    #    resultado2 = executor.submit(cotizacionesTicketyfinance, nombreticket)
    #    resultado3 = executor.submit(cotizacionesTicketYahooFinancials, nombreticket)

        # Obtener el resultado de la primera función que termine
    #    resultados_terminados, _ = concurrent.futures.wait(
    #        [resultado1, resultado2], #, resultado3],
    #        return_when=concurrent.futures.FIRST_COMPLETED
    #    )

        # Obtener y comparar resultados
    #    for resultado_terminado in resultados_terminados:
    #        datosurl = resultado_terminado.result()
    #        print(f"Resultado de la función  :{datosurl}")

            # Almacenar el resultado y cancelar las funciones restantes
    #        resultado_final = resultado_terminado
    #        for resultado_pendiente in [resultado1, resultado2]:#, resultado3]:
    #            if resultado_pendiente != resultado_terminado and not resultado_pendiente.done():
    #                resultado_pendiente.cancel()

    #if resultado_final is not None:
    #    print("Resultado General :" + resultado_final.result())

    #print(f"Resultado de la función: {datosurl}")

    # Comparar resultados aleatoriamente entre dos funciones
    if random.random() < 0.1:  # 10% de probabilidad de comparar resultados
        otra_funcion = random.choice([f for f in funciones_obtencion_datos if f != funcion_seleccionada])
        datosurl_otra_funcion = otra_funcion(nombreticket)

        if datosurl[3:] != datosurl_otra_funcion[3:]: #solo compara los datos que corresponden a datomax52, datomaxDia, datomin52, datominDia, datoValorActual, datovolumenMedio, datovolumen, datoerror
                                                      #no comparamos los datos que corresponden a datonombre, datoticket, datomercado porque el datomercado cambia en funcion del modo obtenido
            print("¡Alerta! Los resultados no son iguales entre dos funciones.")
            print(datosurl[3:])
            print(datosurl_otra_funcion[3:])
            logging.debug('Error: %s; Ticket: %s' % ("Resultados de funciones obtencion de datos cotizacion dispares", nombreticket.encode('utf-8')))

    if __name__ != '__main__':
        BBDD.ticketcotizaciones(nombreticket, datosurl)

    return datosurl


def cotizacionesTicketWeb(nombreticket):
    """."""
    nombreticket = nombreticket.upper()
    # habilitar en la funcion la posibilidad de descargar multiples tickets, tienen que ir separados o unidos por '+'
    # Tendriamos que separar nombreticket con un split y obtener una lista, comprobar la longitud de la misma, hacer la descarga, leer las lineas, comparar la lista inicial con la lista obtenida, crear un bucle en el else despues del try de la conxion en el que actualiza la BBDD

    error = 'null'

    web = None

        # datonombre, datoticket, datomercado, datomax52, datomaxDia, datomin52, datominDia, datoValorActual, datovolumenMedio, datovolumen, datoerror
        # "Apple Inc.","AAPL","NasdaqNM",705.07,N/A,419.00,N/A,431.144,20480200,6870,null
    
    #reintentos = 0
    #while (datos == None or datos2 == None) and reintentos <= 1:
    
    urldatos = "https://finance.yahoo.com/quote/" + nombreticket + "?p=" + nombreticket
    r = urllib.request.Request(urldatos, headers=webheaders)

    while web is None:
        try:
            f = urllib.request.urlopen(r, timeout=pausareconexion)
            web = f.read().decode('utf-8')
            f.close()
        except urllib.error.HTTPError as e:
            print('Conexion Perdida')
            print(e.code)
            web = None
            if e.code == 301 or e.code == 404:
                error = 'No such ticker symbol'
                web = ""
            sleep(pausareconexion)
            # input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
        except (urllib.error.URLError, IOError, http.client.BadStatusLine, socket.timeout) as e:
            print('Conexion Erronea')
            print(e)
            web = None
            logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, nombreticket.encode('utf-8'), urldatos.encode('utf-8')))
            print('Pausa de %d segundos' % pausareconexion)
            sleep(pausareconexion)
        except UnicodeDecodeError:
            print(f.read())
            #print(nombreticket)


    if not (web == None):
        inicio = web.find('h1 class="') + len('h1 class="')
        inicio = web.find('>',inicio) + len('>')
        fin = web.find("("+nombreticket+")</h1>", inicio)  # - len(nombreticket) - 2
        # print(web)
        datonombre = web[inicio:fin].strip()
        datonombre = datonombre.strip('"')
        datonombre = datonombre.replace('"', '')
        if len(datonombre) > 300:
            error = 'No such ticker symbol'
    else:
        datonombre = 'null'
        error = 'No such ticker symbol'
        
    if not (web == None):
        inicio = fin
        inicio = web.find('<span>', inicio) + len('<span>')
        fin = web.find(' - ', inicio)
        if 'Currency in' in web[inicio:fin].strip() or len (web[inicio:fin].strip()) > 150:
            #fin = web.find('</span>', inicio)
            fin = web.find(' . ', inicio)       
        datomercado = web[inicio:fin].strip()
        if len(datomercado) > 150:
            error = 'No such ticker symbol'
    else:
        datomercado = 'null'
        error = 'No such ticker symbol'

    if not (web == None):
        inicio = web.find('data-test="PREV_CLOSE-value">') + len('data-test="PREV_CLOSE-value">')
        fin = web.find('</td>', inicio)
        try:
            datoValorActual = float(web[inicio:fin].replace(',', '.'))
        except ValueError:
            datoValorActual = 'null'
    else:
        datoValorActual = 'null'

    if not (web == None):
        # Con el mercado abierto este datos es correcto buscarlo asi
        inicio = web.find('data-test="DAYS_RANGE-value">') + len('data-test="DAYS_RANGE-value">')
        fin = web.find(' - ', inicio)
        try:
            datominDia = round(float(web[inicio:fin].replace(',', '.')), 3)  # Este dato puede se N/A, no siendo posible la conversion a float
        except ValueError:
            datominDia = 'null'
        inicio = fin + len(' - ')
        fin = web.find('</td>', inicio)
        try:
            datomaxDia = round(float(web[inicio:fin].replace(',', '.')), 3)  # Este dato puede se N/A, no siendo posible la conversion a float
        except ValueError:
            datomaxDia = 'null'
    else:
        datominDia = 'null'
        datomaxDia = 'null'

    if not (web == None):
        inicio = web.find('data-test="FIFTY_TWO_WK_RANGE-value">') + len('data-test="FIFTY_TWO_WK_RANGE-value">')
        fin = web.find(' - ', inicio)
        try:
            datomin52 = round(float(web[inicio:fin].replace(',', '.')), 3)
        except ValueError:
            datomin52 = 'null'
        inicio = fin + len(' - ')
        fin = web.find('</td>', inicio)
        try:
            datomax52 = round(float(web[inicio:fin].replace(',', '.')), 3)
        except ValueError:
            datomax52 = 'null'
    else:
        datomin52 = 'null'
        datomax52 = 'null'

    if not (web == None):
        inicio = web.find('data-field="regularMarketVolume"') + len('data-field="regularMarketVolume"')
        inicio = web.find('>', inicio) + len ('>')
        fin = web.find('</', inicio)
        try:
            datovolumen = int((web[inicio:fin].replace(',', '')).replace('.', ''))
        except ValueError:
            datovolumen = 'null'
    else:
        datovolumen = 'null'

    if not (web == None):
        inicio = web.find('data-test="AVERAGE_VOLUME_3MONTH-value">') + len('data-test="AVERAGE_VOLUME_3MONTH-value">')
        fin = web.find('</td>', inicio)
        try:
            datovolumenMedio = int((web[inicio:fin].replace(',', '')).replace('.', ''))
        except ValueError:
            datovolumenMedio = 'null'
    else:
        datovolumenMedio = 'null'
    # "CEWE Stiftung &amp; Co. KGaA","CWC.SW","Swiss",92.6,None,73.1,None,73.1,0,None,null
    datosurl = ('"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,%s' % (datonombre,
                                                            nombreticket,
                                                            datomercado,
                                                            str(datomax52).replace('None', 'null'),
                                                            str(datomaxDia).replace('None', 'null'),
                                                            str(datomin52).replace('None', 'null'),
                                                            str(datominDia).replace('None', 'null'),
                                                            str(datoValorActual).replace('None', 'null'),
                                                            str(datovolumenMedio).replace('None', 'null'),
                                                            str(datovolumen).replace('None', 'null'),
                                                            error))

    print ("Datos de WEB             :" + datosurl)

    return datosurl

def cotizacionesTicketYahooFinancials(nombreticket):
    """."""
    nombreticket = nombreticket.upper()
    # habilitar en la funcion la posibilidad de descargar multiples tickets, tienen que ir separados o unidos por '+'
    # Tendriamos que separar nombreticket con un split y obtener una lista, comprobar la longitud de la misma, hacer la descarga, leer las lineas, comparar la lista inicial con la lista obtenida, crear un bucle en el else despues del try de la conxion en el que actualiza la BBDD

    error = 'null'

    datos = None
    datos2 = None

        # datonombre, datoticket, datomercado, datomax52, datomaxDia, datomin52, datominDia, datoValorActual, datovolumenMedio, datovolumen, datoerror
        # "Apple Inc.","AAPL","NasdaqNM",705.07,N/A,419.00,N/A,431.144,20480200,6870,null
    
    yahoo = YahooFinancials(nombreticket)

    #reintentos = 0
    #while (datos == None or datos2 == None) and reintentos <= 1:
    try:
        datos = yahoo.get_summary_data()
        datos2 = yahoo.get_stock_quote_type_data()
    except Exception as e:
        #duerme()
        logging.debug('Error: %s; Ticket: %s' % (e, nombreticket.encode('utf-8')))
        #print (nombreticket)
        #print (datos)
        #print (datos2)
    #    print (reintentos)
    #    reintentos= reintentos+1


    if not (datos == None and datos2 == None) and 'longName' in datos[nombreticket]:
        datonombre = datos2[nombreticket]['longName']
        datonombre = datonombre.strip('"')
        datonombre = datonombre.replace('"', '')
    else:
        datonombre = 'null'
        error = 'No such ticker symbol'
        
    if not (datos == None and datos2 == None) and 'exchange' in datos[nombreticket]:
        #datomercado = datos2[nombreticket]['market']
        datomercado = datos2[nombreticket]['exchange']
    else:
        datomercado = 'null'
        error = 'No such ticker symbol'

    if not (datos == None and datos2 == None) and 'regularMarketPreviousClose' in datos[nombreticket]:
        datoValorActual = datos[nombreticket]['regularMarketPreviousClose']
    else:
        datoValorActual = 'null'

    if not (datos == None and datos2 == None) and 'regularMarketDayLow' in datos[nombreticket] and 'regularMarketDayHigh' in datos[nombreticket]:
        #datominDia = datos[nombreticket]['dayLow']
        datominDia = datos[nombreticket]['regularMarketDayLow']
        #datomaxDia = datos[nombreticket]['dayHigh']
        datomaxDia = datos[nombreticket]['regularMarketDayHigh']
    else:
        datominDia = 'null'
        datomaxDia = 'null'

    if not (datos == None and datos2 == None) and 'fiftyTwoWeekLow' in datos[nombreticket] and 'fiftyTwoWeekHigh' in datos[nombreticket]:
        datomin52 = datos[nombreticket]['fiftyTwoWeekLow']
        datomax52 = datos[nombreticket]['fiftyTwoWeekHigh']
    else:
        datomin52 = 'null'
        datomax52 = 'null'

    if not (datos == None and datos2 == None) and 'regularMarketVolume' in datos[nombreticket]:
        datovolumen = datos[nombreticket]['regularMarketVolume']
    else:
        datovolumen = 'null'

    if not (datos == None and datos2 == None) and 'averageVolume' in datos[nombreticket]:
        datovolumenMedio = datos[nombreticket]['averageVolume']
    else:
        datovolumenMedio = 'null'
    # "CEWE Stiftung &amp; Co. KGaA","CWC.SW","Swiss",92.6,None,73.1,None,73.1,0,None,null
    datosurl = ('"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,%s' % (datonombre,
                                                            nombreticket,
                                                            datomercado,
                                                            str(datomax52).replace('None', 'null'),
                                                            str(datomaxDia).replace('None', 'null'),
                                                            str(datomin52).replace('None', 'null'),
                                                            str(datominDia).replace('None', 'null'),
                                                            str(datoValorActual).replace('None', 'null'),
                                                            str(datovolumenMedio).replace('None', 'null'),
                                                            str(datovolumen).replace('None', 'null'),
                                                            error))

    print ("Datos de YahooFinancials :" + datosurl)

    return datosurl

def cotizacionesTicketyfinance(nombreticket):
    """."""
    nombreticket = nombreticket.upper()
    # habilitar en la funcion la posibilidad de descargar multiples tickets, tienen que ir separados o unidos por '+'
    # Tendriamos que separar nombreticket con un split y obtener una lista, comprobar la longitud de la misma, hacer la descarga, leer las lineas, comparar la lista inicial con la lista obtenida, crear un bucle en el else despues del try de la conxion en el que actualiza la BBDD

    error = 'null'

    datos = None

        # datonombre, datoticket, datomercado, datomax52, datomaxDia, datomin52, datominDia, datoValorActual, datovolumenMedio, datovolumen, datoerror
        # "Apple Inc.","AAPL","NasdaqNM",705.07,N/A,419.00,N/A,431.144,20480200,6870,null
    
    yahoo = yf.Ticker(nombreticket)

    #reintentos = 0
    #while (datos == None or datos2 == None) and reintentos <= 1:
    try:
        datos = yahoo.info
    except Exception as e:
        #duerme()
        logging.debug('Error: %s; Ticket: %s' % (e, nombreticket.encode('utf-8')))
        print (nombreticket)
        print (datos)
    #    print (reintentos)
    #    reintentos= reintentos+1


    if not (datos == None) and 'longName' in datos:
        datonombre = datos['longName']
        datonombre = datonombre.strip('"')
        datonombre = datonombre.replace('"', '')
    else:
        datonombre = 'null'
        error = 'No such ticker symbol'
        
    if not (datos == None) and 'exchange' in datos:
        #datomercado = datos2[nombreticket]['market']
        datomercado = datos['exchange']
    else:
        datomercado = 'null'
        error = 'No such ticker symbol'

    if not (datos == None) and 'regularMarketPreviousClose' in datos:
        datoValorActual = datos['regularMarketPreviousClose']
    else:
        datoValorActual = 'null'

    if not (datos == None) and 'regularMarketDayLow' in datos and 'regularMarketDayHigh' in datos:
        #datominDia = datos['dayLow']
        datominDia = datos['regularMarketDayLow']
        #datomaxDia = datos['dayHigh']
        datomaxDia = datos['regularMarketDayHigh']
    else:
        datominDia = 'null'
        datomaxDia = 'null'

    if not (datos == None) and 'fiftyTwoWeekLow' in datos and 'fiftyTwoWeekHigh' in datos:
        datomin52 = datos['fiftyTwoWeekLow']
        datomax52 = datos['fiftyTwoWeekHigh']
    else:
        datomin52 = 'null'
        datomax52 = 'null'

    if not (datos == None) and 'regularMarketVolume' in datos:
        datovolumen = datos['regularMarketVolume']
    else:
        datovolumen = 'null'

    if not (datos == None) and 'averageVolume' in datos:
        datovolumenMedio = datos['averageVolume']
    else:
        datovolumenMedio = 'null'
    # "CEWE Stiftung &amp; Co. KGaA","CWC.SW","Swiss",92.6,None,73.1,None,73.1,0,None,null
    datosurl = ('"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,%s' % (datonombre,
                                                            nombreticket,
                                                            datomercado,
                                                            str(datomax52).replace('None', 'null'),
                                                            str(datomaxDia).replace('None', 'null'),
                                                            str(datomin52).replace('None', 'null'),
                                                            str(datominDia).replace('None', 'null'),
                                                            str(datoValorActual).replace('None', 'null'),
                                                            str(datovolumenMedio).replace('None', 'null'),
                                                            str(datovolumen).replace('None', 'null'),
                                                            error))

    print ("Datos de yFinance        :" + datosurl)

    return datosurl


def cotizacionesMoneda(nombreticket):
    """."""
    nombreticket = nombreticket.upper()
    datos = None
    yahoo = yf.Ticker(nombreticket)
    try:
        datos = yahoo.info
    except Exception as e:
        #duerme()
        logging.debug('Error: %s; Ticket: %s' % (e, nombreticket.encode('utf-8')))
        print (nombreticket)
        print (datos)

    if not (datos == None) and 'regularMarketPreviousClose' in datos:
        datoValorActual = datos['regularMarketPreviousClose']
    else:
        datoValorActual = '0'
    
    # urldatos = "https://finance.yahoo.com/quote/" + nombreticket.replace("=", "%3D") + "?p=" + nombreticket.replace("=", "%3D")
    # web = None
    # r = urllib.request.Request(urldatos, headers=webheaders)
    # 
    # while web is None:
    #     try:
    #         f = urllib.request.urlopen(r, timeout=pausareconexion)
    #         web = f.read().decode('utf-8')
    #         f.close()
    #     except urllib.error.HTTPError as e:
    #         print('Conexion Perdida')
    #         print((e.code))
    #         web = None
    #         sleep(pausareconexion)
    #         # input('Pulsa una tecla cuando este reestablecida la conexion para continuar')
    #     except (urllib.error.URLError, IOError, http.client.BadStatusLine, socket.timeout) as e:
    #         print('Conexion Erronea')
    #         print(e)
    #         web = None
    #         logging.debug('Error: %s; Ticket: %s; Url: %s' % (e, nombreticket.encode('utf-8'), urldatos.encode('utf-8')))
    #         print(('Pausa de %d segundos' % pausareconexion))
    #         sleep(pausareconexion)
    #     except UnicodeDecodeError:
    #         print((f.read()))
    #         print(nombreticket)
    # 
    # inicio = web.find('data-symbol="'+nombreticket+'"')
    # inicio = web.find('data-field="regularMarketPrice"',inicio) + len('data-field="regularMarketPrice"')
    # inicio = web.find('">',inicio) + len ('">')
    # fin = web.find('</', inicio)
    # 
    # try:
    #     datoValorActual = float(web[inicio:fin].replace(',', '.'))
    # except ValueError:
    #     # Esta busqueda se debe a que el mercado al que pertenece el valor esta cerrado o aun no cotiza
    #     inicio = web.find('data-test="PREV_CLOSE-value">') + len('data-test="PREV_CLOSE-value">')
    #     fin = web.find('</td>', inicio)
    #     try:
    #         datoValorActual = float(web[inicio:fin].replace(',', '.'))
    #     except ValueError:
    #         datoValorActual = 'null'

    datos = ("%s,%s" % (nombreticket, datoValorActual))

    BBDD.monedacotizaciones(nombreticket, datos)

    return datos


def subirtimming(datos, **config):
    """
    Pasa un timming inferior a uno superior, el orden seria diario, semana y mensual.

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
    """
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
            fechaagr = list(map(int, (((datos[0][fechadatos]).split('-')))))
            fechaagr = (date(fechaagr[0], fechaagr[1], fechaagr[2]))
            fechaagr += timedelta(days=6 - fechaagr.weekday())

        i = 0
        while i < len(datos):
            fecha = datos[i][fechadatos]
            fecha = strptime(fecha, '%Y-%m-%d')
# FIXME : en mensual es correcto, cuando cambia de ANO y MES, pero en semanal hay que acumular de domingo a domingo, siendo el corte el domingo siguiente
            if ((timming == 'm' and fechaagr != strftime('%Y, %m', fecha)) or (timming == 'w' and datos[i][fechadatos] >= str(fechaagr))) and i != inicio:
                if timming == 'm':
                    fechaagr = strftime('%Y, %m', fecha)
                elif timming == 'w':
                    fechaagr = list(map(int, (((datos[i][fechadatos]).split('-')))))
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


# def yahoocrumb(naccion, **config):
#     """Funcion para la descarga de la cookie o campo crumb
# 
#     Parametros : naccion - nombre de la accion
#                 fechaini - fecha de inicio
#                 fechafin - fecha fin
#     el formato del las fecha debe ser AAAA-MM-DD
#     Modificado desde Mayo 2017
#     el formato de las fechas es en segundos, considerando la fecha 1 de enero de 1970 como el punto 0,
#     apartir de ahi en segundos desde esa fecha en adelante
# 
#     el return devuelve valor de crumb
#     """
#     global cookier, _cookie, _crumb
# 
#     # Perform a Yahoo financial lookup on SP500
#     cookier.cookiejar.clear()
# 
#     naccion = naccion.upper()
#     fechaini = config.get('fechaini', None)
#     fechafin = config.get('fechafin', None)
# 
#     if fechafin is None:
#         fechafin = int(mktime((date.today().timetuple())))
# 
#     else:
# 
#         fechafin = int(mktime((strptime(fechafin, "%Y-%m-%d"))))
#     fechafin = str(fechafin - 86400)
# 
#     if fechaini is not None:
#         fechaini = str(int(mktime((strptime(fechaini, "%Y-%m-%d")))))
# 
#     preurl = "https://finance.yahoo.com/quote/" + naccion + "/history?period1=0&period2=" + fechafin + "&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
#     #     logging.debug('Error: Falta relacion Prefijo-Sufijo; Sufijo: %s' % sufijo)
# 
#     r1 = urllib.request.Request(preurl, headers=webheaders)
# 
#     alines = None
#     while alines is None:
#         try:
#             f1 = urllib.request.urlopen(r1, timeout=pausareconexion)
#             # prevenir: type (aline)
#             #           <class 'bytes'>
#             alines = f1.read().decode('utf-8')
#             f1.close()
#         except urllib.error.HTTPError as e:
#             print((e.code))
#             print('Url invalida, accion no disponible')
#             print(preurl)
#             alines = None
#         except (KeyboardInterrupt, urllib.error.URLError, IOError, http.client.BadStatusLine, socket.timeout, http.client.IncompleteRead) as e:
#             print('Conexion Perdida')
#             # print(e.reason)
#             print((preurl, e))
#             logging.debug('Error: %s; Ticket: %s; PreUrl: %s' % (e, naccion.encode('utf-8'), preurl.encode('utf-8')))
#             alines = None
#         finally:
#             print('Pausa de 1 segundo')
#             duerme(tiempo=1000)
# 
#     crumbinweb = (('"CrumbStore":{"crumb":"', '"}'),
#                   ('"],"crumb":"', '","'),
#                   (':{"user":{"crumb":"', '","'),
#                   ('&crumb=', '&')
#                   )
# 
#     crumbOK = False
#     while crumbOK is False:
#         # TODO: limitar el len(crumb) a la longitud que debe de tener hasta que localice y encuentre el verdadero crumb, utilizando los distintos formatos de busqueda
#         for (ini, fin) in crumbinweb:
#             if alines.find(ini) != -1:
#                 crumbini = alines.find(ini) + len(ini)
#                 crumbfin = alines.find(fin, crumbini)
#                 crumb = alines[crumbini:crumbfin].strip()
#                 # crumb = crumb.decode('unicode_escape','ignore')
#                 # crumb = crumb.encode('utf-8')
#                 # crumb = str(crumb)
#                 crumb = crumb.replace('\\u002F', '/')
#                 if len(crumb) <= 12:
#                     crumbOK = True
#                     break
#                 else:
#                     print(crumb)
# 
#     # Extract the crumb from the response
#     # cs = alines.find('CrumbStore')
#     # cr = alines.find('crumb', cs + 10)
#     # cl = alines.find(':', cr + 5)
#     # q1 = alines.find('"', cl + 1)
#     # q2 = alines.find('"', q1 + 1)
#     # crumb = alines[q1 + 1:q2]
#     _crumb = crumb
# 
#     # Extract the cookie from cookiejar
#     for c in cookier.cookiejar:
#         # print(c)
#         if c.domain != '.yahoo.com':
#             continue
#         if c.name != 'B':
#             continue
#         _cookie = c.value
# 
#     print('Cookie:', _cookie)
#     print('Crumb:', _crumb)
#     # return _crumb


if __name__ == '__main__':
    _test()
