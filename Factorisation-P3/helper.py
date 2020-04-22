from time import time
from primes import next_prime
from math import sqrt

def timer(func):
    def f(*args, **kwargs):
        start = time()
        x = func(*args, **kwargs)
        end = f'{time() - start:.4e}'
        if (func.__name__ == 'main'):
            res = f'\n{func.__name__.upper():<9}took ---> {end} '
        else:
            res = f'{func.__name__:<9}{args[0]:<10} took ---> {end} '
        print(f'{res} sec')
        return x
    return f

@timer
def factor(number):
    ceiling = sqrt(number)
    tmp = number
    div = 2
    while (tmp != 1):
        if (tmp%div == 0):
            tmp /= div
            yield div
        elif (div > ceiling):
            div = number
        else:
            div = next_prime(div)