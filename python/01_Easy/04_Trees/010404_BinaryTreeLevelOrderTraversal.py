from collections import deque

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Perform BFS
def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if root:
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            levels.append(level)
    return levels



if __name__ == "__main__":
    trees = []
    trees.append(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    trees.append(TreeNode(1))
    trees.append(None)

    for i in range(len(trees)):
        print(f"Tree{i+1}")
        print(levelOrder(trees[i]))
        print("")
