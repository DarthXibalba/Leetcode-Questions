import ArrayData as AD
import ArrayFunctions as AF

def insertionSort(array):
    arraySize = len(array)
    AF.printArray(array)
    # i = unsortedIdx
    # j = sortedIdx
    for i in range(1, arraySize):
        sortVal = array[i]
        j = i - 1
        while (j >= 0) and (sortVal < array[j]):
            array[j+1] = array[j]
            array[j] = sortVal
            j -= 1
        AF.printArray(array)



if __name__ == "__main__":
    data = AD.dataXL1
    insertionSort(data)
