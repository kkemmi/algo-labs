import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab7 import max_flow

class TestFlowerDelivery(unittest.TestCase):
    def test_flow(self):
        farms, shops = ["F1"], ["S1"]
        roads = [("F1", "X1", 10), ("X1", "S1", 5)]
        self.assertEqual(max_flow(farms, shops, roads), 5)

if __name__ == "__main__":
    unittest.main()
