# norvig_solver.py
# author: Josue Mendoza
# date: 4-12-2015

import collections
from singleton import Singleton


class NorvigSolver(object):
    """NorvigSolver instance objects have attributes containing values
    required for the norvigs algorithm to solve a sudoku game.
    Can there only be one instance of this object.
    """
    __metaclass__ = Singleton

    def __init__(self):
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.squares = self.cross(self.rows, self.cols)
        self.unit_list = ([self.cross(self.rows, col) for col in self.cols] +
                        [self.cross(row, self.cols) for row in self.rows] +
                        [self.cross(row_square, col_square) for row_square in ('ABC','DEF','GHI')
                        for col_square in ('123','456','789')])
        self.units = dict((square, [unit for unit in self.unit_list if square in unit])
                        for square in self.squares)
        self.peers = dict((square, set(sum(self.units[square],[]))-set([square]))
                        for square in self.squares)

    def cross(self, list_A, list_B):
        """Cross product of elements in A and elements in B.
        Keyword arguments:
        list_A -- list with elements to be combined
        list_B -- list with elements to be combined
        """
        return [a+b for a in list_A for b in list_B]

    def parse_grid(self, grid):
        """Converts grid to a dictionary of possible values, {square: digits}, or
        return False if a contradiction is detected.
        Keyword arguments:
        grid -- it is a list containing the grid values, it will have a zero ('0') for
        non-set values (i.e. ['0', '0', '3', '0', '2', '0', '6', '0', '0', '9',...)
        """
        ## To start, every square can be any digit; then assign values from the grid.
        values = dict((square, self.digits) for square in self.squares)
        for square, digit in self.grid_values(grid).items():
            if digit in self.digits and not self.assign(values, square, digit):
                return False
        return values

    def grid_values(self, grid):
        """Converts grid into a dict of {square: char} with '0' for empties.
        Returns the dictionary generated (i.e. OrderedDict([('A1', '2'), ('A2', '0')...).
        Keyword arguments:
        grid -- it is a list containing the grid values, it will have a zero ('0') for
        non-set values (i.e. ['0', '0', '3', '0', '2', '0', '6', '0', '0', '9',...)"""
        assert len(grid) == 81
        grid_values_dict = self.order_dictionary(dict(zip(self.squares, grid)))
        return grid_values_dict

    def order_dictionary(self, dict):
        """Orders a dictionary and returns an OrderedDict object with the result
        Keyword arguments:
        dict -- it is the dictionary to be ordered (i.e. {'I6': '7', 'H9': '9',...)"""
        ordered_dict = collections.OrderedDict(sorted(dict.items()))
        return ordered_dict

    def assign(self, values, square, digit):
        """Eliminates all the other values (except digit) from values[square] and propagate.
        Returns values, except return False if a contradiction is detected.
        Keyword arguments:
        values -- dictionary containing the game values (i.e. {'I6': '7', 'H9': '9',...)
        square -- string containing the square to be handled in the method (i.e. 'I6')
        digit -- string containing the digit to be handled in the method (i.e. '7')
        """
        other_values = values[square].replace(digit, '')
        if all(self.eliminate(values, square, digit2) for digit2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, digit):
        """Eliminate digit from values[square]; propagate when values or places <= 2.
        Returns values, except return False if a contradiction is detected.
        Keyword arguments:
        values -- dictionary containing the game values (i.e. {'I6': '7', 'H9': '9',...)
        square -- string containing the square to be handled in the method (i.e. 'I6')
        digit -- string containing the digit to be handled in the method (i.e. '7')
        """
        if digit not in values[square]:
            return values ## Already eliminated
        values[square] = values[square].replace(digit,'')
        if len(values[square]) == 0:
            return False ## Contradiction: removed last value
        elif len(values[square]) == 1:
            digit2 = values[square]
            if not all(self.eliminate(values, square2, digit2) for square2 in self.peers[square]):
                return False
        for unit in self.units[square]:
            digit_places = [square for square in unit if digit in values[square]]
            if len(digit_places) == 0:
                return False ## Contradiction: no place for this value
            elif len(digit_places) == 1:
                if not self.assign(values, digit_places[0], digit):
                    return False
        return values

    def solve(self, grid):
        """Calls the search method in charge of searching solutions for the grid provided
        Returns a list containing containing the grid values corresponding to the solved
        game (i.e. ['4', '8', '3', '9', '2', '1', '6', '5', '7', '9',...), except
        it will return boolean False if the game grid has no solution.
        Keyword arguments:
        grid -- it is a list containing the grid values, it will have a zero ('0') for
        non-set values (i.e. ['0', '0', '3', '0', '2', '0', '6', '0', '0', '9',...)
        """
        if self.search(self.parse_grid(grid)):
            return self.search(self.parse_grid(grid)).values()
        else:
            return False

    def search(self, values):
        """Using depth-first search and propagation, try all possible values.
        Returns an OrderedDict object containing the result
        (i.e. ([('A1', '4'), ('A2', '8'),...) except it returns False if it fails finding a solution.
        Keyword arguments:
        values -- dictionary containing the game values (i.e. {'I6': '7', 'H9': '9',...)"""
        if values is False:
            return False ## Failed earlier
        if all(len(values[square]) == 1 for square in self.squares):
            return self.order_dictionary(values) ## Solved!
        n, square = min((len(values[square]), square) for square in self.squares if len(values[square]) > 1)
        return self.some(self.search(self.assign(values.copy(), square, digit))
                    for digit in values[square])

    def some(self, sequence):
        """Returns an element of sequence that is True.
        Keyword arguments:
        sequence -- it is an OrderedDict object containing a sequence"""
        print "Sec: ", type(sequence)
        for element in sequence:
            if element:
                return element
        return False