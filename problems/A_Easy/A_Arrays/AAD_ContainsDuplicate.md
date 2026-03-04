# [Contains Duplicate](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/)
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

#### Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```

#### Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```

#### Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

#### Constraints:
- `1 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`

#### Follow up #1:
Can you do it with O(1) extra space?

#### Follow up #2:
How would you handle data  too large to fit in memory?" (Streaming detection)

<details>
<summary><b>Hint</b></summary>
“Streaming” means you don’t necessarily have the full list up front; values arrive one-by-one (e.g., from a file/socket). You want to detect duplicates as you read.

Time: amortized O(1) per item
Space: O(k) where k is the number of distinct items seen so far

Approximate streaming (Bloom filter idea)
If memory is tight and “maybe duplicates” is acceptable, a Bloom filter can detect duplicates with false positives but no false negatives (for membership). That’s typically the “advanced follow-up” discussion.
</details>

#### Follow up #3:
What if we have a bounded range of [0, M]? How would you solve this using a bitset / bitmap detection?

<details>
<summary><b>Hint</b></summary>
If inputs are integers in a known small range [0, M], you can use a bit array where bit x indicates “seen x”.

- Time: O(n)
- Space: O(M) bits (very compact)
- Constraints: Only works if x is a non-negative int within a manageable max range.
- Follow-up angle: “Numbers are between 0 and 1,000,000; optimize memory.”
  - Use `bytearray` or a real bitarray library
</details>