from pydantic import BaseModel

from endpoints_models.register.model import DataRegister
from endpoints_models.user_info.model import DataUserInfo
from utils.logger import log

from utils.validator import Validator


class UserInfo(Validator):
    """API endpoint post."""

    POST_USER_INFO = "/user_info/{}"

    def __init__(self, app):
        self.app = app

    @log("Post User info")
    def post_user_info(self, data: DataUserInfo, user_uuid: int, headers=None, type_response=None):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_uuid)}",
            json=data.dict(),
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("GET User info")
    def get_user_info(self, user_uuid: int, headers=None, type_response=None):
        """Get request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_uuid)}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("DELETE User info")
    def delete_user_info(self, user_uuid: int, headers=None, type_response=None):
        """Get request."""
        response = self.app.client.request(
            method="DELETE",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_uuid)}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("Put User info")
    def put_user_info(self, data: DataUserInfo, user_uuid: int, headers=None, type_response=None):
        """Put request."""
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_uuid)}",
            json=data.dict(),
            headers=headers
        )
        return self.structure(response, type_response=type_response)