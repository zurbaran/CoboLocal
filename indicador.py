# /usr/bin/python
# -*- coding: UTF-8 -*-
"""
indicador.py - v0.02 2013-07-16 Antonio Caballero, Paco Corbi

Este modulo proporciona los indicadores utilizados en el resto de modulos

License: http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode
"""

__version__ = '0.02'
__date__ = '2013-07-16'
__author__ = 'Antonio Caballero, Paco Corbi'

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

"""
Ejemplos de datos tomados en la accion ticket MSG

"""
from datetime import date


def _test():
    import doctest
    doctest.testmod()
    # pruebas doctest
    # ejemplos en : http://mundogeek.net/archivos/2008/09/17/pruebas-en-python/  http://magmax9.blogspot.com.es/2011/09/python-como-hacer-pruebas-1.html
    # Externalizar los test
    # doctest.testfile('example2.txt')


def MME(datos, **config):
    """
    devuelve de la lista, datos, el indicadorMME calculado
    indicedatos, es el valor del indice de las tuplas de datos al que se utiliza para calcular el indicador, por defecto 4 que corresponde al precio de cierre.

    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> MME(datos)
    [('2010-01-25', 19.6), ('2010-02-01', 19.594), ('2010-03-01', 19.731), ('2010-04-01', 19.797), ('2010-05-03', 19.879), ('2010-06-01', 19.866), ('2010-07-01', 19.825), ('2010-08-02', 19.808), ('2010-09-01', 19.89), ('2010-10-01', 19.95), ('2010-11-01', 20.078), ('2010-12-01', 20.446), ('2011-01-03', 20.754), ('2011-02-01', 21.253), ('2011-03-01', 21.623), ('2011-04-01', 21.993), ('2011-05-02', 22.349), ('2011-06-01', 22.683), ('2011-07-01', 22.929), ('2011-08-01', 23.009), ('2011-09-01', 22.995), ('2011-10-03', 23.217), ('2011-11-01', 23.598), ('2011-12-01', 23.923), ('2012-01-03', 24.23), ('2012-02-01', 24.722), ('2012-03-01', 25.334), ('2012-04-02', 26.02), ('2012-05-01', 26.76), ('2012-06-01', 27.449), ('2012-07-02', 28.148)]
    """
    # para los indicadores como la Media Movil 30 en la que en los primeros 29 periodos no se puede calcular, hay que asignarles valor 0

    n = int(config.get('MME', 30))
    numberound = config.get('numberound', True)
    indicedatos = config.get('indicedatos', 'cierre')
    indicedatos = ('fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'volumen').index(indicedatos)

    resultado = []

    k = (2.0 / (1.0 + n))
    for iMME in range(0, len(datos)):
        fechaMME = datos[iMME][0]
        cierreMME = datos[iMME][indicedatos]
        if iMME == 0:
            puntoMME = datos[iMME][indicedatos]  # Este es el pirmer cierre de los datos historicos
        else:
            puntoMME = (cierreMME * k) + (puntoMME * (1 - k))

        if indicedatos == 5:
            resultado.append((fechaMME, int(puntoMME)))
        else:
            if numberound == True:
                resultado.append((fechaMME, round(puntoMME, 3)))
            else:
                resultado.append((fechaMME, puntoMME))

    return (resultado)


def TR(datos, **config):
    """
    True Range

    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> TR(datos)
    [('2010-01-25', 0.0), ('2010-02-01', 4.41), ('2010-03-01', 3.47), ('2010-04-01', 2.17), ('2010-05-03', 3.86), ('2010-06-01', 3.06), ('2010-07-01', 3.52), ('2010-08-02', 2.39), ('2010-09-01', 1.93), ('2010-10-01', 1.42), ('2010-11-01', 3.16), ('2010-12-01', 3.92), ('2011-01-03', 2.13), ('2011-02-01', 4.92), ('2011-03-01', 3.07), ('2011-04-01', 3.39), ('2011-05-02', 1.83), ('2011-06-01', 2.26), ('2011-07-01', 1.67), ('2011-08-01', 5.09), ('2011-09-01', 2.76), ('2011-10-03', 6.16), ('2011-11-01', 5.16), ('2011-12-01', 2.08), ('2012-01-03', 2.05), ('2012-02-01', 4.8), ('2012-03-01', 2.83), ('2012-04-02', 2.43), ('2012-05-01', 3.57), ('2012-06-01', 2.78), ('2012-07-02', 2.25)]
    """
    numberound = config.get('numberound', True)
    listaTR = []

    for i in range(0, len(datos)):

        fecha, _apertura, maximo, minimo, _cierre, _volumen = datos[i]
        if i == 0:
            valorTR = 0.0  # round(max((abs(maximo - minimo), abs(maximo - cierre), abs(minimo - cierre))), 3)
        else:
            ant = i - 1
            _fechaanterior, _aperturaanterior, _maximoanterior, _minimoanterior, cierreanterior, _volumenanterior = datos[ant]
            if numberound == True:
                valorTR = round(max((abs(maximo - minimo), abs(maximo - cierreanterior), abs(minimo - cierreanterior))), 3)
            else:
                valorTR = max((abs(maximo - minimo), abs(maximo - cierreanterior), abs(minimo - cierreanterior)))

        listaTR.append((fecha, valorTR))
    assert len(listaTR) == len(datos)
    return (listaTR)


def TAR(datos, **config):
    """
    True Averange Range
    TAR = Entero

    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> TAR(datos)
    [('2010-01-25', 0.0), ('2010-02-01', 2.205), ('2010-03-01', 2.627), ('2010-04-01', 2.513), ('2010-05-03', 2.782), ('2010-06-01', 2.828), ('2010-07-01', 2.927), ('2010-08-02', 2.86), ('2010-09-01', 2.757), ('2010-10-01', 2.623), ('2010-11-01', 2.672), ('2010-12-01', 2.776), ('2011-01-03', 2.726), ('2011-02-01', 2.883), ('2011-03-01', 3.102), ('2011-04-01', 3.029), ('2011-05-02', 2.912), ('2011-06-01', 2.919), ('2011-07-01', 2.762), ('2011-08-01', 2.907), ('2011-09-01', 2.853), ('2011-10-03', 3.122), ('2011-11-01', 3.353), ('2011-12-01', 3.4), ('2012-01-03', 3.321), ('2012-02-01', 3.384), ('2012-03-01', 3.434), ('2012-04-02', 3.256), ('2012-05-01', 3.291), ('2012-06-01', 3.248), ('2012-07-02', 3.278)]
    """
    n = int(config.get('TAR', 14))
    numberound = config.get('numberound', True)

    listaTR = TR(datos, numberound=False)
    assert len(datos) == len(listaTR)

    valoresTR = []
    listaTAR = []

    for i in range(0, len(listaTR)):
        assert datos[i][0] == listaTR[i][0]  # Comprobamos que cohinciden las fechas

        inicio = (i + 1) - n
        if inicio < 0:
            inicio = 0

        fecha, valorTR = listaTR[i]
        valoresTR.append(valorTR)

        valorTAR = (sum(valoresTR[inicio:])) / (len(valoresTR[inicio:]))
        if numberound == True:
            listaTAR.append((fecha, round(valorTAR, 3)))
        else:
            listaTAR.append((fecha, valorTAR))

    assert len(datos) == len(listaTAR)
    return (listaTAR)


def DM(datos, **config):
    """
    Directional Move Indicator
    Formato (fecha,DM+,DM-)

    datos de prorealtime
    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> DM(datos)
    [('2010-01-25', 0.0, 0.0), ('2010-02-01', 0, 3.15), ('2010-03-01', 1.33, 0), ('2010-04-01', 0.62, 0), ('2010-05-03', 0, 1.84), ('2010-06-01', 0, 0), ('2010-07-01', 0, 0.54), ('2010-08-02', 0, 0), ('2010-09-01', 0.11, 0), ('2010-10-01', 0.74, 0), ('2010-11-01', 1.5, 0), ('2010-12-01', 2.42, 0), ('2011-01-03', 0.21, 0), ('2011-02-01', 3.9, 0), ('2011-03-01', 0, 0), ('2011-04-01', 0.5, 0), ('2011-05-02', 0, 1.07), ('2011-06-01', 0.41, 0), ('2011-07-01', 0, 0), ('2011-08-01', 0, 4.6), ('2011-09-01', 0, 0), ('2011-10-03', 2.48, 0), ('2011-11-01', 2.51, 0), ('2011-12-01', 0.58, 0), ('2012-01-03', 0, 0.34), ('2012-02-01', 3.49, 0), ('2012-03-01', 1.16, 0), ('2012-04-02', 1.53, 0), ('2012-05-01', 2.72, 0), ('2012-06-01', 0, 0.38), ('2012-07-02', 1.84, 0)]
    """
    listaDM = []
    numberound = config.get('numberound', True)

    for i in range(0, len(datos)):

        fecha, _apertura, maximo, minimo, _cierre, _volumen = datos[i]
        if i == 0:
            listaDM.append((fecha, 0.0, 0.0))
        else:
            ant = i - 1
            _fechaanterior, _aperturaanterior, maximoanterior, minimoanterior, _cierreanterior, _volumenanterior = datos[ant]

            if numberound == True:
                deltamaximo = max(0, round(maximo - maximoanterior, 3))
                deltaminimo = max(0, round(minimoanterior - minimo, 3))
            else:
                deltamaximo = max(0, maximo - maximoanterior)
                deltaminimo = max(0, minimoanterior - minimo)

            if (deltamaximo == 0 and deltaminimo == 0) or deltamaximo == deltaminimo:
                deltamaximo = 0
                deltaminimo = 0
            elif deltamaximo > deltaminimo:
                deltaminimo = 0
            elif deltamaximo < deltaminimo:
                deltamaximo = 0

            listaDM.append((fecha, deltamaximo, deltaminimo))

    assert len(listaDM) == len(datos)
    return (listaDM)


def ADM(datos, **config):
    """
    Average Directional Move Indicator
    periodos = Entero
    Formato (fecha,ADM+,ADM-)

    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> ADM(datos)
    [('2010-01-25', 0.0, 0.0), ('2010-02-01', 0.0, 3.15), ('2010-03-01', 1.33, 3.15), ('2010-04-01', 1.95, 3.15), ('2010-05-03', 1.95, 4.99), ('2010-06-01', 1.95, 4.99), ('2010-07-01', 1.95, 5.53), ('2010-08-02', 1.95, 5.53), ('2010-09-01', 2.06, 5.53), ('2010-10-01', 2.8, 5.53), ('2010-11-01', 4.3, 5.53), ('2010-12-01', 6.72, 5.53), ('2011-01-03', 6.93, 5.53), ('2011-02-01', 10.83, 5.53), ('2011-03-01', 10.83, 5.53), ('2011-04-01', 10.556, 5.135), ('2011-05-02', 9.802, 5.838), ('2011-06-01', 9.512, 5.421), ('2011-07-01', 8.833, 5.034), ('2011-08-01', 8.202, 9.274), ('2011-09-01', 7.616, 8.612), ('2011-10-03', 9.552, 7.997), ('2011-11-01', 11.38, 7.426), ('2011-12-01', 11.147, 6.895), ('2012-01-03', 10.351, 6.743), ('2012-02-01', 13.101, 6.261), ('2012-03-01', 13.326, 5.814), ('2012-04-02', 13.904, 5.399), ('2012-05-01', 15.631, 5.013), ('2012-06-01', 14.514, 5.035), ('2012-07-02', 15.317, 4.675)]
    """
    n = int(config.get('ADM', 14))
    numberound = config.get('numberound', True)

    listaDM = DM(datos, numberound=False)

    assert len(datos) == len(listaDM)  # Comprobamos que tienen la misma cantidad de datos

    listaADM = []
    # valorADMas=0.0
    # valorADMenos=0.0

    valoresDMas = []
    valoresDMenso = []
    valorADMas = 0.0
    valorADMenos = 0.0

    for i in range(0, len(listaDM)):
        assert datos[i][0] == listaDM[i][0]  # Comprobamos que cohinciden las fechas

        inicio = (i + 1) - n
        if inicio < 0:
            inicio = 0

        fecha, valorDMas, valorDMenos = listaDM[i]
        valoresDMas.append(valorDMas)
        valoresDMenso.append(valorDMenos)

        if i <= n:
            valorADMas = valorADMas + valorDMas
            valorADMenos = valorADMenos + valorDMenos
        else:
            valorADMas = valorADMas - (valorADMas / n) + valorDMas
            valorADMenos = valorADMenos - (valorADMenos / n) + valorDMenos

# #        valorADMas = (sum(valoresDMas[inicio:])) / (len(valoresDMas[inicio:]))
# #        valorADMenos = (sum(valoresDMenso[inicio:])) / (len(valoresDMenso[inicio:]))

        if numberound == True:
            listaADM.append((fecha, round(valorADMas, 3), round(valorADMenos, 3)))
        else:
            listaADM.append((fecha, valorADMas, valorADMenos))
# #        if i <= n:
# #            listaADM.append((fecha, listaDM[i][1] * (1 / n), listaDM[i][2] * (1 / n)))
# #        else:
# #            listaADMultimo=listaADM[-1]
# #            listaADM.append((fecha,
# #                             (listaADMultimo[1] * (n - 1 / n)) + (listaDM[i][1] * (1 / n)),
# #                             (listaADMultimo[2] * (n - 1 / n)) + (listaDM[i][2] * (1 / n))))

    assert len(datos) == len(listaADM)  # Comprobamos que el resultado contiene la misma cantidad de datos que el origen
    return (listaADM)


def DI(datos, **config):
    """
    Directional Index
    Formato (fecha,DI+,DI-)

    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> DI(datos)
    [('2010-01-25', 0.0, 0.0), ('2010-02-01', 0.0, 71.429), ('2010-03-01', 16.878, 39.975), ('2010-04-01', 19.403, 31.343), ('2010-05-03', 14.019, 35.873), ('2010-06-01', 11.491, 29.405), ('2010-07-01', 9.517, 26.989), ('2010-08-02', 8.523, 24.17), ('2010-09-01', 8.303, 22.289), ('2010-10-01', 10.675, 21.083), ('2010-11-01', 14.631, 18.816), ('2010-12-01', 20.174, 16.602), ('2011-01-03', 19.554, 15.604), ('2011-02-01', 26.833, 13.702), ('2011-03-01', 24.937, 12.733), ('2011-04-01', 24.147, 11.746), ('2011-05-02', 23.105, 13.761), ('2011-06-01', 22.836, 13.015), ('2011-07-01', 21.891, 12.476), ('2011-08-01', 19.273, 21.793), ('2011-09-01', 18.014, 20.37), ('2011-10-03', 21.031, 17.607), ('2011-11-01', 24.042, 15.688), ('2011-12-01', 24.215, 14.979), ('2012-01-03', 23.107, 15.052), ('2012-02-01', 28.239, 13.495), ('2012-03-01', 29.025, 12.663), ('2012-04-02', 30.855, 11.98), ('2012-05-01', 34.419, 11.039), ('2012-06-01', 32.29, 11.201), ('2012-07-02', 34.821, 10.628)]
    """
    n = int(config.get('DI', 14))
    numberound = config.get('numberound', True)
    listaADM = ADM(datos, ADM=n, numberound=False)
    listaTAR = Averange(datos, indicador='TR', n=n, tipo='averange', numberound=False)

    listaDI = []

    assert len(datos) == len(listaADM) and len(datos) == len(listaTAR)  # Comprobamos que tienen la misma cantidad de datos

    for i in range(0, len(datos)):

        assert datos[i][0] == listaADM[i][0] and datos[i][0] == listaTAR[i][0]  # Comprobamos que cohinciden las fechas

        fecha = datos[i][0]

        try:
            DImas = (listaADM[i][1] / listaTAR[i][1]) * 100
        except ZeroDivisionError:
            DImas = 0.0
        try:
            Dimenos = (listaADM[i][2] / listaTAR[i][1]) * 100
        except ZeroDivisionError:
            Dimenos = 0.0

        if numberound == True:
            listaDI.append((fecha, round(DImas, 3), round(Dimenos, 3)))
        else:
            listaDI.append((fecha, DImas, Dimenos))

    assert len(datos) == len(listaDI)  # Comprobamos que el resultado contiene la misma cantidad de datos que el origen
    return (listaDI)


def DX(datos, **config):
    """
    Directional Movement Index

    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> DX(datos)
    [('2010-01-25', 0.0), ('2010-02-01', 100.0), ('2010-03-01', 40.625), ('2010-04-01', 23.529), ('2010-05-03', 43.804), ('2010-06-01', 43.804), ('2010-07-01', 47.861), ('2010-08-02', 47.861), ('2010-09-01', 45.718), ('2010-10-01', 32.773), ('2010-11-01', 12.513), ('2010-12-01', 9.714), ('2011-01-03', 11.236), ('2011-02-01', 32.396), ('2011-03-01', 32.396), ('2011-04-01', 34.55), ('2011-05-02', 25.345), ('2011-06-01', 27.395), ('2011-07-01', 27.395), ('2011-08-01', 6.137), ('2011-09-01', 6.137), ('2011-10-03', 8.862), ('2011-11-01', 21.027), ('2011-12-01', 23.565), ('2012-01-03', 21.108), ('2012-02-01', 35.328), ('2012-03-01', 39.247), ('2012-04-02', 44.063), ('2012-05-01', 51.433), ('2012-06-01', 48.49), ('2012-07-02', 53.23)]
    """
    n = int(config.get('DX', 14))
    numberound = config.get('numberound', True)
    listaDI = DI(datos, DI=n, numberound=False)
    listaDX = []

    assert len(datos) == len(listaDI)  # Comprobamos que tienen la misma cantidad de datos

    for i in range(0, len(datos)):

        assert datos[i][0] == listaDI[i][0]  # Comprobamos que cohinciden las fechas

        fecha = datos[i][0]
        try:
            DX = ((abs(listaDI[i][1] - listaDI[i][2])) / (listaDI[i][1] + listaDI[i][2])) * 100
        except ZeroDivisionError:
            DX = 0
        if numberound == True:
            listaDX.append((fecha, round(DX, 3)))
        else:
            listaDX.append((fecha, DX))

    assert len(datos) == len(listaDX)  # Comprobamos que el resultado contiene la misma cantidad de datos que el origen
    return (listaDX)


def ADX(datos, **config):
    """
    Average Directional Movement Index

    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> ADX(datos)
    [('2010-01-25', 0.0), ('2010-02-01', 0.0), ('2010-03-01', 0.0), ('2010-04-01', 0.0), ('2010-05-03', 0.0), ('2010-06-01', 0.0), ('2010-07-01', 0.0), ('2010-08-02', 0.0), ('2010-09-01', 0.0), ('2010-10-01', 0.0), ('2010-11-01', 0.0), ('2010-12-01', 0.0), ('2011-01-03', 0.0), ('2011-02-01', 0.0), ('2011-03-01', 0.0), ('2011-04-01', 0.0), ('2011-05-02', 0.0), ('2011-06-01', 0.0), ('2011-07-01', 0.0), ('2011-08-01', 0.0), ('2011-09-01', 0.0), ('2011-10-03', 0.0), ('2011-11-01', 0.0), ('2011-12-01', 0.0), ('2012-01-03', 0.0), ('2012-02-01', 0.0), ('2012-03-01', 0.0), ('2012-04-02', 25.183), ('2012-05-01', 27.058), ('2012-06-01', 28.588), ('2012-07-02', 30.349)]
    """
    n = config.get('ADX', 14)
    numberound = config.get('numberound', True)
    listaDX = DX(datos, DX=n, numberound=False)
    assert len(datos) == len(listaDX)
    listaADX = []
    valoresDX = []

    for i in range(0, len(datos)):

        assert datos[i][0] == listaDX[i][0]

        fecha, valorDX = listaDX[i]
        valoresDX.append(valorDX)

        if i < (n * 2) - 1:
            ADX = 0.0
        elif i == ((n * 2) - 1):
            ADX = sum(valoresDX[(i + 1) - n:]) / n
        else:
            ADX = (((ADX * (n - 1)) + listaDX[i][1])) / n

        if numberound == True:
            listaADX.append((fecha, round(ADX, 3)))
        else:
            listaADX.append((fecha, ADX))

    assert len(datos) == len(listaADX)
    return (listaADX)


def Averange(datos, **config):
    """
    Averange de cualquier indicador
    n=periodos Entero
    indicedatos=False/entero, Falso para aplicar el indicador a todos los elementos, entero para aplicar el indicador solo a un elemento de la tupla de datos
    indicador= Indicador utilizado (TR)
    tipo=averange/exponencial

    Tipos de medias moviles:

    Simple Moving Average (SMA) - Media Movil Simple
        La media movil simple o aritmetica se calcula mediante la suma de los precios de cierre de un instrumento durante un determinado numero de periodos simples (por ejemplo, durante 12 horas), dividiendo a continuacion la suma por el numero de estos periodos.
        SMA = SUM (CLOSE (i), N) / N
        aqui:
        SUM - suma;
        CLOSE (i) - precio de cierre del periodo actual;
        N - numero de periodos calculados.

    Exponential Moving Average (EMA) - Media Movil Exponencial
        La media movil suavizada exponencialmente se calcula mediante la adicion de una cierta parte del precio de cierre actual al valor anterior de la media movil. A la hora de usar las medias moviles exponenciales, el mayor valor tienen los ultimos precios de cierre. La media movil exponencial de P% sera la siguiente:
        EMA = (CLOSE (i) * P) + (EMA (i - 1) * (1 - P))
        aqui:
        CLOSE (i) - precio de cierre del periodo actual;
        EMA (i - 1) - valor de la media movil para el periodo anterior;
        P - parte de uso del valor de precios.

    Smoothed Moving Average (SMMA) - Media Movil Suavizada
        El primer valor de la media movil suavizada se calcula como la media movil simple (SMA):
        SUM1 = SUM (CLOSE (i), N)
        SMMA1 = SUM1 / N
        Para obtener el segundo valor se utiliza la siguiente formula:
        SMMA (i) = (SMMA1*(N-1) + CLOSE (i)) / N
        Las medias moviles subsecuentes se calculan segun el formula siguiente:
        PREVSUM = SMMA (i - 1) * N
        SMMA (i) = (PREVSUM - SMMA (i - 1) + CLOSE (i)) / N
        aqui:
        SUM - suma;
        SUM1 - suma de precios de cierre para periodos N; se calcula a partir de la barra anterior;
        PREVSUM - suma suavizada de la barra anterior;
        SMMA (i-1) - media movil suavizada de la barra anterior;
        SMMA (i) - media movil suavizada de la barra actual (salvo la primera barra);
        CLOSE (i) - precio de cierre actual;
        N - periodo de suavizado.

        Se puede simplificar esta formula mediante algunas transformaciones aritmeticas:
        SMMA (i) = (SMMA (i - 1) * (N - 1) + CLOSE (i)) / N


    Linear Weighted Moving Average (LWMA) - Media Movil Ponderada Lineal
        En una media movil ponderada los ultimos datos tienen mes valor que los datos iniciales. La media movil ponderada se calcula multiplicando cada uno de los precios de cierre en la serie a considerar por un coeficiente ponderal determinado:
        LWMA = SUM (CLOSE (i) * i, N) / SUM (i, N)
        aqui:
        SUM - suma;
        CLOSE(i) - precio de cierre actual;
        SUM (i, N) - suma de coeficientes ponderales;
        N - periodo de suavizado.

    >>> MME(datos,MME=30,indicedatos='cierre',numberound=False)==Averange(datos,n=30,indicedatos='cierre',indicador=False,numberound=False,tipo='exponencial')
    True
    >>> ADM(datos,numberound=False)==Averange(datos,indicador='DM',tipo='averange',numberound=False)
    True
    >>> TAR(datos,TAR=14)==Averange(datos, indicador='TR', tipo='simple',n=14)
    True
    >>> Averange(datos,n=30,indicador=False,tipo='exponencial',indicedatos='cierre')
    [('2010-01-25', 19.6), ('2010-02-01', 19.594), ('2010-03-01', 19.732), ('2010-04-01', 19.798), ('2010-05-03', 19.88), ('2010-06-01', 19.866), ('2010-07-01', 19.826), ('2010-08-02', 19.808), ('2010-09-01', 19.891), ('2010-10-01', 19.95), ('2010-11-01', 20.078), ('2010-12-01', 20.446), ('2011-01-03', 20.754), ('2011-02-01', 21.253), ('2011-03-01', 21.623), ('2011-04-01', 21.992), ('2011-05-02', 22.348), ('2011-06-01', 22.682), ('2011-07-01', 22.928), ('2011-08-01', 23.007), ('2011-09-01', 22.994), ('2011-10-03', 23.216), ('2011-11-01', 23.597), ('2011-12-01', 23.922), ('2012-01-03', 24.23), ('2012-02-01', 24.722), ('2012-03-01', 25.333), ('2012-04-02', 26.019), ('2012-05-01', 26.759), ('2012-06-01', 27.448), ('2012-07-02', 28.147)]
    >>> Averange(datos,n=30,indicador=False,tipo='exponencial')
    [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800.0), ('2010-02-01', 20.045, 22.893, 19.297, 19.594, 750612.903), ('2010-03-01', 20.018, 22.841, 19.253, 19.732, 732528.2), ('2010-04-01', 20.132, 22.833, 19.336, 19.798, 710494.123), ('2010-05-03', 20.169, 22.815, 19.295, 19.88, 688062.244), ('2010-06-01', 20.225, 22.762, 19.271, 19.866, 659174.357), ('2010-07-01', 20.193, 22.707, 19.214, 19.826, 651382.463), ('2010-08-02', 20.141, 22.603, 19.181, 19.808, 627822.304), ('2010-09-01', 20.118, 22.512, 19.187, 19.891, 600762.801), ('2010-10-01', 20.181, 22.475, 19.273, 19.95, 575236.169), ('2010-11-01', 20.224, 22.537, 19.338, 20.078, 556278.997), ('2010-12-01', 20.362, 22.751, 19.532, 20.446, 538893.255), ('2011-01-03', 20.722, 22.965, 19.816, 20.754, 517945.303), ('2011-02-01', 21.024, 23.417, 20.154, 21.253, 504110.122), ('2011-03-01', 21.521, 23.823, 20.572, 21.623, 501773.985), ('2011-04-01', 21.882, 24.235, 20.975, 21.992, 491085.341), ('2011-05-02', 22.234, 24.451, 21.283, 22.348, 478370.158), ('2011-06-01', 22.569, 24.679, 21.57, 22.682, 463926.922), ('2011-07-01', 22.88, 24.891, 21.875, 22.928, 453312.282), ('2011-08-01', 23.132, 25.014, 21.864, 23.007, 454717.941), ('2011-09-01', 23.202, 25.0, 21.875, 22.994, 441368.396), ('2011-10-03', 23.163, 25.147, 21.826, 23.216, 435486.564), ('2011-11-01', 23.338, 25.447, 22.007, 23.597, 434790.657), ('2011-12-01', 23.703, 25.765, 22.412, 23.922, 424765.453), ('2012-01-03', 24.037, 26.038, 22.769, 24.23, 410283.811), ('2012-02-01', 24.343, 26.519, 23.154, 24.722, 412988.081), ('2012-03-01', 24.829, 27.044, 23.713, 25.333, 412117.882), ('2012-04-02', 25.424, 27.633, 24.361, 26.019, 406852.212), ('2012-05-01', 26.101, 28.36, 25.069, 26.759, 401300.456), ('2012-06-01', 26.801, 28.965, 25.706, 27.448, 389229.459), ('2012-07-02', 27.484, 29.649, 26.455, 28.147, 377234.01)]
    >>> Averange(datos,indicador='DM',tipo='averange')
    [('2010-01-25', 0.0, 0.0), ('2010-02-01', 0.0, 3.15), ('2010-03-01', 1.33, 3.15), ('2010-04-01', 1.95, 3.15), ('2010-05-03', 1.95, 4.99), ('2010-06-01', 1.95, 4.99), ('2010-07-01', 1.95, 5.53), ('2010-08-02', 1.95, 5.53), ('2010-09-01', 2.06, 5.53), ('2010-10-01', 2.8, 5.53), ('2010-11-01', 4.3, 5.53), ('2010-12-01', 6.72, 5.53), ('2011-01-03', 6.93, 5.53), ('2011-02-01', 10.83, 5.53), ('2011-03-01', 10.83, 5.53), ('2011-04-01', 10.556, 5.135), ('2011-05-02', 9.802, 5.838), ('2011-06-01', 9.512, 5.421), ('2011-07-01', 8.833, 5.034), ('2011-08-01', 8.202, 9.274), ('2011-09-01', 7.616, 8.612), ('2011-10-03', 9.552, 7.997), ('2011-11-01', 11.38, 7.426), ('2011-12-01', 11.147, 6.896), ('2012-01-03', 10.351, 6.743), ('2012-02-01', 13.102, 6.261), ('2012-03-01', 13.326, 5.814), ('2012-04-02', 13.904, 5.399), ('2012-05-01', 15.631, 5.013), ('2012-06-01', 14.514, 5.035), ('2012-07-02', 15.317, 4.675)]
    >>> Averange(datos, indicador='DX', tipo='suavizada')
    [('2010-01-25', 0.0), ('2010-02-01', 0.0), ('2010-03-01', 0.0), ('2010-04-01', 0.0), ('2010-05-03', 0.0), ('2010-06-01', 0.0), ('2010-07-01', 0.0), ('2010-08-02', 0.0), ('2010-09-01', 0.0), ('2010-10-01', 0.0), ('2010-11-01', 0.0), ('2010-12-01', 0.0), ('2011-01-03', 0.0), ('2011-02-01', 0.0), ('2011-03-01', 0.0), ('2011-04-01', 0.0), ('2011-05-02', 0.0), ('2011-06-01', 0.0), ('2011-07-01', 0.0), ('2011-08-01', 0.0), ('2011-09-01', 0.0), ('2011-10-03', 0.0), ('2011-11-01', 0.0), ('2011-12-01', 0.0), ('2012-01-03', 0.0), ('2012-02-01', 0.0), ('2012-03-01', 0.0), ('2012-04-02', 25.183), ('2012-05-01', 27.058), ('2012-06-01', 28.589), ('2012-07-02', 30.349)]
    >>> Averange(datos, indicador='TR', tipo='simple')
    [('2010-01-25', 0.0), ('2010-02-01', 2.205), ('2010-03-01', 2.627), ('2010-04-01', 2.513), ('2010-05-03', 2.782), ('2010-06-01', 2.828), ('2010-07-01', 2.927), ('2010-08-02', 2.86), ('2010-09-01', 2.757), ('2010-10-01', 2.623), ('2010-11-01', 2.672), ('2010-12-01', 2.776), ('2011-01-03', 2.726), ('2011-02-01', 2.883), ('2011-03-01', 3.102), ('2011-04-01', 3.029), ('2011-05-02', 2.912), ('2011-06-01', 2.919), ('2011-07-01', 2.762), ('2011-08-01', 2.907), ('2011-09-01', 2.853), ('2011-10-03', 3.122), ('2011-11-01', 3.353), ('2011-12-01', 3.4), ('2012-01-03', 3.321), ('2012-02-01', 3.384), ('2012-03-01', 3.434), ('2012-04-02', 3.256), ('2012-05-01', 3.291), ('2012-06-01', 3.248), ('2012-07-02', 3.278)]
    """
    n = int(config.get('n', 14))
    indicedatos = config.get('indicedatos', False)
    if indicedatos != False:
        indicedatos = ('fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'volumen').index(indicedatos)
    else:
        indicedatos = 0
    indicador = str(config.get('indicador', False))
    numberound = config.get('numberound', True)
    tipo = str(config.get('tipo', 'averange'))

    # todos los indicadores el elemento [0] es una fecha, pero despues puede tener mas de un elemento, ejemplo el DM
    # aunque tenga  mas de un elemento puede que nos interese calcular el averange de uno en concreto devolviendo la lista igual pero con ese elemento cambiado

    # ejemplo: Averange(datos,n=30, indicador=False,tipo='exponencial',indicedatos='cierre'), si en este caso no le especifico el indicedatos, me deberia responder con los calculos para todos los elementos por separado
    # ejemplo: Averante(datos,n=14, indicador=DM,tipo='averange'), mezclara los datos de DM+ y DM-
    if indicador == 'TR':
        lista = TR(datos, numberound=False)
    elif indicador == 'DM':
        lista = DM(datos, numberound=False)
    elif indicador == 'DX':
        lista = DX(datos, DX=n, numberound=False)
    else:
        lista = datos

    assert len(datos) == len(lista)

    listaA = []
    valores = []

    for i in range(0, len(lista)):
        assert datos[i][0] == lista[i][0]  # Comprobamos que cohinciden las fechas

        valores.append(list(lista[i]))

        for i2 in range(1, len(lista[i])):

            valor = lista[i][i2]
            if i == 0:
                valorA = 0.0
            else:
                valorA = valores[i - 1][i2]

            # Valorar bien el tema de los nombres para los tipos de Averange
            if tipo == 'simple' or tipo == 'SMA':

                inicio = i - n
                if inicio < 0:
                    inicio = 0
                    divisor = 2
                else:
                    divisor = 1

                for i3 in range(inicio + 1, i):
                    valor = lista[i3][i2] + valor
                    divisor += 1

                valorA = valor / divisor

            elif tipo == 'exponencial' or tipo == 'EMA':
                k = (2.0 / (1.0 + n))
                if i == 0:
                    valorA = valor
                else:
                    valorA = (valor * k) + (valorA * (1 - k))

            # Apartir de aqui la relacion de nombres para los tipos de Averanges detallados mas arriba no esta claro
            elif tipo == 'suavizada' or tipo == 'SMMA':  # en el calculo del adx emplamos esta
                if i < (n * 2) - 1:
                    valorA = 0.0
                elif i == ((n * 2) - 1):
                    for i3 in range((i + 1) - n, i):
                        valor = lista[i3][i2] + valor
                    valorA = valor / n
                else:
                    valorA = (((valorA * (n - 1)) + valor)) / n

            elif tipo == 'averange':
                if i <= n:
                    valorA = valorA + valor
                else:
                    valorA = valorA - (valorA / n) + valor

            if numberound == True:
                valores[i][i2] = round(valorA, 3)
            else:
                valores[i][i2] = valorA

        listaA.append(tuple(valores[i]))

    if indicedatos != 0 and indicedatos > 0:
        listaB = []
        for i in range(0, len(listaA)):
            listaB.append((listaA[i][0], listaA[i][indicedatos]))
        listaA = listaB
        del (listaB)

    assert len(datos) == len(listaA)
    return (listaA)


def sesionesHL(datos, **config):
    """
    Devuelve la barra anteriormente dejada como high o low de un periodo de tiempo. No tiene en cuenta la actual
    configurado con un periodo de 52 semanas y en high, equivaldria al "52 week high"
    Parametros:
    HL = 'high'/'low'
    periodos = int


    >>> datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    >>> sesionesHL(datos)
    [('2010-01-25', '2010-01-25', 23.04), ('2010-02-01', '2010-01-25', 23.04), ('2010-03-01', '2010-01-25', 23.04), ('2010-04-01', '2010-01-25', 23.04), ('2010-05-03', '2010-01-25', 23.04), ('2010-06-01', '2010-01-25', 23.04), ('2010-07-01', '2010-01-25', 23.04), ('2010-08-02', '2010-01-25', 23.04), ('2010-09-01', '2010-01-25', 23.04), ('2010-10-01', '2010-01-25', 23.04), ('2010-11-01', '2010-01-25', 23.04), ('2010-12-01', '2010-11-01', 23.44), ('2011-01-03', '2010-12-01', 25.86), ('2011-02-01', '2011-01-03', 26.07), ('2011-03-01', '2011-02-01', 29.97), ('2011-04-01', '2011-02-01', 29.97), ('2011-05-02', '2011-04-01', 30.21), ('2011-06-01', '2011-04-01', 30.21), ('2011-07-01', '2011-04-01', 30.21), ('2011-08-01', '2011-04-01', 30.21), ('2011-09-01', '2011-04-01', 30.21), ('2011-10-03', '2011-04-01', 30.21), ('2011-11-01', '2011-04-01', 30.21), ('2011-12-01', '2011-04-01', 30.21), ('2012-01-03', '2011-12-01', 30.37), ('2012-02-01', '2011-12-01', 30.37), ('2012-03-01', '2012-02-01', 33.49), ('2012-04-02', '2012-03-01', 34.65), ('2012-05-01', '2012-04-02', 36.18), ('2012-06-01', '2012-05-01', 38.9), ('2012-07-02', '2012-05-01', 38.9)]
    >>> sesionesHL(datos,HL='low')
    [('2010-01-25', '2010-01-25', 19.5), ('2010-02-01', '2010-01-25', 19.5), ('2010-03-01', '2010-02-01', 16.35), ('2010-04-01', '2010-02-01', 16.35), ('2010-05-03', '2010-02-01', 16.35), ('2010-06-01', '2010-02-01', 16.35), ('2010-07-01', '2010-02-01', 16.35), ('2010-08-02', '2010-02-01', 16.35), ('2010-09-01', '2010-02-01', 16.35), ('2010-10-01', '2010-02-01', 16.35), ('2010-11-01', '2010-02-01', 16.35), ('2010-12-01', '2010-02-01', 16.35), ('2011-01-03', '2010-07-01', 18.39), ('2011-02-01', '2010-07-01', 18.39), ('2011-03-01', '2010-07-01', 18.39), ('2011-04-01', '2010-07-01', 18.39), ('2011-05-02', '2010-07-01', 18.39), ('2011-06-01', '2010-08-02', 18.7), ('2011-07-01', '2010-09-01', 19.27), ('2011-08-01', '2010-11-01', 20.28), ('2011-09-01', '2010-11-01', 20.28), ('2011-10-03', '2011-08-01', 21.7), ('2011-11-01', '2011-10-03', 21.12), ('2011-12-01', '2011-10-03', 21.12), ('2012-01-03', '2011-10-03', 21.12), ('2012-02-01', '2011-10-03', 21.12), ('2012-03-01', '2011-10-03', 21.12), ('2012-04-02', '2011-10-03', 21.12), ('2012-05-01', '2011-10-03', 21.12), ('2012-06-01', '2011-10-03', 21.12), ('2012-07-02', '2011-10-03', 21.12)]
    """
    HL = config.get('HL', 'high')
    periodos = config.get('periodos', 10)
    listaHL = []
    listamaximos = ([n[2] for n in datos])
    listaminimos = ([n[3] for n in datos])

    for i in range(0, len(datos)):

        fecha, _apertura, maximo, minimo, _cierre, _volumen = datos[i]

        inicio = i - periodos
        if inicio < 0:
            inicio = 0

        if HL == 'high':
            if i == 0:
                valorHL = maximo
                fechaHL = fecha
            else:
                valorHL = max(listamaximos[inicio:i])
                fechaHL = datos[listamaximos.index(valorHL, inicio, i)][0]

        if HL == 'low':
            if i == 0:
                valorHL = minimo
                fechaHL = fecha
            else:
                valorHL = min(listaminimos[inicio:i])
                fechaHL = datos[listaminimos.index(valorHL, inicio, i)][0]

        listaHL.append((fecha, fechaHL, valorHL))
    assert len(listaHL) == len(datos)
    return (listaHL)


def fibonacci(numero):
    """
    >>> fibonacci(24)
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]
    >>>
    """
    a, b = 0, 1
    lista = [1, ]
    for _i in range(numero - 2):
        a, b = b, a + b
        lista.append(b)
    return lista


def puntocurvaexponencial(ltdateini, ltpriceini, ltdatefin, ltpricefin, timming, **config):
    """
    >>> precioentradaLT('2008-01-25', 48.260, '2008-04-18', 76.958, 'w', fechahoy='2008-04-18')
    76.958
    >>> precioentradaLT('2008-01-25', 48.260, '2008-04-18', 76.958, 'w', fechahoy='2008-04-25')
    80.01
    >>> precioentradaLT('2008-01-25', 48.260, '2008-04-18', 76.958, 'w', fechahoy='2008-05-02')
    83.182
    >>> precioentradaLT('2008-01-25', 48.260, '2008-04-18', 76.958, 'm', fechahoy='2008-04-25')
    76.958
    >>> precioentradaLT('2008-01-25', 48.260, '2008-04-18', 76.958, 'w', fechahoy='2008-06-27')
    113.538
    >>> precioentradaLT('2012-05-01', 24.90, '2013-04-01', 43.61, 'm', fechahoy='2013-05-01')
    45.886
    >>> precioentradaLT('2012-05-01', 24.90, '2013-04-01', 43.61, 'm', fechahoy='2013-05-15')
    45.886
    >>> precioentradaLT('2012-05-01', 24.90, '2013-04-01', 43.61, 'm', fechahoy='2013-06-01')
    48.282
    >>> precioentradaLT('2011-06-01', 4.5, '2013-02-01', 15.2, 'w', fechahoy='2013-06-10')
    19.537
    >>> precioentradaLT('2011-06-01', 15.2, '2013-02-01', 4.5, 'm', fechahoy='2013-06-10')
    3.531
    >>> precioentradaLT('2011-06-01', 15.2, '2013-02-01', 4.5, 'w', fechahoy='2013-06-10')
    3.501
    """

    fechahoy = config.get('fechahoy', False)
    incremperiod = config.get('incremperiod', 0)

    ltdateini = list(map(int, (ltdateini.split('-'))))
    ltdatefin = list(map(int, (ltdatefin.split('-'))))

    if fechahoy:
        fechahoy = list(map(int, (fechahoy.split('-'))))
    else:
        fechahoy = (date.today().year, date.today().month, date.today().day)

    diffechas = (date(ltdatefin[0], ltdatefin[1], ltdatefin[2]) - date(ltdateini[0], ltdateini[1], ltdateini[2])).days
    diffechas2 = (date(fechahoy[0], fechahoy[1], fechahoy[2]) - date(ltdatefin[0], ltdatefin[1], ltdatefin[2])).days

    _rentaanual = (((1.0 + (ltpricefin - ltpriceini) / ltpriceini) ** (365.0 / diffechas)) - 1.0)

    # Calculos de entrada obtenidos apartir de la hoja Excel, Analisis y reducida ecuacion con Maple
    if timming == 'd':
        entrada = ltpricefin * (((ltpricefin / ltpriceini) ** (365.0 / diffechas)) ** (1.0 / 365.0)) ** (diffechas2 + incremperiod + 0.0)
    elif timming == 'w':
        entrada = ltpricefin * (((ltpricefin / ltpriceini) ** (365.0 / diffechas)) ** (7.0 / 365.0)) ** (int((1.0 / 7.0) * diffechas2) + incremperiod + 0.0)
    elif timming == 'm':
        entrada = ltpricefin * (((ltpricefin / ltpriceini) ** (365.0 / diffechas)) ** (1.0 / 12.0)) ** (int((1.0 / 30.0) * diffechas2) + incremperiod + 0.0)

    return round(entrada, 3)


if __name__ == '__main__':
    datos = [('2010-01-25', 20.0, 23.04, 19.5, 19.6, 706800), ('2010-02-01', 20.7, 20.76, 16.35, 19.5, 1385900), ('2010-03-01', 19.63, 22.09, 18.62, 21.73, 470300), ('2010-04-01', 21.79, 22.71, 20.54, 20.75, 391000), ('2010-05-03', 20.7, 22.56, 18.7, 21.07, 362800), ('2010-06-01', 21.04, 21.99, 18.93, 19.67, 240300), ('2010-07-01', 19.73, 21.91, 18.39, 19.24, 538400), ('2010-08-02', 19.39, 21.09, 18.7, 19.55, 286200), ('2010-09-01', 19.79, 21.2, 19.27, 21.09, 208400), ('2010-10-01', 21.1, 21.94, 20.52, 20.81, 205100), ('2010-11-01', 20.84, 23.44, 20.28, 21.94, 281400), ('2010-12-01', 22.36, 25.86, 22.35, 25.78, 286800), ('2011-01-03', 25.94, 26.07, 23.94, 25.22, 214200), ('2011-02-01', 25.4, 29.97, 25.05, 28.49, 303500), ('2011-03-01', 28.73, 29.71, 26.64, 26.99, 467900), ('2011-04-01', 27.11, 30.21, 26.82, 27.35, 336100), ('2011-05-02', 27.34, 27.58, 25.75, 27.51, 294000), ('2011-06-01', 27.42, 27.99, 25.73, 27.53, 254500), ('2011-07-01', 27.39, 27.97, 26.3, 26.5, 299400), ('2011-08-01', 26.79, 26.79, 21.7, 24.16, 475100), ('2011-09-01', 24.21, 24.8, 22.04, 22.8, 247800), ('2011-10-03', 22.6, 27.28, 21.12, 26.43, 350200), ('2011-11-01', 25.88, 29.79, 24.63, 29.12, 424700), ('2011-12-01', 29.0, 30.37, 28.29, 28.64, 279400), ('2012-01-03', 28.88, 30.0, 27.95, 28.69, 200300), ('2012-02-01', 28.78, 33.49, 28.74, 31.85, 452200), ('2012-03-01', 31.88, 34.65, 31.82, 34.2, 399500), ('2012-04-02', 34.05, 36.18, 33.75, 35.97, 330500), ('2012-05-01', 35.92, 38.9, 35.33, 37.49, 320800), ('2012-06-01', 36.95, 37.73, 34.95, 37.44, 214200), ('2012-07-02', 37.39, 39.57, 37.32, 38.28, 203300)]
    _test()
