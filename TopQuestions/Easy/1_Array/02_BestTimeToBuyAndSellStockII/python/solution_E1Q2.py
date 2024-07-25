def BestTimeToBuyAndSell_PeaksAndValleys(prices):
    # Add up the profits between all the valleys and peaks
    i = 0
    profit = 0
    while (i < len(prices) - 1):
        while (i < len(prices) - 1) and (prices[i] >= prices[i+1]):
            i += 1
        valley = prices[i]
        while (i < len(prices) - 1) and (prices[i] <= prices[i+1]):
            i += 1
        peak = prices[i]
        profit += peak - valley
    return profit
            

# Simple Approach: Just track all the profits, none of the losses
def BestTimeToBuyAndSell_Simple(prices):
    profit = 0
    for i in range(1,len(prices)):
        p = prices[i] - prices[i-1]
        if (p > 0):
            profit += p
    return profit

if __name__ == "__main__":
    prices1 = [7,1,5,3,6,4]
    prices2 = [1,2,3,4,5]
    prices3 = [7,6,4,3,1]
    profit1 = BestTimeToBuyAndSell_Simple(prices1)
    profit2 = BestTimeToBuyAndSell_Simple(prices2)
    profit3 = BestTimeToBuyAndSell_Simple(prices3)
    print(f"Profit1 = {profit1}")
    print(f"Profit2 = {profit2}")
    print(f"Profit3 = {profit3}")
