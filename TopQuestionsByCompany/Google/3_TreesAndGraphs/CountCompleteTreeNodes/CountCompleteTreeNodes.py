# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    nodes = 0

    def countNodes(self, rootNode):
        if (rootNode == None):
            return self.nodes

        else:
            self.nodes = self.nodes + 1
            self.countNodes(rootNode.left)
            self.countNodes(rootNode.right)
            return self.nodes

t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
t3 = None
t4 = TreeNode(1)

s = Solution()
nodes = s.countNodes(t1)