#include <iostream>

using namespace std;

void swap(int& a, int& b)
{
    int temp = a;
    a = b;
    b = temp;
}

void bubbleSort(int* A, int n)
{
    for (int i = 0; i < n; i++)
    {
        // The last i elements are already sorted
        for (int j = 0; j < (n - i - 1); j++)
        {
            if (A[j+1] < A[j])
            {
                swap(A[j+1], A[j]);
            }
        }
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
    int A[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(A)/sizeof(A[0]);
    print(A, n);
    bubbleSort(A, n);
    print(A, n);
}
