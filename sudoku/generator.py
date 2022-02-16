"""A python module to create valid sudoku solutions
"""

from random import choice, shuffle
debug = False
time = 1

def get_square_number(line, colum):
    """to get the correct square address"""
    return 3 * (line // 3) + (colum // 3)

class Sudoku:
    """Class for the sudoku table"""
    def __init__(self):
        self.matriz = [[0 for _ in range(9)] for j in range(9)]
        self.lines = [set() for _ in range(9)]
        self.colums = [set() for _ in range(9)]
        self.squares = [set() for _ in range(9)]
        self.numbers = {i:0 for i in range(1, 10)}
        self.random_walker = [(i, j) for i in range(9) for j in range(9)]
        shuffle(self.random_walker)

    def print_matriz(self):
        """some eye candy for a sudoku matriz print"""
        print('*-----------------------*')
        for num, line in enumerate(self.matriz):
            if num in (3, 6):
                print('|-------+-------+-------|')
            print('| {} {} {} | {} {} {} | {} {} {} |'.format(*line))
        print('*-----------------------*')

    def is_valid_position(self, elem, line, colum):
        """check if the element can be placed without breaking game rules"""
        if elem in self.lines[line]:
            return False
        if elem in self.colums[colum]:
            return False
        if elem in self.squares[get_square_number(line, colum)]:
            return False
        return True

    def add_element(self, elem, line, colum):
        """if doesn't break any game rule, add the element and returns true"""
        valid = self.is_valid_position(elem, line, colum)
        if valid:
            self.matriz[line][colum] = elem
            self.lines[line].add(elem)
            self.colums[colum].add(elem)
            self.squares[get_square_number(line, colum)].add(elem)
            self.numbers[elem] += 1
            from os import system
            if debug:
                system(f'sleep {time} && clear')
                print(f'({line},{colum}) = {elem}')
                self.print_matriz()
        return valid

    def get_position_possibilities(self, line, colum):
        square = get_square_number(line, colum)
        pos = {1,2,3,4,5,6,7,8,9}
        taken = self.lines[line] | self.colums[colum] | self.squares[square]
        return list(pos - taken)

    def get_shuffled_position_possibilities(self, line, colum):
        sfl = self.get_position_possibilities(line, colum)
        shuffle(sfl)
        return sfl

    def get_free_positions(self):
        return ((i, j) for i in range(9) for j in range(9) if self.matriz[i][j] == 0)

    def get_next_free_position(self):
        try:
            return next(self.get_free_positions())
        except StopIteration:
            return (-1, -1)

    def get_random_free_position(self, start=0):
        while True:
            i, j = self.random_walker[start]
            if self.matriz[i][j] == 0:
                return (i, j)
            start += 1

    def is_solved_game(self):
        return self.get_next_free_position() == (-1, -1)

    def update_line(self, line):
        self.lines[line] = set(self.matriz[line])

    def update_colum(self, colum):
        self.colums[colum] = set()
        for line in self.matriz:
            self.colums[colum].add(line[colum])

    def update_square(self, square):
        self.squares[square] = set()
        line = (square // 3) * 3
        colum = (square % 3) * 3
        for i in range(line, line + 3):
            for j in range(colum, colum + 3):
                self.squares[square].add(self.matriz[i][j])

    def clear_position(self, line, colum):
        elem = self.matriz[line][colum]
        square = get_square_number(line, colum)
        if elem != 0:
            self.matriz[line][colum] = 0
            self.update_line(line)
            self.update_colum(colum)
            self.update_square(square)
            self.numbers[elem] -= 1

    def get_invalid_numbers_for_position(self, i, j):
        return self.lines[i] | self.colums[j] | self.squares[get_square_number(i,j)]

    def find_a_tough_place(self):
        #return max(((i, j) for i in range(9) for j in range(9) if self.matriz[i][j] == 0), default=(-1,-1), key=lambda add: len(self.lines[add[0]] | self.colums[add[1]] | self.squares[get_square_number(add[0], add[1])]))
        #return max(self.get_free_positions(), default=(-1,-1), key=lambda add: len(self.get_invalid_numbers_for_position(*add)))
        #m = max(map(self.get_free_positions(), lambda a: len(self.get_invalid_numbers_for_position(*a))))
        m = max(map(lambda a: len(self.get_invalid_numbers_for_position(*a)), self.get_free_positions()))
        l = [e for e in self.get_free_positions() if len(self.get_invalid_numbers_for_position(*e)) == m]
        return choice(l)

    def get_random_game_solution(self):
        try:
            i, j = self.find_a_tough_place()
        except ValueError:
            return
        #pos = self.get_shuffled_position_possibilities(i, j)
        pos = sorted(self.get_position_possibilities(i,j), key=lambda i: self.numbers[i])
        while len(pos) > 0:
            self.add_element(pos.pop(), i, j)
            self.get_random_game_solution()
            if self.is_solved_game():
                return
            else:
                self.clear_position(i, j)

if __name__ == '__main__':
    from sys import argv
    for _ in range(int(argv[1])):
        s = Sudoku()
        s.get_random_game_solution()
        s.print_matriz()
