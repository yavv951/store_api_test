from endpoints_models.user_info.model import DataUserInfo
from utils.logger import log

from utils.validator import Validator


class StoreItem(Validator):
    """API endpoint post."""

    POST_USER_INFO = "/item/{}"

    def __init__(self, app):
        self.app = app

    @log("Post Item store")
    def post_item(self, data: DataUserInfo, name_item: str, headers=None, type_response=None):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USER_INFO.format(name_item)}",
            json=data.dict(),
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("GET Item store")
    def get_item(self, name_item: str, headers=None, type_response=None):
        """Get request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.POST_USER_INFO.format(name_item)}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("Put Item store")
    def put_item(self, data: DataUserInfo, name_item: str, headers=None, type_response=None):
        """Put request."""
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.POST_USER_INFO.format(name_item)}",
            json=data.dict(),
            headers=headers
        )
        return self.structure(response, type_response=type_response)