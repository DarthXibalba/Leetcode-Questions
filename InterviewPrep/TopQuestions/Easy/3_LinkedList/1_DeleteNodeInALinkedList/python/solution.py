from collections import deque

class LinkedList():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(values):
    i = 0
    head = LinkedList(values[i])
    curNode = head
    while i + 1 < len(values):
        i += 1
        nextNode = LinkedList(values[i])
        curNode.next = nextNode
        curNode = nextNode
    return head

def printLinkedList(head):
    output = "->"
    node = head
    while node:
        output += f"{node.val}-->"
        node = node.next
    print(output)

# Since we don't have access to head, we cannot set prevNode.next = curNode.next
# Therefore we must copy all values after node and delete the last node
def deleteNode(head):
    """
    :type node: ListNode
    :rtype: void - Do not return anything, modify in-place instead
    """
    nodeDeque = deque()
    nodeDeque.append(head)
    while head:
        if head.next:
            head.val = head.next.val
            if len(nodeDeque) > 1:
                nodeDeque.popleft()
            nodeDeque.append(head.next)
        head = head.next
    # Snip off the tail node
    newTail = nodeDeque.popleft()
    newTail.next = None





if __name__ == '__main__':
    head1 = createLinkedList([4,5,1,9])
    node1 = head1.next
    head2 = createLinkedList([4,5,1,9])
    node2 = head2.next.next

    print(f"Linked List #1")
    printLinkedList(head1)
    print(f"Deleting node {node1.val}")
    deleteNode(node1)
    print("     |\n     V")
    printLinkedList(head1)
    print("")

    print(f"Linked List #2")
    printLinkedList(head2)
    print(f"Deleting node {node1.val}")
    deleteNode(node2)
    print("     |\n     V")
    printLinkedList(head2)
    print("")
