import cProfile
from time import perf_counter
from clogs import logger

def get_time(func):
    """Times any function"""
    
    def wrapper():
        start = perf_counter()
        
        func()
        
        end = perf_counter()
        time_lapse = end - start
        
        print(f'Time lapse : {time_lapse:.4f} (s)')
        
    return wrapper

def sum_of_squares(a, b) -> int:
    """
        (a + b)² = a² + 2*a*b + b²
    """
    return (f'(a + b)² = {a**2 + (2*a*b) + b**2}')

def subtract_of_squares(a, b) -> int:
    """
        (a - b)² = a² - 2*a*b + b²
    """
    return (f'(a - b)² = {a**2 - (2*a*b) + b**2}')

def subtract_two_squares(a, b) -> int:
    """
        a² - b² = (a - b)*(a + b)
    """
    return (f'a² - b²  = {(a - b)*(a + b)}')

def sum_of_cubes(a, b) -> int:
    """
        (a + b)³ = a³ + b³ + 3*a*b*(a + b)
    """
    return (f'(a + b)³ = {a**3 + b**3 + 3*a*b*(a + b)}')

def subtract_of_cubes(a, b) -> int:
    """
        (a - b)³ = a³ - b³ - 3*a*b*(a - b)
    """
    return (f'(a - b)³ = {a**3 - b**3 - 3*a*b*(a - b)}')

def cube_two_sums(a, b) -> int:
    """
        a³ + b³ = (a + b)*(a² - a*b + b²)
    """
    return (f'a³ + b³  = {(a + b)*((a**2) - a*b + (b**2))}')

def cube_two_subtracts(a, b) -> int:
    """
        a³ - b³ = (a - b)*(a² + a*b + b²)
    """
    return (f'a³ - b³  = {(a - b)*((a**2) + a*b + (b**2))}')

# try:
#     a = int('Enter a > ')
#     b = int('Enter b > ')
    
# except ValueError:
#     logger.warning('Both a and b must be integer.')


# @get_time
# def get_result():
#     with cProfile.Profile() as pr:
#         pass
    
#     pr.print_stats()
    

if __name__ == '__main__':
    logger.info(sum_of_squares(2, 3))
    logger.info(subtract_of_squares(3, 4))
    logger.info(subtract_two_squares(5, 6))
    logger.info(sum_of_cubes(4, 8))
    logger.info(subtract_of_cubes(4, 6))
    logger.info(cube_two_sums(6, 7))
    logger.info(cube_two_subtracts(6, 7))