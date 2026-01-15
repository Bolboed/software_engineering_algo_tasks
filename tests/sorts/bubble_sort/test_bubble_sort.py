import io
import unittest
from unittest.mock import patch
from tasks.sorts.bubble_sort.solution_bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sorted_array(self, mock_stdout: io.StringIO) -> None:
        arr = [1, 2, 3]
        bubble_sort(arr)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "1 2 3")
        self.assertEqual(arr, [1, 2, 3])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_reverse_array(self, mock_stdout: io.StringIO) -> None:
        arr = [3, 2, 1]
        bubble_sort(arr)
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = ["2 1 3", "1 2 3"]
        self.assertEqual(output, expected_output)
        self.assertEqual(arr, [1, 2, 3])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_example_case_1(self, mock_stdout: io.StringIO) -> None:
        arr = [3, 7, 9, 4, 3, 1, 8, 5]
        bubble_sort(arr)
        output = mock_stdout.getvalue().strip().split('\n')

        expected_snapshots = [
            "3 7 4 3 1 8 5 9",
            "3 4 3 1 7 5 8 9",
            "3 3 1 4 5 7 8 9",
            "3 1 3 4 5 7 8 9",
            "1 3 3 4 5 7 8 9"
        ]
        self.assertEqual(output, expected_snapshots)
        self.assertEqual(arr, sorted([3, 7, 9, 4, 3, 1, 8, 5]))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_numbers(self, mock_stdout: io.StringIO) -> None:
        arr = [7, -2, -1]
        bubble_sort(arr)
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output, ["-2 -1 7"])
        self.assertEqual(arr, [-2, -1, 7])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_element_does_not_crash(self, mock_stdout: io.StringIO) -> None:
        arr = [42]
        bubble_sort(arr)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "42")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_array(self, mock_stdout: io.StringIO) -> None:
        arr = []
        bubble_sort(arr)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()