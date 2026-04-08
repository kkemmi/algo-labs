import unittest
from lab3 import *


class TestBinaryTreeDiameter(unittest.TestCase):

    def test_example_tree(self):

        root = BinaryTree(1)

        root.left = BinaryTree(3)
        root.right = BinaryTree(2)

        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)

        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(5)

        root.left.left.left.left = BinaryTree(9)
        root.left.left.left.right = BinaryTree(6)

        self.assertEqual(binary_tree_diameter(root), 6)


if __name__ == "__main__":
    unittest.main()

