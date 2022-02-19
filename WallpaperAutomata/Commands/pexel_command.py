"""
    Pexels command
"""

from random import choice
from typing import Dict, List

from WallpaperAutomata.Vendors.pexels_vendor import PexelsVendor

from .command_interface import CommandInterface


class PexelsCommand(CommandInterface):

    _description = 'Get photos from Pexels'

    _arguments = [
        {
            'args': ['-s', '--search'],
            'kwargs': {
                'name': '--search',
                'short_name': '-s',
                'default': '',
                'action': 'store',
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
    def exec(cls, token: str, args: Dict) -> Dict[str, str]:

        pexels = PexelsVendor.create(token, args['search'])

        photos = pexels.photos()

        return choice(photos)
