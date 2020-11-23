import unittest
from fracs import *
from points import *


class TestPoints(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(Point(3, 4).__str__(), "(3, 4)")

    def test_repr(self):
        self.assertEqual(Point(3, 4).__repr__(), "Point(3, 4)")

    def test_eq(self):
        self.assertTrue(Point(3, 4).__eq__(Point(3, 4)))
        self.assertFalse(Point(3, 4).__eq__(Point(6, 9)))

    def test_ne(self):
        self.assertFalse(Point(3, 4).__ne__(Point(3, 4)))
        self.assertTrue(Point(3, 4).__ne__(Point(6, 9)))

    def test_add(self):
        self.assertEqual(Point(3, 4).__add__(Point(3, 4)), Point(6, 8))
        self.assertEqual(Point(-3, -4).__add__(Point(3, 4)), Point(0, 0))

    def test_sub(self):
        self.assertEqual(Point(3, 4).__sub__(Point(3, 4)), Point(0, 0))
        self.assertEqual(Point(3, 4).__sub__(Point(2, 1)), Point(1, 3))

    def test_mul(self):
        self.assertEqual(Point(3, 4).__mul__(Point(3, 4)), 25)

    def test_cross(self):
        self.assertEqual(Point(3, 4).cross(Point(3, 4)), 0)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)

    def tearDown(self): pass


f1 = Frac(-1, 2)  # -1/2
f2 = Frac(0, 1)  # zero
f3 = Frac(3, 1)  # 3
f4 = Frac(6, 2)  # 3 (niejednoznaczność)
f5 = Frac(0, 2)  # zero (niejednoznaczność)


class TestFractions(unittest.TestCase):

    def setUp(self):
        pass

    def test_str(self):
        self.assertEqual(f1.__str__(), "-1/2")
        self.assertEqual(f2.__str__(), "0")
        self.assertEqual(f3.__str__(), "3")
        self.assertEqual(f4.__str__(), "6/2")
        self.assertEqual(f5.__str__(), "0/2")

    def test_repr(self):
        self.assertEqual(f1.__repr__(), "Frac(-1, 2)")
        self.assertEqual(f2.__repr__(), "Frac(0, 1)")
        self.assertEqual(f3.__repr__(), "Frac(3, 1)")
        self.assertEqual(f4.__repr__(), "Frac(6, 2)")
        self.assertEqual(f5.__repr__(), "Frac(0, 2)")

    def test_eq(self):
        self.assertFalse(f1.__eq__(f2))
        self.assertTrue(f2.__eq__(f5))
        self.assertTrue(f3.__eq__(f4))

    def test_ne(self):
        self.assertTrue(f1.__ne__(f2))
        self.assertFalse(f2.__ne__(f5))
        self.assertFalse(f3.__ne__(f4))

    def test_lt(self):
        self.assertTrue(f1.__lt__(f2))
        self.assertTrue(f1.__lt__(f3))
        self.assertFalse(f2.__lt__(f5))
        self.assertFalse(f3.__lt__(f4))
        self.assertFalse(f3.__lt__(f5))

    def test_le(self):
        self.assertTrue(f1.__le__(f2))
        self.assertTrue(f1.__le__(f3))
        self.assertTrue(f2.__le__(f5))
        self.assertTrue(f3.__le__(f4))
        self.assertFalse(f3.__le__(f5))

    def test_gt(self):
        self.assertFalse(f1.__gt__(f2))
        self.assertFalse(f1.__gt__(f3))
        self.assertFalse(f2.__gt__(f5))
        self.assertFalse(f3.__gt__(f4))
        self.assertTrue(f3.__gt__(f5))

    def test_ge(self):
        self.assertFalse(f1.__ge__(f2))
        self.assertFalse(f1.__ge__(f3))
        self.assertTrue(f2.__ge__(f5))
        self.assertTrue(f3.__ge__(f4))
        self.assertTrue(f3.__ge__(f5))

    def test_add(self):
        self.assertEqual(f1.__add__(f3), Frac(5, 2))
        self.assertEqual(f2.__add__(f1), f1)
        self.assertEqual(f3.__add__(f4), Frac(6, 1))

    def test_sub(self):
        self.assertEqual(f1.__sub__(f3), Frac(-7, 2))
        self.assertEqual(f2.__sub__(f1), Frac(1, 2))
        self.assertEqual(f3.__sub__(f4), f2)

    def test_mul(self):
        self.assertEqual(f1.__mul__(f3), Frac(-3, 2))
        self.assertEqual(f2.__mul__(f1), Frac(0, 1))
        self.assertEqual(f3.__mul__(f5), Frac(0, 1))

    def test_div(self):
        self.assertEqual(f1.__div__(f3), Frac(-1, 6))
        self.assertEqual(f2.__div__(f1), Frac(0, 1))
        self.assertEqual(f3.__div__(f4), Frac(1, 1))

    def test_pos(self):
        self.assertEqual(f1.__pos__(), f1)
        self.assertEqual(f2.__pos__(), f2)
        self.assertEqual(f3.__pos__(), f3)
        self.assertEqual(f4.__pos__(), f4)
        self.assertEqual(f5.__pos__(), f5)

    def test_neg(self):
        self.assertEqual(f1.__neg__(), Frac(-f1.x, f1.y))
        self.assertEqual(f2.__neg__(), Frac(-f2.x, f2.y))
        self.assertEqual(f3.__neg__(), Frac(-f3.x, f3.y))
        self.assertEqual(f4.__neg__(), Frac(-f4.x, f4.y))
        self.assertEqual(f5.__neg__(), Frac(-f5.x, f5.y))

    def test_invert(self):
        self.assertEqual(f1.__invert__(), Frac(f1.y, f1.x))
        self.assertEqual(f2.__invert__(), 'denominator is 0')
        self.assertEqual(f3.__invert__(), Frac(f3.y, f3.x))
        self.assertEqual(f4.__invert__(), Frac(f4.y, f4.x))
        self.assertEqual(f5.__invert__(), 'denominator is 0')

    def test_float(self):
        self.assertEqual(f1.__float__(), -0.5)
        self.assertEqual(f2.__float__(), 0)
        self.assertEqual(f3.__float__(), 3)
        self.assertEqual(f4.__float__(), 3)
        self.assertEqual(f5.__float__(), 0)

    def tearDown(self): pass


unittest.main()
