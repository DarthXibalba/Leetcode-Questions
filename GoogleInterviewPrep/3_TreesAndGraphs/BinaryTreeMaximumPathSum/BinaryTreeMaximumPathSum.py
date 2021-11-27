# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, rootNode):
        self.maxSum = rootNode.val
        nodalGain = self.nodalMaxPathSum(rootNode)
        if self.maxSum < nodalGain:
            self.maxSum = nodalGain
        return self.maxSum

    def nodalMaxPathSum(self, rootNode):
        if rootNode == None:
            return 0
        
        leftGain = max(self.nodalMaxPathSum(rootNode.left), 0)
        rightGain = max(self.nodalMaxPathSum(rootNode.right), 0)
        subtreeGain = rootNode.val + leftGain + rightGain
        if self.maxSum < subtreeGain:
            self.maxSum = subtreeGain
        return rootNode.val + max(leftGain, rightGain)


t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
t3 = TreeNode(-3)
s = Solution()
maxGain = s.maxPathSum(t2)
