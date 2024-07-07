def isPalindrome(s):
    p = "" # processed string
    for c in s:
        val = ord(c)
        # Convert uppercase to lowercase
        if (val >= ord("0") and val <= ord("9")):
            p += chr(val)
        elif (val >= ord("A")) and (val <= ord("Z")):
            p += chr(val + 32)
        elif (val >= ord("a")) and (val <= ord("z")):
            p += chr(val)
    # Now check that p is symmetrical
    for i in range(len(p)//2):
        if (p[i] != p[len(p)-1-i]):
            return False
    return True



if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "
    result1 = isPalindrome(s1)
    result2 = isPalindrome(s2)
    result3 = isPalindrome(s3)
    print(s1)
    print(result1)
    print(s2)
    print(result2)
    print(s3)
    print(result3)
