def RotateArray1(nums, k):
    L = len(nums)
    k = k % L
    output = [0]*L
    # Populate output from array[k->end->start->k]
    j = 0
    for i in range(L-k, L):
        output[j] = nums[i]
        j += 1
    for i in range(L-k):
        output[j] = nums[i]
        j += 1
    for i in range(L):
        nums[i] = output[i]

#def RotateArray2(nums, k):
#    L = len(nums)
#    for _ in range(k):
#        #shiftRight(nums)
#        for i in range(L):
#            temp = nums[0]
#            nums[i] = nums[i-1]



if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    nums2 = [-1,-100,3,99]
    k2 = 2

    print(f"nums = {nums1}, k = {k1}")
    RotateArray1(nums1,k1)
    print(nums1)
    print(f"nums = {nums2}, k = {k2}")
    RotateArray1(nums2,k2)
    print(nums1)
