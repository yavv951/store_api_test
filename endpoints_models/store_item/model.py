from faker import Faker
from pydantic import BaseModel

fake = Faker()


class DataStoreItem(BaseModel):
    """Модель для регистрации."""
    price: str
    store_id: int
    description: str
    image: str

    @staticmethod
    def random(store_id):
        """Генерация данных для регистрации."""
        return DataStoreItem(price=fake.name(), store_id=store_id, description=fake.catch_phrase())


class ResponseStoreItem(BaseModel):
    """Модель для ответа."""
    message: str


class ResponseStoreItemData(BaseModel):
    name: str
    store_id: int
    itemID: int
    description: int
    image: str



