import src.sce as s
from src.clogs import logger

def test_sce_with_int():
    a = 2
    b = 2
    assert s.sum_of_squares(a, b)

def test_sce_with_float():
    a = 2.2
    b = 2
    assert s.sum_of_squares(a, b)