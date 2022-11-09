# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # Base cases
    if root == None:
        return 0
    if (root.left == None) and (root.right == None):
        return 1

    leftDepth = 0
    rightDepth = 0
    if root.left != None:
        leftDepth = maxDepth(root.left) + 1

    if root.right != None:
        rightDepth = maxDepth(root.right) + 1

    # Determine which depth is deeper and return that
    return max(leftDepth, rightDepth)



if __name__ == '__main__':
    tree1 = TreeNode(3)
    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20, TreeNode(15), TreeNode(7))

    tree2 = TreeNode(1, None, TreeNode(2))

    print("Tree1")
    print(maxDepth(tree1))
    print("Tree2")
    print(maxDepth(tree2))
