from math import sqrt

def is_div(x, y):
    return not x % y

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if is_div(x, 2) or is_div(x, 3):
        return False
    div = 6
    while div**2 - 2*div + 1 <= x:
    # while div <= sqrt(x):
        if is_div(x, div-1) or is_div(x, div+1):
            return False
        div += 6
    return True
    

def next_prime(x):
    if x == 2:
        return 3

    x+=2
    while not is_prime(x):
        x+=2

    return x