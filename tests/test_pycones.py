from pycones import *


def test_flatten():
    assert flatten([1, 2, [3, [4, 5]]]) == [1, 2, 3, 4, 5]


def test_list_join():
    assert list_join(list("abc"), list("def"), sep=",") == "a,b,c,d,e,f"
