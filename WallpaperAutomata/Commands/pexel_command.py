"""
    Pexels command
"""

import argparse
from ast import arg
from random import choice
from typing import Dict, List

from WallpaperAutomata.Vendors.pexels_vendor import PexelsVendor

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
    def exec(cls, token: str, args: Dict) -> Dict[str, str]:

        pexels = PexelsVendor.create(token, args['query'])

        photos = pexels.photos()

        return choice(photos)
