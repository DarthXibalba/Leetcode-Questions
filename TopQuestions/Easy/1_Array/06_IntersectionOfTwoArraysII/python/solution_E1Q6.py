# Approach 1: Make two hash maps that count frequencies of values
def intersect1(nums1, nums2):
    hash1 = {}
    hash2 = {}
    # Tally up the numbers
    for n in nums1:
        if n in hash1:
            hash1[n] += 1
        else:
            hash1[n] = 1
    for n in nums2:
        if n in hash2:
            hash2[n] += 1
        else:
            hash2[n] = 1
    # Now compare both hash tables
    intersection = []
    for k in hash1:
        if (k in hash1) and (k in hash2):
            # Find how many times k occured in both lists
            sharedOccurences = min(hash1[k], hash2[k])
            i = 0
            while i < sharedOccurences:
                intersection.append(k)
                i += 1
    return intersection
    
# Approach 2: Make one hashmap that counts frequencies of values
def intersect2(nums1, nums2):
    smallTally = {}
    smallNums = []
    largeNums = []
    if len(nums1) < len(nums2):
        smallNums = nums1
        largeNums = nums2
    else:
        smallNums = nums2
        largeNums = nums1
    # Tally nums
    for n in smallNums:
        if n in smallTally:
            smallTally[n] += 1
        else:
            smallTally[n] = 1
    # Now compare with the larger nums
    intersection = []
    for n in largeNums:
        if (n in smallTally) and (smallTally[n] > 0):
                intersection.append(n)
                smallTally[n] -= 1
    return intersection

# Approach 3: Sorted arrays, Two pointer approach
def intersect3(nums1, nums2):
    smaller = []
    larger = []
    if len(nums1) < len(nums2):
        smaller = nums1
        larger = nums2
    else:
        smaller = nums2
        larger = nums1
    # Optimize this by using two pointers
    i = 0
    j = 0
    xsection = []
    while i < len(smaller):
        if smaller[i] == larger[j]:
            xsection.append(smaller[i])
            i += 1
            j += 1
        else:
            while (i < len(smaller) and (j < len(larger))) and (smaller[i] != larger[j]):
                if (smaller[i] < larger[j]):
                    i += 1
                else:
                    j += 1
    return xsection



if __name__ == '__main__':
    nums1 = [
        [1,2,2,1],
        [4,9,5]
    ]
    nums2 = [
        [2,2],
        [9,4,9,8,4]
    ]

    for i in range(len(nums1)):
        print(f"nums1 = {nums1[i]}")
        print(f"nums2 = {nums2[i]}")
        nums1[i].sort()  # Approach 3 pre-req
        nums2[i].sort()  # Approach 3 pre-req
        print(f"intersection = {intersect3(nums1[i], nums2[i])}\n")
