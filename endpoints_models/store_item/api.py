from endpoints_models.store_item.model import DataStoreItem
from utils.logger import log

from utils.validator import Validator


class StoreItem(Validator):
    """API endpoint post."""

    POST_STORE_ITEM = "/item/{}"
    POST_STORE_ITEMS = "/items"

    def __init__(self, app):
        self.app = app

    @log("Post Item store")
    def post_store_item(self, data: DataStoreItem, name_item: str, headers=None, type_response=None):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_STORE_ITEM.format(name_item)}",
            json=data.dict(),
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("GET Item store")
    def get_store_item(self, name_item: str, headers=None, type_response=None):
        """Get request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.POST_STORE_ITEM.format(name_item)}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("Put Item store")
    def put_store_item(self, data: DataStoreItem, name_item: str, headers=None, type_response=None):
        """Put request."""
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.POST_STORE_ITEM.format(name_item)}",
            json=data.dict(),
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("GET Items store")
    def get_store_items(self, headers=None, type_response=None):
        """Get request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.POST_STORE_ITEMS}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)
