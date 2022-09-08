# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import Command


class setwall(Command):
    """:setwall [opts]

    Set wallpaper with `wallmenu` script.
    """

    def execute(self):
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            opts = self.rest(1)
        else:
            opts = ''
        self.fm.execute_console(f'shell wallmenu {opts} %s')


class dotadd(Command):
    """:dotadd

    Add or remove dotfiles.
    """

    def execute(self):
        self.fm.execute_console('shell dotctl add %s')


class dotrm(Command):
    """:dotrm

    Add or remove dotfiles.
    """

    def execute(self):
        self.fm.execute_console('shell dotctl remove %s')


class trash(Command):
    """:trash

    Put selected files in the trash can.
    """

    def execute(self):
        self.fm.execute_console("shell echo %s | xargs trash-put")


class trashcut(Command):
    """:trashcut

    Put cut files in the trash can.
    """

    def execute(self):
        self.fm.execute_console('shell echo %c | xargs trash-put')


class deletecut(Command):
    """:trashcut

    Put cut files in the trash can.
    """

    def execute(self):
        self.fm.execute_console('shell echo %c | xargs rm')


class trashempty(Command):
    """:trashempty

    Empty trash can.
    """

    def execute(self):
        self.fm.execute_console('shell trash-empty')


class trashrestore(Command):
    """:trashrestore

    Restore files in trash can.
    """

    def execute(self):
        self.fm.execute_console('shell trash-restore')
