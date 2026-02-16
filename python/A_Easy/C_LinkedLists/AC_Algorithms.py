from python.A_Easy.C_LinkedLists.AC_LinkedLists import *

def fast_slow_pointer_traversal(head: ListNode) -> (ListNode, ListNode):
    fast = head
    slow = head
    # Handle both edge cases of tail or tail.next within while condition
    while fast != None and fast.next != None:
        fast = fast.next
        fast = fast.next
        slow = slow.next

    midpt = slow
    tail = fast
    return midpt, tail
