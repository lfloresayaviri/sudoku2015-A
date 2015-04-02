# sudoku_solver.py

from decorator_menu import request_answer_menu
from menu import Menu
from menu import Item

@request_answer_menu
def gameMenu(op=999):
    menu = Menu("Sudoku Solver - Game Section")
    menu.add_item(Item(1,"Start New Game",None,gameMenu))
    menu.add_item(Item(2,"Import Game",None,gameMenu))
    menu.add_item(Item(9,"Back",mainMenu,gameMenu))
    menu.add_item(Item(0,"Exit",None,gameMenu))
    menu.draw()
    if (op!=999):
        menu.clickItem(op)
        menu.destroy()

@request_answer_menu
def configMenu(op=999):
    menu = Menu("Sudoku Solver - Config Section")
    menu.add_item(Item(1,"Select Level",None,configMenu))
    menu.add_item(Item(2,"Select Algorithm",None,configMenu))
    menu.add_item(Item(9,"Back",mainMenu,configMenu))
    menu.add_item(Item(0,"Exit",None,configMenu))
    menu.draw()
    if (op!=999):
        menu.clickItem(op)
        menu.destroy()

@request_answer_menu
def mainMenu(op=999):
    menu = Menu("Sudoku Solver")
    menu.add_item(Item(1,"Configuration Game",configMenu,mainMenu))
    menu.add_item(Item(2,"Start Game",gameMenu,mainMenu))
    menu.add_item(Item(0,"Exit",None,mainMenu))
    menu.draw()
    if (op!=999):
        menu.clickItem(op)
        menu.destroy()

mainMenu()



