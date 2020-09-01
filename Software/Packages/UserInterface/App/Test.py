# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk

# add file information
__version__ ='0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class Test:
    def __init__(self, parent, *args, **kwargs):
        pass

    def onTestSettings(self):
        print("onTestSettings")

    def onTestLoad(self):
        print("onTestLoad")

    def onTestUpdate(self):
        print("onTestUpdate")

    def onTestStart(self):
        print("onTestStart")

    def onTestStop(self):
        print("onTestStop")

    def onTestResume(self):
        print("onTestResume")

    def test_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Test")
        mb_ivar.add_new_command('Settings', self.onTestSettings)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Load...', self.onTestLoad)
        mb_ivar.add_new_command('Update...', self.onTestUpdate)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Start', self.onTestStart)
        mb_ivar.add_new_command('Stop', self.onTestStop)
        mb_ivar.add_new_command('Resume', self.onTestResume)
