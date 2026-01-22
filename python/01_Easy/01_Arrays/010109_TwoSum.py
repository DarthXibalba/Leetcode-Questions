class TestCase:
    def __init__(self, nums: list[int], target: int, expNums: list[int]):
        self.nums = nums
        self.target = target
        self.expNums = expNums

    def Check(self, answer: list[int]):
        self.answer = answer
        self.correct = (answer[0] == self.expNums[0] and answer[1] == self.expNums[1])
        return self.correct
    
    def Print(self):
        print("nums:", self.nums)
        print("target:", self.target)
        print("expNums:", self.expNums)
        print("answer:", self.answer)
        print("Correct:", self.correct)
        

def TwoSum(nums: list[int], target: int) -> list[int]:
    hmap = {}

    for i in range(len(nums)):
        hmap[nums[i]] = i
        nmt = nums[i] - target
        if (nmt in hmap):
            return [i, hmap[i]]
        
    return []

if __name__ == "__main__":
    tests = [
        TestCase([2,7,11,15], 9, [0,1]),
        TestCase([3,2,4], 6, [1,2]),
        TestCase([3,3], 6, [0,1])
    ]

    for t in tests:
        t.Check(TwoSum(t.nums, t.target))
        t.Print()
