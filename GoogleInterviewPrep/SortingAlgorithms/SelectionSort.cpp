#include <iostream>

using namespace std;

void swap(int& a, int&b)
{
    int temp = a;
    a = b;
    b = temp;
}

void selectionSort(int* A, int n)
{
    // Traverse thru all the elements
    for (int i = 0; i < n; i++)
    {
        // Find the minimum element
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
        {
            if (A[j] < A[min_idx])
            {
                min_idx = j;
            }
        }

        // Swap the min element and maintain the order of the [sorted | unsorted] array
        if (i != min_idx)
            swap(A[i], A[min_idx]);
    }
}

void print(int* A, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}

int main()
{
    int A[] = {64, 25, 12, 22, 11};
    int n = sizeof(A)/sizeof(A[0]);
    print(A, n);
    selectionSort(A, n);
    print(A, n);
}
