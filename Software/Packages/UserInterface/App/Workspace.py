# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk

# add file information
__version__ ='0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class Workspace:
    def __init__(self, parent, *args, **kwargs):
        pass

    def onNewWorkspace(self):
        print("onNewWorkspace")

    def onOpenWorkspace(self):
        print("onOpenWorkspace")

    def onSaveWorkspace(self):
        print("onSaveWorkspace")

    def onSaveAsWorkspace(self):
        print("onSaveAsWorkspace")

    def workspace_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Workspace")
        mb_ivar.add_new_command('New', self.onNewWorkspace)
        mb_ivar.add_new_command('Open...', self.onOpenWorkspace)
        mb_ivar.add_new_command('Save', self.onSaveWorkspace)
        mb_ivar.add_new_command('Save As...', self.onSaveAsWorkspace)


def main():
    root = tk.Tk()
    Workspace(root)
    root.mainloop()


if __name__=='__main__':
    main()