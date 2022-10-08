import ArrayData as AD
import ArrayFunctions as AF

def bubbleSort(array, optimal=True):
    if (optimal):
        print("Using optimal solution!")
        bubbleSortOptImpl(array)
    else:
        print("NOT using optimal solution!")
        bubbleSortImpl(array)

def bubbleSortImpl(array):
    arraySize = len(array)
    AF.printArray(data)
    # Loop to access all elements in the array
    ## This ensures we make at least N passes for N values to bubble up
    compCount = 0
    swapCount = 0
    for i in range(arraySize):
        # Compare this value to the rest of the *unsorted* array
        ## Subtract one to prevent index to go out of range
        for j in range(arraySize - i - 1):
            compCount += 1
            # Compare values and swap if necessary
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                AF.printArray(array)
                swapCount += 1
    print(f"Number of Comparisons: {compCount}")
    print(f"Number of Swaps:       {swapCount}")

def bubbleSortOptImpl(array):
    arraySize = len(array)
    AF.printArray(data)
    # Loop to access all elements in the array
    ## This ensures we make at least N passes for N values to bubble up
    compCount = 0
    swapCount = 0
    for i in range(arraySize):
        # Compare this value to the rest of the *unsorted* array
        ## Subtract one to prevent index to go out of range
        performedSwap = False
        for j in range(arraySize - i - 1):
            compCount += 1
            # Compare values and swap if necessary
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                AF.printArray(array)
                performedSwap = True
                swapCount += 1
        # If no swaps were performed, then we can consider this array sorted and break out of the loop
        if not performedSwap:
            break
    print(f"Number of Comparisons: {compCount}")
    print(f"Number of Swaps:       {swapCount}")



if __name__ == "__main__":
    data = AD.data1
    optimal = True
    bubbleSort(data, optimal)
    