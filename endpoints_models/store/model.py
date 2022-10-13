from faker import Faker
from pydantic import BaseModel

fake = Faker()


class StoreData(BaseModel):
    """Модель для регистрации."""
    name: str

    @staticmethod
    def random():
        """Генерация данных для регистрации."""
        return StoreData(name=fake.first_name().lower())


class ResponseStore(BaseModel):
    """Модель для ответа."""
    name: str
    uuid: int
    items: list



