# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk

# add file information
__version__ ='0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class Report:
    def __init__(self, parent, *args, **kwargs):
        pass

    def onGenerateReport(self):
        print("onGenerateReport")

    def report_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Report")
        mb_ivar.add_new_command('Generate Test Report', self.onGenerateReport)