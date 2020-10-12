# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox as msg
import tkinter.font as font
from userinterface.gui.subwindow import ConsoleWindow
from userinterface.gui.menubar import MenuBar
from userinterface.app.workspace import Workspace
from userinterface.app.test import Test
from userinterface.app.com_if import CommunicationInterface
from userinterface.app.project import Project
from userinterface.app.environment import TestEnvironment
from userinterface.app.report import Report
from userinterface.app.info import Help

# add file information
__version__ = '0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class MainWindow:
    def __init__(self, parent):
        # create a copy of root instance
        self.parent = parent
        # set main window size
        self.win_width = 650
        self.win_height = self.parent.winfo_screenheight() - 100
        # create gui main window
        self.main_window()

        # toplevel - console window
        self.cs = ConsoleWindow(self.parent, self.win_width, self.win_height)

        # instances
        menu_bar_ivar = MenuBar(parent)
        tst = Test(self.parent)
        ws = Workspace(self.parent)
        ci = CommunicationInterface(self.parent)
        self.prj = Project(self.parent)
        env = TestEnvironment(self.parent)
        rpt = Report(self.parent)
        info = Help(self.parent)

        # menu bars
        self.file_menu(menu_bar_ivar)
        self.view_menu(menu_bar_ivar)
        ws.workspace_menu(menu_bar_ivar)
        tst.test_menu(menu_bar_ivar)
        self.prj.project_menu(menu_bar_ivar)
        ci.com_menu(menu_bar_ivar)
        env.environment_menu(menu_bar_ivar)
        rpt.report_menu(menu_bar_ivar)
        info.help_menu(menu_bar_ivar)
        # buttons
        self.exit_button()
        self.start_button()
        self.stop_button()

    def main_window(self):
        # add title
        self.parent.title("   UltraInstest")
        # add background color
        self.parent.configure(background="skyblue")
        # disable resizing of window's width and height
        self.parent.resizable(False, False)

        # get the screen width and height
        screen_w = self.parent.winfo_screenwidth()
        screen_h = self.parent.winfo_screenheight()
        # calculates the x and y coordinate
        s_x = (screen_w // 2) - (self.win_width // 2)
        s_y = (screen_h // 2) - (self.win_height // 2)
        # set the dimensions of the screen and the position
        self.parent.geometry('%dx%d+%d+%d' % (self.win_width, self.win_height, s_x, s_y))

        # change the default window's logo and add our logo
        photo = PhotoImage(file='../../Icon/ultrainstest_logo.png')
        self.parent.iconphoto(False, photo)

        # add background image
        background_image = PhotoImage(file='../../Icon/background.png')
        background_label = Label(self.parent, image=background_image)
        # keep the reference of the image otherwise
        # it will destroy by garbage collector
        background_label.photo = background_image
        background_label.place(x=0, y=0)

    def on_exit(self):
        # pop-up message box
        ans = msg.askyesnocancel("", "Are you sure you want to exit?")
        if ans:
            # exit the gui cleanly
            self.parent.quit()
            self.parent.destroy()
            exit()

    def on_start(self):
        # pop-up message box
        ans = msg.askyesno("", "Start testing?")
        if ans:
            # start testing
            print(self.prj.get_variant())
            print(self.prj.get_carline())
            print(self.prj.get_position())
            self.cs.add_console_info("Hello World!")

    def on_stop(self):
        # pop-up message box
        ans = msg.askyesno("", "Stop testing?")
        if ans:
            # stop testing
            pass

    def on_console_window(self):
        self.cs.show_console_window()

    def exit_button(self):
        b_exit = Button(self.parent, text="Exit", command=self.on_exit, font=('Arial', 14, 'normal'),
                        height=1, width=10, fg='Black')
        b_exit.place(x=((self.win_width // 2) - 184), y=self.win_height - 70)

    def start_button(self):
        b_start = Button(self.parent, text="Start", command=self.on_start, font=('Arial', 14, 'normal'),
                        height=1, width=10, fg='Black')
        b_start.place(x=((self.win_width // 2) - 62), y=self.win_height - 70)

    def stop_button(self):
        b_start = Button(self.parent, text="Stop", command=self.on_stop, font=('Arial', 14, 'normal'),
                        height=1, width=10, fg='Black')
        b_start.place(x=((self.win_width // 2) + 60), y=self.win_height - 70)

    def file_menu(self, mb_ivar):
        mb_ivar.create_new_menu("File")
        mb_ivar.add_new_command('Open...')
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Exit', self.on_exit)

    def view_menu(self, mb_ivar):
        mb_ivar.create_new_menu("View")
        mb_ivar.add_new_command('Console Window', self.on_console_window)


def main():
    root = Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
