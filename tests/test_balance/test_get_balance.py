import allure
from allure_commons.types import Severity

from endpoints_models.balance.model import ResponseDataBalance
from endpoints_models.models import UserStore


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 014 Изменение баланса в магазине')
@allure.link('https://github.com/yavv951', name='Owner')
def test_get_balance(app, balance):
    """Get user balance"""
    res = app.balance.get_balance(user_id=balance[UserStore.USER_UUID],
                                  headers=balance[UserStore.HEADERS],
                                  type_response=ResponseDataBalance)
    data_balance = balance[UserStore.USER_BALANCE]
    assert res.status_code == 200, "Check code"
    assert res.data.message == f"User balance is {data_balance.balance}", "Check message"
    assert res.data.balance == data_balance.balance, "Check balance"
