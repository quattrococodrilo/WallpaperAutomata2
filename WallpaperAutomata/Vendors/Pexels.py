"""
    Get images from Pexels.
"""


class Pexels:

    def __init__(self, token, url) -> None:
        """Constructor

        Args:
            token (str): token from Pexels.
            url (str): url query.
        """

        self.token = token
        self.url = url

    @staticmethod
    def create(token, url):
        return Pexels(token, url)
