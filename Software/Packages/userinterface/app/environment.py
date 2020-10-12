# Code compatibility
from __future__ import absolute_import
from __future__ import print_function


class TestEnvironment:
    def __init__(self, parent):
        pass

    def on_env_config(self):
        print("on_env_config")

    def environment_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Environment")
        mb_ivar.add_new_command('Configuration...', self.on_env_config)