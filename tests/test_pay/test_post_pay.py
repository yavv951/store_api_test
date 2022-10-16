import allure
import pytest
from allure_commons.types import Severity

from endpoints_models.models import UserStore
from endpoints_models.pay.model import DataPay, ResponseDataPay


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 015 Оплата за товар в магазине')
@allure.link('https://github.com/yavv951', name='Owner')
@pytest.mark.xfail(reason="Bug in metod")
def test_post_pay(app, balance):
    """Add user balance"""
    data_pay = DataPay(itemId=balance[UserStore.ITEM].itemID)
    res = app.balance.post_balance(user_id=balance[UserStore.USER_UUID],
                                   data=data_pay,
                                   headers=balance[UserStore.HEADERS],
                                   type_response=ResponseDataPay)
    assert res.status_code == 201, "Check code"
