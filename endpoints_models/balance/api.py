from endpoints_models.balance.model import DataBalance
from endpoints_models.store_item.model import DataStoreItem
from utils.logger import log

from utils.validator import Validator


class Balance(Validator):
    """API endpoint post."""

    POST_BALANCE = "/balance/{}"

    def __init__(self, app):
        self.app = app

    @log("Post Item store")
    def post_balance(self, data: DataBalance, user_id: str, headers=None, type_response=None):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_BALANCE.format(user_id)}",
            json=data.dict(),
            headers=headers
        )
        return self.structure(response, type_response=type_response)

    @log("GET Item store")
    def get_balance(self, user_id: str, headers=None, type_response=None):
        """Get request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.POST_BALANCE.format(user_id)}",
            headers=headers
        )
        return self.structure(response, type_response=type_response)
