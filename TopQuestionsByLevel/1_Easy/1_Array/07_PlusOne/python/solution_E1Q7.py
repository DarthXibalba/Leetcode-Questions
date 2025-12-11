import copy

class TestCase:
    def __init__(self, digits, output):
        self.originalInput = copy.deepcopy(digits)
        self.digits = digits
        self.output = output

    def Check(self):
        print("Input:  ", self.originalInput)
        print("Result: ", self.digits)
        print()
        assert self.digits == self.output, f"Expected result={self.output}, got {self.digits}"

def PlusOne(digits):
    i = len(digits) - 1
    while i >= 0:
        sum = digits[i] + 1
        if sum <= 9:
            digits[i] = sum
            return
        else:
            digits[i] = 0
            i-=1
    # If i = -1 then this means all entries were '9' and we have a carry over
    digits[0] = 1
    digits.append(0)

if __name__ == "__main__":
    tests = [
        TestCase([1,2,3], [1,2,4]),
        TestCase([4,3,2,1], [4,3,2,2]),
        TestCase([9],[1,0]),
        TestCase([9,9],[1,0,0]),
        TestCase([9,9,9],[1,0,0,0]),
        TestCase([9,9,9,9],[1,0,0,0,0]),
        TestCase([8,9,8,9],[8,9,9,0]),
        TestCase([8,9,9,9],[9,0,0,0]),
        TestCase([7,8,9,9],[7,9,0,0]),
        TestCase([6,7,8,9],[6,7,9,0]),
        TestCase([5,9,9,9],[6,0,0,0]),
    ]

    for t in tests:
        PlusOne(t.digits)
        t.Check()

    print("All tests passed!")
