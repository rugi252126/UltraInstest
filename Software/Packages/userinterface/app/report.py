# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
import os
import tkinter as tk
from tkinter import ttk
from userinterface.gui.subwindow import PopUpWindow


class Report(PopUpWindow):
    def __init__(self, parent):
        super().__init__(parent)

    def on_generate_report(self):
        print("on_generate_report")
        super().popup_window("Report Generation", 300, 200)

        print("Report")
        ivar = super().get_ivar()
        print(super().get_ivar())

        number = tk.StringVar()
        number_chosen = ttk.Combobox(ivar, width=12, textvariable=number)
        number_chosen['values'] = (1, 2, 3, 42, 100)
        number_chosen.grid(column=1, row=1)
        number_chosen.current(4)

        print(number_chosen.get())

    def report_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Report")
        mb_ivar.add_new_command('Generate Test Report', self.on_generate_report)