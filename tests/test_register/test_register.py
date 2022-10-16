import allure
from allure_commons.types import Severity

from endpoints_models.register.model import DataRegister, ResponseRegister


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 001 Регистрация пользователя')
@allure.link('https://github.com/yavv951', name='Owner')
def test_register(app):
    """"""
    data = DataRegister.random()
    response = app.register.post_registred(data=data, type_response=ResponseRegister)
    assert response.status_code == 201, "Check code"
