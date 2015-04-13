# sudoku_solver.py
# author: Daniel Jauergui
# date: 3-31-2015

from configuration.configuration import *
from file_manager.file_manager import *
from decorator_menu import request_answer_menu
from menu import Menu
from menu import Item
from game import *


@request_answer_menu
def main_menu(option=999):
    menu = Menu('Sudoku Solver')
    menu.add_item(Item(1, 'Configuration Game', config_menu, main_menu))
    menu.add_item(Item(2, 'Start Game', game_menu, main_menu))
    menu.add_item(Item(0, 'Exit', None, main_menu))
    menu.draw()
    if option != 999:
        menu.click_item(option)
        menu.destroy()


@request_answer_menu
def config_menu(option=999):
    menu = Menu('Sudoku Solver - Config Section')
    menu.add_item(Item(1, 'Select Level', None, config_menu))
    menu.add_item(Item(2, 'Select Algorithm', None, config_menu))
    menu.add_item(Item(3, 'Print Config File', print_config_file, config_menu))
    menu.add_item(Item(4, 'Print Config Level', print_level_file, config_menu))
    menu.add_item(Item(9, 'Back', main_menu, config_menu))
    menu.add_item(Item(0, 'Exit', None, config_menu))
    menu.draw()
    if option != 999:
        menu.click_item(option)
        menu.destroy()


def print_config_file():
    os.system('cls')
    print ('Print Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.get_xml_as_string())
    input('\n\nPress any key: ')


def print_level_file():
    os.system('cls')
    print ('Print Level of Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.level)
    input('\n\nPress any key: ')


@request_answer_menu
def game_menu(option=999):
    menu = Menu('Sudoku Solver - Game Section')
    menu.add_item(Item(1, 'Start New Game', game, game_menu))
    menu.add_item(Item(2, 'Import Game', None, game_menu))
    menu.add_item(Item(9, 'Back', main_menu, game_menu))
    menu.add_item(Item(0, 'Exit', None, game_menu))
    menu.draw()
    if option != 999:
        menu.click_item(option)
        menu.destroy()


def game():
    """
         def print_code(self, number):
        #It will be removed and defined in new class related with UI
        if number is None:
            return '*'
        return str(number + 1)

    def print_board(self, board):
        #It will be removed and defined in new class related with UI#
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
    """
    os.system('cls')
    print ('\n      Sudoku Game')
    print ('      """""" """"\n\n')
    sudoku_game = Game("easy")
    #board = sudoku_game.generate_game()
    # print(temp)
    #print sudoku_game.print_board(board)
    #c = 0
    #for x in board:
    #    if x:
    #        c += 1
    #c = 81 - c
    #print("Missing numbers: %i" % c)
    input('\n\nPress any key: ')

main_menu()