import math

def add(a, b):
    a + b
def subtract(a, b):
    a - b
def multiply(a, b):
    a * b
def divide(a, b):#
    if a == 0:
        raise ZeroDivisionError
    else:
        b / a
def logarithm(a, b):# use math library/raise ValueError
    math.log(a,b)
    if a == 0 or b == 0:
        raise ValueError
def exponent(a, b):
    a**b
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass
