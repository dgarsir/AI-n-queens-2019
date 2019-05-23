# n queens using a genetic algorithm
import random
import numpy as np

def generateBoard(val):
    board = []
    row = []
    init_queen_indices = np.random.permutation(val)
    for i in range(len(init_queen_indices)):
        for j in range(val):
            if j == init_queen_indices[i]:
                row.append(1)
            else:
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
        fitness = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 1:
                    #check column
                    for r in range(self.size):
                        if r != row:
                            if self.board[r][col] == 1:
                                break
                        if r == self.size-1:
                            fitness += 1
                    #check row
                    for c in range(self.size):
                        if c != col:
                            if self.board[row][c] == 1:
                                break
                        if c == self.size-1:
                            fitness += 1
                    #check lower right diagonal
                    r = row+1
                    c = col+1
                    while (r < self.size) & (c < self.size):
                        if self.board[r][c] == 1:
                            break
                        if (r == self.size-1) | (c == self.size-1):
                            fitness += 1
                        r += 1
                        c += 1
                    #check lower left diagonal
                    r = row+1
                    c = col-1
                    while (r < self.size) & (c >= 0):
                        if self.board[r][c] == 1:
                            break
                        if (r == self.size-1) | (c == 0):
                            fitness += 1
                        r += 1
                        c -= 1
                    #check upper right diagonal
                    r = row-1
                    c = col+1
                    while (r >= 0) & (c < self.size):
                        if self.board[r][c] == 1:
                            break
                        if (r == 0) | (c == self.size-1):
                            fitness += 1
                        r -= 1
                        c += 1
                    #check upper left diagonal
                    r = row-1
                    c = col-1
                    while (r >= 0) & (c >= 0):
                        if self.board[r][c] == 1:
                            break
                        if (r == 0) | (c == 0):
                            fitness += 1
                        r -= 1
                        c -= 1
        return fitness


class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
    
    def populate(self, ind_size):
        for i in range(self.size):
            self.population.append(Individual(ind_size))

    def update(self, index, updated_board):
        self.population[index].board = updated_board


def solution(population):
    max_iterations = 100
    new_population = Population(population.size)

    while max_iterations > 0:
        fitness = []
        for i in range(population.size):
            fitness.append(population.population[i].getFitness())
        total_fitness = np.sum(fitness)
        fitness_probability = np.array(fitness)/total_fitness

        #generate new population based on fitness probability
        i = 0
        while len(new_population.population) < population.size:
            if np.random.random() <= fitness_probability[i]:
                new_population.population.append(population.population[i])
            i += 1
            i %= population.size

        #mate new "fitter" population
        for i in range(new_population.size):
            mating_partner = np.random.randint(new_population.size)
            crossover_point = np.random.randint(new_population.population[0].size)
            offspring = new_population.population[i].board[:crossover_point] + new_population.population[mating_partner].board[crossover_point:]
            
            #mutate offspring with 0.001 probability
            # for row in range(new_population.population[0].size):
            #     for col in range(new_population.population[0].size):
            #         if (offspring[row][col] == 1) & (np.random.random() < 0.001):
            #             offspring[row][col] = 0
            #             if row > 0:
            #                 offspring[row-1][col] = 1
            #             else:
            #                 offspring[row+1][col] = 1

            new_population.update(i, offspring)

        max_iterations -= 1

    #return best solution
    fitness = []
    for i in range(new_population.size):
        fitness.append(new_population.population[i].getFitness())

    return new_population.population[fitness.index(max(fitness))]
    

pop_size = 10
board_size = int(input("Enter a board size: "))
initial_population = Population(pop_size)
initial_population.populate(board_size)

print(solution(initial_population))
