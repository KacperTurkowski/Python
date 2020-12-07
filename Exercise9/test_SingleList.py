from unittest import TestCase
from SingleList import *
from Node import *


class TestSingleList(TestCase):

    def setUp(self):
        self.list1 = SingleList()
        self.list2 = SingleList()
        self.list2.insert_head(Node('a'))
        self.list2.insert_head(Node('b'))
        self.list3 = SingleList()
        self.list3.insert_head(Node('c'))
        self.list3.insert_head(Node('d'))
        self.list4 = SingleList()
        for i in range(0, 4):
            self.list4.insert_tail(Node(i))

    def test_is_empty(self):
        self.assertTrue(self.list1.is_empty())
        self.assertFalse(self.list2.is_empty())

    def test_count(self):
        self.assertEqual(self.list1.count(), 0)
        self.assertEqual(self.list2.count(), 2)

    def test_insert_head(self):
        node = Node('c')
        self.list2.insert_head(node)
        self.assertEqual(self.list2.head, node)

    def test_insert_tail(self):
        node = Node('d')
        self.list2.insert_tail(node)
        self.assertEqual(self.list2.tail, node)

    def test_remove_head(self):
        node = self.list2.remove_head()
        self.assertEqual(node.data, 'b')
        with self.assertRaises(ValueError):
            self.list1.remove_head()

    def test_remove_tail(self):
        node = self.list4.remove_tail()
        self.assertEqual(node.data, 3)
        self.assertEqual(self.list4.head.next.next.data, self.list4.tail.data)
        with self.assertRaises(ValueError):
            self.list1.remove_head()

    def test_merge(self):
        listtest = SingleList()
        listtest.insert_head(Node('a'))
        listtest.insert_head(Node('b'))
        listtest.insert_tail(Node('d'))
        listtest.insert_tail(Node('c'))
        self.list2.merge(self.list3)
        self.assertEqual(self.list2.head.data, listtest.head.data)
        self.assertEqual(self.list2.tail.data, listtest.tail.data)
        self.assertEqual(self.list2.length, listtest.length)
        self.assertEqual(self.list3.length, 0)

    def test_clear(self):
        self.list1.clear()
        self.list2.clear()
        self.list3.clear()
        self.assertEqual(self.list1.length, 0)
        self.assertEqual(self.list2.length, 0)
        self.assertEqual(self.list3.length, 0)

    def test_search(self):
        self.assertEqual(self.list1.search('a'), None)
        self.assertEqual(self.list2.search('a').data, 'a')
        self.assertEqual(self.list3.search('a'), None)
        self.assertEqual(self.list4.search('a'), None)

    def test_find_min(self):
        self.assertEqual(self.list4.find_min().data, 0)

    def test_find_max(self):
        self.assertEqual(self.list4.find_max().data, 3)

    def test_reverse(self):
        head = self.list4.head
        tail = self.list4.tail
        length = self.list4.length
        self.list4 = self.list4.reverse()
        self.assertEqual(self.list4.tail.data, head.data)
        self.assertEqual(self.list4.head.data, tail.data)
        self.assertEqual(self.list4.length, length)
