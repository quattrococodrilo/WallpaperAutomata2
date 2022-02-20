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
            self._config_file = Path(self._dir) / CONFIG_FILE_NAME

        self._mkdir()
        self._set_config_file()
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
    def config_file(self) -> Path:
        return self._config_file

    def _extractData(self) -> None:
        """
            Get data from config file yml.
        """

        self._data = load(self._config_file.read_text(), Loader=Loader)

    def _mkdir(self):
        if not self._dir.exists():
            self._dir.mkdir(parents=True)

    def _set_config_file(self):
        if not self._config_file.exists():
            self._data['config']['store'] = input('Set store directory: ')
            self._data['vendors']['pexels']['token'] = input(
                'Set Pexels token: '
            )
            dump(self._data, self._config_file.open(
                'w'), Dumper=Dumper, allow_unicode=True)
