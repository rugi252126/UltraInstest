# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import messagebox as msg
import tkinter.font as font
from SubWindow import ConsoleWindow
from MenuBar import MenuBar
from UserInterface.App.Workspace import Workspace
from UserInterface.App.Test import Test
from UserInterface.App.ComIf import CommunicationInterface
from UserInterface.App.Project import Project
from UserInterface.App.Environment import TestEnvironment
from UserInterface.App.Report import Report
from UserInterface.App.Info import Help

# add file information
__version__ = '0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class MainWindow:
    def __init__(self, parent, *args, **kwargs):
        # create a copy of root instance
        self.parent = parent
        # set main window size
        self.win_width = 900
        self.win_height = 800

        # toplevel - console window
        cs = ConsoleWindow(self.parent)

        # instances
        menu_bar_ivar = MenuBar(parent)
        tst = Test(self.parent)
        ws = Workspace(self.parent)
        ci = CommunicationInterface(self.parent)
        prj = Project(self.parent)
        env = TestEnvironment(self.parent)
        rpt = Report(self.parent)
        info = Help(self.parent)

        # create the gui window
        self.main_window()
        self.file_menu(menu_bar_ivar)
        ws.workspace_menu(menu_bar_ivar)
        tst.test_menu(menu_bar_ivar)
        prj.project_menu(menu_bar_ivar)
        ci.com_menu(menu_bar_ivar)
        env.environment_menu(menu_bar_ivar)
        rpt.report_menu(menu_bar_ivar)
        info.help_menu(menu_bar_ivar)
        self.exit_button()

    def main_window(self):
        # add title
        self.parent.title("   UltraInstest")
        # add background color
        self.parent.configure(background="White")
        # disable resizing of window's width and height
        self.parent.resizable(False, False)
        # change the default window's logo and add our logo
        photo = PhotoImage(file='../../Icon/ultrainstest_logo.png')
        self.parent.iconphoto(False, photo)

        # add background image
        background_image = PhotoImage(file='../../Icon/background.png')
        background_label = tk.Label(self.parent, image=background_image)
        # keep the reference of the image otherwise
        # it will destroy by garbage collector
        background_label.photo = background_image
        background_label.pack()

        # get the screen width and height
        screen_w = self.parent.winfo_screenwidth()
        screen_h = self.parent.winfo_screenheight()
        # calculates the x and y coordinate
        s_x = (screen_w / 2) - (self.win_width / 2)
        s_y = (screen_h / 2) - (self.win_height / 2)
        # set the dimensions of the screen and the position
        self.parent.geometry('%dx%d+%d+%d' % (self.win_width, self.win_height, s_x, s_y))

    def onExit(self):
        # pop-up message box
        ans = msg.askyesnocancel("", "Are you sure you want to exit?")
        if ans:
            # exit the gui cleanly
            self.parent.quit()
            self.parent.destroy()
            exit()

    def exit_button(self):
        b_h = 1
        b_w = 11
        w_h_offset = 70
        b_font = font.Font(family='Helvetica', size=15)
        b_exit = Button(self.parent, text="Exit", command=self.onExit, font=b_font,
                        height=1, width=11, bg='Orange', fg='Black')
        b_exit.place(x=((self.win_width // 2) - 220), y=self.win_height - 70)

    def file_menu(self, mb_ivar):
        mb_ivar.create_new_menu("File")
        mb_ivar.add_new_command('Open...')
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Exit', self.onExit)


def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__=='__main__':
    main()
