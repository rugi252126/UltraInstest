# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

class CommunicationInterface:
    def __init__(self, parent):
        pass

    def on_com_settings(self):
        print("on_com_settings")

    def on_com_connect(self):
        print("on_com_connect")

    def on_com_disconnect(self):
        print("on_com_disconnect")

    def on_com_start(self):
        print("on_com_start")

    def on_com_stop(self):
        print("on_com_stop")

    def com_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Communication")
        mb_ivar.add_new_command('Settings...', self.on_com_settings)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Connect', self.on_com_connect)
        mb_ivar.add_new_command('Disconnect', self.on_com_disconnect)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Start', self.on_com_start)
        mb_ivar.add_new_command('Stop', self.on_com_stop)