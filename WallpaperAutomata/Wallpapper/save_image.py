from typing import Union
from pathlib import Path
import requests


class SaveImage:
    """
    Save image to disk
    """

    @classmethod
    def save(cls, store_path: Union[str, Path], url: str) -> Union[str, Path]:
        """Save image to disk

        Args:
            url (str): Image URL

        Returns:
            str: Path to image
        """

        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(store_path, 'wb') as f:
                for chunk in response:
                    f.write(chunk)

        return store_path
