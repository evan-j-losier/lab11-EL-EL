# https://github.com/evan-j-losier/lab11-EL-EL.git
# Partner 1: Evan Losier
# Partner 2: Enric Lin

import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)


def exp(a, b):
    return a ** b
def square_root(a): # raise ValueError if a < 0
    math.sqrt(a)
    if a < 0:
        raise ValueError
def hypotenuse(a, b):  # can have negative nums
    math.hypot(a, b)