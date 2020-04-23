import unittest
from matrix_search import array_search

class Test_BinarySearch(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(array_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(array_search([1], 1), 0)
        self.assertRaises(ValueError, array_search, [], 1)
if __name__ == "__main__":
    unittest.main()