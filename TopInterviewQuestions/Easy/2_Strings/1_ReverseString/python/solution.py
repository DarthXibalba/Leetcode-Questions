def ReverseString(s):
    L = len(s)
    for i in range(len(s)//2):
        temp = s[i]
        s[i] = s[L-i-1]
        s[L-i-1] = temp

if __name__ == "__main__":
    s1 = ["h","e","l","l","o"]
    s2 = ["H","a","n","n","a","h"]
    print(s1)
    ReverseString(s1)
    print(s1)
    print(s2)
    ReverseString(s2)
    print(s2)
