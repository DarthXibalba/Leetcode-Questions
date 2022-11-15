from collections import deque

class ListNode():
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next


def createLinkedList(values):
    # Create the last node first
    i = len(values)-1
    nextNode = ListNode(values[i], None)
    while i > 0:
        i -= 1
        prevNode = ListNode(values[i], nextNode)
        nextNode = prevNode
    return nextNode

def printLinkedList(root):
    node = root
    output = "->"
    while node:
        output += f"{node.val}-->"
        node = node.next
    print(output)

# Approach 1: Using a list to map out the entire linked list
def removeNthFromEnd1(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # Traverse the linked list while creating a list of all nodes
    allNodes = []
    curNode = head
    while curNode:
        allNodes.append(curNode)
        curNode = curNode.next
    # Delete the ith from the last node
    idx = len(allNodes) - n - 1
    # If we're deleting the first node (tail) and it is the only node
    if len(allNodes) == 1:
        return None
    # If we're deleting the head node
    elif idx == -1:
        head = head.next
    # If we're deleting the last node (tail)
    elif n == 1:
        allNodes[idx].next = None
    else:
        allNodes[idx].next = allNodes[idx+2]
    return head

# Approach 2: Using a Queue to keep track of the last n nodes
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int    
    :rtype: ListNode
    """
    lastNodes = deque()
    # Begin traversing the linked list
    curNode = head
    while curNode:
        if len(lastNodes) > n:
            lastNodes.popleft()
        lastNodes.append(curNode)
        curNode = curNode.next
    # lastNodes[0] should contain the node that comes just before the node to be deleted, unless we are deleting the head
    # if len(lastNodes) == n, then we are deleting the head
    if len(lastNodes) == n:
        # If we are deleting the head and its the only node, return None
        if len(lastNodes) == 1:
            return None
        else:
            return lastNodes.popleft().next
    # If we are not deleting the head, then set prevNode.next = (nextNode || None)
    prevNode = lastNodes.popleft()
    # Skip over node to be deleted
    lastNodes.popleft()
    # If there are no more nodes to pop, then set next = None because there are no nodes that proceed after nodeToBeDeleted
    if len(lastNodes):
        prevNode.next = lastNodes.popleft()
    else:
        prevNode.next = None
    return head



if __name__ == '__main__':
    heads = [
        createLinkedList([1,2,3,4,5]),
        createLinkedList([1]),
        createLinkedList([1,2]),
        createLinkedList([1,2])
    ]
    N = [2, 1, 1, 2]
    
    for i in range(len(heads)):
        print(f"Linked List {i+1}")
        printLinkedList(heads[i])
        print(f"n = {N[i]}")
        printLinkedList(removeNthFromEnd(heads[i], N[i]))
        print("")
