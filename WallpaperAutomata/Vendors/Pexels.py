"""
    Get images from Pexels.
"""
import requests


class Pexels:

    _base_url = 'https://api.pexels.com/'

    _end_point = 'v1/search'

    _params = {
        'query': '',
        'orientation': 'landscape',
        'size': 'original',
        'per_page': 50,

    }

    _response = ''

    def __init__(self, token, query) -> None:
        """Constructor

        Args:
            token (str): token from Pexels.
            url (str): url query.
        """

        self._token = token
        self._params['query'] = query

    @staticmethod
    def create(token, query):
        return Pexels(token, query)

    def _request(self):
        """
        It do request to Pexels.
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

    def photos(self) -> list:
        """Get photos.

        Returns:
            list: [{author: string, url: string}, ...]
        """
        self._request()

        photosRaw = self._response['photos']

        photos = []

        for photo in photosRaw:
            photos.append({
                'author': photo['photographer'],
                'url': photo['src'][self._params['size']],
                'id': photo['id'],
                'title': photo['alt'] if photo['alt'] else photo['id'],
            })

        return photos
