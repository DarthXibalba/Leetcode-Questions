# [Linked List Cycle](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/)
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.  
  
There is a cycle in a linked list if there is some node in the list can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a paramter**.  
  
Return `true` *if there is a cycle in a linked list*. Otherwise, return `false`.

#### Example 1:
<img src="images/example1.png" width="400" height="120">

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

#### Example 2:
<img src="images/example2.png" width="200" height="120">

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

#### Example 3:
<img src="images/example3.png" width="70" height="70">

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

#### Constraints:
- The number of nodes in the list is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked list

#### Follow up:
Can you solve it using `O(1)` memory?
