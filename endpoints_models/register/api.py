from pydantic import BaseModel

from endpoints_models.register.model import DataRegister
from utils.logger import log

from utils.validator import Validator


class Register(Validator):
    """API endpoint post."""

    POST_REGISTER = "/register"

    def __init__(self, app):
        self.app = app

    @log("Post Register")
    def post_registred(self, data: DataRegister, type_response: BaseModel):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_REGISTER}",
            json=data.dict(),
        )
        return self.structure(response, type_response=type_response)
