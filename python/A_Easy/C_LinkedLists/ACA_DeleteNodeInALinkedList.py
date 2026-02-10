from __future__ import annotations

class Node:
    def __init__(self, val : int | str = None, next : Node | None = None):
        self.val = val
        self.next = next


class SLinkedList:
    def __init__(self, vals : list[int] | list[str]):
        if len(vals) == 0:
            self.head = None
        else:
            self.head = Node(vals[0])
            curNode = self.head
            for v in vals[1:]:
                curNode.next = Node(v)
                curNode = curNode.next


def delete_node_in_a_linked_list(n: Node):
    n.val = n.next.val
    n.next = n.next.next
