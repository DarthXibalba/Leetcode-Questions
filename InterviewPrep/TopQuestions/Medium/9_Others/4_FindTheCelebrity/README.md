# [Find the Celebrity](https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/825/)
Suppose you are at a party with `n` people labeled from `0` to `n - 1` and among them, there may exist one celebrity. The definition of a celebrity is that all the other `n - 1` people know the celebrity, but the celebrity does not know any of them.  
  
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify that there is not one) by asking as few questions as possible (in the asymptotic sense).  
  
You are given a helper function `bool knows(a, b)` that tells you whether A knows B. Implement a function `int findCelebrity(n)`. There will be exactly one celebrity if they are at the party.  
  
Return *the celebrity's label if there is a celebrity at the party*. If there is no celebrity, return `-1`.

#### Example 1:
<img src="images/example1.jpg" width="200" height="150">

```
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
```

#### Example 2:
<img src="images/example2.jpg" width="200" height="150">

```
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
```

#### Constraints:
- `n == graph.length == graph[i].length`
- `2 <= n <= 100`
- `graph[i][j]` is `0` or `1`
- `graph[i][i] == 1`

#### Follow up:
If the maximum number of allowed calls to the API `knows` is `3 * n`, could you find a solution without exceeding the maximum number of calls?

##### Hint #1
<img src="images/hint1.png" width="450" height="300">

The best hint for this problem can be provided by the following figure:

##### Hint #2
Well, if you understood the gist of the above idea, you can extend it to find a candidate that can possibly be a celebrity. Why do we say a "candidate"? That is for you to think. This is clearly a greedy approach to find the answer. However, there is some information that would still remain to be verified without which we can't obtain an answer with certainty. To get that stake in the ground, we would need some more calls to the knows API.
