# https://github.com/samigrace111/lab10-SS
# Partner 1: Samantha Sobrino
# Partner 2:

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def mul(a, b):
    """Same logic as multiply"""
    return a * b

def div(a, b):
    """Same logic as divide"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def logarithm(x, base):
    """
    Raises ValueError if x <= 0, base <= 0, or base == 1.
    """
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid domain for logarithm")
    return math.log(x, base)

def exp(base, exponent):
    """ Raise base to a given exponent. """
    return base ** exponent

def hypotenuse(a, b):
    """ Returns the length of the hypotenuse for legs a and b. """
    return math.sqrt(a*a + b*b)

def square_root(x):
    """ Returns the square root of x, raises ValueError if x < 0. """
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)
