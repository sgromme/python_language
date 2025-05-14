from math import sqrt

from src.exercises.decorators import count_calls

def quadratic(a, b, c):
    """
    Returns the two roots of the quadratic equation ax^2 + bx + c = 0.
    """
    d = b**2 - 4*a*c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2*a)
    else:
        return (-b + sqrt(d)) / (2*a), (-b - sqrt(d)) / (2*a)
    
