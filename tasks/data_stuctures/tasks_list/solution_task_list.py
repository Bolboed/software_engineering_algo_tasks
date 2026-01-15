from __future__ import annotations


class Node:
    def __init__(self, value, next_item: Node | None = None) -> None:
        self.value = value
        self.next_item = next_item


def solution(node: Node | None) -> None:
    current = node
    while current is not None:
        print(current.value)
        current = current.next_item