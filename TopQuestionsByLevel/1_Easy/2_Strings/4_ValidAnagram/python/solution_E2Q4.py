def isAnagram(s, t):
    # If string lengths are not idential, then they can not be anagrams
    if len(s) != len(t):
        return False
    # Populate the maps with their respective character count (using ord() to include Unicode characters)
    sMap = {}
    tMap = {}
    for c in s:
        if ord(c) in sMap:
            sMap[ord(c)] += 1
        else:
            sMap[ord(c)] = 1
    for k in t:
        if ord(k) in tMap:
            tMap[ord(k)] += 1
        else:
            tMap[ord(k)] = 1
    # Check that the values in both maps are equivalent
    if len(sMap) != len(tMap):
        return False
    for m in sMap:
        if (m not in tMap) or (sMap[m] != tMap[m]):
            return False
    # If we've reached this point, then the two strings must be anagrams
    return True

if __name__ == "__main__":
    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"
    output1 = isAnagram(s1, t1)
    output2 = isAnagram(s2, t2)
    print(f"s = {s1}, t = {t1}")
    print(output1)
    print(f"s = {s2}, t = {t2}")
    print(output2)
