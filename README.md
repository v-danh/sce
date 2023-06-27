# Summary
The seven memorable equality constants.


## Sum of squares
"""
    (a + b)² = a² + 2ab + b² 
""" \

## Subtract of squares
"""
    (a - b)² = a² - 2ab + b² 
""" \

## Subtract two squares
"""
    a² - b² = (a - b)(a + b)
""" \

## Sum of cubes
"""
    (a + b)³ = a³ + b³ + 3ab(a + b)
""" \

## Subtract of cubes
"""
    (a - b)³ = a³ - b³ - 3ab(a - b)
""" \

## Cube two sums
"""
    a³ + b³ = (a + b)(a² - ab + b²)
""" \

## Cube two subtracts
"""
    a³ - b³ = (a - b)(a² + ab + b²)
""" \


# Instructions
Run the following to install
```
pip install sce
```
import **sce** library
```
import sce
```

## Usage
```
from sce.seven import (
    sum_of_squares,
    subtract_of_squares,
    subtract_two_squares,
    sum_of_cubes,
    subtract_of_cubes,
    cube_two_sums,
    cube_two_subtracts
)

# Print out all the results of the seven memorable equality constants.
print(sum_of_squares(2, 2))
print(subtract_of_squares(2, 2))
print(subtract_two_squares(4, 2))
print(sum_of_cubes(3, 5))
print(subtract_of_cubes(5, 4))
print(cube_two_sums(4, 6))
print(cube_two_subtracts(6, 4))
```