import Node

class SLinkedList:
    def __init__(self):
        self.head = None
    def __init__(self, head: Node.SListNode):
        self.head = head
    
    def Read(self, idx):
        curNode = self.head
        curIdx = 0
        while curIdx < idx:
            if (curNode == None):
                return None
            curNode = curNode.next
            curIdx += 1
        return curNode.val

    # Search and return idx if it exists else return None
    def IndexOf(self, value):
        curNode = self.head
        curIdx = 0
        while curNode != None:
            if curNode.val == value:
                return curIdx
            curNode = curNode.next
            curIdx += 1
        return None

    def InsertAtIndex(self, index, value):
        # Create a new node with the provided value
        newNode = Node.SListNode(value)
        # If we are inserting at the beginning of the list
        if index == 0:
            newNode.next = self.head
            self.head = newNode.next
        # If we are inserting anywhere other than the beginning
        curNode = self.head
        curIdx = 0
        # First we access the node immediately before where the new node will go
        while (curIdx < index - 1) and (curNode != None):
            curNode = curNode.nextNode
            curIdx += 1
        # Have the new node link to the next node
        newNode.next = curNode.next
        # Modify the link of the previous node to point to our new node
        curNode.next = newNode
    
    def DeleteAtIndex(self, index):
        # If we are deleting the first node
        if index == 0:
            self.head = self.head.next
        else:
            curNode = self.head
            curIdx = 0
            # First, we find the node immediately before the one we want to delete and call it curNode
            while (curIdx < index - 1):
                curNode = curNode.next
                curIdx += 1
            # We find the node that comes after the one we're deleting
            nodeAfterDeletedNode = curNode.next.next
            # We change the link of the curNode to point to the nodeAfterDeletedNode, leaving the node we want to delete out of the list
            curNode.next = nodeAfterDeletedNode


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __init__(self, firstNode: Node.DListNode):
        self.head = firstNode
        self.tail = firstNode

    def InsertAtEnd(self, value):
        newNode = Node.DListNode()
        # If there are no elements yet
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        # If the linked list already has at least one node
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def RemoveFromFront(self):
        removeNode =  self.head
        self.head = self.head.next
