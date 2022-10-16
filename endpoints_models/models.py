from enum import Enum


class MessageResponse:
    message: str


class UserStore(Enum):
    USER = 'user'
    USER_UUID = 'user_uuid'
    HEADERS = 'headers'
    USER_INFO = 'user_info'
    STORE = 'store'
    ITEM = 'item'
    USER_BALANCE = 'user_balance'


class AuthInvalidResponse:
    description: str
    error: str
    status_code: int