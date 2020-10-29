# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from userinterface.gui.subwindow import PopUpWindow
from utilities.excel import Excel

POPUP_WIN_WIDTH = 260
POPUP_WIN_HEIGHT = 70


class Test(PopUpWindow, Excel):
    def __init__(self, parent):
        # initialize parent class
        PopUpWindow.__init__(self,parent)
        Excel.__init__(self)
        self.test_type = "SMT"
        self.ccb_test_type = None
        self.ccb_test_type_idx = 0
        self.test_cfg_win_status = False
        #print(Test.__mro__)

    def on_closing_test_cfg_window(self):
        # clear the flag as popup window is destroyed
        self.test_cfg_win_status = False
        ivar = PopUpWindow.get_popup_win_ivar(self)
        ivar.destroy()

    def on_cancel_test_bttn(self):
        ans = msg.askyesno("", "Discard changes?")
        if ans:
            self.on_closing_test_cfg_window()

    def on_accept_test_bttn(self):
        # get and assign the selected value
        self.test_type = self.ccb_test_type.get()
        # get and assign the corresponding index
        self.ccb_test_type_idx = self.ccb_test_type.current()

    def on_test_settings(self):
        # create a popup window if it is not yet created
        if not self.test_cfg_win_status:
            self.test_cfg_win_status = True

            # create a new window
            PopUpWindow.popup_window(self, "Test Configuration", POPUP_WIN_WIDTH, POPUP_WIN_HEIGHT)
            # get the instance of the newly created window
            ivar = PopUpWindow.get_popup_win_ivar(self)
            # create buttons
            self.cancel_test_bttn(ivar)
            self.accept_test_bttn(ivar)
            # set the window's background color
            ivar.configure(background="skyblue")
            # make access to excel file
            Excel.load_file(self)
            # read specific sheet from excel file
            Excel.read_sheet(self, "TEST_CONFIG")

            # add label for test type information
            lbl_var = tk.Label(ivar, text="Type of Test: ", width=14, bg='skyblue', font=('Arial', 12), anchor="e")
            lbl_var.grid(column=0, row=0)
            # add combobox for test type options
            self.ccb_test_type = ttk.Combobox(ivar, width=14, state='readonly')
            # assign the values to combobox
            self.ccb_test_type['values'] = Excel.get_cell_value(self)
            self.ccb_test_type.grid(column=1, row=0)
            # set the current position/value of the combobox
            self.ccb_test_type.current(self.ccb_test_type_idx)

            # do a proper exit of a popup window
            ivar.protocol("WM_DELETE_WINDOW", self.on_closing_test_cfg_window)

    def cancel_test_bttn(self, ivar):
        b_cancel = tk.Button(ivar, text="Cancel", command=self.on_cancel_test_bttn, font=('Arial', 10, 'normal'),
                          height=1, width=7, fg='Black')
        b_cancel.place(x=(POPUP_WIN_WIDTH // 2), y=POPUP_WIN_HEIGHT - 30)

    def accept_test_bttn(self, ivar):
        b_accept = tk.Button(ivar, text="Accept", command=self.on_accept_test_bttn, font=('Arial', 10, 'normal'),
                          height=1, width=7, fg='Black')
        b_accept.place(x=(POPUP_WIN_WIDTH // 2) - 60, y=POPUP_WIN_HEIGHT - 30)

    def get_test_type(self):
        return self.test_type

    def on_test_load(self):
        print("on_test_load")

    def on_test_update(self):
        print("on_test_update")

    def on_test_start(self):
        print("on_test_start")

    def on_test_stop(self):
        print("on_test_stop")

    def on_test_resume(self):
        print("on_test_resume")

    def test_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Test")
        mb_ivar.add_new_command('Settings', self.on_test_settings)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Load...', self.on_test_load)
        mb_ivar.add_new_command('Update...', self.on_test_update)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Start', self.on_test_start)
        mb_ivar.add_new_command('Stop', self.on_test_stop)
        mb_ivar.add_new_command('Resume', self.on_test_resume)
