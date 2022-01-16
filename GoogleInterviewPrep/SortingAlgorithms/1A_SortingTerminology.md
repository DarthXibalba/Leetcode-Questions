# Sorting Terminology
## In-Place Sorting
In-Place sorting algorithm uses **constant space** for producing the output (modifies the given array only). It sorts the list only by modifying the order of the elements within the list.  
For example, *Insertion Sort* & *Selection Sort* are in-place sorting algorithms as they do not use any additional space for sorting the list. (*Merge Sort* is not in-place)

## What are Internal and External Sortings?
When all data is placed in-memory, this sorting is called **internal sorting**.
When all data that needs to be sorted cannot be placed in-memory at a time, the sorting is called **external sorting**. External Sorting is used for massive amount of data. (Merge Sort and its variations are typically used for external sorting.)

## Stable Sorting
Stability is mainly important when we have key value pairs with duplicate keys possible (like people names as keys and their details as values). And we wish to sort these objects by keys.