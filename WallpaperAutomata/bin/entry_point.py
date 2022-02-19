from sys import argv

from WallpaperAutomata.Commands.command_bootstrap import CommandBootstrap


def exec() -> None:
    CommandBootstrap.create()
