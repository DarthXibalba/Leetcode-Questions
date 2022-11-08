# This is the easy method of string manipulation, but what if this is not an allowed solution or even possible to perform under the given circumstances?
def hammingWeight_easy(n):
    """
    :type n: int
    :rtype: int
    """
    n_str = bin(n)[2:]
    weight = 0
    for b in n_str:
        if b == "1":
            weight += 1
    return weight

# Bitwise operator approach
def hammingWeight_intuitive(n):
    i = 0
    weight = 0
    mask = 1
    while (i < 32):
        # AND n with mask to get the specified digit in n
        if (n & mask) != 0:
            weight += 1
        # Shift mask to the left to get the next digit in n
        mask <<= 1
        i+=1
    return weight

# Bitwise operator approach: n AND (n-1)
def hammingWeight(n):
    weight = 0
    while (n != 0):
        n &= (n-1)
        weight += 1
    return weight


if __name__ == "__main__":
    N = [
        11,  #"00000000000000000000000000001011",
        128,  #"00000000000000000000000010000000",
        4294967293,  #"11111111111111111111111111111101"
    ]
    for n in N:
        print(bin(n))
        print(hammingWeight(n))
        print("")
