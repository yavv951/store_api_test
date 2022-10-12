from pydantic import BaseModel

from endpoints_models.register.model import DataRegister
from utils.logger import log

from utils.validator import Validator


class Auth(Validator):
    """API endpoint post."""

    POST_AUTH = "/auth"

    def __init__(self, app):
        self.app = app

    @log("Post Authorization")
    def post_auth(self, data: DataRegister, type_response: BaseModel):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTH}",
            json=data.dict(),
        )
        return self.structure(response, type_response=type_response)
