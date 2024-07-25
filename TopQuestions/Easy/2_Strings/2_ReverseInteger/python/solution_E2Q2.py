def ReverseInt(x):
    isNegative = False
    if x == 0:
        return 0
    if x < 0:
        isNegative = True
        x *= -1  # Make x positive and revert it back to negative before returning
    revX = 0
    while (x // 10 != 0):
        # Increment order of revX by 10, and add the remainder
        revX = (revX * 10) + (x % 10)
        x = x // 10
    # Add the last digit
    revX = (revX * 10) + (x % 10)
    if (isNegative):
        revX *= -1
    if (revX >= (2**31 - 1)) or (revX <= (-2**31)):
        return 0
    return revX

if __name__ == "__main__":
    x1 = 123
    x2 = -123
    x3 = 120

    print(x1)
    rx1 = ReverseInt(x1)
    print(rx1)
    print(x2)
    rx2 = ReverseInt(x2)
    print(rx2)
    print(x3)
    rx3 = ReverseInt(x3)
    print(rx3)
