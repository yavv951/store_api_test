from faker import Faker
from pydantic import BaseModel

fake = Faker()


class Address(BaseModel):
    city: str
    street: str
    home_number: str


class DataUserInfo(BaseModel):
    """Модель для регистрации."""

    phone: str
    email: str
    address: dict

    @staticmethod
    def random():
        """Генерация данных для регистрации."""
        city = fake.city()
        street = fake.street_name()
        home_number = fake.building_number()
        return DataUserInfo(phone=fake.name(), email=fake.password(), address=Address(city=city, street=street, home_number=home_number))


class ResponseUserInfo(BaseModel):
    """Модель для ответа."""

    message: str


class ResponseUserInfoData(BaseModel):
    city: str
    street: str
    userID: int
    phone: str
    email: str


