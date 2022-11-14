from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetricIter(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    q = deque()
    q.append(root)
    while q:
        qLen = len(q)
        level = deque()
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                level.append(None)
        # Process level stack for all levels past the 1st
        while len(level) > 1:
            if level.popleft() != level.pop():
                return False
    return True



if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    tree1.right = TreeNode(2, TreeNode(4), TreeNode(3))

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2, None, TreeNode(3))
    tree2.right = TreeNode(2, None, TreeNode(3))

    trees = [tree1, tree2]
    answers = [True, False]

    for i in range(len(trees)):
        print(f"Tree{i}")
        ans = isSymmetricIter(trees[i])
        print(f"isSymmetric = {ans}")
        assert answers[i] == ans, f"expected = {answers[i]} | result = {ans}"
