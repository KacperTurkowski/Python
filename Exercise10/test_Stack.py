import unittest
from Stack import *


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(2)

    def test_pop(self):
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertRaises(NothingToPopException, self.stack.pop)

    def test_push(self):
        self.stack.push(3)
        self.stack.push(4)
        with self.assertRaises(FullStackException):
            self.stack.push(4)


if __name__ == '__main__':
    unittest.main()
