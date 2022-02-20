"""
    Get images from Pexels.
"""
from typing import Dict, List

import requests

from .vendor_interface import VendorInterface


class PexelsVendor(VendorInterface):

    _base_url: str = 'https://api.pexels.com/'

    _end_point: str = 'v1/search'

    _params: Dict = {
        'query': '',
        'orientation': 'landscape',
        'size': 'original',
        'per_page': 50,
    }

    _response: Dict = {}

    def __init__(self, token: str, query: str) -> None:
        """Constructor

        Args:
            token (str): token from Pexels.
            url (str): url query.
        """

        self._token = token
        self._params['query'] = query

    @classmethod
    def create(cls, token: str, query: str):
        return PexelsVendor(token, query)

    def _request(self) -> None:
        """
        Make a request to Pexels.
        """

        url = f'{self._base_url}{self._end_point}'

        request = requests.get(
            url,
            params=self._params,
            headers={
                'Authorization': self._token,
            }
        )

        self._response = request.json()

    def photos(self) -> List[Dict[str, str]]:
        """Get photos

        Returns:
            list[dict[str, str]]: [
                {
                    'author': str,
                    'id': str,
                    'title': str,
                    'url': str,
                }
                ...
            ]
        """

        self._request()

        photosRaw = self._response['photos']

        photos = []

        for photo in photosRaw:
            photos.append({
                'author': photo['photographer'],
                'url': photo['src'][self._params['size']],
                'id': f"pexels-{photo['id']}",
                'title': photo['alt'] if photo['alt'] else photo['id'],
                'ext': photo['src'][self._params['size']].split('.')[-1]
            })

        return photos
