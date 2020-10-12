# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
import tkinter as tk
from tkinter import ttk
from userinterface.gui.subwindow import PopUpWindow
import openpyxl


class Project(PopUpWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.variant = "NA"
        self.carline = "NA"
        self.position = "NA"
        self.ccb_variant = None
        self.ccb_carline = None
        self.ccb_position = None
        self.ccb_variant_idx = 0
        self.ccb_carline_idx = 0
        self.ccb_position_idx = 0
        self.popup_win_status = False

    def on_variant(self, event):
        # get and assign the selected value
        self.variant = self.ccb_variant.get()
        # get and assign the corresponding index
        self.ccb_variant_idx = self.ccb_variant.current()

    def on_carline(self, event):
        # get and assign the selected value
        self.carline = self.ccb_carline.get()
        # get and assign the corresponding index
        self.ccb_carline_idx = self.ccb_carline.current()

    def on_position(self, event):
        # get and assign the selected value
        self.position = self.ccb_position.get()
        # get and assign the corresponding index
        self.ccb_position_idx = self.ccb_position.current()

    def on_closing_window(self):
        # clear the flag as popup window is destroyed
        self.popup_win_status = False
        ivar = super().get_ivar()
        ivar.destroy()

    def get_cell_Value(self, actv_sheet, col_name="A"):
        # take individual value from cells
        a = []
        # excluding the first row(header)
        for row in range(2, actv_sheet.max_row + 1):
            # specify the column coverage
            for column in col_name:
                cell_name = "{}{}".format(column, row)
                if actv_sheet[cell_name].value is not None:
                    a.append(actv_sheet[cell_name].value)

        return a

    def on_project_settings(self):
        # create a popup window if it is not yet created
        if not self.popup_win_status:
            self.popup_win_status = True

            # create a new window
            super().popup_window("Project Settings", 260, 90)
            # get the instance of the newly created window
            ivar = super().get_ivar()
            # set the window's background color
            ivar.configure(background="skyblue")
            # make access to excel file
            xls = openpyxl.load_workbook('../../Resources/Project_Information.xlsx', data_only=True)
            # read specific sheet from excel file
            ps = xls["PROJECT_CONFIG"]

            # add label for project variant information
            lbl_var = tk.Label(ivar, text="Project Variant: ", width=14, bg = 'skyblue', font=('Arial', 12), anchor="e")
            lbl_var.grid(column=0, row=0)
            # add combobox for project variant options
            self.ccb_variant = ttk.Combobox(ivar, width=14, state='readonly')
            # assign the values to combobox
            self.ccb_variant['values'] = self.get_cell_Value(ps, "A")
            self.ccb_variant.grid(column=1, row=0)
            # set the current position/value of the combobox
            self.ccb_variant.current(self.ccb_variant_idx)
            # bind the calback function
            # this will be called everytime the value is changed
            self.ccb_variant.bind("<<ComboboxSelected>>", self.on_variant)

            # add label for carline information
            lbl_carline = tk.Label(ivar, text="Carline: ", width=14, bg = 'skyblue', font=('Arial', 12), anchor="e")
            lbl_carline.grid(column=0, row=1)
            # add combobox for project variant options
            self.ccb_carline = ttk.Combobox(ivar, width=14, state='readonly')
            # assign the values to combobox
            self.ccb_carline['values'] = self.get_cell_Value(ps, "B")
            self.ccb_carline.grid(column=1, row=1)
            # set the current position/value of the combobox
            self.ccb_carline.current(self.ccb_carline_idx)
            # bind the calback function
            # this will be called everytime the value is changed
            self.ccb_carline.bind("<<ComboboxSelected>>", self.on_carline)

            # add label for position information
            lbl_pos = tk.Label(ivar, text="Position: ", width=14, bg = 'skyblue', font=('Arial', 12), anchor="e")
            lbl_pos.grid(column=0, row=2)
            # add combobox for project variant options
            self.ccb_position = ttk.Combobox(ivar, width=14, state='readonly')
            # assign the values to combobox
            self.ccb_position['values'] = self.get_cell_Value(ps, "C")
            self.ccb_position.grid(column=1, row=2)
            # set the current position/value of the combobox
            self.ccb_position.current(self.ccb_position_idx)
            # bind the calback function
            # this will be called everytime the value is changed
            self.ccb_position.bind("<<ComboboxSelected>>", self.on_position)

            # do a proper exit of a popup window
            ivar.protocol("WM_DELETE_WINDOW", self.on_closing_window)

    def get_variant(self):
        return self.variant

    def get_carline(self):
        return self.carline

    def get_position(self):
        return self.position

    def project_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Project")
        mb_ivar.add_new_command('Settings...', self.on_project_settings)

