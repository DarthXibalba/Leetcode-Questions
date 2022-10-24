import math
from collections import deque

def plusOne1(digits):
    num = 0
    for d in digits:
        num = num*10 + d
    # Increment by 1
    num += 1
    # Determine how many digits we will be returning by taking the log10(num)
    # math.log10(10) // 1 == 1
    # math.log10(9) // 1 == 0
    L = int(math.log10(num) // 1) + 1
    numArray = [0] * L  # Initialize a zero array of size L
    for i in range(L):
        numArray[L-1-i] = num % 10
        num = num // 10
    return numArray

# Second attempt, using deque
def plusOne2(digits):
    inDeque = deque(digits)
    outDeque = deque()
    carryover = 1
    for i in range(len(inDeque)):
        result = inDeque.pop() + carryover
        outDeque.appendleft(result % 10)
        carryover = result // 10
    # If there is still a carryover at the end, then append it
    if (carryover != 0):
        outDeque.appendleft(carryover)
    # Convert to list/array
    output = [0] * len(outDeque)
    for i,v in enumerate(outDeque):
        output[i] = v
    return output



if __name__ == "__main__":
    digits = [
        [1,2,3],
        [4,3,2,1],
        [9]
    ]
    for d in digits:
        print(d)
        print(plusOne2(d))
