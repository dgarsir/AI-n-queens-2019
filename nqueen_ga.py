# n queens using a genetic algorithm
import random

def generateBoard(val):
    board = []
    row = []
    while (len(board) < val):
        for i in range(val):
            row.append(0)
        board.append(row)
        row = []
    return board


class Individual:
    def __init__(self, size):
        self.size = size
        self.board = generateBoard(size)

    def __str__(self):
        ind_str = ''
        for i in range(self.size):
            ind_str += str(self.board[i]) + '\n'
        return ind_str[:-1]

    def new_board(self, board):
        self.board = board
    
    def getFitness(self):
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



class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
    
    def populate(self, ind_size):
        for i in range(self.size):
            self.population.append(Individual(ind_size))

    


x = Individual(4)
x.new_board([[0,0,1,0], [1,0,0,0], [0,0,0,1],[0,1,0,0]])

print(x)