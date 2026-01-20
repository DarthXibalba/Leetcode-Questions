def printArray(array):
    output = "[ "
    arraySize = len(array)
    for i in range(arraySize):
        output += f"{array[i]}"
        if (i != arraySize - 1):
            output += ","
        output += " "
    output += "]"
    print(output)
