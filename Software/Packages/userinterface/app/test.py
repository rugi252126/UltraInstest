# Code compatibility
from __future__ import absolute_import
from __future__ import print_function


class Test:
    def __init__(self, parent):
        pass

    def on_test_settings(self):
        print("on_test_settings")

    def on_test_load(self):
        print("on_test_load")

    def on_test_update(self):
        print("on_test_update")

    def on_test_start(self):
        print("on_test_start")

    def on_test_stop(self):
        print("on_test_stop")

    def on_test_resume(self):
        print("on_test_resume")

    def test_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Test")
        mb_ivar.add_new_command('Settings', self.on_test_settings)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Load...', self.on_test_load)
        mb_ivar.add_new_command('Update...', self.on_test_update)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Start', self.on_test_start)
        mb_ivar.add_new_command('Stop', self.on_test_stop)
        mb_ivar.add_new_command('Resume', self.on_test_resume)
