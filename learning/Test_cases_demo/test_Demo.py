import math, pytest

def test_sqrt():
    num = 121
    assert math.sqrt(num) == 11
    
def test_square():
    num = 8
    assert 8*8 == 68

def test_equal():
    assert 10==10