# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#class Solution:
def maxPathSum(rootNode):
    leftGain = 0
    rightGain = 0

    if rootNode.left != None:
        gain = maxPathSum(rootNode.left)
        if leftGain < gain:
            leftGain = gain
    if rootNode.right != None:
        gain = maxPathSum(rootNode.right)
        if rightGain < gain:
            rightGain = gain
    
    return rootNode.val + leftGain + rightGain


t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
maxGain = maxPathSum(t)