"""
Command Interface
"""

import abc
from typing import Dict, List, Optional


class CommandInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'description') and
            callable(subclass.description) and
            hasattr(subclass, 'arguments') and
            callable(subclass.arguments) and
            hasattr(subclass, 'exec') and
            callable(subclass.exec)
        )

    @abc.abstractclassmethod
    def description(cls) -> str:
        """Command description.
        """

        raise NotImplementedError

    @abc.abstractclassmethod
    def exec(cls, token: str, args_parsed: Dict, data_local_config: Optional[Dict]) -> None:
        """Executes command

        Args:
            args_parsed (Dict): arguments from args_parse.
        """

        raise NotImplementedError

    @abc.abstractclassmethod
    def arguments(cls) -> List[Dict]:
        """Arguments to add to args_parse.

        Returns:
            List[Dict]: argument configuration.
        """

        raise NotImplementedError
