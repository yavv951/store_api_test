from enum import Enum


class MessageResponse:
    message: str


class UserStore(Enum):
    USER = 'user'
    USER_UUID = 'user_uuid'
    HEADERS = 'headers'
    USER_INFO = 'user_info'
    STORE = 'store'
    #store_uuid: int
    ITEM = 'item'
    #price: int
    #item_uuid: int
    #user_balance: Balance = attr.ib(default=None)


class AuthInvalidResponse:
    description: str
    error: str
    status_code: int