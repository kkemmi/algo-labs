import unittest
from lab6 import *

class TestGasPipeline(unittest.TestCase):
    def test_all_reachable(self):
        storages = ["Сховище_1"]
        cities = ["Львів", "Стрий"]
        pipelines = [["Сховище_1", "Львів"], ["Львів", "Стрий"]]
        self.assertEqual(find_unreachable_cities(storages, cities, pipelines), [])

    def test_unreachable_city(self):
        storages = ["Сховище_1"]
        cities = ["Львів", "Стрий", "Долина"]
        pipelines = [["Сховище_1", "Львів"], ["Львів", "Стрий"]]
        expected = [["Сховище_1", ["Долина"]]]
        self.assertEqual(find_unreachable_cities(storages, cities, pipelines), expected)

    def test_multiple_storages(self):
        storages = ["Сховище_1", "Сховище_2"]
        cities = ["Львів", "Стрий"]
        pipelines = [["Сховище_1", "Львів"], ["Львів", "Стрий"]]
        expected = [["Сховище_2", ["Львів", "Стрий"]]]
        self.assertEqual(find_unreachable_cities(storages, cities, pipelines), expected)


if __name__ == "__main__":
    unittest.main()