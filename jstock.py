#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
jstock.py - v0.01 2014-10-22 Antonio Caballero.

Este modulo proporciona las herramientas necesarias para leer del repositorio de github de jstock las acciones que se han incorporado nuevas

License: http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode

"""

__version__ = '0.06'
__date__ = '2020-03-09'
__author__ = ('Antonio Caballero', )
__mail__ = ('zurbaran79@hotmail.com', )
__license__ = 'http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode'

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
jstock.py - Extrae tickets de acciones nuevas desde el repositorio JStock en GitHub.
"""

import os
import csv
import shutil
import logging
import requests
from time import sleep
from zipfile import ZipFile
from settings import CARPETAS, ARCHIVO_LOG
from yahoofinance import webheaders, pausareconexion

logging.basicConfig(
    filename=ARCHIVO_LOG,
    format='%(asctime)s : %(processName)s : %(levelname)s : %(module)s : %(funcName)s: %(lineno)d :%(message)s',
    level=logging.DEBUG)

JSTOCK_URL = 'https://github.com/yccheok/jstock/archive/refs/heads/master.zip'
ZIP_DEST = os.path.join(os.getcwd(), CARPETAS['Log'], "jstock-master.zip")
EXTRACT_DIR = os.path.join(os.getcwd(), CARPETAS['Log'], "jstock-master")


def descarga():
    """Descarga el archivo ZIP del repositorio de JStock"""
    while True:
        try:
            r = requests.get(JSTOCK_URL, headers=webheaders, stream=True, timeout=pausareconexion)
            with open(ZIP_DEST, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            break
        except (requests.HTTPError, requests.ReadTimeout, requests.ConnectionError) as e:
            print(f"Error de conexión ({type(e).__name__}): {e}. Reintentando en {pausareconexion} segundos...")
            sleep(pausareconexion)


def descomprime():
    """Descomprime el ZIP descargado"""
    with ZipFile(ZIP_DEST) as zip_ref:
        zip_ref.extractall(os.path.join(os.getcwd(), CARPETAS['Log']))


def extrae_tickets():
    """Lee y devuelve los tickets de los archivos CSV descomprimidos"""
    tickets = []
    info_dir = os.path.join(EXTRACT_DIR, 'appengine/jstock-static/war/stocks_information/')
    paises = [p for p in os.listdir(info_dir) if os.path.isdir(os.path.join(info_dir, p))]

    # Filtrar carpetas irrelevantes
    carpetas_omitidas = {'google-code-database-meta.json', 'stock-info-database-meta.json',
                         'stock-info-sqlite-meta.json', 'sqlite'}
    paises = [p for p in paises if p not in carpetas_omitidas]

    for pais in paises:
        zip_path = os.path.join(info_dir, pais, 'stocks.zip')
        try:
            with ZipFile(zip_path, 'r') as zip_file:
                zip_file.extractall(os.path.join(info_dir, pais))
        except Exception as e:
            print(f"No se pudo descomprimir {zip_path}: {e}")
            continue

        csv_path = os.path.join(info_dir, pais, 'stocks.csv')
        if not os.path.exists(csv_path):
            continue

        with open(csv_path, newline='', encoding="ISO-8859-1") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].strip().upper() != "CODE":
                    symbol = row[0].upper().replace('@%5E', '^').strip("'")
                    tickets.append(symbol)
        print(f"Añadido país: {pais}")
        os.remove(csv_path)

    return tickets


def limpieza():
    """Elimina archivos temporales y carpetas descargadas"""
    for path in [ZIP_DEST, EXTRACT_DIR]:
        if os.path.exists(path):
            try:
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)
            except Exception as e:
                print(f"Error eliminando {path}: {e}")


def ticketsJstock():
    """Función principal que orquesta la descarga, extracción y lectura de tickets"""
    limpieza()
    descarga()
    descomprime()
    listtickets = extrae_tickets()
    return listtickets
