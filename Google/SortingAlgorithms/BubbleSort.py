class Solution:
    def bubbleSort(A):
        n = len(A)
        for i in range(n):
            # The last i elements are already sorted
            for j in range(n-i-1):
                # Swap with the adjacent value if lesser than
                if A[j+1] < A[j]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1] = temp
        return A

if __name__ == '__main__':
    A = [64, 34, 25, 12, 22, 11, 90]
    print(f"A = {A}")
    S = Solution.bubbleSort(A)
    print(f"A = {A}")
    print(f"S = {S}")