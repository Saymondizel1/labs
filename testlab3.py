import unittest
from lab3 import BinaryTree

class TestInOrderTraversal(unittest.TestCase):
    def test_example_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.left.right = BinaryTree(7)
        expected = [2, 5, 1, 6, 7, 3]
        self.assertEqual(BinaryTree.in_order_traversal(root), expected)

    def test_empty_tree(self):
        self.assertEqual(BinaryTree.in_order_traversal(None), [])

    def test_single_node(self):
        root = BinaryTree(42)
        self.assertEqual(BinaryTree.in_order_traversal(root), [42])

    def test_left_skewed_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(1)
        expected = [1, 2, 3]
        self.assertEqual(BinaryTree.in_order_traversal(root), expected)

    def test_right_skewed_tree(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.right.right = BinaryTree(3)
        expected = [1, 2, 3]
        self.assertEqual(BinaryTree.in_order_traversal(root), expected)

unittest.main()