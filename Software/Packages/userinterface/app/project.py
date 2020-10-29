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
POPUP_WIN_HEIGHT = 110


class Project(PopUpWindow, Excel):
    def __init__(self, parent):
        # initialize the parent class
        PopUpWindow.__init__(self,parent)
        Excel.__init__(self)
        self.variant = "NA"
        self.carline = "NA"
        self.position = "NA"
        self.ccb_variant = None
        self.ccb_carline = None
        self.ccb_position = None
        self.ccb_variant_idx = 0
        self.ccb_carline_idx = 0
        self.ccb_position_idx = 0
        self.prj_cfg_win_status = False
        #print(Project.__mro__)

    def on_closing_prj_cfg_window(self):
        # clear the flag as popup window is destroyed
        self.prj_cfg_win_status = False
        ivar = PopUpWindow.get_popup_win_ivar(self)
        ivar.destroy()

    def on_cancel_prj_bttn(self):
        ans = msg.askyesno("", "Discard changes?")
        if ans:
            self.on_closing_prj_cfg_window()

    def on_accept_prj_bttn(self):
        # get and assign the selected value
        self.variant = self.ccb_variant.get()
        self.carline = self.ccb_carline.get()
        self.position = self.ccb_position.get()
        # get and assign the corresponding index
        self.ccb_variant_idx = self.ccb_variant.current()
        self.ccb_carline_idx = self.ccb_carline.current()
        self.ccb_position_idx = self.ccb_position.current()

    def on_project_settings(self):
        # create a popup window if it is not yet created
        if not self.prj_cfg_win_status:
            self.prj_cfg_win_status = True

            # create a new window
            PopUpWindow.popup_window(self, "Project Settings", POPUP_WIN_WIDTH, POPUP_WIN_HEIGHT)
            # get the instance of the newly created window
            ivar = PopUpWindow.get_popup_win_ivar(self)
            # create buttons
            self.cancel_prj_bttn(ivar)
            self.accept_prj_bttn(ivar)
            # set the window's background color
            ivar.configure(background="skyblue")
            # make access to excel file
            Excel.load_file(self)
            # read specific sheet from excel file
            Excel.read_sheet(self, "PROJECT_CONFIG")

            # add label for project variant information
            lbl_var = tk.Label(ivar, text="Project Variant: ", width=14, bg = 'skyblue', font=('Arial', 12), anchor="e")
            lbl_var.grid(column=0, row=0)
            # add combobox for project variant options
            self.ccb_variant = ttk.Combobox(ivar, width=14, state='readonly')
            # assign the values to combobox
            self.ccb_variant['values'] = Excel.get_cell_value(self)
            self.ccb_variant.grid(column=1, row=0)
            # set the current position/value of the combobox
            self.ccb_variant.current(self.ccb_variant_idx)
            # bind the calback function
            # this will be called everytime the value is changed
            # self.ccb_variant.bind("<<ComboboxSelected>>", self.on_variant)

            # add label for carline information
            lbl_carline = tk.Label(ivar, text="Carline: ", width=14, bg = 'skyblue', font=('Arial', 12), anchor="e")
            lbl_carline.grid(column=0, row=1)
            # add combobox for project variant options
            self.ccb_carline = ttk.Combobox(ivar, width=14, state='readonly')
            # assign the values to combobox
            self.ccb_carline['values'] = Excel.get_cell_value(self, "B")
            self.ccb_carline.grid(column=1, row=1)
            # set the current position/value of the combobox
            self.ccb_carline.current(self.ccb_carline_idx)

            # add label for position information
            lbl_pos = tk.Label(ivar, text="Position: ", width=14, bg = 'skyblue', font=('Arial', 12), anchor="e")
            lbl_pos.grid(column=0, row=2)
            # add combobox for project variant options
            self.ccb_position = ttk.Combobox(ivar, width=14, state='readonly')
            # assign the values to combobox
            self.ccb_position['values'] = Excel.get_cell_value(self, "C")
            self.ccb_position.grid(column=1, row=2)
            # set the current position/value of the combobox
            self.ccb_position.current(self.ccb_position_idx)

            # do a proper exit of a popup window
            ivar.protocol("WM_DELETE_WINDOW", self.on_closing_prj_cfg_window)

    def cancel_prj_bttn(self, ivar):
        b_cancel = tk.Button(ivar, text="Cancel", command=self.on_cancel_prj_bttn, font=('Arial', 10, 'normal'),
                          height=1, width=7, fg='Black')
        b_cancel.place(x=(POPUP_WIN_WIDTH//2), y=POPUP_WIN_HEIGHT-30)

    def accept_prj_bttn(self, ivar):
        b_accept = tk.Button(ivar, text="Accept", command=self.on_accept_prj_bttn, font=('Arial', 10, 'normal'),
                          height=1, width=7, fg='Black')
        b_accept.place(x=(POPUP_WIN_WIDTH//2) - 60, y=POPUP_WIN_HEIGHT-30)

    def get_variant(self):
        return self.variant

    def get_carline(self):
        return self.carline

    def get_position(self):
        return self.position

    def project_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Project")
        mb_ivar.add_new_command('Settings...', self.on_project_settings)

