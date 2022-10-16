import random

from faker import Faker
from pydantic import BaseModel

fake = Faker()


class DataBalance(BaseModel):
    """Модель для регистрации."""
    balance: float

    @staticmethod
    def random():
        """Генерация данных для регистрации."""
        return DataBalance(balance=random.randint(50, 100))


class ResponseDataBalance(BaseModel):
    message: str
    balance: float


class ResponseBalance(BaseModel):
    message: str