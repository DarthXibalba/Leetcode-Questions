def ContainsDuplicate(array):
    valMap = {}
    for val in array:
        if val in valMap:
            return True
        else:
            valMap[val] = True
    return False

if __name__ == "__main__":
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    ans1 = ContainsDuplicate(nums1)
    ans2 = ContainsDuplicate(nums2)
    ans3 = ContainsDuplicate(nums3)
    print(nums1)
    print(ans1)
    print(nums2)
    print(ans2)
    print(nums3)
    print(ans3)
