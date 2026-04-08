import unittest
from red_black_priority_queue import RedBlackPriorityQueue


class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()


    def test_insert_and_inorder(self):
        data = [("A", 2), ("B", 5), ("C", 1), ("D", 4)]
        for v, p in data:
            self.pq.insert(v, p)

        result = []
        self.collect_inorder(self.pq.root, result)

        priorities = [p for _, p in result]
        self.assertEqual(priorities, sorted(priorities, reverse=True))


    def collect_inorder(self, node, result):
        if node != self.pq.NIL:
            self.collect_inorder(node.left, result)
            result.append((node.value, node.priority))
            self.collect_inorder(node.right, result)


    def test_get_max(self):
        data = [("A", 2), ("B", 10), ("C", 5)]
        for v, p in data:
            self.pq.insert(v, p)

        max_node = self.pq.get_max()
        self.assertEqual(max_node.priority, 10)
        self.assertEqual(max_node.value, "B")


    def test_extract_max(self):
        data = [("A", 2), ("B", 10), ("C", 5)]
        for v, p in data:
            self.pq.insert(v, p)

        max_value = self.pq.extract_max()
        self.assertEqual(max_value, "B")

        new_max = self.pq.get_max()
        self.assertEqual(new_max.priority, 5)


    def test_multiple_extracts(self):
        data = [("A", 3), ("B", 8), ("C", 1), ("D", 6)]
        for v, p in data:
            self.pq.insert(v, p)

        results = []
        while self.pq.root != self.pq.NIL:
            results.append(self.pq.extract_max())

        self.assertEqual(results, ["B", "D", "A", "C"])


    def test_same_priorities(self):
        data = [("A", 5), ("B", 5), ("C", 5)]
        for v, p in data:
            self.pq.insert(v, p)

        results = []
        while self.pq.root != self.pq.NIL:
            results.append(self.pq.extract_max())

        self.assertEqual(len(results), 3)


    def test_root_is_black(self):
        self.pq.insert("A", 10)
        self.assertEqual(self.pq.root.color, "black")

    def test_no_red_red_violation(self):
        data = [("A", 10), ("B", 20), ("C", 30), ("D", 15)]
        for v, p in data:
            self.pq.insert(v, p)

        self.check_no_red_red(self.pq.root)

    def check_no_red_red(self, node):
        if node == self.pq.NIL:
            return

        if node.color == "red":
            self.assertEqual(node.left.color, "black")
            self.assertEqual(node.right.color, "black")

        self.check_no_red_red(node.left)
        self.check_no_red_red(node.right)


if __name__ == "__main__":
    unittest.main()