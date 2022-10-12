from faker import Faker
from pydantic import BaseModel

fake = Faker()


class DataRegister(BaseModel):
    """Модель для регистрации."""

    username: str
    password: str

    @staticmethod
    def random():
        """Генерация данных для регистрации."""
        return DataRegister(username=fake.name(), password=fake.password())


class ResponseRegister(BaseModel):
    """Модель для ответа."""

    message: str
    uuid: int
