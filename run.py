from sce.seven import (
    sum_of_squares,
    subtract_of_squares,
    subtract_two_squares,
    sum_of_cubes,
    subtract_of_cubes,
    cube_two_sums,
    cube_two_subtracts,
)

from sce.clogs import logger

logger.info(sum_of_squares(2, 2))

print(sum_of_squares(2, 2))
print(subtract_of_squares(2, 2))
print(subtract_two_squares(4, 2))
print(sum_of_cubes(3, 5))
print(subtract_of_cubes(5, 4))
print(cube_two_sums(4, 6))
print(cube_two_subtracts(6, 4))