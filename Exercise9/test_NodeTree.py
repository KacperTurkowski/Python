from unittest import TestCase
from NodeTree import *


class TestNode(TestCase):
    def setUp(self):
        self.root = Node(5)
        self.root.left = Node(4)
        self.root.right = Node(3)
        self.root.left.left = Node(2)
        self.root.right.left = Node(6)
        self.root.right.right = Node(1)

    def test_count_leafs(self):
        self.assertEqual(self.root.count_leafs(), 3)

    def test_count_total(self):
        print(self.root.count_total())
        self.assertEqual(self.root.count_total(), 21)
