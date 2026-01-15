import unittest
from tasks.data_structures.double_connected_node.solution_double_connected_node import (
    DoubleConnectedNode,
    solution
)


def build_doubly_linked_list(values: list) -> DoubleConnectedNode:
    if not values:
        raise ValueError("Не опустошить")

    head = DoubleConnectedNode(values[0])
    current = head

    for val in values[1:]:
        new_node = DoubleConnectedNode(val, prev_item=current)
        current.next = new_node
        current = new_node

    return head


def to_list_forward(head: DoubleConnectedNode) -> list:
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


def to_list_backward(head: DoubleConnectedNode) -> list:
    current = head
    if current is None:
        return []

    while current.next is not None:
        current = current.next

    result = []
    while current is not None:
        result.append(current.value)
        current = current.prev
    return result


def test_reverse_simple():
    head = build_doubly_linked_list([0, 1, 2, 3])

    new_head = solution(head)

    assert to_list_forward(new_head) == [3, 2, 1, 0]
    assert to_list_backward(new_head) == [0, 1, 2, 3]


def test_reverse_single_element():
    head = build_doubly_linked_list([42])
    new_head = solution(head)

    assert new_head is head
    assert new_head.next is None
    assert new_head.prev is None
    assert to_list_forward(new_head) == [42]


def test_reverse_two_elements():
    head = build_doubly_linked_list(["a", "b"])
    new_head = solution(head)

    assert to_list_forward(new_head) == ["b", "a"]
    assert new_head.value == "b"
    assert new_head.next.value == "a"
    assert new_head.prev is None
    assert new_head.next.next is None
    assert new_head.next.prev is new_head


def test_reverse_long_list():
    values = list(range(100))
    head = build_doubly_linked_list(values)
    new_head = solution(head)

    assert to_list_forward(new_head) == list(reversed(values))
    assert to_list_backward(new_head) == values


def test_internal_links_integrity():
    head = build_doubly_linked_list(["node0", "node1", "node2"])
    original_node0 = head
    original_node1 = head.next
    original_node2 = head.next.next

    new_head = solution(head)

    assert new_head is original_node2
    assert new_head.next is original_node1
    assert new_head.next.next is original_node0

    assert original_node0.prev is original_node1
    assert original_node1.prev is original_node2


if __name__ == "__main__":
    test_reverse_simple()
    test_reverse_single_element()
    test_reverse_two_elements()
    test_reverse_long_list()
    test_internal_links_integrity()
    print("Все тесты пройдены")