# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk

# add file information
__version__ ='0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class Help:
    def __init__(self, parent, *args, **kwargs):
        pass

    def onAbout(self):
        print("onAbout")

    def onContactSupport(self):
        print("onContactSupport")

    def onCheckUpdates(self):
        print("onCheckUpdates")

    def onDocumentation(self):
        print("onDocumentation")

    def help_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Help")
        mb_ivar.add_new_command('About', self.onAbout)
        mb_ivar.add_new_command('Contact Support', self.onContactSupport)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Check for Updates', self.onCheckUpdates)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Documentation', self.onDocumentation)