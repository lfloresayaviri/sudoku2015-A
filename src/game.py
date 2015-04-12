# make_sudoku.py
# author: David Bau
# Copyright (c) 2006 David Bau.  All rights reserved.
# URL: http://davidbau.com/downloads/sudoku.py
# Modified by Daniel Jauregui for study purposes

import random


class Game(object):

    def __init__(self, level):
        self.level = level

    def generate_game(self):
        """Call to make_puzzle with a empty board to generate game
        with level defined and it will return a array e.g.: Array: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        Where the position are from 0 to 80

        Keyword arguments:
        return -- Array e.g.: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        """
        return self.make_puzzle(self.solution([None] * 81))

    def make_puzzle(self, board):
        """Get the solved board and remove the range of values
         defined for level, the random position values will be
         replaced for None.

        Keyword arguments:
        board -- Array with all values solved for sudoku.
        return -- Array e.g.: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        """
        """ Implement random according level defined """
        puzzle = []
        deduced = [None] * 81
        order = random.sample(xrange(81), 81)
        for position in order:
            if deduced[position] is None:
                puzzle.append((position, board[position]))
                deduced[position] = board[position]
                self.deduce(deduced)
        return self.board_for_entries(puzzle)

    def board_for_entries(self, entries):
        """Get array with tuples of position and value.
        This method will return an array with final array
        with values (Numbers and None).

        Keyword arguments:
        entries -- Array of tuples e.g.: [(23, 5), (80, 9),..., (2, 5), (15, 1)]
        return  -- Array e.g.: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        """
        board = [None] * 81
        for position, number in entries:
            board[position] = number
        return board

    def solution(self, board):
        """Get an empty array with 81 positions and call
        solve_board method to get a solved sudoku.

        Keyword arguments:
        board -- Array e.g.: [None, None,..., None, None]
        return  -- Array e.g.: [4, 9, 3, 4, 5, ...., 8, 7, 4, 8, 1]
        """
        return self.solve_board(board)[1]

    def solve_board(self, original):
        """Get an empty array (it can be resolve the puzzle)
        and create an arrays of board in order to get an unique solution

        Keyword arguments:
        original -- Array of Arrays e.g.: [[None, None,..., None, None]]
        return  -- Array e.g.: [4, 9, 3, 4, 5, ...., 8, 7, 4, 8, 1]
        """
        board = list(original)
        guesses = self.deduce(board)
        if guesses is None:
            return [], board
        track = [(guesses, 0, board)]
        return self.solve_next(track)

    def solve_next(self, remembered):
        """Get a board and guesses required if game is empty,
        it will create all game until a board does not contains None values

        Keyword arguments:
        remembered -- Array e.g.: [[None, None,..., None, None]]
        return  -- Array e.g.: [4, 9, 3, 4, 5, ...., 8, 7, 4, 8, 1]
        """
        while len(remembered) > 0:
            guesses, c, board = remembered.pop()
            if c >= len(guesses):
                continue
            remembered.append((guesses, c + 1, board))
            workspace = list(board)
            pos, n = guesses[c]
            workspace[pos] = n
            guesses = self.deduce(workspace)
            if guesses is None:
                return (remembered, workspace)
            remembered.append((guesses, 0, workspace))
        return [], None

    def print_code(self, n):
        """ It will be removed and defined in new class related with UI"""
        if n is None:
            return '*'
        return str(n + 1)

    def print_board(self, board):
        """ It will be removed and defined in new class related with UI"""
        out = '-----------------------\n'
        y = 8
        for matrix in xrange(81):
            out += self.print_code(board[matrix]) + ' '
            if (matrix % 3) == 2:
                    out += "| "
            if matrix == y:
                    out += '\n'
                    if ((matrix >= 19) and (matrix <= 27)) or ((matrix >= 45) and (matrix <= 54)):
                            out += '------+-------+--------\n'
                    y += 9
        out += '-----------------------\n'
        return out

    def deduce(self, board):
        """Get a board that require to deduce the value following the
         sudoku rules

        Keyword arguments:
        board -- Array e.g.: [[None, None,..., None, None]]
        return  -- Array of tuples [(Position, Value)], the number of array items depends of number gasses found
        """
        while True:
            stuck, guess, count = True, None, 0
            # fill in any spots determined by direct conflicts
            allowed, needed = self.figure_bits(board)
            for position in xrange(81):
                if None == board[position]:
                    numbers = self.list_bits(allowed[position])
                    if len(numbers) == 0:
                        return []
                    elif len(numbers) == 1:
                        board[position] = numbers[0]
                        stuck = False
                    elif stuck:
                        guess, count = self.pick_better(guess, count, [(position, number) for number in numbers])
            if not stuck:
                allowed, needed = self.figure_bits(board)
            # fill in any spots determined by elimination of other locations
            for axis in xrange(3):
                for x in xrange(9):
                    numbers = self.list_bits(needed[axis * 9 + x])
                    for number in numbers:
                        bit = 1 << number
                        spots = []
                        for y in xrange(9):
                            position = self.position_for(x, y, axis)
                            if allowed[position] & bit:
                                spots.append(position)
                        if len(spots) == 0:
                            return []
                        elif len(spots) == 1:
                            board[spots[0]] = number
                            stuck = False
                        elif stuck:
                            guess, count = self.pick_better(guess, count, [(position, number) for position in spots])
            if stuck:
                if guess is not None:
                    random.shuffle(guess)
                return guess

    def figure_bits(self, board):
        """Get a board that require verify if a position is allowed according with
         sudoku rules

        Keyword arguments:
        board -- Array e.g.: [[None, None,..., 1, None]]
        return  -- Two arrays "Allowed" and "Needed" with figure bits value
        """
        allowed, needed = [e is None and 511 or 0 for e in board], []
        for axis in xrange(3):
            for x in xrange(9):
                bits = self.axis_missing(board, x, axis)
                needed.append(bits)
                for y in xrange(9):
                    allowed[self.position_for(x, y, axis)] &= bits
        return allowed, needed

    def axis_missing(self, board, x, axis):
        """Verify the missing azis using the board

        Keyword arguments:
        board -- Array e.g.: [[None, 8,..., 1, None]]
        x -- position in axis X
        axis -- axis of board in current context.
        return  -- return a figure bits
        """
        bits = 0
        for y in xrange(9):
            e = board[self.position_for(x, y, axis)]
            if e is not None:
                bits |= 1 << e
        return 511 ^ bits

    def position_for(self, x, y, axis=0):
        """Determine of position in sudoku for current arguments.

        Keyword arguments:
        x -- position in axis X
        y -- position in axis y
        axis -- axis of board in current context.
        return  -- a position in array that contain all values e.g: Row:2 Column: 3, it will return 12
        """
        if axis == 0:
            return x * 9 + y
        elif axis == 1:
            return y * 9 + x
        else:
            return (0, 3, 6, 27, 30, 33, 54, 57, 60)[x] + (0, 1, 2, 9, 10, 11, 18, 19, 20)[y]

    def list_bits(self, bits):
        """Determine when bits is allowed or needed returning and array with possible values of solution

        Keyword arguments:
        bits -- Get a figure bits
        return  -- Return an Array of numbers candidate of solution e.g.: [1, 2, 3, 4, 5, 7, 8, 9]
        """
        return [value for value in xrange(9) if 0 != bits & 1 << value]

    def pick_better(self, guess, count, positions_in_spot):
        """Determine with of positions in spot is the best to solve puzzle.

        Keyword arguments:
        guess -- Array returned by figure_bits method
        count -- Count how many times position was guessed
        positions_in_spot -- Array of positions got from spots.
        return  -- It will return an array guess and count
        """
        if guess is None or len(positions_in_spot) < len(guess):
            return positions_in_spot, 1
        if len(positions_in_spot) > len(guess):
            return guess, count
        if random.randint(0, count) == 0:
            return positions_in_spot, count + 1
        else:
            return guess, count + 1