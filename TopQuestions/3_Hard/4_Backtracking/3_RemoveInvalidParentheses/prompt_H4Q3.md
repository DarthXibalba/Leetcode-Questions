# [Remove Invalid Parentheses](https://leetcode.com/explore/interview/card/top-interview-questions-hard/119/backtracking/854/)
Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return *a list of **unique strings** that are valid with the minimum number of removals.* You may return the answer in **any order**.

#### Example 1:
```
Input: s = "()())()"
Output: ["(())()","()()()"]
```

#### Example 2:
```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
```

#### Example 3:
```
Input: s = ")("
Output: [""]
```

#### Constraints:
- `1 <= s.length <= 25`
- `s` consists of lowercase English letters and parentheses `'('` and `')'`.
- There will be at most `20` parentheses in `s`.

<summary><b>Hint #1</b></summary>
Since we do not know which brackets can be removed, we try all the options! We can use recursion.
</details>

<summary><b>Hint #2</b></summary>
In the recursion, for each bracket, we can either use it or remove it.
</details>

<summary><b>Hint #3</b></summary>
Recursion will generate all the valid parentheses strings but we want the ones with the least number of parentheses deleted.
</details>

<summary><b>Hint #4</b></summary>
We can count the number of invalid brackets to be deleted and only generate the valid strings in the recusrion.
</details>
