import unittest
from lab2 import largest_min_distance


class TestAggressiveCows(unittest.TestCase):


    def test_example(self):
        stalls = [1, 2, 8, 4, 9]
        self.assertEqual(largest_min_distance(stalls, 5, 3), 3)


    def test_simple_case(self):
        stalls = [1, 2, 3, 4, 5]
        self.assertEqual(largest_min_distance(stalls, 5, 2), 4)


    def test_equal_spacing(self):
        stalls = [1, 3, 5, 7, 9]
        self.assertEqual(largest_min_distance(stalls, 5, 3), 4)


    def test_already_sorted(self):
        stalls = [2, 4, 6, 8, 10]
        self.assertEqual(largest_min_distance(stalls, 5, 2), 8)


    def test_reverse_sorted(self):
        stalls = [10, 8, 6, 4, 2]
        self.assertEqual(largest_min_distance(stalls, 5, 2), 8)


    def test_min_stalls(self):
        stalls = [1, 100]
        self.assertEqual(largest_min_distance(stalls, 2, 2), 99)


    def test_one_cow(self):
        stalls = [1, 2, 3, 4, 5]
        self.assertEqual(largest_min_distance(stalls, 5, 1), 0)


    def test_same_positions(self):
        stalls = [5, 5, 5, 5]
        self.assertEqual(largest_min_distance(stalls, 4, 2), 0)

    def test_cows(self):
        stalls = [1, 2, 3, 4, 6, 7, 10]
        self.assertEqual(largest_min_distance(stalls, 7, 3), 4)

if __name__ == "__main__":
    unittest.main()