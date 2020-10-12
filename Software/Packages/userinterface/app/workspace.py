# Code compatibility
from __future__ import absolute_import
from __future__ import print_function


class Workspace:
    def __init__(self, parent):
        pass

    def on_new_workspace(self):
        print("on_new_workspace")

    def on_open_workspace(self):
        print("on_open_workspace")

    def on_save_workspace(self):
        print("on_save_workspace")

    def on_saveas_workspace(self):
        print("on_saveas_workspace")

    def workspace_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Workspace")
        mb_ivar.add_new_command('New', self.on_new_workspace)
        mb_ivar.add_new_command('Open...', self.on_open_workspace)
        mb_ivar.add_new_command('Save', self.on_save_workspace)
        mb_ivar.add_new_command('Save As...', self.on_saveas_workspace)