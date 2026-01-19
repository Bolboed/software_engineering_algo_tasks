import unittest
from tasks.data_structures.update_list.solution_update_list import Node, solution


def build_list(values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def to_list(head):
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next_item
    return result


def test_delete_middle():
    node3 = Node("node3")
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


def test_delete_head():
    head = build_list([1, 2, 3])
    new_head = solution(head, 0)
    assert to_list(new_head) == [2, 3]


def test_delete_last():
    head = build_list(["a", "b", "c"])
    new_head = solution(head, 2)
    assert to_list(new_head) == ["a", "b"]


def test_single_element():
    head = build_list([42])
    new_head = solution(head, 0)
    assert new_head is None


def test_long_list_tail():
    values = list(range(5000))
    head = build_list(values)
    new_head = solution(head, 4999)
    assert new_head is head
    assert to_list(new_head) == values[:-1]


if __name__ == "__main__":
    test_delete_middle()
    test_delete_head()
    test_delete_last()
    test_single_element()
    test_long_list_tail()
    print("All tests passed")