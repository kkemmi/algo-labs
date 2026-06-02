import unittest
from lab9 import *


class TestTrieStructure(unittest.TestCase):
    def setUp(self):
        self.patterns = ["cat", "car", "cart", "dog", "apple", "app"]
        self.trie = build_trie_from_patterns(self.patterns)

    def test_insert_and_search_exact_words(self):
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("car"))
        self.assertTrue(self.trie.search("cart"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))

    def test_search_non_existent_words(self):
        self.assertFalse(self.trie.search("house"))
        self.assertFalse(self.trie.search("cats"))
        self.assertFalse(self.trie.search("ca"))

    def test_starts_with_valid_prefixes(self):
        self.assertTrue(self.trie.starts_with("ca"))
        self.assertTrue(self.trie.starts_with("car"))
        self.assertTrue(self.trie.starts_with("do"))
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("apple"))

    def test_starts_with_invalid_prefixes(self):
        self.assertFalse(self.trie.starts_with("b"))
        self.assertFalse(self.trie.starts_with("doc"))
        self.assertFalse(self.trie.starts_with("cartoons"))

    def test_empty_and_edge_cases(self):
        empty_trie = build_trie_from_patterns([])
        self.assertFalse(empty_trie.search("anything"))
        self.assertFalse(empty_trie.starts_with("any"))

        self.assertTrue(self.trie.starts_with(""))


if __name__ == "__main__":
    unittest.main()