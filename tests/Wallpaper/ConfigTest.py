"""
    Test for Config module.
"""

from pathlib import Path
import unittest
from WallpaperAutomata.Wallpapper import ConfigLocalData


class TestConfig(unittest.TestCase):

    def test_data(self):
        """ Test that extracts data from configuration file. """

        ConfigLocalData.create()
