import random

from faker import Faker
from pydantic import BaseModel

fake = Faker()


class DataPay(BaseModel):
    """Модель для регистрации."""
    itemId: int


class ResponseDataPay(BaseModel):
    message: str
    balance: float
    name: str
    price: float

