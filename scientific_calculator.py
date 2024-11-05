import math
from functools import wraps

class MyCalculator:

    # Found a nice way of removing duplicate code for checking numeric input
    # Wrappers used as a decorator, is helping in removing duplicate code for every method.

    @staticmethod
    def validate_numeric_input(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) == 1:
                if not isinstance(args[0], (int, float)):
                    raise ValueError("Input must be a number")
            else:
                if not all(isinstance(arg, (int, float)) for arg in args):
                    raise ValueError("All inputs must be numbers")
            return func(*args)
        return wrapper

    # add 2 real numbers.
    @staticmethod
    @validate_numeric_input
    def add(a, b):
        return a + b

    # subtract 2 real numbers.
    @staticmethod
    @validate_numeric_input
    def subtract(a, b):
        return a - b

    # sine of a number.
    @staticmethod
    @validate_numeric_input
    def sin(x):
        return math.sin(math.radians(x))

    # cosine of a number.
    @staticmethod
    @validate_numeric_input
    def cos(x):
        return math.cos(math.radians(x))

    # tangent of a number.
    @staticmethod
    @validate_numeric_input
    def tan(x):
        if x % 180 == 90:
            raise ValueError("Tangent is infinite for 90 degrees and its multiples")
        return math.tan(math.radians(x))

    # square root of a number.
    @staticmethod
    @validate_numeric_input
    def sqrt(x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)

    # logarithm of a number.
    @staticmethod
    @validate_numeric_input
    def log(x):
        if x <= 0:
            raise ValueError("Cannot calculate logarithm of a non-positive number")
        return math.log(x)

    # exponent of a number.
    @staticmethod
    @validate_numeric_input
    def exp(x):
        return math.exp(x)

    # sine inverse of a number.
    @staticmethod
    @validate_numeric_input
    def asin(x):
        if x < -1 or x > 1:
            raise ValueError("Input for asin must be between -1 and 1")
        return math.degrees(math.asin(x))

    # cosine inverse of a number.
    @staticmethod
    @validate_numeric_input
    def acos(x):
        if x < -1 or x > 1:
            raise ValueError("Input for acos must be between -1 and 1")
        return math.degrees(math.acos(x))

    # tangent inverse of a number.
    @staticmethod
    @validate_numeric_input
    def atan(x):
        return math.degrees(math.atan(x))

    # sine hyperbolic of a number.
    @staticmethod
    @validate_numeric_input
    def sinh(x):
        return math.sinh(x)

    # cosine hyperbolic of a number.
    @staticmethod
    @validate_numeric_input
    def cosh(x):
        return math.cosh(x)

    # tangent hyperbolic of a number.
    @staticmethod
    @validate_numeric_input
    def tanh(x):
        return math.tanh(x)