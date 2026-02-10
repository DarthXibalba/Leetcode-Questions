from python.A_Easy.C_LinkedLists.AC_LinkedLists import *

def remove_nth_node_from_the_end(head : ListNode, n : int) -> ListNode:
    curNode = head
    for _ in range(n-1):
        curNode = curNode.next
    # Create 2nd ptr to keep track of nth element
    nthNode = head
    # Iterate to the end
    while curNode.next != None:
        curNode = curNode.next
        nthNode = nthNode.next
    # Remove Node with copy-left method
    nthNode.val = nthNode.next.val
    nthNode.next = nthNode.next.next
    return head
