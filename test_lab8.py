import unittest
from lab8 import solve_wchain

class TestWChain(unittest.TestCase):
    def test_example_1(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        self.assertEqual(solve_wchain(len(words), words), 6)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(solve_wchain(len(words), words), 4)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(solve_wchain(len(words), words), 1)

    def test_empty_or_single(self):
        self.assertEqual(solve_wchain(1, ["python"]), 1)
        self.assertEqual(solve_wchain(0, []), 0)

if __name__== "__main__":
    unittest.main()