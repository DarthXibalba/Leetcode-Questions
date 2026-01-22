class TestCase:
    def __init__(self, input, output):
        self.input = input
        self.output = output

def ContainsDuplicate(nums):
    entryMap = {}
    for n in nums:
        if n in entryMap:
            return True
        else:
            entryMap[n] = True
    return False

if __name__ == "__main__":
    tests = [
        TestCase([1,2,3,1], True),
        TestCase([1,2,3,4], False),
        TestCase([1,1,1,3,3,4,3,2,4,2], True)
    ]

    for t in tests:
        result = ContainsDuplicate(t.input)
        assert result == t.output, f"Expected result={t.output}, got {result}"

    print("All tests passed!")
