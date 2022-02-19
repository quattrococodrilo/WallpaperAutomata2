"""
Configuration constants.
"""

from typing import Dict

from WallpaperAutomata.Commands.pexel_command import PexelsCommand

CONFIG_DATA = {
    'config': {
        'store': '',
    },
    'vendors': {
        'pexels': {
            'token': 'Your vendor token here.',
            'query': 'mountain',
        }
    }
}


CONFIG_PATH: Dict = {
    'Linux': '.config/wallpapper_automata',
    'Darwin': '',
    'Java': '',
    'Windows': '',
}

CONFIG_FILE_NAME: str = 'wall_automata_conf.yml'

# Commands
# ------------------------------------------------------------

COMMAND_DESCRIPTION: str = 'Set a wallpaper.'

COMMANDS: Dict = {
    'pexels': PexelsCommand
}

# Database
# ------------------------------------------------------------

DATABASES: Dict = {}
