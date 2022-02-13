import requests


class SaveImage:
    """
    Save image to disk
    """

    def __init__(self, store_path: str) -> None:
        self._store_path = store_path

    @staticmethod
    def create(store_path: str) -> object:
        return SaveImage(store_path)

    def _request(self, url: str) -> requests.get:
        """Request to image url.

        Args:
            url (str): Image URL

        Returns:
            requests.get: Response
        """
        return requests.get(url, stream=True)

    def save(self, url: str) -> str:
        """Save image to disk

        Args:
            url (str): Image URL

        Returns:
            str: Path to image
        """

        response = self._request(url)

        if response.status_code == 200:
            with open(self._store_path, 'wb') as f:
                for chunk in response:
                    f.write(chunk)

        return self._store_path
