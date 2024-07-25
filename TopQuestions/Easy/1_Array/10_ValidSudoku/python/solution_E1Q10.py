import copy
from re import sub

'''
Store the information in 3 data structures to easily lookup if the number 
doesn't occur in each {} without remetition:
- Each Row
- Each Column
- Each Subbox

Note: One can use any number of data structures for this problem
1) Use a Hash Table/Dictionary/Set (Set is a hash table with no values)
2) Use an array that contains binary values to signify if a number has been seen or not
3) Using a binary value & using binary math (bitmapping)
'''
def IsValidSudoku1(board):
    N = 9
    rows = [set() for i in range(N)]
    cols = [set() for i in range(N)]
    boxes = [set() for i in range(N)]

    for r in range(N):
        for c in range(N):
            val = board[r][c]
            # If val is "." then ignore value
            if val == ".":
                continue
            # Check if val has appeared in the current row already
            if val in rows[r]:
                return False
            else:
                rows[r].add(val)
            # Check if val has appeared in the current col already
            if val in cols[c]:
                return False
            else:
                cols[c].add(val)
            # Check if val has appeared in its respective subbox already
            # Calculate subbox using coordinates
            subbox = 3*(r // 3) + (c // 3)
            if val in boxes[subbox]:
                return False
            else:
                boxes[subbox].add(val)
    # If we reached this point then it is a valid sudoku
    return True


if __name__ == "__main__":
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    board2 = copy.deepcopy(board1)
    board2[0][0] = "8"
    print("Board1 =")
    print(board1)
    print(f"Is Valid: {IsValidSudoku1(board1)}")
    print("Board2 =")
    print(board2)
    print(f"Is Valid: {IsValidSudoku1(board2)}")
