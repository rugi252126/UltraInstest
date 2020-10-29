# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
import tkinter as tk
from tkinter import scrolledtext


class ConsoleWindow:
    def __init__(self, parent, win_w, win_h):
        self.parent = parent
        self.win_width = win_w
        self.win_height = win_h
        self.scrolled_text = None
        self.parent.bind("<Configure>", self.follow_me_console_window)

        # create the console window
        self.console_window()

    def show_console_window(self):
        # show console window if it is not yet displayed or created
        if 0 == self.console_win.winfo_exists():
            self.console_window()

    def console_window(self):
        x = self.parent.winfo_x()
        y = self.parent.winfo_y()

        # create an instance of toplevel window
        self.console_win = tk.Toplevel(self.parent)
        self.console_win.transient(self.parent)
        self.console_win.title("Console")
        self.console_win.configure(background="White")

        self.console_win.geometry('+{}+{}'.format(x+5, y+250))
        self.console_win.minsize(self.win_width-10,self.win_height//2)
        self.console_win.maxsize(self.win_width-10,self.win_height//2)
        # disable the resizing of window's width and height
        self.console_win.resizable(False, False)
        # remove the tkinter logo
        self.console_win.iconbitmap(default='../../Icon/transparent.ico')

        # add scrolled text
        self.scrolled_console()

    def scrolled_console(self):
        self.scrolled_text = scrolledtext.ScrolledText(self.console_win, width=87, height=18, wrap=tk.WORD,
                                                       bg='lightblue', font=("Times New Roman", 11))
        #self.scrolled_text.configure(state=DISABLED)
        self.scrolled_text.place(x=0, y=0)

    def add_console_info(self, text=""):
        # make sure window exists
        if self.console_win.winfo_exists():
            self.scrolled_text.insert(tk.INSERT, text + "\n")
            #self.scrolled_text.insert(END, "")

    # whenever the position of main window has changed, the toplevel console window follows it
    def follow_me_console_window(self, event):
        try:
            if self.console_win is not None:
                x = self.parent.winfo_x()
                y = self.parent.winfo_y()
                self.console_win.geometry('+{}+{}'.format(x+5, y+250))
        except: # to avoid getting error when closing the toplevel window
            pass


class PopUpWindow:
    def __init__(self, parent):
        self.__parent = parent
        self.__popup_win = None

    def popup_window(self, str_win_name, w=900, h=900):
        # create an instance of toplevel window
        self.__popup_win = tk.Toplevel(self.__parent)
        self.__popup_win.transient(self.__parent)
        self.__popup_win.title(str_win_name)

        self.__popup_win.geometry('+{}+{}'.format(0, 0))
        self.__popup_win.minsize(w, h)
        self.__popup_win.maxsize(w, h)
        # disable the resizing of window's width and height
        self.__popup_win.resizable(False, False)
        # add window's logo
        photo = tk.PhotoImage(file='../../Icon/ultrainstest_logo.png')
        self.__popup_win.iconphoto(False, photo)

    def get_popup_win_ivar(self):
        return self.__popup_win


def main():
    root = tk.Tk()
    ConsoleWindow(root)
    root.mainloop()


if __name__=='__main__':
    main()