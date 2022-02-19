"""
Command
"""

import argparse
from sys import argv
from typing import Dict
from WallpaperAutomata.Wallpapper.config_local_data import ConfigLocalData
from WallpaperAutomata.Wallpapper.paper import Paper
from WallpaperAutomata.Wallpapper.save_image import SaveImage

from WallpaperAutomata.settings import COMMAND_DESCRIPTION, COMMANDS


class CommandBootstrap:

    def __init__(self) -> None:
        config = ConfigLocalData.create()
        self._configDir = config.dir
        self._configFile = config.configFile
        self._data = config.data
        self._commands: Dict = COMMANDS
        self._args: Dict = {}
        self._entry_point = argv[1]
        self._boot()

    @staticmethod
    def create():
        return CommandBootstrap()

    def _boot(self):
        self._parser: object = argparse.ArgumentParser(
            description=COMMAND_DESCRIPTION
        )

        if self._entry_point in self._commands.keys():
            command = self._commands[self._entry_point]

            self._parser.add_argument(
                self._entry_point, help=command.description()
            )

            if len(command.arguments()) > 0:
                for argument in command.arguments():
                    self._parser.add_argument(**argument)

            photo = command.exec(
                self._data['vendors'][self._entry_point]['token'],
                self._parser.parse_args()
            )

            image_path = (
                SaveImage
                .create(self._data['config']['store'])
                .save(photo['url'])
            )

            Paper.create(image_path)

        else:
            print(f'Argument {self._entry_point} doesn\'t exist in commands.')
            for name, command in self._commands:
                print(f'{name}: {command.description()}')
