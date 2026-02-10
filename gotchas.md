# Gotchas
A comprehensive list to learn from my mistakes.

| Index | Problem Name | Gotchas |
| --- | --- | --- |
| ABB | Reverse Integer | - Forgot to check out of bounds.<br>- Need to check if int will be greater than MAX // 10 in the second to last interation. |
| ACA | Delete Node In A Linked List | - SinglyLL constructor I designed leaves a dangling Node(val=None,next=None).<br>- Need to check nums parameter if we can assign head to element 0, and then add all subsequent nodes. Basically iterate with curNode.next not curNode.<br>- Only need to copy-left once, not on all subsequent values after the deleted node. |
| | | **ADVICE:** Draw picture, ask for claritiy, confirm picture is correct, solve.<br>If you are given the node to be deleted, you don't need to start traversing from the head. You are already at the damn thing. |