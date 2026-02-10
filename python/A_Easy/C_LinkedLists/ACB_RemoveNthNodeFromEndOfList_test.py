import pytest

from python.A_Easy.C_LinkedLists.ACB_RemoveNthNodeFromEndOfList import *

CASES = [
    (CreateLinkedList([1,2,3,4,5]), 4, CreateLinkedList([1,3,4,5])),
    (CreateLinkedList([1,2,3,4,5]), 3, CreateLinkedList([1,2,4,5])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 9, CreateLinkedList([10,30,40,50,60,70,80,90,100])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 8, CreateLinkedList([10,20,40,50,60,70,80,90,100])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 5, CreateLinkedList([10,20,30,40,50,70,80,90,100]))
]

@pytest.mark.parametrize("head,n,expected", CASES)
def test_remove_nth_node_from_end(head: ListNode, n: int, expected: ListNode):
    print()
    print("n =", n)
    PrettyPrintLinkedList(head)