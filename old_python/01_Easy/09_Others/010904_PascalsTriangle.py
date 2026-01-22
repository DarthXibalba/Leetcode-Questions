def generateRecursive(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    n = [1] * numRows
    # Base Case
    if numRows == 1:
        return [n]
    
    n_1 = generate(numRows-1)
    # We want the range [0, len(n_1) - 1]
    # Since len(n_1) == numRows - 1, then we can use this to our advantage and not call the len() function
    for i in range(numRows - 2):
        n[i+1] = n_1[-1][i] + n_1[-1][i+1]
    n_1.append(n)
    return n_1


# Iterative is much faster approach: 7 ms (13.5MB) on Leetcode vs 36 ms (13MB)
def generateIterative(numRows):
    N = []
    for i in range(numRows):
        n = [1] * (i+1)
        N.append(n)
        for j in range(i - 1):
            N[-1][j+1] = N[-2][j] + N[-2][j+1]
    return N


if __name__ == "__main__":
    numRows = [1, 2, 3, 4, 5, 10]
    for n in numRows:
        print(n)
        print(generateIterative(n))
        print()
