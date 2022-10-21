def strStr(haystack, needle):
    H = len(haystack)
    N = len(needle)
    if N > H:
        return -1
    for i in range(H):
        j = 0
        while (j < N) and (i + j < H):
            if haystack[i+j] != needle[j]:
                break
            # If we've reached the end of the needle and we had a match (cuz we didn't have a mismatch above)
            elif j == N-1:
                return i
            j += 1

    # If we made it here, then needle is not in haystack
    return -1
                    
# Elegant solution found online
def strStr2(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

if __name__ == "__main__":
    haystacks = [
        "sadbutsad",
        "leetcode",
        "mississippi",
        "a"
    ]
    needles = [
        "sad",
        "leeto",
        "issipi",
        "a"
    ]
    for i, h in enumerate(haystacks):
        print(f"haystack = {h} | needle = {needles[i]}")
        print(strStr(h, needles[i]))
