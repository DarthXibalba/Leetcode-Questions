import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        random.seed()
        self.nums = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        randNums = self.nums[:]  # Copy list
        # Perform the famous shuffle algorithm
        i = len(randNums) - 1
        while (i > 0):
            j = random.randint(0, i)
            randNums[i], randNums[j] = randNums[j], randNums[i]
            i -= 1
        return randNums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
if __name__ == '__main__':
    sln = Solution([1,2,3,4,5,6])
    print(f"shuffle = {sln.shuffle()}")
    print(f"reset = {sln.reset()}")
    print(f"shuffle = {sln.shuffle()}")
