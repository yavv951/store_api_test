import allure
from allure_commons.types import Severity

from endpoints_models.models import UserStore
from endpoints_models.store.model import StoreData, ResponseStore


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 007 Добавление магазина')
@allure.link('https://github.com/yavv951', name='Owner')
def test_store(app, auth_user):
    """Add store"""
    data_store = StoreData.random()
    res = app.store.post_store(name_store=data_store.name,
                               headers=auth_user[UserStore.HEADERS],
                               type_response=ResponseStore)
    assert res.status_code == 201, "Check code"
