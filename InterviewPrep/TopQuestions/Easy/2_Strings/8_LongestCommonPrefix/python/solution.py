def longestCommonPrefix(strs):
    prefix = ""
    if len(strs) == 0:
        return prefix
    numStrs = len(strs)
    minStrLen = len(strs[0])
    for s in strs:
        if len(s) < minStrLen:
            minStrLen = len(s)
    for i in range(minStrLen):
        c = strs[0][i]
        isCP = True
        for j in range(0, len(strs)):
            if (c != strs[j][i]):
                isCP = False
                break
        if isCP:
            prefix += c
        else:
            break
    return prefix
        



if __name__ == "__main__":
    strs = [
        ["flower","flow","flight"],
        ["dog","racecar","car"]
    ]
    for s in strs:
        print(s)
        print(longestCommonPrefix(s))
