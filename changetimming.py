'''
Created on 29/10/2012

@author: Antonio
'''
import time


fechadatos = 0
aperturadatos = 1
maximodatos = 2
minimodatos = 3
cierredatos = 4
volumendatos = 5


def _test():
    import doctest
    doctest.testmod()


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
    timming = config.get('timming', 'm')
    datostimming = []

    timmingformat = {'m': '%Y, %m', 'w': '%Y, %W'}
    inicio = 0
    if len(datos) > 0:

        fechaagr = time.strftime(timmingformat[timming], time.strptime(datos[0][fechadatos], '%Y-%m-%d'))

        i = 0
        while i < len(datos):
            fecha = datos[i][fechadatos]
            fecha = time.strptime(fecha, '%Y-%m-%d')

            if fechaagr != time.strftime(timmingformat[timming], fecha):
                fechaagr = time.strftime(timmingformat[timming], fecha)

                maximo = max([(n[maximodatos]) for n in datos][inicio:i])
                minimo = min([(n[minimodatos]) for n in datos][inicio:i])
                volumen = sum([(n[volumendatos]) for n in datos][inicio:i])

                datostimming.append((datos[inicio][fechadatos], datos[inicio][aperturadatos], maximo, minimo, datos[i - 1][cierredatos], volumen))
                inicio = i
            i += 1

        maximo = max([(n[maximodatos]) for n in datos][inicio:])
        minimo = min([(n[minimodatos]) for n in datos][inicio:])
        volumen = sum([(n[volumendatos]) for n in datos][inicio:])
        datostimming.append((datos[inicio][fechadatos], datos[inicio][aperturadatos], maximo, minimo, datos[-1][cierredatos], volumen))

    return datostimming


if __name__ == '__main__':
    _test()