"""Basic calculator operations for the PyBuilder lab."""

import math


def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return y subtracted from x."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return x divided by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def modulus(x, y):
    """Return the remainder when x is divided by y."""
    if y == 0:
        raise ValueError("Cannot calculate modulus with zero.")
    return x % y


def power(x, y):
    """Return x raised to the power y."""
    return x**y


def square_root(x):
    """Return the square root of x."""
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(x)
