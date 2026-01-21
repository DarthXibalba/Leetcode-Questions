# [Serialize and Deserialize Binary Tree](https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/812/)
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be restored in a file or memroy buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.  
  
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.  
  
**Clarification:** The input/output format is the same as [how LeetCode serializes a binary tree](https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

#### Example 1:
<img src="images/020702_example1.jpg" width="250" height="200">

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

#### Example 2:
```
Input: root = []
Output: []
```

#### Constraints:
- The number of nodes in the tree is in the range `[0, 10^4]`
- `-1000 <= Node.val <= 1000`
