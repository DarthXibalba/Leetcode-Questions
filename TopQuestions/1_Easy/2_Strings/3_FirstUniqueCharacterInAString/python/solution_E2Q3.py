def FirstUniqueChar(s):
    letters = {}
    orderOfAppearance = []
    for i in range(len(s)):
        c = s[i]
        # If the letter has not appeared yet, then it is a unique character that appears only once
        if (c not in letters):
            letters[c] = i
            orderOfAppearance.append(c)
        # If the letter already exists in the map, then it has occured more than once
        else:
            letters[c] = -10

    idx = -1
    for c in orderOfAppearance:
        if (letters[c] >= 0):
            idx = letters[c]
            break
    return idx

def FirstUniqueChar2(s):
    letters = {}
    for c in s:
        if (c not in letters):
            letters[c] = 1
        else:
            letters[c] += 1
    for i in range(len(s)):
        if letters[s[i]] == 1:
            return i
    return -1

if __name__ == "__main__":
    s1 = "leetcode"
    s2 = "loveleetcode"
    s3 = "aabb"
    ans1 = FirstUniqueChar(s1)
    print(s1)
    print(ans1)
    ans2 = FirstUniqueChar(s2)
    print(s2)
    print(ans2)
    ans3 = FirstUniqueChar(s3)
    print(s3)
    print(ans3)
