# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk

# add file information
__version__ ='0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class CommunicationInterface:
    def __init__(self, parent, *args, **kwargs):
        pass

    def onComSettings(self):
        print("onComSettings")

    def onComConnect(self):
        print("onComConnect")

    def onComDisconnect(self):
        print("onComDisconnect")

    def onComStart(self):
        print("onComStart")

    def onComStop(self):
        print("onComStop")

    def com_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Communication")
        mb_ivar.add_new_command('Settings...', self.onComSettings)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Connect', self.onComConnect)
        mb_ivar.add_new_command('Disconnect', self.onComDisconnect)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Start', self.onComStart)
        mb_ivar.add_new_command('Stop', self.onComStop)