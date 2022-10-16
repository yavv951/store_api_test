import allure
from allure_commons.types import Severity

from endpoints_models.models import UserStore
from endpoints_models.store.model import ResponseStore


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 008 Получение информации о магазине')
@allure.link('https://github.com/yavv951', name='Owner')
def test_get_store(app, store):
    """Get store"""
    res = app.store.get_store(name_store=store[UserStore.STORE].name,
                              headers=store[UserStore.HEADERS],
                              type_response=ResponseStore)
    assert res.status_code == 200, "Check code"
    data_store = store[UserStore.STORE]
    assert res.data.name == data_store.name, "Check name"