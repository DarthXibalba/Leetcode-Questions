def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    i = 2
    # Because of math, we only need to iterate from [2, n^1/2 + 1]
    while (i < n**.5 // 1 + 1):
        # If p[i] is marked as a prime, mark all multiples of it as False
        if primes[i]:
            j = i*2
            while (j < n):
                primes[j] = False
                j += i
        i += 1
    # Get the sum of number of primes
    sum = 0
    i = 0
    while (i < n):
        if primes[i]:
            sum += 1
        i += 1
    return sum



if __name__ == "__main__":
    inputs = [
        10,
        0,
        1,
        2,
        3
    ]
    for i in inputs:
        print(i)
        print(countPrimes(i))
        print()