# Time Complexities of all Sorting Algorithms
The efficiency of an algorithm depends on two parameters:
1. Time Complexity
2. Space Complexity

**Time Complexity** is defined as the number of times a particular instruction set is executed rather than the total time taken. It is because the total time taken also depends on some external factors like the compiler used, processor's speed, etc.

**Space Complexity** is the total memory space required by the program for its execution.

Z = Omega  
T = Theta

| Algorithm | Time Complexity    |
| --------- | ------------------ |
  
| Algorithm | Best | Avg | Worst |
| ------------------ | ---- |---- | ----- |
| **Selection Sort** | Z(n^2)     | T(n^2)     | O(n^2)     |
| **Bubble Sort**    | Z(n)       | T(n^2)     | O(n^2)     |
| **Insertion Sort** | Z(n)       | T(n^2)     | O(n^2)     |
| **Heap Sort**      | Z(nlog(n)) | T(nlog(n)) | O(nlog(n)) |
| **Quick Sort**     | Z(nlog(n)) | T(nlog(n)) | O(n^2)     |
| **Merge Sort**     | Z(nlog(n)) | T(nlog(n)) | O(nlog(n)) |
| **Bucket Sort**    | Z(n+k)     | T(n+k)     | O(n^2)     |
| **Radix Sort**     | Z(nk)      | T(nk)      | O(nk)      |
