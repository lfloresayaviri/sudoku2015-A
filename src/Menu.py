# menu.py

import os

class Menu(object):
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []

    def add_item(self, item):
        self.items.append(item)
        if item.parent != self:
            item.parent = self

    def remove_item(self, item):
        self.items.remove(item)
        if item.parent == self:
            item.parent = None

    def draw(self):
        os.system("cls")
        print(self.name)
        line = " "
        for x in range(0,len(self.name)):
            line += "="
        print(line + "\n")
        for item in self.items:
            item.draw()

class Item(Menu):
    def __init__(self, name, function, parent=None):
        self.name = name
        self.function = function
        self.parent = parent
        if parent:
            parent.add_item(self)

    def draw(self):
        print("    " + self.name)