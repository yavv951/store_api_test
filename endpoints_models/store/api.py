from utils.logger import log

from utils.validator import Validator


class Store(Validator):
    """API endpoint Store."""

    POST_STORE = "/store/{}"

    def __init__(self, app):
        self.app = app

    @log("Post Store")
    def post_store(self, name_store: str, headers=None, type_response=None):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_STORE.format(name_store)}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("GET Store")
    def get_store(self, name_store: str, headers=None, type_response=None):
        """Get request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.POST_STORE.format(name_store)}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)

