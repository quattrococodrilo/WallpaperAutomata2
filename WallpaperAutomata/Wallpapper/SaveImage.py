import requests


class SaveImage:

    def __init__(self, store_path) -> None:
        self._store_path = store_path

    @staticmethod
    def create(store_path):
        return SaveImage(store_path)

    def _request(self, url):
        return requests.get(url, stream=True)

    def save(self, url):
        response = self._request(url)

        if response.status_code == 200:
            with open(self._store_path, 'wb') as f:
                for chunk in response:
                    f.write(chunk)

        return self._store_path
