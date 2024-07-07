def transpose(matrix):
    R = len(matrix)
    C = len(matrix[0])
    i = 0
    while i < R:
        j = i + 1  # You can skip i = j (diagonal) for transposing a matrix
        while j < C:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j += 1
        i += 1

def reverse(matrix):
    R = len(matrix)
    C = len(matrix[0])
    i = 0
    while i < R:
        j = 0
        while j < C // 2:
            matrix[i][j], matrix[i][C-j-1] = matrix[i][C-j-1], matrix[i][j]
            j += 1
        i += 1

def rotate(matrix):
    transpose(matrix)
    reverse(matrix)

def printMatrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    i = 0
    outputStr = ""
    while i < R:
        j = 0
        outputStr += "["
        while j < C:
            outputStr += f"{matrix[i][j]}"
            if j != (C - 1):
                outputStr += ","
            j += 1
        outputStr += "]\n"
        i += 1
    print(outputStr)

if __name__ == "__main__":
    matrix = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    ]
    for m in matrix:
        printMatrix(m)
        rotate(m)
        printMatrix(m)
