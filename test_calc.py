import calc
import pytest

def test_add():
    assert calc.add(2, 3) == 5

def test_sub():
    assert calc.sub(10, 4) == 6

def test_mul():
    assert calc.mul(3, 5) == 15

def test_div():
    assert calc.div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ValueError):
        calc.div(5, 0)
