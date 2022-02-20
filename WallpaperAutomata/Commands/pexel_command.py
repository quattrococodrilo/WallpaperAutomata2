"""
    Pexels command
"""

from pathlib import Path
from random import choice
from typing import Dict, List

from WallpaperAutomata.Vendors.pexels_vendor import PexelsVendor
from WallpaperAutomata.Wallpapper.paper import Paper
from WallpaperAutomata.Wallpapper.save_image import SaveImage

from .command_interface import CommandInterface


class PexelsCommand(CommandInterface):

    _description = 'Get photos from Pexels'

    _arguments = [
        {
            'args': ['-q', '--query'],
            'kwargs': {
                'action': 'store',
                'help': 'Query search.'
            }
        }
    ]

    @classmethod
    def description(cls) -> str:
        return cls._description

    @classmethod
    def arguments(cls) -> List[Dict]:
        return cls._arguments

    @classmethod
    def exec(cls, token: str, args: Dict, data_local_config) -> None:

        pexels = PexelsVendor.create(token, args['query'])

        photos = pexels.photos()

        photo = choice(photos)

        store_path = (Path(data_local_config['config']['store'])
                      / f'{photo["id"]}.{photo["ext"]}')

        image_path = SaveImage.save(store_path, photo['url'])

        Paper.create(image_path)
