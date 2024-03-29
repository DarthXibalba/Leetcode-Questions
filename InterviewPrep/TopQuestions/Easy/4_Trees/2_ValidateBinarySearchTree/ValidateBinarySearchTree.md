# [Validate Binary Search Tree](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/)
Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.  
  
A **valid BST** is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key
- The right subtree of a node contains only nodes with keys **greater than** the node's key
- Both the left and right subtrees must also be binary search trees

#### Example 1:
<img src="images/example1.png" width="200" height="150">

```
Input: root = [2,1,3]
Output: true
```

#### Example 2:
<img src="images/example2.png" width="300" height="240">

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

#### Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`
