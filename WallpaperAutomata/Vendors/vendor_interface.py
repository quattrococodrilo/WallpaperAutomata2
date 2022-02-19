"""Vendor interface
    """

import abc
from typing import Dict, List


class VendorInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'create') and
            callable(subclass.create) and
            hasattr(subclass, 'photos') and
            callable(subclass.photos)
        )

    @abc.abstractclassmethod
    def create(cls, token: str, query: str) -> object:
        """Create new instance of VendorInterface class.

        Args:
            token (string): Token from vendor.
            query (string): Query.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def photos(self) -> List[Dict[str, str]]:
        """List of photos requested

        Raises:
            NotImplementedError: If method is not implemented.

        Returns:
            list[dict[str, str]]: [
                {
                    'author': str,
                    'url': str,
                    'title': str,
                    'id': str,
                    'ext': str,
                }
                ...
            ]
        """

        raise NotImplementedError
