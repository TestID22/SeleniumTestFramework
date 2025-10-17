

class _APImetaCategory:
    """

    """
    def __init__(self, mock_api) -> None:
        self._api = mock_api

    @property
    def api(self):
        return self._api
