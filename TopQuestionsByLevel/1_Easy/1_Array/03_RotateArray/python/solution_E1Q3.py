import copy

class TestCase:
    def __init__(self, input, k, output):
        self.input = input
        self.originalInput = copy.deepcopy(input)
        self.k = k
        self.output = output

    def Check(self):
        print("Input: ", self.originalInput)
        print("k: ", self.k)
        print("Result: ", self.input)
        print("Exp Result: ", self.output)
        print()
        assert sameArray(self.output, self.input), f"Expected output={self.output}, got {self.input}"

def RotateArray(nums, k):
    print(nums)
    n = len(nums)
    kmod = k % n
    reverseArray(nums, 0, n-1)
    print(nums)
    reverseArray(nums, 0, kmod-1)
    print(nums)
    reverseArray(nums, kmod, n-1)
    print(nums)

def reverseArray(nums, bound1, bound2):
    while bound1 < bound2:
        tmp = nums[bound1]
        nums[bound1] = nums[bound2]
        nums[bound2] = tmp
        bound1 += 1
        bound2 -= 1

def sameArray(output, expOutput):
    if len(output) != len(expOutput):
        return False
    
    for i in range(len(output)):
        if output[i] != expOutput[i]:
            return False
        
    return True

if __name__ == "__main__":
    tests = [
        TestCase([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        TestCase([-1,-100,3,99], 2, [3,99,-1,-100]),
        TestCase(["U","R","Q","U","I","Z","U"], 2, ["Z","U","U","R","Q","U","I"]),
        TestCase(["U","R","Q","U","I","Z","U"], 5, ["Q","U","I","Z","U","U","R"]),
        TestCase([-1], 2, [-1])
    ]

    for t in tests:
        RotateArray(t.input, t.k)
        t.Check()

    print("All tests passed!")