def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    output = [None] * n
    i = 1
    while (i <= n):
        if (i % 3 == 0):
            if (i % 5 == 0):
                output[i-1] = "FizzBuzz"
            else:
                output[i-1] = "Fizz"
        elif (i % 5 == 0):
            output[i-1] = "Buzz"
        else:
            output[i-1] = f"{i}"
        i += 1
    return output



if __name__ == '__main__':
    N = [3,5,15,1,120,99,100]
    for n in N:
        print(f"n = {n}")
        print(f"{fizzBuzz(n)}")
        print("")
