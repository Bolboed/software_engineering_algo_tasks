import unittest
from tasks.recursion.binary_search.solution_binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_found_middle(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)

    def test_found_start(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 1), 0)

    def test_found_end(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 5), 4)

    def test_not_found_less(self):
        arr = [1, 3, 5]
        self.assertEqual(binary_search(arr, 0), -1)

    def test_not_found_greater(self):
        arr = [1, 3, 5]
        self.assertEqual(binary_search(arr, 6), -1)

    def test_not_found_middle(self):
        arr = [1, 3, 5]
        self.assertEqual(binary_search(arr, 2), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 10), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([42], 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([42], 1), -1)

    def test_duplicates_first_occurrence(self):
        arr = [1, 2, 2, 2, 4, 7]
        idx = binary_search(arr, 2)
        self.assertNotEqual(idx, -1)
        self.assertEqual(arr[idx], 2)

    def test_large_numbers(self):
        arr = [10**9, 10**9 + 5, 10**9 + 10]
        target = 10**9 + 5
        self.assertEqual(binary_search(arr, target), 1)


if __name__ == '__main__':
    unittest.main()