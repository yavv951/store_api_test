from faker import Faker
from pydantic import BaseModel

fake = Faker()


class DataAuth(BaseModel):
    """Модель для авторизации."""

    username: str
    password: str

    @staticmethod
    def random():
        """Генерация данных для авторизации."""
        return DataAuth(username=fake.name(), password=fake.password())


class ResponseAuth(BaseModel):
    """Модель для ответа."""

    access_token: str
