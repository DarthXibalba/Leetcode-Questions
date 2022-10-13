def RemoveDuplicates(sortedArray):
    nonValue = "X"
    i = 0  # Let i be the pointer to the non-duplicate portion of the array
    for j in range(1, len(sortedArray)):
        # If array[j] is the same as array[i], then overwrite with nonValue
        if (sortedArray[i] == sortedArray[j]):
            sortedArray[j] = nonValue
        # Else, see if we need to perform any swaps
        else:
            # Increment non-duplicate pointer
            i += 1
            # If i & j are no the same index, swap the values at these pointers
            if (i != j):
                sortedArray[i] = sortedArray[j]
                sortedArray[j] = nonValue
    return i + 1


if __name__ == "__main__":
    input1 = [1,1,2]  # k = 2
    input2 = [0,0,1,1,1,2,2,3,3,4]  # k = 5
    input3 = [1,2]  # k = 2
    ans1 = RemoveDuplicates(input1)
    print(f"k1 = {ans1}")
    print(f"output = {input1}")
    ans2 = RemoveDuplicates(input2)
    print(f"k2 = {ans2}")
    print(f"output = {input2}")
    ans3 = RemoveDuplicates(input3)
    print(f"k2 = {ans3}")
    print(f"output = {input3}")
