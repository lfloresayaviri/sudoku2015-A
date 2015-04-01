# menu.py

import os

class Menu(object):
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []

    def add_item(self, item):
        self.items.append(item)

    def draw(self):
        os.system("cls")
        print(self.name)
        line = " "
        for x in range(0,len(self.name)):
            line += "="
        print(line + "\n")
        for item in self.items:
            item.draw()

    def clickItem(self,op):
        for item in self.items:
            if (item.id == op):
                try:
                    item.function()
                except:
                    item.parent()

    def destroy(self):
        del self

class Item(Menu):
    def __init__(self,id , name, function, parent):
        self.id = id
        self.name = name
        self.function = function
        self.parent = parent

    def draw(self):
        print("    " + str(self.id) + ". " + self.name)