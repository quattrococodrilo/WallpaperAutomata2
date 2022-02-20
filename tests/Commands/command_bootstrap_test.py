import unittest

from WallpaperAutomata.Commands.command_bootstrap import CommandBootstrap


class CommandBootstrapTest(unittest.TestCase):

    def test_command(self):
        CommandBootstrap.create()
