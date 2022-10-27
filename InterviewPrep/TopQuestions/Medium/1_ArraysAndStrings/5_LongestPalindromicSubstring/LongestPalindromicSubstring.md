# [Longest Palindromic Substring](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/)
Given a string `s`, return *the longest palindromic substring* in `s`.  
  
A string is called a palindrome string if the reverse of that string is the same as the original string.

#### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

#### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

#### Constraints:
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

##### Hint #1
How can we reuse a previously computed palindrome to compute a larger palindrome?

##### Hint #2
If "aba" is a plaindrome, is "xabax" a plaindrome? Similarly is "xabay" a palindrome?

##### Hint #3
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.
