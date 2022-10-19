# Merge Sort
Like Quick Sort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. **The merge() function** is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l...m] and arr[m+1...r] are sorted and merges the two sorted sub-arrays into one.  

**Algorithm:**  
**MergeSort(arr[], l, r)**  
If r > 1  
1. Find the middle point to divide the array into two halves:  
```middle m = l + (r-1)/2```  
2. Call mergeSort() for first half:  
```Call mergeSort(arr, l, m)```  
3. Call mergeSort() for second half:  
```Call mergeSort(arr, m+1, r)```  
4. Merge the two halves sorted in step 2 and 3:  
```Call merge(arr, l, m, r)```  

The following diagram on [Wikipedia](https://en.wikipedia.org/wiki/File:Merge_sort_algorithm_diagram.svg) shows the complete merge sort process for an example array {38, 27, 43, 3, 9, 82, 10}.  

## Complexity
**Time Complexity:** O(nlogn)  
**Auxilary Space:** O(n)  
**In Place:**  No  

## Links
https://www.geeksforgeeks.org/merge-sort/  
[C++ Implementation](MergeSort.cpp)  
