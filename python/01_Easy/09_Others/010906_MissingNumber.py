def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    theoreticalSum = 0
    actualSum = 0
    i = 1
    containsZero = False
    for n in nums:
        if (n == 0):
            containsZero = True
        actualSum += n
        theoreticalSum += i
        i += 1
    # If the sums match, then it is a valid [0,n-1] range
    # Therefore a missing number could be either 0 or n
    if (actualSum == theoreticalSum):
        if not containsZero:
            return 0
        else:
            return i
    else:
        return theoreticalSum - actualSum



if __name__ == "__main__":
    nums = [
        [3,0,1],
        [0,1],
        [9,6,4,2,3,5,7,0,1],
        [1]  # missing 0
    ]
    for n in nums:
        print(n)
        print(missingNumber(n))
