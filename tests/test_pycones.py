from pycones import *
import numpy as np


def test_flatten():
    assert flatten([1, 2, [3, [4, 5]]]) == [1, 2, 3, 4, 5]


def test_list_join():
    assert list_join(list("abc"), list("def"), sep=",") == "a,b,c,d,e,f"

def test_signif_number():

    test_numbers = [
        1.1, 1.14, 1.151, 10, 10.5, 10.51, 10.52, 115, 115.5, 6.9785,
        0.5273, 0.526, -0.5273, -9, 9, 9.213, -9.213,
        0.0000000000000002, 2451, 2450, -2451, -2450
    ]

    res_numbers = [
        1.1, 1.1, 1.2, 10.0, 10.0, 11.0, 11.0, 120.0, 120.0, 7.0, 
        0.53, 0.53, -0.53, -9.0, 9.0, 9.2, -9.2, 
        0.0000000000000002, 2500.0, 2400.0, -2500.0, -2400.0
    ]

    assert [ signif_number(x, 2) for x in test_numbers ] == res_numbers

    assert signif_number(None) == None
    assert np.isnan(signif_number(np.nan))
