# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = head
    slow = head
    while fast:
        # If fast ends in the next node or the one after that, then it has a valid tail and we can break out of this loop and return False
        if (fast.next == None) or (fast.next.next == None):
            break
        else:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
    return False

def printLinkedList(head):
    print("->")
    while head:
        print(f"{head.val}-->")
        head = head.next


if __name__ == '__main__':
    # Can't get linkedlist to reference itself
    list1 = ListNode(3)
    node = list1
    node.next = ListNode(2)
    node = node.next
    pos = node
    node.next = ListNode(0)
    node = node.next
    node.next = ListNode(-4, pos)

    list2 = ListNode(1)
    node = list2
    list2.next = ListNode(2, node)

    list3 = ListNode(1)

    lists = [list1, list2, list3]

    for i in range(len(lists)):
        printLinkedList(lists[i])
        print()
        print(f"Linked List {i+1}: {hasCycle(lists[i])}\n")
