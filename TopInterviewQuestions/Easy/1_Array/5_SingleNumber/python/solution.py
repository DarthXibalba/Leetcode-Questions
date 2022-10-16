'''
Time Complexity: O(2n)
Space Complexity: O(n)
'''
def SingleNumber(nums):
    numsCount = {}
    # Count how many occurences of each value occur in nums
    for val in nums:
        if val not in numsCount:
            numsCount[val] = 1
        else:
            numsCount[val] += 1
    # Iterate over the values and return the first occurance of a value that has only 1 occurance
    for val in nums:
        if numsCount[val] == 1:
            return val

'''
Approach 4: Bit Manipulation
Concept:
- If we take XOR of zero and some bit, it will return that bit
-- a ⊕ 0 = a
-If we take XOR of two same bits, it will return 0
-- a ⊕ a = 0
- a ⊕ b ⊕ a => (a ⊕ a) ⊕ b => 0 ⊕ b => b
So we can XOR all bits together to find the unique number.

Time Complexity: O(n)
Space Complexity: O(1)
'''
def SingleNumberXOR(nums):
    a = 0
    for val in nums:
        a ^= val
    return a


if __name__ == "__main__":
    nums1 = [2,2,1]
    nums2 = [4,1,2,1,2]
    nums3 = [1]
    ans1 = SingleNumber(nums1)
    ans2 = SingleNumber(nums2)
    ans3 = SingleNumber(nums3)
    print(nums1)
    print(ans1)
    print(nums2)
    print(ans2)
    print(nums3)
    print(ans3)
