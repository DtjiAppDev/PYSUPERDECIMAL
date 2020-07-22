import unittest
from PySuperDecimal import *
import math


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        a: PySuperDecimal = PySuperDecimal("5.13")
        b: PySuperDecimal = PySuperDecimal("4.69")
        self.assertEqual(str(a + b), str(PySuperDecimal("9.82")))

    def test_subtraction(self):
        a: PySuperDecimal = PySuperDecimal("5.13")
        b: PySuperDecimal = PySuperDecimal("4.69")
        self.assertEqual(str(a - b), str(PySuperDecimal("0.44")))

    def test_multiplication(self):
        a: PySuperDecimal = PySuperDecimal("5.13")
        b: PySuperDecimal = PySuperDecimal("4.69")
        self.assertEqual(str(a * b), str(PySuperDecimal("24.0597")))

    def test_division(self):
        a: PySuperDecimal = PySuperDecimal("5.13")
        b: PySuperDecimal = PySuperDecimal("4.69")
        self.assertEqual(str(a / b), str(PySuperDecimal("1.09381663113006")))

    def test_integer_division(self):
        a: PySuperDecimal = PySuperDecimal("5.13")
        b: PySuperDecimal = PySuperDecimal("4.69")
        self.assertEqual(str(a // b), str(PySuperDecimal("1")))

    def test_modulus(self):
        a: PySuperDecimal = PySuperDecimal("8")
        b: PySuperDecimal = PySuperDecimal("3")
        self.assertEqual(str(a % b), str(PySuperDecimal("2")))

    def test_exponent(self):
        a: PySuperDecimal = PySuperDecimal("2")
        b: PySuperDecimal = PySuperDecimal("3")
        self.assertEqual(str(a ** b), str(PySuperDecimal("8")))

    def test_sine(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(sin(a)), str(PySuperDecimal("1.0")))

    def test_cosine(self):
        a: PySuperDecimal = PySuperDecimal(str(0))
        self.assertEqual(str(cos(a)), str(PySuperDecimal("1.0")))

    def test_tangent(self):
        a: PySuperDecimal = PySuperDecimal(str(0))
        self.assertEqual(str(tan(a)), str(PySuperDecimal("0")))

    def test_cosecant(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(cosec(a)), str(PySuperDecimal("1.0")))

    def test_secant(self):
        a: PySuperDecimal = PySuperDecimal(str(0))
        self.assertEqual(str(sec(a)), str(PySuperDecimal("1.0")))

    def test_cotangent(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 4))
        self.assertEqual(str(cot(a)), str(PySuperDecimal("1")))

    def test_sinh(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(sinh(a)), str(PySuperDecimal("2.3012989023073")))

    def test_cosh(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(cosh(a)), str(PySuperDecimal("2.50917847865806")))

    def test_tanh(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(tanh(a)), str(PySuperDecimal("0.917152335667275")))

    def test_cosech(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(cosech(a)), str(PySuperDecimal("0.434537208094695")))

    def test_sech(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(sech(a)), str(PySuperDecimal("0.398536815338386")))

    def test_coth(self):
        a: PySuperDecimal = PySuperDecimal(str(math.pi / 2))
        self.assertEqual(str(coth(a)), str(PySuperDecimal("1.09033141072737")))

    def test_sqrt(self):
        a: PySuperDecimal = PySuperDecimal("6.25")
        self.assertEqual(str(sqrt(a)), str(PySuperDecimal("2.5")))


if __name__ == '__main__':
    unittest.main()
