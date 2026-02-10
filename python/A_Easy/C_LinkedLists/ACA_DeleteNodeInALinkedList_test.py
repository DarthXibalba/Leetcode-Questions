import pytest

from python.A_Easy.C_LinkedLists.ACA_DeleteNodeInALinkedList import *

CASES = [
    (SLinkedList([1,2,3,4,5]), 1, SLinkedList([1,3,4,5])),
    (SLinkedList([1,2,3,4,5]), 2, SLinkedList([1,2,4,5])),
    (SLinkedList([10,20,30,40,50,60,70,80,90,100]), 1, SLinkedList([10,30,40,50,60,70,80,90,100])),
    (SLinkedList([10,20,30,40,50,60,70,80,90,100]), 2, SLinkedList([10,20,40,50,60,70,80,90,100])),
    (SLinkedList([10,20,30,40,50,60,70,80,90,100]), 5, SLinkedList([10,20,30,40,50,70,80,90,100])),
    (SLinkedList([10,20,30,40,50,60,70,80,90,100]), 2, SLinkedList([10,20,40,50,60,70,80,90,100])),
    (SLinkedList([10,20,30,40,50,60,70,80,90,100]), 8, SLinkedList([10,20,30,40,50,60,70,80,100]))
]

class HeadlessLinkedList:
    def __init__(self, ll : SLinkedList, idx : int):
        # Increment to node that will serve as the psuedo head
        curNode = ll.head
        for i in range(idx):
            curNode = curNode.next
        self.head = curNode

@pytest.mark.parametrize("case,idx,expected", CASES)
def test_delete_node_in_a_linked_list(case : SLinkedList, idx : int, expected : SLinkedList):
    # Get node
    curNode = case.head
    for i in range(idx):
        curNode = curNode.next
    delete_node_in_a_linked_list(curNode)
    # assert equal
    curNode = case.head
    expNode = expected.head
    while (curNode != None):
        print("curNode:", curNode.val)
        print("expNode:", expNode.val)
        assert curNode.val == expNode.val
        curNode = curNode.next
        expNode = expNode.next
    assert curNode == None
    assert expNode == None