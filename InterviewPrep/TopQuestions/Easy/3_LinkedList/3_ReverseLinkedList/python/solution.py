class LinkedList():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(values):
    if len(values):
        i = 0
        head = LinkedList(values[i])
        curNode = head
        while i + 1 < len(values):
            i += 1
            nextNode = LinkedList(values[i])
            curNode.next = nextNode
            curNode = nextNode
        return head
    else:
        return None

def printLinkedList(head):
    output = "->"
    while head:
        output += f"{head.val}-->"
        head = head.next
    print(output)

# Approach 1: Create a new LL as we're traversing the original LL
# Time Complexity: O(N)
# Space Complexity: O(N)
def reverseListIter1(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return None
    node2 = LinkedList(head.val, None)
    node1 = head.next 
    while node1:
        newNode = LinkedList(node1.val, node2)
        node2 = newNode
        node1 = node1.next
    return node2

# Approach 2: Reverse the direction of the linked list
# Time Complexity: O(N)
# Space Complexity: O(1)
def reverseList(node):
    if node == None:
        return None
    nextNode = node.next
    node.next = None
    while nextNode:
        prevNode = node
        node = nextNode
        nextNode = nextNode.next
        node.next = prevNode
    return node



if __name__ == '__main__':
    heads = [
        [1,2,3,4,5],
        [1,2],
        []
    ]
    for i in range(len(heads)):
        print(f"Linked List #{i+1}")
        head = createLinkedList(heads[i])
        printLinkedList(head)
        print(f"     |\n     V")
        printLinkedList(reverseList(head))
        print("")
