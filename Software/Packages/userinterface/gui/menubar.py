# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
from tkinter import Menu


class MenuBar:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.menu_bar = Menu(parent)
        self.parent.config(menu=self.menu_bar)
        self.new_menu = None

    def create_new_menu(self, str_label):
        self.new_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=str_label, menu=self.new_menu)

    def add_new_command(self, str_label, cmd=None):
        self.new_menu.add_command(label=str_label, command=cmd)

    def add_command_separator(self):
        self.new_menu.add_separator()