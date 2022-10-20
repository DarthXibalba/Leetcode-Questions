class SListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class DListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = next
