# Effectively a modified bubbleSort but specifically just for 0's to bubble up to the end of the array
def moveZeroes_orig(nums):
    L = len(nums)
    for i in range(L):
        performedSwap = False
        for j in range(L - 1 - i):
            if (nums[j] == 0):
                performedSwap = True
                nums[j] = nums[j+1]
                nums[j+1] = 0
        if not performedSwap:
            break

# Two pointer approach
def moveZeroes(nums):
    L = len(nums)
    i = 0
    j = 0
    zeroes = 0
    while i < L:
        if (nums[i] == 0):
            zeroes += 1
        else:
            nums[j] = nums[i]
            j += 1
        i += 1
    i = L - zeroes
    while i < L:
        nums[i] = 0
        i += 1



if __name__ == "__main__":
    nums = [
        [0,1,0,3,12],
        [0]
    ]
    for n in nums:
        print(n)
        moveZeroes(n)
        print(n)
