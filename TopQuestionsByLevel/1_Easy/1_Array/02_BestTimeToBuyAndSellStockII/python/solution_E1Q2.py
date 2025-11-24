class TestCase:
    def __init__(self, input, expOutput):
        self.input = input
        self.profit = expOutput

def BestTimeToBuyAndSell(prices):
    profit = 0
    i = 0
    j = i + 1
    
    while j < len(prices):
        if prices[i] < prices[j]:
            profit += prices[j]-prices[i]
        i += 1
        j += 1

    return profit

if __name__ == "__main__":
    tests = [
        TestCase([7,1,5,3,6,4], 7),
        TestCase([1,2,3,4,5], 4),
        TestCase([7,6,4,3,1], 0),
        TestCase([1], 0),
        TestCase([], 0),
        TestCase([1,10,7], 9),
        TestCase([1,10,7,10], 12),
        TestCase([2,2,2], 0),
        TestCase([2,2], 0),
        TestCase([2,2,2,2,10,2,2,10],16)
    ]
    
    for t in tests:
        profit = BestTimeToBuyAndSell(t.input)
        assert profit == t.profit, f"Expected profit={t.profit}, got {profit}"

    print("All tests passed!")
