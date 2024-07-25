# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def __init__(self):
        self.prev = None

    # Use DFS InOrder Traversal to traverse the tree in ascending order
    # This will allow us to check that each subsequent value is greater than the previous
    def isValidBST(self, node):
        if node == None:
            return True
        # Check that left subtree is valid, return False if it is not
        if not self.isValidBST(node.left):
            return False
        # Now check this node to see that it is greater than prev
        # Also assign self.prev if it has not been assigned yet and is set to None
        if (self.prev == None) or (node.val > self.prev):
            self.prev = node.val
        else:
            return False
        # Check that the right subtree is valid
        return self.isValidBST(node.right)


if __name__ == '__main__':
    tree1 = TreeNode(2, TreeNode(1), TreeNode(3))

    tree2 = TreeNode(5)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(4, TreeNode(3), TreeNode(6))

    tree3 = TreeNode(5)
    tree3.left = TreeNode(4)
    tree3.right = TreeNode(6, TreeNode(3), TreeNode(7))

    trees = [tree1, tree2, tree3]

    for i in range(len(trees)):
        s = Solution()
        print(f"Tree{i+1}")
        print(s.isValidBST(trees[i]))
        print("")
