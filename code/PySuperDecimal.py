"""
This file contains code of PySuperDecimal data type.
Author: CreativeCloudAppDev2020
"""


# Importing necessary libraries


from mpmath import *
import copy
import math

mp.pretty = True


class PySuperDecimal:
    def __init__(self, value):
        # type: (str) -> None
        self.value: mpf = mpf(str(value))

    # Addition
    def __add__(self, other):
        # type: (PySuperDecimal) -> PySuperDecimal
        return PySuperDecimal(str(mpf(str(self.value)) + mpf(str(other.value))))

    # Subtraction
    def __sub__(self, other):
        # type: (PySuperDecimal) -> PySuperDecimal
        return PySuperDecimal(str(mpf(str(self.value)) - mpf(str(other.value))))

    # Multiplication
    def __mul__(self, other):
        # type: (PySuperDecimal) -> PySuperDecimal
        return PySuperDecimal(str(mpf(str(self.value)) * mpf(str(other.value))))

    # Division
    def __truediv__(self, other):
        # type: (PySuperDecimal) -> PySuperDecimal
        return PySuperDecimal(str(mpf(str(self.value)) / mpf(str(other.value))))

    # Integer Division
    def __floordiv__(self, other):
        # type: (PySuperDecimal) -> PySuperDecimal
        return PySuperDecimal(str(int(mpf(str(self.value)) / mpf(str(other.value)))))

    # Modulus
    def __mod__(self, other):
        # type: (PySuperDecimal) -> PySuperDecimal
        return PySuperDecimal(str(mpf(str(self.value)) % mpf(str(other.value))))

    # Exponent
    def __pow__(self, power):
        # type: (PySuperDecimal) -> PySuperDecimal
        return PySuperDecimal(str(mpf(str(self.value)) ** mpf(str(power.value))))

    def __str__(self):
        # type: () -> str
        return str(mpf(str(self.value)))

    def clone(self):
        # type: () -> PySuperDecimal
        return copy.deepcopy(self)


# Trigonometric functions


def sin(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal(mpf(math.sin(mpf(str(py_super_decimal.value)))))


def cos(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal(mpf(math.cos(mpf(str(py_super_decimal.value)))))


def tan(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal(mpf(math.tan(mpf(str(py_super_decimal.value)))))


def cosec(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal("1") / sin(py_super_decimal)


def sec(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal("1") / cos(py_super_decimal)


def cot(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal("1") / tan(py_super_decimal)


# Hyperbolic functions


def sinh(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal(mpf(math.sinh(mpf(str(py_super_decimal.value)))))


def cosh(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal(mpf(math.cosh(mpf(str(py_super_decimal.value)))))


def tanh(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal(mpf(math.tanh(mpf(str(py_super_decimal.value)))))


def cosech(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal("1") / sinh(py_super_decimal)


def sech(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal("1") / cosh(py_super_decimal)


def coth(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return PySuperDecimal("1") / tanh(py_super_decimal)


# Square Root


def sqrt(py_super_decimal: PySuperDecimal) -> PySuperDecimal:
    return py_super_decimal ** PySuperDecimal("0.5")
