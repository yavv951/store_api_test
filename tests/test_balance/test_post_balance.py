import allure
from allure_commons.types import Severity

from endpoints_models.balance.model import DataBalance, ResponseDataBalance
from endpoints_models.models import UserStore


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 013 Пополнение баланса в магазине')
@allure.link('https://github.com/yavv951', name='Owner')
def test_balance(app, store_item):
    """Add user balance"""
    data_balance = DataBalance.random()
    res = app.balance.post_balance(user_id=store_item[UserStore.USER_UUID],
                                   data=data_balance,
                                   headers=store_item[UserStore.HEADERS],
                                   type_response=ResponseDataBalance)
    assert res.status_code == 201, "Check code"
