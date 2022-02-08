"""Vendor interface
    """


class VendorInterface:

    @staticmethod
    def create(token, queryUrl):
        """Create new instance of VendorInterface class.

        Args:
            token (string): Token from vendor.
            queryUrl ([type]): Url for query.
        """
        pass

    def _request(self) -> None:
        """ Get data from vendor. """
        pass

    def data(self) -> dict:
        """Data from vendor as dict.

        Returns:
            dict: {
                url: string
                author: string
            }
        """
        pass
