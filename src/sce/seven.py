import cProfile
from time import perf_counter
# from clogs import logger

def get_time(func):
    """Times any function"""
    
    def wrapper():
        start = perf_counter()
        
        func()
        
        end = perf_counter()
        time_lapse = end - start
        
        print(f'Time lapse : {time_lapse:.4f} (s)')
        
    return wrapper

def sum_of_squares(a: int, b: int) -> int:
    """
        (a + b)² = a² + 2*a*b + b²
    """
    return (f'(a + b)² = {a**2 + (2*a*b) + b**2}')

def subtract_of_squares(a: int, b: int) -> int:
    """
        (a - b)² = a² - 2*a*b + b²
    """
    return (f'(a - b)² = {a**2 - (2*a*b) + b**2}')

def subtract_two_squares(a: int, b: int) -> int:
    """
        a² - b² = (a - b)*(a + b)
    """
    return (f'a² - b²  = {(a - b)*(a + b)}')

def sum_of_cubes(a: int, b: int) -> int:
    """
        (a + b)³ = a³ + b³ + 3*a*b*(a + b)
    """
    return (f'(a + b)³ = {a**3 + b**3 + 3*a*b*(a + b)}')

def subtract_of_cubes(a: int, b: int) -> int:
    """
        (a - b)³ = a³ - b³ - 3*a*b*(a - b)
    """
    return (f'(a - b)³ = {a**3 - b**3 - 3*a*b*(a - b)}')

def cube_two_sums(a: int, b: int) -> int:
    """
        a³ + b³ = (a + b)*(a² - a*b + b²)
    """
    return (f'a³ + b³  = {(a + b)*((a**2) - a*b + (b**2))}')

def cube_two_subtracts(a: int, b: int) -> int:
    """
        a³ - b³ = (a - b)*(a² + a*b + b²)
    """
    return (f'a³ - b³  = {(a - b)*((a**2) + a*b + (b**2))}')
    

if __name__ == '__main__':
    print(sum_of_squares(2, 3))
    print(subtract_of_squares(3, 4))
    print(subtract_two_squares(5, 6))
    print(sum_of_cubes(4, 8))
    print(subtract_of_cubes(4, 6))
    print(cube_two_sums(6, 7))
    print(cube_two_subtracts(6, 7))