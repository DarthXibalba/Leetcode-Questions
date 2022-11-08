# The Hamming Distance is defined as the number of bits that are different given two integers
# Therefore to find the difference, take the two integers X and Y, and XOR them to get the differences and then count number of 1 bits
'''
XOR Truth Table:
A B | Result
----|-------
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0
'''
def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    n = x ^ y  # x XOR y
    hDist = 0
    # Use the n & (n-1) =! 0 mask to get the number of 1's
    while (n != 0):
        hDist += 1
        n &= n-1
    return hDist



if __name__ == '__main__':
    X = [1,3]
    Y = [4,1]
    for i in range(len(X)):
        print(f"x = {X[i]}")
        print(f"y = {Y[i]}")
        print(f"Hamming Distance = {hammingDistance(X[i], Y[i])}")
        print("")
