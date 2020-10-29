# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages


class Report:
    def __init__(self, parent):
        pass

    def on_generate_report(self):
        print("on_generate_report")

    def report_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Report")
        mb_ivar.add_new_command('Generate Test Report', self.on_generate_report)