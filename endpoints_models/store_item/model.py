import random

from faker import Faker
from pydantic import BaseModel

fake = Faker()


class DataStoreItem(BaseModel):
    """Модель для регистрации."""
    price: float
    store_id: int
    description: str
    #image: str

    @staticmethod
    def random(store_id):
        """Генерация данных для регистрации."""
        return DataStoreItem(price=random.randint(1, 50), store_id=store_id, description=fake.catch_phrase())


class ResponseStoreItemData(BaseModel):
    name: str
    price: float
    itemID: int
    description: str
    #image: str


class ResponseStoreItemsData(BaseModel):
    items: list or list[ResponseStoreItemData]
