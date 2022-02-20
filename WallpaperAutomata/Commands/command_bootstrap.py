"""
Command
"""

import argparse
from email.mime import image
from pathlib import Path
from sys import argv
from typing import Dict
from WallpaperAutomata.Wallpapper.config_local_data import ConfigLocalData

from WallpaperAutomata.settings import COMMAND_DESCRIPTION, COMMANDS


class CommandBootstrap:

    def __init__(self) -> None:
        config = ConfigLocalData.create()
        self._config_dir = config.dir
        self._config_file = config.config_file
        self._data = config.data
        self._commands: Dict = COMMANDS
        self._args: Dict = {}

        try:
            self._entry_point = argv[1]

            if self._entry_point == '--help' or self._entry_point == '-h':
                self._show_help()
                exit(0)

        except IndexError:
            self._show_help()
            exit()

        self._boot()

    @staticmethod
    def create():
        return CommandBootstrap()

    def _boot(self):
        """
            Execute all process
        """
        self._parser: argparse.ArgumentParser = argparse.ArgumentParser(
            description=COMMAND_DESCRIPTION
        )

        if self._entry_point in self._commands.keys():
            command = self._commands[self._entry_point]

            self._parser.add_argument(
                self._entry_point, help=command.description()
            )

            if len(command.arguments()) > 0:
                for argument in command.arguments():
                    self._parser.add_argument(
                        *argument['args'], **argument['kwargs']
                    )

            args = self._parser.parse_args()

            args.query = (args.query
                          if args.query
                          else self._data['vendors'][self._entry_point]['query'])

            args = vars(args)

            command.exec(
                self._data['vendors'][self._entry_point]['token'],
                args,
                self._data
            )

        else:
            print(
                f'Argument {self._entry_point} doesn\'t exist in commands.\n'
            )
            self._show_help()

    def _show_help(self):
        """
         Print help
        """
        for name, command in self._commands.items():
            print(f'{name}: {command.description()}')
