class TestCase:
    def __init__(self, input, output):
        self.input = input
        self.output = output

def SingleNumber(nums):
    xorSum = 0
    for n in nums:
        xorSum ^= n
    return xorSum

if __name__ == "__main__":
    tests = [
        TestCase([2,2,1],1),
        TestCase([4,1,2,1,2],4),
        TestCase([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1], 9),
        TestCase([1],1)
    ]

    for t in tests:
        result = SingleNumber(t.input)
        assert result == t.output, f"Expected result={t.output}, got {result}"

    print("All tests passed!")
