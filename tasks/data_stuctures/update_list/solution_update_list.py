class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node: Node, idx: int) -> Node:
    if idx == 0:
        return node.next_item

    current = node
    current_index = 0

    while current is not None and current_index < idx - 1:
        current = current.next_item
        current_index += 1

    if current is not None and current.next_item is not None:
        current.next_item = current.next_item.next_item

    return node