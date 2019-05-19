# place 10 queens on a 10 x 10 w backtracking
# place 25 queens on a 25 x 25 w backtracking

# use recursion

# set up board

def generateBoard(val):
    board = []
    row = []
    while (len(board) < val):
        for i in range(val):
            row.append(0)
        board.append(row)
        row = []
    return board


def canPlace(board, row, col):
    #check row
    if (1 in board[row]): 
        return False
    #check column
    for i in range(len(board)):
        if (board[i][col] == 1):
            return False
    #check upper left diagonal
    r = row
    c = col
    while (r >= 0 and c >= 0):
        if (board[r][c] == 1):
            return False
        r -= 1
        c -= 1
    #check upper right diagonal
    r = row
    c = col
    while (r >= 0 and c < len(board)):
        if (board[r][c] == 1):
            return False
        r -= 1
        c += 1
    #check lower left diagonal
    r = row
    c = col
    while (r < len(board) and c >= 0):
        if (board[r][c] == 1):
            return False
        r += 1
        c -= 1
    r = row
    c = col
    while (r < len(board) and c < len(board)):
        if (board[r][c] == 1):
            return False
        r += 1
        c += 1
    return True
    
# use recursion to check for solution
def findSolution(board, col):
    if (col == len(board)):
        return True
    for i in range(len(board)):
        if (canPlace(board, i, col)):
            board[i][col] = 1
            if (findSolution(board, col+1) == True):
                return True
            board[i][col] = 0
    return False

def printBoard(board):
    for x in board:
        print(x)

n = input('Please enter val n for nxn board: ')
board = generateBoard(n)
if findSolution(board, 0):
    printBoard(board)
else:
    print('No solution found')
