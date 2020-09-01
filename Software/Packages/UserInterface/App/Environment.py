# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import packages
import tkinter as tk

# add file information
__version__ ='0.0.1'
__author__ = 'Rudy Manalo Alfonso'


class TestEnvironment:
    def __init__(self, parent, *args, **kwargs):
        pass

    def onEnvConfig(self):
        print("onEnvConfig")

    def environment_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Environment")
        mb_ivar.add_new_command('Configuration...', self.onEnvConfig)