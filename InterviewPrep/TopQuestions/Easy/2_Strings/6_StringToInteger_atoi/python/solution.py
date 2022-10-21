def myAtoi(s):
    # Trim the leading whitespace
    s = s.strip()
    if len(s) == 0:
        return 0
    # Trim the leading pos/neg sign, and keep track if it is negative
    isNegative = False
    if (s[0] == "-") or (s[0] == "+"):
        if (s[0] == "-"):
            isNegative = True
        s = s[1:]
    # Split the string into [numbers, decimal]
    s = s.split(".")
    # Read in the next character until the end or until a non-digit character appears
    n = 0
    for c in s[0]:
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            n = n*10 + (ord(c) - ord("0"))
        else:
            break
    # Now add the decimal portion
    if (len(s) > 1):
        i = 1
        for c in s[1]:
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                n += (ord(c) - ord("0")) / 10**i
                i += 1
    # Correct sign
    if isNegative:
        n *= -1
    # Return n within bounds
    if n < -2**31:
        return -2**31
    elif n > 2**31 - 1:
        return 2**31 - 1
    else:
        return n
    

if __name__ == "__main__":
    strings = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "",
        "123.45"
    ]

    for s in strings:
        print(s)
        print(myAtoi(s))
