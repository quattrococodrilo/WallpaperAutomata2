import unittest
from pathlib import Path

from WallpaperAutomata.Vendors import Pexels
from WallpaperAutomata.Vendors.vendor_interface import VendorInterface
from WallpaperAutomata.Wallpapper import ConfigLocalData


class TestPexels(unittest.TestCase):

    def test_correct_implementation_of_vendor_interface(self):
        self.assertTrue(issubclass(Pexels, VendorInterface))

    def test_pexel_api(self):
        filePath = (Path(__file__)
                    .parent
                    .parent
                    .parent
                    .joinpath('data/config.yml'))

        config = ConfigLocalData.create(filePath)

        dataPexels = config.data['vendors']['Pexels']

        pexels = Pexels.create(dataPexels['token'], dataPexels['query'])

        photos = pexels.photos()

        self.assertEqual(len(photos), 50)
