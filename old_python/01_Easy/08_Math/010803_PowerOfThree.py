def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    # If n is negative, then it cannot be a power of 3
    if n < 0:
        return False
    i = 0
    m = 3**i
    while(m <= n):
        if (m == n):
            return True
        m *= 3
        i += 1
    # If we've reached this point, then m > n && m != n
    return False



if __name__ == "__main__":
    n = [27, 0, -1, -3, -27, 81, 82, 1]
    for v in n:
        print(v)
        print(isPowerOfThree(v))
        print()
