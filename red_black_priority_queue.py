class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, None)
        self.NIL.color = "black"
        self.root = self.NIL


    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y


    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y


    def insert(self, value, priority):
        node = Node(value, priority)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.priority >= current.priority:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.priority >= parent.priority:
            parent.left = node
        else:
            parent.right = node

        node.color = "red"
        self.fix_insert(node)


    def fix_insert(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)

        self.root.color = "black"


    def get_max(self):
        current = self.root
        while current.left != self.NIL:
            current = current.left
        return current


    def extract_max(self):
        node = self.get_max()
        value = node.value
        self.delete(node)
        return value


    def delete(self, node):
        if node.left == self.NIL:
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            self.transplant(node, node.left)
        else:
            successor = self.minimum(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node


    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(f"{node.value} (priority={node.priority}, {node.color})")
            self.inorder(node.right)