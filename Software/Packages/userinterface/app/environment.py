# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
import tkinter as tk
from userinterface.gui.subwindow import PopUpWindow
from utilities.excel import Excel

POPUP_WIN_WIDTH = 200
POPUP_WIN_HEIGHT = 130


class TestEnvironment(PopUpWindow, Excel):
    def __init__(self, parent):
        # initialize the parent class
        PopUpWindow.__init__(self,parent)
        Excel.__init__(self)
        self.oscilloscope = tk.IntVar()
        self.logic_analyzer = tk.IntVar()
        self.power_supply = tk.IntVar()
        self.debugger = tk.IntVar()
        self.test_env_win_status = False
        #print(TestEnvironment.__mro__)

    def on_closing_test_env_window(self):
        # clear the flag as popup window is destroyed
        self.test_env_win_status = False
        ivar = PopUpWindow.get_popup_win_ivar(self)
        ivar.destroy()

    def on_oscilloscope(self):
        pass

    def on_env_config(self):
        # create a popup window if it is not yet created
        if not self.test_env_win_status:
            self.test_env_win_status = True

            # create a new window
            PopUpWindow.popup_window(self, "Test Environment", POPUP_WIN_WIDTH, POPUP_WIN_HEIGHT)
            # get the instance of the newly created window
            ivar = PopUpWindow.get_popup_win_ivar(self)
            # set the window's background color
            ivar.configure(background="skyblue")
            # make access to excel file
            #Excel.load_file(self)
            # read specific sheet from excel file
            #Excel.read_sheet(self, "TEST_CONFIG")

            # add label
            tk.Label(ivar, text="Select Tools: ", width=14, bg='skyblue',
                     font=('Times New Roman', 11, 'bold'),anchor="w").grid(row=0, sticky=tk.W)
            # add checkbutton widget
            tk.Checkbutton(ivar, text="Oscilloscope", variable=self.oscilloscope, bg='skyblue', onvalue=1,
                        offvalue=0, command=self.on_oscilloscope).grid(row=1, sticky=tk.W)
            tk.Checkbutton(ivar, text="Logic Analyzer", variable=self.logic_analyzer, bg='skyblue', onvalue=1,
                        offvalue=0).grid(row=2, sticky=tk.W)
            tk.Checkbutton(ivar, text="Power Supply", variable=self.power_supply, bg='skyblue', onvalue=1,
                        offvalue=0).grid(row=3, sticky=tk.W)
            tk.Checkbutton(ivar, text="Debugger", variable=self.debugger, bg='skyblue', onvalue=1,
                        offvalue=0).grid(row=4, sticky=tk.W)

            # do a proper exit of a popup window
            ivar.protocol("WM_DELETE_WINDOW", self.on_closing_test_env_window)

    def get_oscilloscope_status(self):
        return self.oscilloscope.get()

    def get_logic_analyzer_status(self):
        return self.logic_analyzer.get()

    def get_power_supply_status(self):
        return self.power_supply.get()

    def get_debugger_status(self):
        return self.debugger.get()

    def environment_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Environment")
        mb_ivar.add_new_command('Configuration...', self.on_env_config)