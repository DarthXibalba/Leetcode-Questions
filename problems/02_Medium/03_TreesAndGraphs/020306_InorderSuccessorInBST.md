# [Inorder Successor in BST](https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/791/)
Given the `root` of a binary search tree and a node `p` in it, return *the inorder traversal of that node in the BST*. If the given node has no inorder successor in the tree, return `null`.  
  
The successor of a node `p` is the node with the smallest key greater than `p.val`.  


#### Example 1
<img src="images/020306_example1.png" width="100" height="100">

```
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's inorder successor node is 2. Note that both p and the return value is of TreeNode type.
```

#### Example 2
<img src="images/020306_example2.png" width="200" height="200">

```
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no inorder successor of the current node, so the answer is null.
```

#### Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- All Nodes will have unique values.
