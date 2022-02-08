"""
    Get config from config file.
"""

from pathlib import Path

from yaml import load, Loader


class Config:

    _data = {}

    def __init__(self, filePath) -> None:
        self.filePath = Path(filePath)
        self._extractData()

    @staticmethod
    def create(filePath):
        """Create a instance of Config.

        Args:
            filePath (string): Path to file in yml.

        Returns:
            Object: instance of Config
        """

        return Config(filePath)

    def _extractData(self) -> None:
        """
            Get data from config file yml.
        """

        self._data = load(self.filePath.read_text(), Loader=Loader)

    @property
    def data(self):
        return self._data
