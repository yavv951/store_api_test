import allure
import pytest
from allure_commons.types import Severity
from faker import Faker

from endpoints_models.models import UserStore
from endpoints_models.store_item.model import DataStoreItem, ResponseStoreItemData

fake = Faker()

@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 012 Изменение информации о товаре в магазине')
@allure.link('https://github.com/yavv951', name='Owner')
@pytest.mark.xfail(reason="Bug in metod")
@pytest.mark.bug
def test_put_store_item(app, store_item):
    """Put store item"""
    data_item = DataStoreItem.random(store_id=store_item[UserStore.STORE].uuid)
    res = app.store_item.put_store_item(name_item=store_item[UserStore.ITEM].name,
                                        data=data_item,
                                        headers=store_item[UserStore.HEADERS],
                                        type_response=ResponseStoreItemData)
    assert res.status_code == 200, "Check code"
    assert res.data.price == data_item.price, "Check price"
    assert res.data.description == data_item.description, "Check description"