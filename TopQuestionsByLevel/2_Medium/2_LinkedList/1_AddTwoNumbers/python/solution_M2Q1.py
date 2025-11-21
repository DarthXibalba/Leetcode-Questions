class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToStr(node):
    output = f"{node.val}->"
    node = node.next
    while node:
        output += f"{node.val}->"
        node = node.next
    return output

def listToLinkedList(vals):
    head = ListNode(vals[0])
    node = head
    i = 1
    while (i < len(vals)):
        node.next = ListNode(vals[i])
        node = node.next
        i += 1
    return head

# Both input lists are reverse
# Therefore add the two lists in the order given, append a [1] if there is a carry
# Lastly reverse the direction linked list and return the lastNode (which will now be the first node in the new direction)
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Get initial sum node & carryover
    nodalSum = l1.val + l2.val
    result = ListNode(nodalSum % 10)
    head = result
    carryover = nodalSum // 10
    # Increment lists
    l1 = l1.next
    l2 = l2.next
    # Begin iterating over lists
    while l1 and l2:
        nodalSum = l1.val + l2.val + carryover
        result.next = ListNode(nodalSum % 10)
        carryover = nodalSum // 10
        # Increment lists
        l1 = l1.next
        l2 = l2.next
        result = result.next
    while l1:
        nodalSum = l1.val + carryover
        result.next = ListNode(nodalSum % 10)
        carryover = nodalSum // 10
        # Increment
        l1 = l1.next
        result = result.next
    while l2:
        nodalSum = l2.val + carryover
        result.next = ListNode(nodalSum % 10)
        carryover = nodalSum // 10
        # Increment
        l2 = l2.next
        result = result.next
    if carryover != 0:
        result.next = ListNode(carryover)
    return head



if __name__ == '__main__':
    l1 = []
    l1.append([2,4,3])
    l1.append([0])
    l1.append([9,9,9,9,9,9,9])
    
    l2 = []
    l2.append([5,6,4])
    l2.append([0])
    l2.append([9,9,9,9])

    for i in range(len(l1)):
        ll1 = listToLinkedList(l1[i])
        ll2 = listToLinkedList(l2[i])
        print(f"l1 = {listToStr(ll1)}")
        print(f"l2 = {listToStr(ll2)}")
        result = addTwoNumbers(ll1, ll2)
        print(f"rs = {listToStr(result)}\n")
