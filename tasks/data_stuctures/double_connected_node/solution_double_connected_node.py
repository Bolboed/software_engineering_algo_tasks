from __future__ import annotations


class DoubleConnectedNode:
    def __init__(
        self,
        value,
        next_item: DoubleConnectedNode | None = None,
        prev_item: DoubleConnectedNode | None = None,
    ) -> None:
        self.value = value
        self.next = next_item
        self.prev = prev_item


def solution(node: DoubleConnectedNode | None) -> DoubleConnectedNode | None:
    current: DoubleConnectedNode | None = node
    new_head: DoubleConnectedNode | None = None

    while current is not None:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev
    return new_head