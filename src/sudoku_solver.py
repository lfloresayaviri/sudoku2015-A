# sudoku_solver.py

from decorator_menu import request_answer_menu
from menu import Menu
from menu import Item
from file_manager.configuration import *
from file_manager.file_manager import *


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

@request_answer_menu
def configMenu(op=999):
    menu = Menu("Sudoku Solver - Config Section")
    menu.add_item(Item(1,"Select Level",None,configMenu))
    menu.add_item(Item(2,"Select Algorithm",None,configMenu))
    menu.add_item(Item(3,"Print Config File",printConfigFile,configMenu))
    menu.add_item(Item(4,"Print Config Level",None,configMenu))
    menu.add_item(Item(9,"Back",mainMenu,configMenu))
    menu.add_item(Item(0,"Exit",None,configMenu))
    menu.draw()
    if (op!=999):
        menu.clickItem(op)
        menu.destroy()

def printConfigFile():
    os.system("cls")
    print ("Print Configuration file\n\n")
    file = File("conf/xmlTest.xml")
    config = Configuration(file.read_content())
    print config.get_xml_as_string()
    x = input("\n\nPress any key: ")

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

mainMenu()



