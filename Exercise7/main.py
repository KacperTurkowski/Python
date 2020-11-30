from fracs import *
from rectangle import *
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.f1 = Frac(-1, 2)  # -1/2
        self.f2 = Frac(0, 1)  # zero
        self.f3 = Frac(3, 1)  # 3
        self.f4 = Frac(6, 2)  # 3 (niejednoznaczność)
        self.f5 = Frac(0, 2)  # zero (niejednoznaczność)

    def test_str(self):
        self.assertEqual(str(self.f1), "-1/2")
        self.assertEqual(str(self.f2), "0")
        self.assertEqual(str(self.f3), "3")
        self.assertEqual(str(self.f4), "3")
        self.assertEqual(str(self.f5), "0")

    def test_repr(self):
        self.assertEqual(repr(self.f1), "Frac(-1, 2)")
        self.assertEqual(repr(self.f2), "Frac(0, 1)")
        self.assertEqual(repr(self.f3), "Frac(3, 1)")
        self.assertEqual(repr(self.f4), "Frac(3, 1)")
        self.assertEqual(repr(self.f5), "Frac(0, 1)")

    def test_eq(self):
        self.assertFalse(self.f1 == self.f2)
        self.assertTrue(self.f2 == self.f5)
        self.assertTrue(self.f3 == self.f4)

    def test_ne(self):
        self.assertTrue(self.f1 != self.f2)
        self.assertFalse(self.f2 != self.f5)
        self.assertFalse(self.f3 != self.f4)

    def test_lt(self):
        self.assertTrue(self.f1 < self.f2)
        self.assertTrue(self.f1 < self.f3)
        self.assertFalse(self.f2 < self.f5)
        self.assertFalse(self.f3 < self.f4)
        self.assertFalse(self.f3 < self.f5)

    def test_le(self):
        self.assertTrue(self.f1 <= self.f2)
        self.assertTrue(self.f1 <= self.f3)
        self.assertTrue(self.f2 <= self.f5)
        self.assertTrue(self.f3 <= self.f4)
        self.assertFalse(self.f3 <= self.f5)

    def test_gt(self):
        self.assertFalse(self.f1 > self.f2)
        self.assertFalse(self.f1 > self.f3)
        self.assertFalse(self.f2 > self.f5)
        self.assertFalse(self.f3 > self.f4)
        self.assertTrue(self.f3 > self.f5)

    def test_ge(self):
        self.assertFalse(self.f1 >= self.f2)
        self.assertFalse(self.f1 >= self.f3)
        self.assertTrue(self.f2 >= self.f5)
        self.assertTrue(self.f3 >= self.f4)
        self.assertTrue(self.f3 >= self.f5)

    def test_add(self):
        self.assertEqual(self.f1 + self.f3, Frac(5, 2))
        self.assertEqual(self.f2 + self.f1, self.f1)
        self.assertEqual(self.f3 + self.f4, Frac(6, 1))
        self.assertEqual(self.f1 + 2, Frac(3, 2))
        self.assertEqual(2 + self.f1, Frac(3, 2))
        self.assertEqual(self.f1 + 2.5, Frac(2, 1))
        self.assertEqual(2.5 + self.f1, Frac(2, 1))

    def test_sub(self):
        self.assertEqual(self.f1 - self.f3, Frac(-7, 2))
        self.assertEqual(self.f2 - self.f1, Frac(1, 2))
        self.assertEqual(self.f3 - self.f4, self.f2)
        self.assertEqual(self.f1 - 2, Frac(-5, 2))
        self.assertEqual(2 - self.f1, Frac(5, 2))
        self.assertEqual(self.f1 - 2.5, Frac(-3, 1))
        self.assertEqual(2.5 - self.f1, Frac(3, 1))

    def test_mul(self):
        self.assertEqual(self.f1 * self.f3, Frac(-3, 2))
        self.assertEqual(self.f2 * self.f1, Frac(0, 1))
        self.assertEqual(self.f3 * self.f5, Frac(0, 1))
        self.assertEqual(self.f1 * 2, Frac(-1, 1))
        self.assertEqual(2 * self.f1, Frac(-1, 1))
        self.assertEqual(self.f1 * 2.5, Frac(-5, 4))
        self.assertEqual(2.5 * self.f1, Frac(-5, 4))

    def test_div(self):
        self.assertEqual(self.f1 / self.f3, Frac(-1, 6))
        self.assertEqual(self.f2 / self.f1, Frac(0, 1))
        self.assertEqual(self.f3 / self.f4, Frac(1, 1))
        self.assertEqual(self.f1 / 2, Frac(-1, 4))
        self.assertEqual(2 / self.f1, Frac(-4, 1))
        self.assertEqual(self.f1 / 2.5, Frac(-1, 5))
        self.assertEqual(2.5 / self.f1, Frac(-5, 1))

    def test_neg(self):
        self.assertEqual(-self.f1, Frac(-self.f1.x, self.f1.y))
        self.assertEqual(-self.f2, Frac(-self.f2.x, self.f2.y))
        self.assertEqual(-self.f3, Frac(-self.f3.x, self.f3.y))
        self.assertEqual(-self.f4, Frac(-self.f4.x, self.f4.y))
        self.assertEqual(-self.f5, Frac(-self.f5.x, self.f5.y))

    def test_invert(self):
        self.assertEqual(~self.f1, Frac(self.f1.y, self.f1.x))
        with self.assertRaises(ValueError):
            ~self.f2
        self.assertEqual(~self.f3, Frac(self.f3.y, self.f3.x))
        self.assertEqual(~self.f4, Frac(self.f4.y, self.f4.x))
        with self.assertRaises(ValueError):
            ~self.f5

    def test_float(self):
        self.assertEqual(float(self.f1), -0.5)
        self.assertEqual(float(self.f2), 0)
        self.assertEqual(float(self.f3), 3)
        self.assertEqual(float(self.f4), 3)
        self.assertEqual(float(self.f5), 0)

    def tearDown(self): pass


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(1, 2, 2, 3)
        self.r2 = Rectangle(-1, -1, 1, 1)
        self.r3 = Rectangle(0, 0, 10, 15)

    def test_str(self):
        self.assertEqual(str(self.r1), '[(1, 2), (2, 3)]')
        self.assertEqual(str(self.r2), '[(-1, -1), (1, 1)]')
        self.assertEqual(str(self.r3), '[(0, 0), (10, 15)]')

    def test_repr(self):
        self.assertEqual(repr(self.r1), 'Rectangle(1, 2, 2, 3)')
        self.assertEqual(repr(self.r2), 'Rectangle(-1, -1, 1, 1)')
        self.assertEqual(repr(self.r3), 'Rectangle(0, 0, 10, 15)')

    def test_eq(self):
        self.assertTrue(self.r1 == self.r1)
        self.assertFalse(self.r2 == self.r3)

    def test_ne(self):
        self.assertFalse(self.r3 != self.r3)
        self.assertTrue(self.r2 != self.r3)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(1.5, 2.5))
        self.assertEqual(self.r2.center(), Point(0, 0))
        self.assertEqual(self.r3.center(), Point(5, 7.5))

    def test_area(self):
        self.assertEqual(self.r1.area(), 1)
        self.assertEqual(self.r2.area(), 4)
        self.assertEqual(self.r3.area(), 150)

    def test_move(self):
        self.assertEqual(self.r1.move(2, 2), Rectangle(3, 4, 4, 5))
        self.assertEqual(self.r2.move(3, 3), Rectangle(2, 2, 4, 4))
        self.assertEqual(self.r3.move(3.5, 3.5), Rectangle(3.5, 3.5, 13.5, 18.5))

    def test_intersection(self):
        self.assertEqual(self.r1.intersection(self.r2), None)
        self.assertEqual(self.r1.intersection(self.r3), Rectangle(1, 2, 2, 3))
        self.assertEqual(self.r2.intersection(self.r3), Rectangle(0, 0, 1, 1))

    def test_cover(self):
        self.assertEqual(self.r1.cover(self.r2), Rectangle(-1, -1, 2, 3))
        self.assertEqual(self.r1.cover(self.r3), Rectangle(0, 0, 10, 15))
        self.assertEqual(self.r2.cover(self.r3), Rectangle(-1, -1, 10, 15))

    def test_make4(self):
        self.assertEqual(self.r2.make4(), (Rectangle(-1, -1, 0, 0), Rectangle(-1, 0, 0, 1), Rectangle(0, -1, 1, 0), Rectangle(0, 0, 1, 1)))


unittest.main()
