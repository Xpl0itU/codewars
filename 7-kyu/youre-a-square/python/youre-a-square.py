from math import sqrt

def is_square(n):
    try:
        n_square = sqrt(n)
    except:
        return False
    return n == n_square * n_square