from unittest import TestCase
from DoubleList import *
from NodeDouble import *


class TestDoubleList(TestCase):

    def setUp(self):
        self.list1 = DoubleList()
        self.list2 = DoubleList()
        self.list2.insert_head(Node(0))
        self.list2.insert_head(Node(1))
        self.list2.insert_head(Node(2))
        self.list3 = DoubleList()

    def test_is_empty(self):
        self.assertTrue(self.list1.is_empty())
        self.assertFalse(self.list2.is_empty())

    def test_count(self):
        self.assertEqual(self.list1.count(), 0)
        self.assertEqual(self.list2.count(), 3)

    def test_insert_head(self):
        self.list1.insert_head(Node(0))
        self.assertEqual(self.list1.length, 1)
        self.assertEqual(self.list1.head, self.list1.tail)
        self.assertEqual(self.list1.head.data, 0)

    def test_insert_tail(self):
        self.list1.insert_tail(Node(0))
        self.assertEqual(self.list1.length, 1)
        self.assertEqual(self.list1.head, self.list1.tail)
        self.assertEqual(self.list1.tail.data, 0)

    def test_remove_head(self):
        length = self.list2.length
        x = self.list2.remove_head()
        self.assertEqual(self.list2.length, length-1)
        self.assertTrue(x.data != self.list2.head)

    def test_remove_tail(self):
        length = self.list2.length
        x = self.list2.remove_tail()
        self.assertEqual(self.list2.length, length-1)
        self.assertTrue(x.data != self.list2.head)

    def test_find_max(self):
        self.assertEqual(self.list2.find_max().data, 2)

    def test_find_min(self):
        self.assertEqual(self.list2.find_min().data, 0)

    def test_remove(self):
        node = self.list2.find_min()
        length = self.list2.length
        self.list2.remove(node)
        self.assertEqual(self.list2.length, length)

    def test_clear(self):
        self.list2.clear()
        self.assertEqual(self.list2.length, 0)
