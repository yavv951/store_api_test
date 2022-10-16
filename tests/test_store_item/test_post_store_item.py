import allure
from allure_commons.types import Severity
from faker import Faker

from endpoints_models.models import UserStore
from endpoints_models.store_item.model import DataStoreItem, ResponseStoreItemData

fake = Faker()


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 009 Добавление товаров в магазин')
@allure.link('https://github.com/yavv951', name='Owner')
def test_store_item(app, store):
    """Add store item"""
    data_store_item = DataStoreItem.random(store_id=store[UserStore.STORE].uuid)
    res = app.store_item.post_store_item(name_item=fake.name(),
                                         data=data_store_item,
                                         headers=store[UserStore.HEADERS],
                                         type_response=ResponseStoreItemData)
    assert res.status_code == 201, "Check code"
