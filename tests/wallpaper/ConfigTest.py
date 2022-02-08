"""
    Test for Config module.
"""

from pathlib import Path
import unittest
from WallpaperAutomata.Wallpapper.Config import Config


class TestConfig(unittest.TestCase):

    def test_data(self):
        """ Test that extracts data from configuration file. """

        filePath = (Path(__file__)
                    .parent
                    .parent
                    .parent
                    .joinpath('data/config.yml'))

        config = Config.create(filePath)

        self.assertTrue('vendors' in config.data)
        self.assertTrue('config' in config.data)
