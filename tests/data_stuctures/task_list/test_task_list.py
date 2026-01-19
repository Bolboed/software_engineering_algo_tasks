
import io
import unittest
from unittest.mock import patch
from tasks.data_structures.tasks_list.solution_tasks_list import Node, solution


class TestPrintList(unittest.TestCase):
    def build_list(self, values: list) -> Node:
        head = None
        for value in reversed(values):
            head = Node(value, head)
        return head 

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_simple_list(self, mock_stdout: io.StringIO) -> None:
        head = self.build_list(["node0", "node1", "node2", "node3"])

        solution(head)

        output = mock_stdout.getvalue()
        expected_output = "node0\nnode1\nnode2\nnode3\n"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_single_element(self, mock_stdout: io.StringIO) -> None:
        head = self.build_list([42])

        solution(head)

        output = mock_stdout.getvalue()
        self.assertEqual(output, "42\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_long_list(self, mock_stdout: io.StringIO) -> None:
        values = list(range(100))
        head = self.build_list(values)

        solution(head)

        output = mock_stdout.getvalue().strip().split('\n')
        output_ints = [int(x) for x in output if x]
        self.assertEqual(output_ints, values)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_mixed_types(self, mock_stdout: io.StringIO) -> None:
        head = self.build_list([1, "string", 3.14, True])

        solution(head)

        output = mock_stdout.getvalue()
        expected_output = "1\nstring\n3.14\nTrue\n"
        self.assertEqual(output, expected_output)

    def test_empty_input_handling(self) -> None:
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            solution(None)  
            self.assertEqual(mock_stdout.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
