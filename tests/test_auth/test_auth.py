import allure
import pytest
from allure_commons.types import Severity

from endpoints_models.auth.model import DataAuth, ResponseAuth
from endpoints_models.models import UserStore


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 002 Авторизация пользователя')
@allure.link('https://github.com/yavv951', name='Owner')
@pytest.mark.smoke
def test_auth(app, register_user):
    """"""
    res = app.auth.post_auth(data=register_user[UserStore.USER], type_response=ResponseAuth)
    assert res.status_code == 200, "Check code"
