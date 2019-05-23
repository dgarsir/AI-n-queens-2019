# n queens using a genetic algorithm
import numpy as np

def generateBoard(val):
    board = []
    row = []
    while (len(board) < val):
        for i in range(val):
            row.append(0)
        board.append(row)
        row = []
    return board

def randRow(n):
    row = []
    one = np.random.randint(0, n)
    for i in range(0, n):
        if (i == one):
            row.append(1)
        else:
            row.append(0)
    return row

def crossover(mother, father):
    break_point = np.random.randint(1, mother.size)
    for i in range (0, break_point):
        father_row_temp = father.board[i]
        father.board[i] = mother.board[i]
        mother.board[i] = father_row_temp

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
        fitness = 0
        placements = []
        for i in range (self.size):
            placements.append([i, self.board[i].index(1)])
        for rc in placements:
            if (self.canPlace(self.board, rc[0], rc[1])):
                fitness += 1
        return fitness

    def mutate(self):
        # 1/100 chance to mutate
        if (np.random.randint(0, 100) == 0):
            rand_row = np.random.randint(0, self.size)
            rand_col = np.random.randint(0, self.size)
            self.board[rand_row][self.board[rand_row].index(1)] = 0
            self.board[rand_row][rand_col] = 1

    def canPlace(self, board, row, col):
        board[row][col] = 0
        #check column
        for i in range(len(board)):
            if (board[i][col] == 1):
                board[row][col] = 1
                return False
        #check upper left diagonal
        r = row
        c = col
        while (r >= 0 and c >= 0):
            if (board[r][c] == 1):
                board[row][col] = 1
                return False
            r -= 1
            c -= 1
        #check upper right diagonal
        r = row
        c = col
        while (r >= 0 and c < len(board)):
            if (board[r][c] == 1):
                board[row][col] = 1
                return False
            r -= 1
            c += 1
        #check lower left diagonal
        r = row
        c = col
        while (r < len(board) and c >= 0):
            if (board[r][c] == 1):
                board[row][col] = 1
                return False
            r += 1
            c -= 1
        r = row
        c = col
        while (r < len(board) and c < len(board)):
            if (board[r][c] == 1):
                board[row][col] = 1
                return False
            r += 1
            c += 1
        board[row][col] = 1
        return True

class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
    
    def populate(self, ind_size):
        for i in range(self.size):
            self.population.append(Individual(ind_size))
    

#driver
pop_size = int(input("Please enter a population size: "))
board_size = int(input("Please enter a board size: "))
gen_limit = int(input("Please enter a generation limit: "))

print("Initializing population...")

#initialize population
pop = Population(pop_size)
pop.populate(board_size)
for ind in pop.population:
    for i in range(ind.size):
        ind.board[i] = randRow(ind.size)
    print(ind)

print("Beginning algorithm.")

curr_gen = 0

while(curr_gen < gen_limit):

    print("Current generation = ", curr_gen)
    for ind, index in enumerate(pop.population):
        print(index, ind)
        print('')
    #get fitness of individuals
    fitwheel = []
    for ind in pop.population:
        for i in range(ind.getFitness()+1):
            fitwheel.append(ind)
    
    #create new population
    for i in range(pop.size):
        pop.population[i] = np.random.choice(fitwheel)
    
    for ind, index in enumerate(pop.population):
        print(index, ind)
        print('')

    #crossover and mutate
    count = 0
    while (count < pop.size-1):
        crossover(pop.population[count], pop.population[count+1])
        pop.population[count].mutate()
        pop.population[count+1].mutate()
        count += 2

    for i in range(pop.size):
        if (pop.population[i].getFitness() == 4):
            print("Solution found")
            print(pop.population[i])
            curr_gen = gen_limit
            break

    curr_gen += 1