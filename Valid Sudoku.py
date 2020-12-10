#Runtime: 128 ms, faster than 7.69% of
#Python online submissions for Valid Sudoku.

#Memory Usage: 12.7 MB, less than 65.38% of
#Python online submissions for Valid Sudoku.

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    boxlist = []
    #Test for same in column
    for i in range(9):
        #column i
        for j in range(9):
            #row j
            for k in range(j+1,9):
                #row k
                if board[j][i] == board[k][i] and (board[j][i] != "." and board[k][i] != "."):
                    return False
    #Test for same in row            
    for i in range(9):
        #row i
        for j in range(9):
            #column j
            boxlist.append(board[i][j])
            for k in range(j+1,9):
                #column k
                if board[i][j] == board[i][k] and (board[i][j] != "." and board[i][k] != "."):
                    return False
    #Test for same in box
    #print(boxlist)
    row02 = []
    row35 = []
    row68 = []
    for i in range(81):
        if i % 9 <= 2:
            row02.append(boxlist[i])
        elif i % 9 >= 6:
            row68.append(boxlist[i])
        else:
            row35.append(boxlist[i])
    for i in range(0,27):
        if i < 9:
            end = 9
        elif i < 18:
            end = 18
        else:
            end = 27
        for j in range(i+1,end):
            if row02[i] == row02[j] and (row02[i] != "." and row02[j] != "."):
                return False
            elif row35[i] == row35[j] and (row35[i] != "." and row35[j] != "."):
                return False
            elif row68[i] == row68[j] and (row68[i] != "." and row68[j] != "."):
                return False
                
        
    return True




print(isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".","3","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

"""
print(isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

print(isValidSudoku(
[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]
]))
"""
