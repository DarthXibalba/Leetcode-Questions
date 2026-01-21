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
            curNode.next = LinkedList(values[i])
            curNode = curNode.next
        return head
    else:
        return None

def printLinkedList(head):
    output = "->"
    while head:
        output += f"{head.val}-->"
        head = head.next
    print(output)

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # If one or both of the lists are empty
    if (list1 == None) and (list2 == None):
        return None
    elif list1 == None:
        return list2
    elif list2 == None:
        return list1
    # If both lists are populated
    head = None
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    curNode = head
    while list1 and list2:
        if list1.val < list2.val:
            curNode.next = list1
            curNode = curNode.next
            list1 = list1.next
        else:
            curNode.next = list2
            curNode = curNode.next
            list2 = list2.next
    # Make sure the tail connects to the other list
    if list1:
        curNode.next = list1
    else:
        curNode.next = list2
    return head





if __name__ == '__main__':
    list1 = [
        [1,2,4],
        [],
        []
    ]
    list2 = [
        [1,3,4],
        [],
        [0]
    ]
    for i in range(len(list1)):
        head1 = createLinkedList(list1[i])
        head2 = createLinkedList(list2[i])
        print("List1:")
        printLinkedList(head1)
        print("List2:")
        printLinkedList(head2)
        print("Resultant List:")
        printLinkedList(mergeTwoLists(head1, head2))
        print()