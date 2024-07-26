from collections import deque

class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach #1: BFS with alternating order
def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    # Perform BFS (separate lists for each level)
    vals = []
    q = deque()
    q.append(root)
    while q:
        qL = len(q)
        i = 0
        level = []
        while i < qL:
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            i += 1
        if level != []:
            vals.append(level)
    # Swap odd-indexed levels
    i = 1
    while i < len(vals):
        # Perform swap
        j = 0
        lvlLen = len(vals[i])
        while j < lvlLen // 2:
            k = lvlLen - 1 - j
            vals[i][j], vals[i][k] = vals[i][k], vals[i][j]
            j += 1
        i += 2
    return vals



if __name__ == '__main__':
    trees = []
    trees.append(Node(3, Node(9), Node(20, Node(15), Node(7))))
    trees.append(Node(1))
    trees.append([])

    for i in range(len(trees)):
        print(f"Tree #{i+1}")
        print(zigzagLevelOrder(trees[i]))
        print()