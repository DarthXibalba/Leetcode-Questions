class Solution:
    def selectionSort(A):
        # Traverse thru all elements
        for i in range(len(A)):
            # Find the minimum element in unsorted array
            min_idx = i
            print(f"\tmin_idx = {min_idx}")
            for j in range(i+1, len(A)):
                if A[j] < A[min_idx]:
                    min_idx = j
                    print(f"\tnew min_idx = {min_idx}")

            # Swap the value and maintain the order in the [sorted | unsorted] array
            if (i != min_idx):
                print(f"Swapping values...")
                print(f"  i = {i}\n  min_idx = {min_idx}")
                print(f"  A[i] = {A[i]}\n  A[min_idx] = {A[min_idx]}")
                swap_val = A[i]
                A[i] = A[min_idx]
                A[min_idx] = swap_val
        return A

if __name__ == '__main__':
    A = [64, 25, 12, 22, 11]
    print(f"A = {A}")
    S = Solution.selectionSort(A)
    print(f"A = {A}")
    print(f"S = {S}")
