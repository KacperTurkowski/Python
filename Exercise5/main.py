# ZADANIE 5.1
# Stworzyć plik rekurencja.py i zapisać w nim funkcje z zadań 4.3 (factorial), 4.4 (fibonacci). Sprawdzić operacje importu i przeładowania modułu.
import Rekurencja

print(Rekurencja.factorial(6))
print(Rekurencja.fibonacci(5))

import Rekurencja as rek

print(rek.factorial(6))
print(rek.fibonacci(5))

from Rekurencja import *

print(factorial(6))
print(fibonacci(5))

from Rekurencja import factorial
from Rekurencja import fibonacci as fib

print(factorial(6))
print(fib(5))

# ZADANIE 5.2
# Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.

f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)

import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac(f1, f3), [5, 2])
        self.assertEqual(add_frac(f2, f1), f1)
        self.assertEqual(add_frac(f3, [0, 0]), f3)
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(f1, f3), [-7, 2])
        self.assertEqual(sub_frac(f2, f1), [1, 2])
        self.assertEqual(sub_frac(f3, [0, 0]), f3)
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(f1, f3), [-3, 2])
        self.assertEqual(mul_frac(f2, f1), [0, 0])
        self.assertEqual(mul_frac(f3, [0, 0]), [0, 0])
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac(f1, f3), [-1, 6])
        self.assertEqual(div_frac(f2, f1), [0, 0])
        self.assertEqual(div_frac(f3, [0, 0]), None)
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertFalse(is_positive(f1))
        self.assertFalse(is_positive(f2))
        self.assertTrue(is_positive(f3))
        self.assertTrue(is_positive(f4))
        self.assertFalse(is_positive(f5))
        self.assertTrue(is_positive([1, 2]))

    def test_is_zero(self):
        self.assertFalse(is_zero(f1))
        self.assertTrue(is_zero(f2))
        self.assertFalse(is_zero(f3))
        self.assertFalse(is_zero(f4))
        self.assertTrue(is_zero(f5))
        self.assertTrue(is_zero([0, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(f1, f2), 1)
        self.assertEqual(cmp_frac(f1, f3), 1)
        self.assertEqual(cmp_frac(f1, f4), 1)
        self.assertEqual(cmp_frac(f2, f1), -1)
        self.assertEqual(cmp_frac(f2, f3), 1)
        self.assertEqual(cmp_frac(f2, f5), 0)
        self.assertEqual(cmp_frac(f3, f4), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float(f1), -0.5)
        self.assertEqual(frac2float(f2), 0)
        self.assertEqual(frac2float(f3), 3)
        self.assertEqual(frac2float(f4), 3)
        self.assertEqual(frac2float(f5), 0)
        self.assertEqual(frac2float([2, 4]), float(2 / 4))

    def tearDown(self): pass


unittest.main()
