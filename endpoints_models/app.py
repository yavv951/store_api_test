from endpoints_models.auth.api import Auth
from endpoints_models.register.api import Register
from endpoints_models.store.api import Store
from endpoints_models.user_info.api import UserInfo
from utils.client import Client


class StoreApp:
    """App."""

    def __init__(self, url: str):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.auth = Auth(self)
        self.user_info = UserInfo(self)
        self.store = Store(self)
