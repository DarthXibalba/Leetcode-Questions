import ArrayData as AD
import ArrayFunctions as AF

def quickSort(array, low, high):
    if (low < high):
        # Find pivot element such that smaller elements are on the left and greater elements are on the right
        pivot = partition(array, low, high)
        quickSort(array, low, pivot - 1)
        quickSort(array, pivot + 1, high)
        AF.printArray(array)

def partition(array, low, high):
    pivot = array[high]  # Choose the rightmost element
    i = low - 1              # Pointer for the greater element
    # Traverse thru all elements, compare each element with the pivot
    for j in range(low, high):
        # If element is smaller, swap it with the greater element (pointed to by i)
        if (array[j] <= pivot):
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    # Swap the pivot element with the greater element (pointed to by i)
    array[high] = array[i + 1]
    array[i + 1] = pivot
    # Return the position from where the partition is done
    return i + 1



if __name__ == "__main__":
    data = AD.dataXL1
    AF.printArray(data)
    quickSort(data, 0, len(data) - 1)
