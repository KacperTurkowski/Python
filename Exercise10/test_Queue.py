import unittest
from Queue import *


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(3)

    def test_get(self):
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        self.assertEqual(self.queue.get(), 1)
        self.assertEqual(self.queue.get(), 2)
        self.assertEqual(self.queue.get(), 3)
        with self.assertRaises(EmptyQueueException):
            self.queue.get()

    def test_put(self):
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        with self.assertRaises(FullQueueException):
            self.queue.put(4)


if __name__ == '__main__':
    unittest.main()

