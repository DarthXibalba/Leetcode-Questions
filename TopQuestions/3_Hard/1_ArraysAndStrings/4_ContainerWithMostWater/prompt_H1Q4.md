# [Container With Most Water](https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/830/)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `iᵗʰ` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store.*

**Notice** that you may not slant the container.

#### Example 1:
<img src="images/image1.jpg" width="560" height="300">

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

#### Example 2:
```
Input: height = [1,1]
Output: 1
```

#### Constraints:
- `n == height.length`
- `2 <= n <= 10ˣ`, `x=5`
- `0 <= height[i] <= 10ʸ`, `y=4`

<details>
<summary><b>Hint #1</b></summary>
If you simulate the problem, it will be O(n²) which is not efficient.
</details>

<details>
<summary><b>Hint #2</b></summary>
Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
</details>

<details>
<summary><b>Hint #3</b></summary>
How can you calculate the amount of water at each step?
</details>
