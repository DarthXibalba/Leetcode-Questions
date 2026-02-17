# Gotchas
A comprehensive list to learn from my mistakes.

| Index | Problem Name | Gotchas |
| --- | --- | --- |
| ABB | Reverse Integer | - Forgot to check out of bounds.<br>- Need to check if int will be greater than MAX // 10 in the second to last interation. |
| ACA | Delete Node In A Linked List | - SinglyLL constructor I designed leaves a dangling Node(val=None,next=None).<br>- Need to check nums parameter if we can assign head to element 0, and then add all subsequent nodes. Basically iterate with curNode.next not curNode.<br>- Only need to copy-left once, not on all subsequent values after the deleted node. |
| | | **ADVICE:** Draw picture, ask for claritiy, confirm picture is correct, solve.<br>If you are given the node to be deleted, you don't need to start traversing from the head. You are already at the damn thing. |
| ACB | - Remove Nth Node From End Of List | Use two ptrs to keep track of end & end + nth.<b>- Need to handle tail node properly with prevNode, not copy-left. |
| ACC | Reverse Linked List | Iterate with curNode instead of nextNode to remove head is None or head.next is None edge cases. |
| ACD | Merge Two Sorted Lists | Use sentinel & tail nodes to avoid switching lists (main & compare) |
| ACE | Palindrome Linked List | Use fast/slow pointers to find the midpoint of the list (slow).
| | | Use reverse_linked_list algo to reverse the 2nd half of the list so we can traverse from head & tail simultaneously. |
| | | Account for the odd-invariant by making sure the slow pointer starts reversing from the beginning of the second half, **NOT** the midpoint. |