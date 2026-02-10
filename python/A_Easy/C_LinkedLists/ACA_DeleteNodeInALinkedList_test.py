import pytest

from python.A_Easy.C_LinkedLists.AC_LinkedLists import *
from python.A_Easy.C_LinkedLists.ACA_DeleteNodeInALinkedList import *

CASES = [
    (CreateLinkedList([1,2,3,4,5]), 1, CreateLinkedList([1,3,4,5])),
    (CreateLinkedList([1,2,3,4,5]), 2, CreateLinkedList([1,2,4,5])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 1, CreateLinkedList([10,30,40,50,60,70,80,90,100])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 2, CreateLinkedList([10,20,40,50,60,70,80,90,100])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 5, CreateLinkedList([10,20,30,40,50,70,80,90,100])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 2, CreateLinkedList([10,20,40,50,60,70,80,90,100])),
    (CreateLinkedList([10,20,30,40,50,60,70,80,90,100]), 8, CreateLinkedList([10,20,30,40,50,60,70,80,100]))
]

@pytest.mark.parametrize("n,idx,expected", CASES)
def test_delete_node_in_a_linked_list(n : ListNode, idx : int, expected : ListNode):
    origNode = n
    # Get node
    for _ in range(idx):
        n = n.next
    delete_node_in_a_linked_list(n)
    # assert equal
    curNode = origNode
    expNode = expected
    while (curNode != None):
        print("curNode:", curNode.val)
        print("expNode:", expNode.val)
        assert curNode.val == expNode.val
        curNode = curNode.next
        expNode = expNode.next
    assert curNode == None
    assert expNode == None