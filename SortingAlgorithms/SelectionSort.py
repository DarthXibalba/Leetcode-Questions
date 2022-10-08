import ArrayData as AD
import ArrayFunctions as AF

def selectionSort(array, optimal=True):
    if (optimal):
        print("Using optimal solution!")
        selectionSortOptImpl(array)
    else:
        print("NOT using optimal solution!")
        selectionSortImpl(array)

def selectionSortImpl(array):
    arraySize = len(array)
    AF.printArray(array)
    # Loop thru all the elements to ensure it makes at least N passes for N minValues to be selected
    compCount = 0
    swapCount = 0
    for i in range(arraySize):
        minIdx = i
        # Compare this minVal to the rest of the *unsorted* array
        for j in range(i + 1, arraySize):
            compCount += 1
            if (array[minIdx] > array[j]):
                minIdx = j
        # Swap first value with min value
        if (minIdx != i):
            temp = array[i]
            array[i] = array[minIdx]
            array[minIdx] = temp
            AF.printArray(array)
            swapCount += 1
    print(f"Number of Comparisons: {compCount}")
    print(f"Number of Swaps:       {swapCount}")

def selectionSortOptImpl(array):
    arraySize = len(array)
    AF.printArray(array)
    # Loop thru all the elements to ensure it makes at least N passes for N minValues to be selected
    compCount = 0
    swapCount = 0
    for i in range(arraySize):
        minIdx = i
        # Compare this minVal to the rest of the *unsorted* array
        performedSwap = False
        for j in range(i + 1, arraySize):
            compCount += 1
            if (array[minIdx] > array[j]):
                minIdx = j
        # Swap first value with min value
        if (minIdx != i):
            temp = array[i]
            array[i] = array[minIdx]
            array[minIdx] = temp
            AF.printArray(array)
            swapCount += 1
            performedSwap = True
        if not performedSwap:
            break
    print(f"Number of Comparisons: {compCount}")
    print(f"Number of Swaps:       {swapCount}")



if __name__ == "__main__":
    data = AD.dataXL1
    optimal = True
    selectionSort(data, optimal)
