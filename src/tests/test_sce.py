from sce.seven import (
    sum_of_squares,
    subtract_of_squares,
    subtract_two_squares,
    sum_of_cubes,
    subtract_of_cubes,
    cube_two_sums,
    cube_two_subtracts
)


def test_sce_with_int():
    a = 2
    b = 2
    assert sum_of_squares(a, b)

def test_sce_with_float():
    a = 2.2
    b = 2
    assert sum_of_squares(a, b)