"""Vendor interface
    """


class VendorInterface:

    @staticmethod
    def create(token, query):
        """Create new instance of VendorInterface class.

        Args:
            token (string): Token from vendor.
            query (string): Query.
        """
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
