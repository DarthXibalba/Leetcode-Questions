#include <iostream>

using namespace std;

void print(int* A, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}

void merge(int* A, int const left, int const mid, int const right)
{
    int leftSize = mid - left + 1;
    int rightSize = right - mid;
    cout << "left:  " << left << endl;
    cout << "mid:   " << mid << endl;
    cout << "right: " << right << endl;  
    cout << "leftSize = " << leftSize << endl;
    cout << "rightSize = " << rightSize << endl;

    // Create new temporary arrays
    int* tmpL = new int[leftSize];
    int* tmpR = new int[rightSize];

    // Copy data into temporary arrays
    for (int i = 0; i < leftSize; i++)
    {
        tmpL[i] = A[left + i];
    }
    for (int i = 0; i < rightSize; i++)
    {
        tmpR[i] = A[mid + i + 1];
    }
    print(tmpL, leftSize);
    print(tmpR, rightSize);

    // Merge the data
    int idxA = left;
    int idxL = 0;
    int idxR = 0;
    
    while ((idxL < leftSize) && (idxR < rightSize))
    {
        if (tmpL[idxL] < tmpR[idxR])
        {
            A[idxA++] = tmpL[idxL++];
        }
        else
        {
            A[idxA++] = tmpR[idxR++];
        }
    }
    while (idxL < leftSize)
    {
        A[idxA++] = tmpL[idxL++];
    }
    while (idxR < rightSize)
    {
        A[idxA++] = tmpR[idxR++];
    }

    delete [] tmpL, tmpR;
    cout << endl;
}

void mergeSort(int* A, int const left, int const right)
{
    if (left >= right)
        return;

    int mid = left + (right - left)/2;
    mergeSort(A, left, mid);
    mergeSort(A, mid + 1, right);
    merge(A, left, mid, right);
}

int main()
{
    int A[] = { 12, 11, 13, 5, 6, 7 };
    int n = sizeof(A)/sizeof(A[0]);
    print(A, n);
    mergeSort(A, 0, n-1);
    print(A, n);
    return 0;
}
