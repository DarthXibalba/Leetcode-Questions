#include <iostream>

using namespace std;

void insertionSort(int* A, int n)
{
    for (int i = 1; i <= n; i++)
    {
        int val = A[i];
        int j = i - 1;
        while ((j >= 0) && (A[j] > val))
        {
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = val;
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
    int A[] = { 12, 11, 13, 5, 6 };
    int n = sizeof(A)/sizeof(A[0]);
    print(A, n);
    insertionSort(A, n);
    print(A, n);
}
