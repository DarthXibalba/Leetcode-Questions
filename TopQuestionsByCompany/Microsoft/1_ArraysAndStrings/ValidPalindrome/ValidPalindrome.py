import string

def ValidPalindrome(s):
    validSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    parsed = ""
    for c in s:
        if (c in validSet):
            parsed += c.lower()
    L = len(parsed)
    if (parsed == ""):
        return True
    for i in range(int(L/2+1)):
        if (parsed[i] != parsed[L-i-1]):
            return False
    return True

if __name__ == '__main__':
    # EX1
    s = "A man, a plan, a canal: Panama"
    ans = ValidPalindrome(s)
    print(f'Input: s = "{s}"')
    print(f'Output: {ans}')

    # EX2
    s = "race a car"
    ans = ValidPalindrome(s)
    print(f'Input: s = "{s}"')
    print(f'Output: {ans}')

    # EX3
    s = " "
    ans = ValidPalindrome(s)
    print(f'Input: s = "{s}"')
    print(f'Output: {ans}')
