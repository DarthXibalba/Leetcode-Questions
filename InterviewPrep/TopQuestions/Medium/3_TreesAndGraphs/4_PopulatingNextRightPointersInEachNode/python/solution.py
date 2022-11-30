from collections import deque

class Node():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Approach 1: BFS
# Time Complexity: O(N)
# Space Complexity: O(N/2) = O(N)
def connect1(root):
    """
    :type root: Node
    :rtype: Node
    """
    if root == None:
        return None
    q = deque()
    q.append(root)
    while q:
        qL = len(q)
        i = 0
        levelList = []
        while i < qL:
            i += 1
            node = q.popleft()
            levelList.append(node)
            # If the children are not None, add them to queue
            if node.left:
                q.append(node.left)
                q.append(node.right)
        # Traverse level to connect node to it's next
        j = 0
        levelSize = len(levelList)
        while (j < levelSize - 1):  # -1 because we don't want to edit the rightmost node
            levelList[j].next = levelList[j+1]
            j += 1

# Approach 2: BFS Traversal where the children are connected
def connect(root):
    """
    :type root: Node
    :rtype: Node
    """
    if root:
        # BFS
        q = deque()
        q.append(root)
        while q:
            qL = len(q)
            i = 0
            while i < qL:
                i += 1
                node = q.popleft()
                # If node has valid children, assign their respective .next attribute
                if node.left:
                    node.left.next = node.right
                    q.append(node.left)
                if node.right:
                    if node.next:
                        node.right.next = node.next.left
                    q.append(node.right)
    return root


def printTreeByLevel(root):
    if root == None:
        return
    q = deque()
    q.append(root)
    while q:
        qL = len(q)
        i = 0
        level = []
        while (i < qL):
            i += 1
            node = q.popleft()
            nodeStr = f"{node.val}"
            if node.next:
                nodeStr += f"->{node.next.val}"
            level.append(nodeStr)
            if node.left != None:
                q.append(node.left)
                q.append(node.right)
        print(level)
    print()



if __name__ == '__main__':
    bst1 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    bst2 = None
    bsts = [bst1, bst2]
    for tree in bsts:
        printTreeByLevel(tree)
        connect(tree)
        printTreeByLevel(tree)
