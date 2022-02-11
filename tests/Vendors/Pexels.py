import unittest
from pathlib import Path

from WallpaperAutomata.Vendors.Pexels import Pexels
from WallpaperAutomata.Wallpapper.Config import Config


class TestPexels(unittest.TestCase):

    def test_pexel_api(self):
        filePath = (Path(__file__)
                    .parent
                    .parent
                    .parent
                    .joinpath('data/config.yml'))

        config = Config.create(filePath)

        dataPexels = config.data['vendors']['Pexels']

        pexels = Pexels.create(dataPexels['token'], dataPexels['query'])

        photos = pexels.photos()

        self.assertEqual(len(photos), 50)
