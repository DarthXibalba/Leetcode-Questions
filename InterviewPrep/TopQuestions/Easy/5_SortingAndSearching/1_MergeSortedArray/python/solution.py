def mergeThreePtrs(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # Since we know nums1 is padded with trailing 0's, we can implement a method of 3 pointers
    # Ptr1 at the max of nums1 (nums1[m]), Ptr2 at the max of nums2 (num2[n]), and Ptr3 at the end of nums1[] where we will be overwriting values
    i = m - 1
    j = n - 1
    k = m + n - 1
    while (i >= 0) and (j >= 0):
        if nums2[j] >= nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
    while (j >= 0):
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    tempNums1 = nums1[:m]
    i = j = k = 0
    # Copy whichever value is smaller
    while (i < m) and (j < n):
        if (tempNums1[i] <= nums2[j]):
            nums1[k] = tempNums1[i]
            i += 1
            k += 1
        else:
            nums1[k] = nums2[j]
            j += 1
            k += 1
    while (i < m):
        nums1[k] = tempNums1[i]
        i += 1
        k += 1
    while (j < n):
        nums1[k] = nums2[j]
        j += 1
        k += 1



if __name__ == '__main__':
    nums1 = [
        [1,2,3,0,0,0],
        [1],
        [0]
    ]
    m = [3,1,0]
    nums2 = [
        [2,5,6],
        [],
        [1]
    ]
    n = [3,0,1]
    for i in range(len(nums1)):
        print(f"nums1 = {nums1[i]}")
        print(f"nums2 = {nums2[i]}")
        print(f"m = {m[i]}")
        print(f"n = {n[i]}")
        mergeThreePtrs(nums1[i], m[i], nums2[i], n[i])
        print(f"nums1 = {nums1[i]}")
        print("")
