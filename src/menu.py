# menu.py
# author: Daniel Jauergui
# date: 3-31-2015

import os
from utils.singleton import Singleton

class Menu(object):

    __metaclass__ = Singleton

    def __init__(self, name, items=None):
        self.name = name
        self.items = []

    def add_item(self, item):
        """Get a tuple of id,name and function, in order to get action for each
        item added to current Menu

        Keyword arguments:
        item -- A Tuple of int, string object eg: (1,'Item of Menu', function).
        """
        self.items.append(item)

    def clear_items(self):
        """Remove all items of current menu.
        """
        self.items = []

    def draw(self):
        """Print Current menu and its items.
        """
        os.system("cls")
        print(self.name)
        line = " "
        for x in range(0, len(self.name)):
            line += "="
        print(line + "\n")
        for item in self.items:
            print("    " + str(item[0]) + ". " + item[1])

    def ask(self):
        """Aks an option and validate if input is a number,
        if it is less than 0 or major the options in current menu
        the same menu will be displayed until user set correct value.
        """
        option = 999
        while option != 0:
            self.draw()
            try:
                option = input("\n\nPlease select an option: ")
                val = int(option)
            except:
                option = 999
            if 1 <= option <= len(self.items)-1:
                break
        if option != 0:
            self.click_item(option)

    def click_item(self, option):
        """Move to the next menu or action.

        Keyword arguments:
        option -- A Tuple of int, string object where execute the object
        assigned to the item.
        """
        for item in self.items:
            if item[0] == option:
                item[2]()

    def destroy(self):
        del self