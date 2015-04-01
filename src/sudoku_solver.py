from menu import Menu
from menu import Item


def gameMenu():
    exit = 999
    while (exit != 0):
        menu = Menu("Sudoku Solver - Game Section")
        menu.add_item(Item("1. Start New Game",None,mainMenu))
        menu.add_item(Item("2. Import Game", None,mainMenu))
        menu.add_item(Item("0. Back",None,mainMenu))
        menu.draw()
        try:
            exit = input("\n\nPlease select an option: ")
        except:
            exit = 999

def configMenu():
    exit = 999
    while (exit != 0):
        menu = Menu("Sudoku Solver - Config Section")
        menu.add_item(Item("1. Select Level",None,mainMenu))
        menu.add_item(Item("2. Select Algorithm", None,mainMenu))
        menu.add_item(Item("0. Back",None,mainMenu))
        menu.draw()
        try:
            exit = input("\n\nPlease select an option: ")
        except:
            exit = 999

def mainMenu():
    exit = 999
    while (exit != 0):
        menu = Menu("Sudoku Solver")
        menu.add_item(Item("1. Configuration Game",configMenu))
        menu.add_item(Item("2. Start Game", gameMenu))
        menu.add_item(Item("0. Exit",None))
        menu.draw()
        try:
            exit = input("\n\nPlease select an option: ")
        except:
           exit = 999

mainMenu()



