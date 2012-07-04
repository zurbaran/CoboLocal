

def MME(datos, **config):
    """
    devuelve de la lista, datos, el indicadorMME calculado
    indice, si es True devueve una tupla completa que corresponde al indicadorMME con el formato (Fecha, indicadorMME) para la lista de datos completa
    indice, si es un valor en concreto, nos devuelve el valor del indicadorMME para ese indice en concreto

    indicedatos, es el valor del indice de las tuplas de datos al que se utiliza para calcular el indicador, por defecto 4 que corresponde al precio de cierre.
    """
    # para los indicadores como la Media Movil 30 en la que en los primeros 29 periodos no se puede calcular, hay que asignarles valor 0
    resultado = []
    n = int(config.get('MME', 30))
    indice = config.get('indice', True)
    indicedatos = config.get('indicedatos', 'cierre')

    indicedatos = ('fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'volumen').index(indicedatos)

    if indice == True:
        fin = len(datos)
    else:
        fin = indice + 1

    k = (2.0 / (1.0 + n))
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


def TR(datos):
    """
    True Range
    """
    listaTR = []

    for i in xrange (0, len(datos)):

        fecha, _apertura, maximo, minimo, _cierre, _volumen = datos[i]
        if i == 0:
            valorTR = 0.0
        else:
            ant = i - 1
            _fechaanterior, _aperturaanterior, _maximoanterior, _minimoanterior, cierreanterior, _volumenanterior = datos[ant]
            valorTR = max((abs(maximo - minimo), abs(maximo - cierreanterior), abs(cierreanterior - minimo)))

        listaTR.append((fecha, valorTR))
    assert len(listaTR) == len(datos)
    return listaTR


def TAR(datos, **config):
    """
    True Averange Range
    TAR = Entero
    """
    n = int(config.get('TAR', 10))
    listaTR = TR(datos)
    assert len(datos) == len(listaTR)

    valoresTR = []
    listaTAR = []

    for i in xrange (0, len(listaTR)):
        inicio = (i + 1) - n
        if inicio < 0:
            inicio = 0

        fecha, valorTR = listaTR[i]
        valoresTR.append(valorTR)

        valorTAR = (sum(valoresTR[inicio:])) / (len(valoresTR[inicio:]))
        listaTAR.append((fecha, valorTAR))

    assert len(datos) == len(listaTAR)
    return listaTAR


def DM(datos):
    """
    Directional Move Indicator
    Formato (fecha,DM+,DM-)
    """
    listaDM = []

    for i in xrange (0, len(datos)):

        fecha, _apertura, maximo, minimo, _cierre, _volumen = datos[i]
        if i == 0:
            listaDM.append((fecha, 0.0, 0.0))
        else:
            ant = i - 1
            _fechaanterior, _aperturaanterior, maximoanterior, minimoanterior, _cierreanterior, _volumenanterior = datos[ant]

            deltamaximo = maximo - maximoanterior
            deltaminimo = minimoanterior - minimo

            if (deltamaximo == 0 and deltaminimo == 0) or deltamaximo == deltaminimo:
                listaDM.append((fecha, 0.0, 0.0))
            elif deltamaximo > deltaminimo:
                listaDM.append((fecha, deltamaximo, 0.0))
            elif deltamaximo < deltaminimo:
                listaDM.append((fecha, 0.0, deltaminimo))

    assert len(listaDM) == len(datos)
    return listaDM


def ADM(datos, **config):
    """
    Average Directional Move Indicator
    periodos = Entero
    Formato (fecha,ADM+,ADM-)
    """
    n = int(config.get('periodos', 10))

    listaDM = DM(datos)

    listaADM = []

    assert len(datos) == len(listaDM)#Comprobamos que tienen la misma cantidad de datos

    for i in xrange(0, len(datos)):

        assert datos[i][0] == listaDM[i][0]#Comprobamos que cohinciden las fechas

        fecha = datos[i][0]
        if i == 0:
            listaADM.append((fecha, listaDM[0][1] * (1 / n), listaDM[0][2] * (1 / n)))
        else:
            listaADM.append((fecha,
                             (listaADM[-1][1] * (n - 1 / n)) + (listaDM[i][1] * (1 / n)),
                             (listaADM[-1][2] * (n - 1 / n)) + (listaDM[i][2] * (1 / n))))

    assert len(datos) == len(listaADM)#Comprobamos que el resultado contiene la misma cantidad de datos que el origen
    return listaADM


def DI(datos, **config):
    """
    Directional Index
    Formato (fecha,DI+,DI-)
    """
    listaADM = ADM(datos)
    listaTAR = TAR(datos)

    listaDI = []

    assert len(datos) == len(listaADM)#Comprobamos que tienen la misma cantidad de datos
    assert len(datos) == len(listaTAR)#Comprobamos que tienen la misma cantidad de datos


    for i in xrange(0, len(datos)):

        assert datos[i][0] == listaADM[i][0] and datos[i][0] == listaTAR[i][0]#Comprobamos que cohinciden las fechas

        fecha = datos[i][0]

        listaDI.append((fecha,
                         (listaADM[i][1] / listaTAR[i][1]) * 100,
                         (listaADM[i][2] / listaTAR[i][1]) * 100
                         ))

    assert len(datos) == len(listaDI)#Comprobamos que el resultado contiene la misma cantidad de datos que el origen
    return listaDI


def DMI(datos):
    """
    Directional Movement Index
    """

    listaDI = DI(datos)
    listaDX = []

    assert len(datos) == len(listaDI)#Comprobamos que tienen la misma cantidad de datos


    for i in xrange(0, len(datos)):

        assert datos[i][0] == listaDI[i][0]#Comprobamos que cohinciden las fechas

        fecha = datos[i][0]

        listaDX.append((fecha,
                         ((listaDI[i][1] - listaDI[i][2]) / (listaDI[i][1] - listaDI[i][2])) * 100
                         ))

    assert len(datos) == len(listaDX)#Comprobamos que el resultado contiene la misma cantidad de datos que el origen
    return listaDI


def ADX(datos, **config):
    """
    Average Directional Movement Index
    """
    listaTR = TR(datos)
    assert len(datos) == len(listaTR)
    n = config.get('ADX', 10)
    listaADX = []

    assert len(listaTR) == len(datos)

    for i in xrange(0, len(datos)):

        assert datos[i][0] == listaTR[i][0]

        fecha = datos[i][0]
        if i == 0:
            listaADX.append((fecha, listaTR[0] * (1 / n)))
        else:
            listaADX.append((fecha, (listaADX[-1] * (n - 1 / n)) + (listaTR[i] * (1 / n))))

    assert len(datos) == len(listaADX)
    return listaADX


def Averange(datos, **config):
    """
    Averange de cualquier indicador
    periodos = Entero
    """
    n = int(config.get('periodos', 10))
    indicador = str(config.get('indicador', 'TR'))

    if indicador == 'TR':
        listaTR = TR(datos)
    elif indicador == 'DM':
        listaTR = DM(datos)

    listaTAR = []

    assert len(datos) == len(listaTR)#Comprobamos que tienen la misma cantidad de datos

    for i in xrange(0, len(datos)):

        assert datos[i][0] == listaTR[i][0]#Comprobamos que cohinciden las fechas

        fecha = datos[i][0]
        if i == 0:
            listaTAR.append((fecha, listaTR[0] * (1 / n)))
        else:
            listaTAR.append((fecha, (listaTAR[-1] * (n - 1 / n)) + (listaTR[i] * (1 / n))))

    assert len(datos) == len(listaTAR)#Comprobamos que el resultado contiene la misma cantidad de datos que el origen
    return listaTAR


if __name__ == '__main__':
    pass