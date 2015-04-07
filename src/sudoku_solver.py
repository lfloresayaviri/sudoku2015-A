# sudoku_solver.py
# author: Daniel Jauergui
# date: 3-31-2015

from configuration.configuration import *
from file_manager.file_manager import *
from decorator_menu import request_answer_menu
from menu import Menu
from menu import Item


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
    menu.add_item(Item(1, 'Start New Game', None, game_menu))
    menu.add_item(Item(2, 'Import Game', None, game_menu))
    menu.add_item(Item(9, 'Back', main_menu, game_menu))
    menu.add_item(Item(0, 'Exit', None, game_menu))
    menu.draw()
    if option != 999:
        menu.click_item(option)
        menu.destroy()

main_menu()