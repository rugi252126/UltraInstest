# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages

class Help:
    def __init__(self, parent):
        pass

    def on_about(self):
        print("on_about")

    def on_contact_support(self):
        print("on_contact_support")

    def on_check_updates(self):
        print("on_check_updates")

    def on_documentation(self):
        print("on_documentation")

    def help_menu(self, mb_ivar):
        mb_ivar.create_new_menu("Help")
        mb_ivar.add_new_command('About', self.on_about)
        mb_ivar.add_new_command('Contact Support', self.on_contact_support)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Check for Updates', self.on_check_updates)
        mb_ivar.add_command_separator()
        mb_ivar.add_new_command('Documentation', self.on_documentation)