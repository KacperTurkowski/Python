import unittest
from RandomQueue import *


class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.randomQueue = RandomQueue()

    def test_Insert(self):
        self.randomQueue.insert(3)
        self.assertEqual(1, len(self.randomQueue.elements))
        self.assertEqual(False, self.randomQueue.is_empty())

    def test_Remove(self):
        self.randomQueue.insert(2)
        self.assertEqual(2, self.randomQueue.remove())

    def test_Clear(self):
        self.randomQueue.insert(2)
        self.randomQueue.insert(1)
        self.randomQueue.insert(3)
        self.randomQueue.clear()
        self.assertEqual(0, len(self.randomQueue.elements))


if __name__ == '__main__':
    unittest.main()
