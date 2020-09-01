# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk
from tkinter import Toplevel
from tkinter import scrolledtext
from tkinter import *

# add file information
__version__ = '0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class ConsoleWindow:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.parent.bind("<Configure>", self.follow_me_console_window)

        # create the console window
        self._console_window()

    def show_console_window(self):
        # show console window if it is not yet displayed
        if 0 == self.console_win.winfo_exists():
            self._console_window()

    def _console_window(self):
        x = self.parent.winfo_x()
        y = self.parent.winfo_y()

        # create an instance of toplevel window
        self.console_win = Toplevel(self.parent)
        self.console_win.transient(self.parent)
        self.console_win.title("Console")
        self.console_win.configure(background="White")

        self.console_win.geometry('+{}+{}'.format(x+10, y+310))
        self.console_win.minsize(880,430)
        self.console_win.maxsize(880,430)
        # disable the resizing of window's width and heigh
        self.console_win.resizable(False, False)
        # remove the tkinter logo
        self.console_win.iconbitmap(default='../../Icon/transparent.ico')

        # add the scrolled console
        self.scrolled_console()

    def scrolled_console(self):
        st = scrolledtext.ScrolledText(self.console_win, width=108, height=27, wrap=WORD)
        st.configure(state=DISABLED)
        st.place(x=0, y=0)

    # whenever the position of main window has changed, the toplevel console window follows it
    def follow_me_console_window(self, event):
        try:
            if self.console_win is not None:
                x = self.parent.winfo_x()
                y = self.parent.winfo_y()
                self.console_win.geometry('+{}+{}'.format(x+10, y+310))
        except: # to avoid getting error when closing the toplevel window
            pass


def main():
    root = tk.Tk()
    ConsoleWindow(root)
    root.mainloop()


if __name__=='__main__':
    main()