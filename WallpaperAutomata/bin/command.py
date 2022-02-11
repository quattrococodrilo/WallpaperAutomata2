from pathlib import Path
from random import choice

from WallpaperAutomata.Vendors.Pexels import Pexels
from WallpaperAutomata.Wallpapper.Config import Config
from WallpaperAutomata.Wallpapper.Paper import Paper
from WallpaperAutomata.Wallpapper.SaveImage import SaveImage


class Command:

    def __init__(self, query, config_file_path) -> None:
        self._query = query
        self._config_file_path = config_file_path

    @staticmethod
    def create(query, config_file_path):
        return Command(query, config_file_path)

    def exec(self):
        # TODO: crear directorio para archivo de configuración
        if self._config_file_path:
            file_config_path = self._config_file_path
        else:
            file_config_path = (Path(__file__)
                                .parent
                                .parent
                                .parent
                                .joinpath('data/config.yml'))

        config = Config.create(file_config_path).data

        pexelsData = config['vendors']['Pexels']

        pexels = Pexels.create(
            pexelsData['token'],
            self._query if self._query else pexelsData['query']
        )

        photos = pexels.photos()

        photo = choice(photos)

        photo_name = photo['url'].split('/')[-1]

        store_path = (Path(config['config']['store'])
                      .joinpath(photo_name))

        savei = SaveImage.create(store_path)
        image = savei.save(photo['url'])
        print(image)

        Paper.create(image)
