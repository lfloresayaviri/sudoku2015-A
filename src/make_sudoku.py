# make_sudoku.py
# author: David Bau
# Copyright (c) 2006 David Bau.  All rights reserved.
# Modified by Daniel Jauregui for study purposes

import random

class Sudoku(object):

    def __init__(self, level):
        self.level = level

    def generate_game(self):
        return [self.make_puzzle(self.solution([None] * 81))]

    def make_puzzle(self,board):
        puzzle = []; deduced = [None] * 81
        order = random.sample(xrange(81), 81)
        for position in order:
            if deduced[position] is None:
                puzzle.append((position, board[position]))
                deduced[position] = board[position]
                self.deduce(deduced)
        print self.board_for_entries(puzzle)
        return self.board_for_entries(puzzle)

    def board_for_entries(self, entries):
        board = [None] * 81
        for position, number in entries: board[position] = number
        return board

    def solution(self, board):
            return self.solve_board(board)[1]

    def solve_board(self, original):
        board = list(original)
        guesses = self.deduce(board)
        if guesses is None: return ([], board)
        track = [(guesses, 0, board)]
        return self.solve_next(track)

    def solve_next(self, remembered):
        while len(remembered) > 0:
            guesses, c, board = remembered.pop()
            if c >= len(guesses): continue
            remembered.append((guesses, c + 1, board))
            workspace = list(board)
            pos, n = guesses[c]
            workspace[pos] = n
            guesses = self.deduce(workspace)
            if guesses is None: return (remembered, workspace)
            remembered.append((guesses, 0, workspace))
        return ([], None)


    def print_code(self, n):
        if n is None: return '*'
        return str(n + 1)


    def print_board(self, board):
        out = '-----------------------\n'
        y = 8
        for matrix in xrange(81):
            out += self.print_code(board[matrix]) + ' '
            if (matrix % 3) == 2:
                    out += "| "
            if matrix == y:
                    out += '\n'
                    if ((matrix >= 19) and (matrix <= 27)) or ((matrix >= 45) and (matrix <= 54)):
                            out += '-----------------------\n'
                    y += 9
        out += '-----------------------\n'
        return out


    def deduce(self, board):
        while True:
            stuck, guess, count = True, None, 0
            """ fill in any spots determined by direct conflicts """
            allowed, needed = self.figure_bits(board)
            for position in xrange(81):
                if None == board[position]:
                    numbers = self.list_bits(allowed[position])
                    if len(numbers) == 0: return []
                    elif len(numbers) == 1: board[position] = numbers[0]; stuck = False
                    elif stuck:
                        guess, count = self.pick_better(guess, count, [(position, number) for number in numbers])
            if not stuck: allowed, needed = self.figure_bits(board)
            # fill in any spots determined by elimination of other locations
            for axis in xrange(3):
                for x in xrange(9):
                    numbers = self.list_bits(needed[axis * 9 + x])
                    for number in numbers:
                        bit = 1 << number
                        spots = []
                        for y in xrange(9):
                            position = self.position_for(x, y, axis)
                            if allowed[position] & bit: spots.append(position)
                        if len(spots) == 0: return []
                        elif len(spots) == 1: board[spots[0]] = number; stuck = False
                        elif stuck:
                            guess, count = self.pick_better(guess, count, [(position, number) for position in spots])
            if stuck:
                if guess is not None: random.shuffle(guess)
                return guess


    def figure_bits(self, board):
        allowed, needed = [e is None and 511 or 0 for e in board], []
        for axis in xrange(3):
            for x in xrange(9):
                bits = self.axis_missing(board, x, axis)
                needed.append(bits)
                for y in xrange(9):
                    allowed[self.position_for(x, y, axis)] &= bits
        return allowed, needed

    def axis_missing(self, board, x, axis):
        bits = 0
        for y in xrange(9):
            e = board[self.position_for(x, y, axis)]
            if e is not None: bits |= 1 << e
        return 511 ^ bits

    def position_for(self, x, y, axis = 0):
        if axis == 0: return x * 9 + y
        elif axis == 1: return y * 9 + x
        else: return (0,3,6,27,30,33,54,57,60)[x] + (0,1,2,9,10,11,18,19,20)[y]

    def list_bits(self, bits):
        return [value for value in xrange(9) if 0 != bits & 1 << value]

    def pick_better(self, b, c, t):
        if b is None or len(t) < len(b): return t, 1
        if len(t) > len(b): return b, c
        if random.randint(0, c) == 0: return t, c + 1
        else: return b, c + 1



game = Sudoku("easy")
temp = game.generate_game()
print(temp)
print game.print_board(temp[0])
c=0

for x in temp[0]:
    if x != None:
        c+=1
print(c)