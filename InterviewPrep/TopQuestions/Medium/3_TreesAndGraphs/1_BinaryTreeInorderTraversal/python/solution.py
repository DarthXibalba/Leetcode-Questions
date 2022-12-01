from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreeByLevel(root):
    output = ""
    if root != None:
        q = deque()
        q.append(root)
        while q:
            qL = len(q)
            i = 0
            while (i < qL):
                i += 1
                node = q.popleft()
                if node:
                    output += f"{node.val},"
                    q.append(node.left)
                    q.append(node.right)
                else:
                    output += "null,"
            output += "\n"
    print(output)


# Approach #1: Recursive
def inorderTraversal1(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    vals = []
    inorderTraversalRecursive(root, vals)
    return vals

def inorderTraversalRecursive(node, vals):
    if node:
        # Check left child
        inorderTraversalRecursive(node.left, vals)
        # Get node value
        vals.append(node.val)
        # Check right child
        inorderTraversalRecursive(node.right, vals)

# Approach #2:
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    vals = []
    q = deque()
    curNode = root
    while (len(q) > 0) or (curNode != None):
        # If curNode is valid, then continue DFS downwards
        while (curNode != None):
            # Populate stack with valid nodes
            q.append(curNode)
            curNode = curNode.left
        # Parse stack
        curNode = q.pop()
        vals.append(curNode.val)
        # Search right child
        curNode = curNode.right
    return vals



if __name__ == '__main__':
    trees = []
    trees.append(Node(1, None, Node(2, Node(3))))
    trees.append(None)
    trees.append(Node(1))

    for i in range(len(trees)):
        print(f"Tree #{i + 1}")
        printTreeByLevel(trees[i])
        inorderVals = inorderTraversal(trees[i])
        print(inorderVals)
        print()
