def RemoveDuplicates(sortedArray):
    i = 0
    j = i + 1
    while(j < len(sortedArray)):
        if sortedArray[i] == sortedArray[j]:
            j += 1
        else:
            i += 1
            sortedArray[i] = sortedArray[j]
    return i+1

class TestCase:
    def __init__(self, input, k, nums):
        self.input = input
        self.k = k
        self.nums = nums
    
    def print(self):
        print("Input = " + str(self.input))
        print("k = " + str(self.k))
        print("Expected output = " + str(self.nums))

if __name__ == "__main__":
    tests = [TestCase([1,1,2], 2, [1,2]),
             TestCase([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
             TestCase([1,2], 2, [1,2])]
    
    for t in tests:
        t.print()
        k = RemoveDuplicates(t.input)
        print("| ----- Output ----- |")
        print("k = " + str(k))
        print("Input = " + str(t.input))
        print()
    
