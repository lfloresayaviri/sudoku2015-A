# norvig_solver_test.py
# author: Josue Mendoza
# date: 4-12-2015

import unittest
import os

from norvig_solver import NorvigSolver


class NorvigSolverTest(unittest.TestCase):
    GAME_1_BOARD_STRING = '00302060090030500100180640000810290070000000800670820000' \
                          '2609500800203009005010300'
    GAME_1_BOARD_LIST = list(GAME_1_BOARD_STRING)
    GAME_1_SOLUTION_STRING = '48392165796734582125187649354813297672956413813679824' \
                             '5372689514814253769695417382'
    GAME_1_SOLUTION_LIST = list (GAME_1_SOLUTION_STRING)

    GAME_2_BOARD_STRING = '20008030006007008403050020900010540800000000040270600030' \
                          '1007040720040060004010003'
    GAME_2_BOARD_LIST = list(GAME_2_BOARD_STRING)
    GAME_2_SOLUTION_STRING = '24598137616927358483756421997612543851349862748273695' \
                             '1391657842728349165654812793'
    GAME_2_SOLUTION_LIST = list (GAME_2_SOLUTION_STRING)

    GAME_3_BOARD_STRING = '90000090700042018000070502610090400005000004000050700992' \
                          '0108000034059000507000000'
    GAME_3_BOARD_LIST = list(GAME_3_BOARD_STRING)

    def test_norvig_algorithm_can_solve_sudoku_game_1(self):
        norvig_solver = NorvigSolver()
        game_solved = norvig_solver.solve(self.GAME_1_BOARD_LIST)
        self.assertEquals(self.GAME_1_SOLUTION_LIST, game_solved)

    def test_norvig_algorithm_can_solve_sudoku_game_2(self):
        norvig_solver = NorvigSolver()
        game_solved = norvig_solver.solve(self.GAME_2_BOARD_LIST)
        self.assertEquals(self.GAME_2_SOLUTION_LIST, game_solved)

    def test_norvig_algorithm_returns_false_if_the_game_cannot_be_solved(self):
        norvig_solver = NorvigSolver()
        game_solved = norvig_solver.solve(self.GAME_3_BOARD_LIST)
        self.assertFalse(game_solved)

    def test_just_one_instance_of_norvig_solver_can_be_created(self):
        norvig_solver_instance_a = NorvigSolver()
        norvig_solver_instance_b = NorvigSolver()
        self.assertEqual(norvig_solver_instance_a, norvig_solver_instance_b)

if __name__ == '__main__':
    unittest.main()