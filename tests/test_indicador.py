import math
from indicador import fibonacci, puntocurvaexponencial, curvexprent, MME


def test_fibonacci_basic():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13]


def test_puntocurvaexponencial_example():
    res = puntocurvaexponencial(
        '2008-01-25', 48.260, '2008-04-18', 76.958, 'w', fechahoy='2008-05-02'
    )
    assert math.isclose(res, 83.182, rel_tol=1e-3)


def test_curvexprent_basic():
    res = curvexprent('2010-01-01', 10.0, '2011-01-01', 11.0)
    assert math.isclose(res, 0.1, rel_tol=1e-3)


def test_mme_length_and_values():
    datos = [
        ('2020-01-01', 1, 1, 1, 1, 1),
        ('2020-01-02', 2, 2, 2, 2, 2),
        ('2020-01-03', 3, 3, 3, 3, 3),
        ('2020-01-04', 4, 4, 4, 4, 4),
    ]
    res = MME(datos, MME=3)
    assert len(res) == len(datos)
    assert res[0][1] == 1
    assert math.isclose(res[-1][1], 3.125, rel_tol=1e-3)
