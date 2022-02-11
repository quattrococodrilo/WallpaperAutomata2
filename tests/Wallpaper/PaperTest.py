import unittest
from pathlib import Path
from random import choice

from WallpaperAutomata.Vendors.Pexels import Pexels
from WallpaperAutomata.Wallpapper.Config import Config
from WallpaperAutomata.Wallpapper.Paper import Paper
from WallpaperAutomata.Wallpapper.SaveImage import SaveImage


class SaveImageTest(unittest.TestCase):

    def test_save_image(self):

        filePath = (Path(__file__)
                    .parent
                    .parent
                    .parent
                    .joinpath('data/config.yml'))

        config = Config.create(filePath).data

        pexelsData = config['vendors']['Pexels']

        pexels = Pexels.create(pexelsData['token'], pexelsData['query'])

        photos = pexels.photos()

        photo = choice(photos)

        photo_name = photo['url'].split('/')[-1]

        store_path = (Path(config['config']['store'])
                      .joinpath(photo_name))

        savei = SaveImage.create(store_path)
        image = savei.save(photo['url'])
        print(image)

        Paper.create(image)
