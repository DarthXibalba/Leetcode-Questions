# Recursive solution: Top-Down solution
def climbStairsR(n, cache=None):
    """
    :type n: int
    :rtype: int
    """
    # Use a dictionary/hashmap to make this dynamic programming and reduce overall runtime
    if cache == None:
        cache = [0] * (n+1)
    # Base case
    if (n <= 2):
        cache[n] = n
        return n
    # If entry already exists in cache
    if n in cache:
        return cache[n]
    # Calculate number of steps for n
    cache[n-1] = climbStairsR(n-1, cache)
    cache[n-2] = climbStairsR(n-2, cache)
    cache[n] = cache[n-1] + cache[n-2]
    return cache[n]

# Iterative solution: Bottom-Up solution
def climbStairsI(n):
    """
    :type n: int
    :rtype: int
    """
    if (n <= 2):
        return n
    cache = [0] * (n+1)
    cache[1] = 1
    cache[2] = 2

    for i in range(n+1):
        if (i <= 2):
            continue
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]



if __name__ == "__main__":
    n = [2,3,4,5,10,20,45]
    for i in n:
        print(f"n = {i}")
        print(f"steps = {climbStairsI(i)}")
        print("")
