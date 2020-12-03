import functions
import unittest


class TestFunctions(unittest.TestCase):

    def setUp(self): pass

    def testsolve1(self):
        with self.assertRaises(ValueError):
            functions.solve1(0, 0, 0)
        self.assertEqual(functions.solve1(0, 1, 0), "y = 0")
        self.assertEqual(functions.solve1(1, 0, 0), "x = 0")
        self.assertEqual(functions.solve1(1, 1, 0), "y = -1.0x")
        with self.assertRaises(ValueError):
            functions.solve1(0, 0, 1)
        self.assertEqual(functions.solve1(0, 1, 1), "y = -1.0")
        self.assertEqual(functions.solve1(1, 0, 1), "x = -1.0")
        self.assertEqual(functions.solve1(1, 1, 1), "y = -1.0x -1.0")

    def testcalc_pi(self):
        self.assertTrue(3.13 < functions.calc_pi(100000) < 3.16)

    def testheron(self):
        self.assertEqual(functions.heron(1, 2, 3), 0)
        self.assertEqual(functions.heron(0, 0, 0), 0)
        self.assertEqual(functions.heron(3, 4, 5), 6)

    def testP_R(self):
        self.assertEqual(functions.P_R(2, 3), functions.P(2, 3))
        self.assertEqual(functions.P_R(0, 0), functions.P(0, 0))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
