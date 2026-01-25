def valid_sudoku(board: list[list[int]]) -> bool:
    SIZE = 9
    rowMap = [ dict() for _ in range(SIZE) ]
    colMap = [ dict() for _ in range(SIZE) ]
    sqMap = [ dict() for _ in range(SIZE) ]

    for i in range(SIZE):
        for j in range(SIZE):
            val = board[i][j]
            if val == ".":
                continue

            # Rows Check
            if val in rowMap[i]:
                return False
            else:
                rowMap[i][val] = []

            # Cols Check
            if val in colMap[j]:
                return False
            else:
                colMap[j][val] = []

            # Squares Check
            sq = (i // 3) * 3 + (j // 3)
            if val in sqMap[sq]:
                return False
            else:
                sqMap[sq][val] = []
    
    return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    result = ValidSudoku(board)
    print(result)