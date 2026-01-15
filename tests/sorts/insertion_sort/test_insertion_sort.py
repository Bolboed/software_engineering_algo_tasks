import unittest
from tasks.sorts.insertion_sort.solution_insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort([3]), [3])

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort(arr), [1, 2, 3, 4, 5])

    def test_random_unsorted(self):
        arr = [9, 5, 1, 4, 3]
        expected = [1, 3, 4, 5, 9]
        self.assertEqual(insertion_sort(arr), expected)

    def test_duplicates_and_negatives(self):
        arr = [2, -1, 2, -1, 0]
        expected = [-1, -1, 0, 2, 2]
        self.assertEqual(insertion_sort(arr), expected)

    def test_immutability(self):
        original = [3, 1, 2]
        result = insertion_sort(original)
        self.assertEqual(result, [1, 2, 3])
        self.assertEqual(original, [3, 1, 2],
                         "Исходный список не должен изменяться")


if __name__ == "__main__":
    unittest.main()