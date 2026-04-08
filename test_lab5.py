import unittest
from lab5 import *

class TestIslands(unittest.TestCase):

    def test_example(self):
        matrix = [
            [1,0,1,1,1,0,0,0,0],
            [1,1,1,0,1,0,1,1,1],
            [0,0,0,0,1,0,1,1,1],
            [0,1,1,0,1,0,1,1,1],
            [0,0,0,0,1,1,1,0,0],
            [1,0,1,0,1,1,0,0,0],
            [1,1,1,1,1,0,0,1,1],
            [1,1,1,0,1,1,0,0,1],
            [0,1,0,1,0,1,1,0,1],
            [0,0,0,0,1,1,1,0,0]
        ]

        self.assertEqual(count_islands(matrix), 4)

    def test_empty(self):
        self.assertEqual(count_islands([]), 0)

    def test_no_islands(self):
        matrix = [
            [0,0],
            [0,0]
        ]
        self.assertEqual(count_islands(matrix), 0)

    def test_one_big_island(self):
        matrix = [
            [1,1],
            [1,1]
        ]
        self.assertEqual(count_islands(matrix), 1)

    def test_separate_islands(self):
        matrix = [
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ]
        self.assertEqual(count_islands(matrix), 4)


if __name__ == "__main__":
    unittest.main()