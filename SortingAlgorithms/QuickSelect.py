import ArrayData as AD
import ArrayFunctions as AF

def quickSelect(array, kth_lowest, low, high):
    if (high <= low):
        return array[low]
    # Partition array and grab  the index of the pivot
    pivot_idx = partition(array, low, high)

    # If what we're looking for is to the left of the pivot
    if (kth_lowest < pivot_idx):
        # Recursively perform quickSelect on the left subarray
        quickSelect(array, kth_lowest, low, pivot_idx - 1)
    # If the pivot position is the same as kth_lowest, then we have our result
    elif (kth_lowest == pivot_idx):
        return array[pivot_idx]
    # If what we're looking for is to the right of the pivot
    else:
        quickSelect(array, kth_lowest, pivot_idx + 1, high)

def partition(array, low, high):
    pivot = array[high]  # Choose the rightmost element
    i = low - 1          # Pointer for the greater element
    for j in range(low, high):
        # If element is smaller, swap it with the greater element (pointed to by i)
        if (array[j] <= pivot):
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    # Swap the pivot element with greater element (pointed to by i)
    array[high] = array[i + 1]
    array[i + 1] = pivot
    # Return the position from where the partition is done
    return i + 1



if __name__ == "__main__":
    data = AD.dataXL1
    AF.printArray(data)
    greatestOfK = 3
    kth_lowest = len(data) - greatestOfK
    quickSelect(data, kth_lowest, 0, len(data) - 1)
    AF.printArray(data)
    greatestProduct = 1
    for i in range(kth_lowest, len(data)):
        greatestProduct *= data[i]
    print(f"Greatest Product = {greatestProduct}")
