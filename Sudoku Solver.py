def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    sudoku = {
        "row0" : board[0],
        "row1" : board[1],
        "row2" : board[2],
        "row3" : board[3],
        "row4" : board[4],
        "row5" : board[5],
        "row6" : board[6],
        "row7" : board[7],
        "row8" : board[8],
        "col0" : [],
        "col1" : [],
        "col2" : [],
        "col3" : [],
        "col4" : [],
        "col5" : [],
        "col6" : [],
        "col7" : [],
        "col8" : [],
        "col9" : [],
        }
    for i in board:
        sudoku["col0"].append(i[0])
        sudoku["col1"].append(i[1])
        sudoku["col2"].append(i[2])
        sudoku["col3"].append(i[3])
        sudoku["col4"].append(i[4])
        sudoku["col5"].append(i[5])
        sudoku["col6"].append(i[6])
        sudoku["col7"].append(i[7])
        sudoku["col8"].append(i[8])
    

print(solveSudoku([["5","3",".",".","7",".",".",".","."],
                   ["6",".",".","1","9","5",".",".","."],
                   [".","9","8",".",".",".",".","6","."],
                   ["8",".",".",".","6",".",".",".","3"],
                   ["4",".",".","8",".","3",".",".","1"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".","6",".",".",".",".","2","8","."],
                   [".",".",".","4","1","9",".",".","5"],
                   [".",".",".",".","8",".",".","7","9"]]))
