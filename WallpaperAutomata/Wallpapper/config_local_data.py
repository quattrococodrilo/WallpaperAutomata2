"""
    Get config from config file.
"""

from pathlib import Path
from platform import system
from typing import Dict

from WallpaperAutomata.settings import CONFIG_DATA, CONFIG_FILE_NAME, CONFIG_PATH
from yaml import Dumper, Loader, dump, load


class ConfigLocalData:

    _data: Dict = {}

    def __init__(self) -> None:

        self._data = CONFIG_DATA.copy()

        if system() == 'Linux':
            self._dir: Path = Path.home() / CONFIG_PATH['Linux']
            self._configFile = Path(self._dir) / CONFIG_FILE_NAME

        self._mkdir()
        self._setConfigFile()
        self._extractData()

    @staticmethod
    def create():
        return ConfigLocalData()

    @property
    def data(self) -> dict:
        return self._data

    @property
    def dir(self) -> Path:
        return self._dir

    @property
    def configFile(self) -> Path:
        return self._configFile

    @staticmethod
    def create() -> object:
        """Create a instance of Config.

        Args:
            filePath (string): Path to file in yml.

        Returns:
            Object: instance of Config
        """

        return ConfigLocalData()

    def _extractData(self) -> None:
        """
            Get data from config file yml.
        """

        self._data = load(self._configFile.read_text(), Loader=Loader)

    def _mkdir(self):
        if not self._dir.exists():
            self._dir.mkdir(parents=True)

    def _setConfigFile(self):
        if not self._configFile.exists():
            self._data['config']['store'] = input('Set store directory: ')
            self._data['vendors']['pexels']['token'] = input(
                'Set Pexels token: '
            )
            dump(self._data, self._configFile.open(
                'w'), Dumper=Dumper, allow_unicode=True)
