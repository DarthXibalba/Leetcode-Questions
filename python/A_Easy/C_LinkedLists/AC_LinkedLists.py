from __future__ import annotations

class ListNode:
    def __init__(self, val: int | str, next: ListNode | None = None):
        self.val = val
        self.next = next

def CreateLinkedList(vals: list[int] | list[str]) -> ListNode | None:
    if len(vals) == 0:
        return None
    else:
        head = ListNode(vals[0])
        curNode = head
        for v in vals[1:]:
            curNode.next = ListNode(v)
            curNode = curNode.next
        return head
