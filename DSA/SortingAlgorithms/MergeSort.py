import ArrayData as AD
import ArrayFunctions as AF

def mergeSort(array):
    if len(array) > 1:
        m = len(array)//2
        leftArray = array[:m]
        rightArray = array[m:]
        mergeSort(leftArray)
        mergeSort(rightArray)
        merge(array, leftArray, rightArray)

def merge(origArray, leftArray, rightArray):
        L = len(leftArray)
        R = len(rightArray)
        i = j = k = 0
        # Overwrite array[k] with the smaller value of the two subarrays
        while (i < L) and (j < R):
            if (leftArray[i] < rightArray[j]):
                origArray[k] = leftArray[i]
                i += 1
                k += 1
            else:
                origArray[k] = rightArray[j]
                j += 1
                k += 1
        # Add the rest of the non-empty array
        while (i < L):
            origArray[k] = leftArray[i]
            i += 1
            k += 1
        while (j < R):
            origArray[k] = rightArray[j]
            j += 1
            k += 1
        AF.printArray(origArray)



if __name__ == "__main__":
    data = AD.dataXL1
    AF.printArray(data)
    mergeSort(data)
