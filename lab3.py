class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree):

    diameter = 0

    def height(node):
        nonlocal diameter

        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        diameter = max(diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    height(tree)

    return diameter