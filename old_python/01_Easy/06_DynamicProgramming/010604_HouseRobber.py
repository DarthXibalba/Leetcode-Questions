def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Bruteforce approach to get thoughts jogging
    '''
    evenSum = 0
    for i in range(0, len(nums), 2):
        evenSum += nums[i]
    oddSum = 0
    for i in range(1, len(nums), 2):
        oddSum += nums[i]
    if evenSum > oddSum:
        return evenSum
    else:
        return oddSum
    '''
    # Remember that there are two trees which we must traverse, one that starts at index=0 and the other that starts at index=1
    sum0 = robR(nums, None, 0)
    if (len(nums) > 1):
        sum1 = robR(nums, None, 1)
        return max(sum0, sum1)
    else:
        return sum0


def robR(nums, sums, n):
    """
    :type nums: List[int]
    :rtype: int
    """
    L = len(nums)
    if (sums == None):
        sums = {}
    # If we are being asked to operate outside of the length of the array, do nothing
    if (n > L):
        return
    if (n in sums):
        return sums[n]
    else:
        # Skip recursive call if n+2 or n+3 have already been calculated or are outside of lenght of array
        if n+2 < L:
            sums[n+2] = robR(nums, sums, n+2)
        if n+3 < L:
            sums[n+3] = robR(nums, sums, n+3)
        # Calculate and return sums[n]
        # If both n+2 && n+3 are valid entries
        if (n+2 < L) and (n+3 < L):
            return nums[n] + max(sums[n+2], sums[n+3])
        # If only n+2 is a valid entry
        elif (n+2 < L):
            return nums[n] + sums[n+2]
        # n itself is the only valid entry
        else:
            return nums[n]



if __name__ == "__main__":
    nums = [
        [1,2,3,1],     # 1+3 = 4
        [2,7,9,3,1],   # 2+9+1 = 12
        [2,1,1,2],     # 2+2 = 4
        [1,1,1,1],     # 1+1 = 2
        [1,3,1,3,100],  # 3+100 = 103
        [0]
    ]
    results = [
        4,
        12,
        4,
        2,
        103,
        0
    ]

    for i,n in enumerate(nums):
        print(f"nums = {n}")
        sum = rob(n)
        print(f"greatestSum = {sum}")
        assert sum == results[i], f"{sum} != {results[i]}"
        print("")
