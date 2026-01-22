# [Max Points on a Line](https://leetcode.com/explore/interview/card/top-interview-questions-hard/123/math/873/)

Given an array of `points` where `points[k] = [xₖ, yₖ]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

#### Example 1:
<img src="images/030802_plane1.jpg" width="255" height="250">

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

#### Example 2:
<img src="images/030802_plane2.jpg" width="255" height="250">

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
```

#### Constraints:
- `1 <= points.length <= 300`
- `points[k].length == 2`
- `-10⁴ <= xₖ, yₖ <= 10⁴`
- All the `points` are **unique**.
