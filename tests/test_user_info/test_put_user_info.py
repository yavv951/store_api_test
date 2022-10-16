import allure
from allure_commons.types import Severity

from endpoints_models.models import UserStore
from endpoints_models.user_info.model import DataUserInfo, ResponseUserInfo


@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api site store')
@allure.story(f'Тест кейс 006 Изменение информации пользователя')
@allure.link('https://github.com/yavv951', name='Owner')
def test_put_user_info(app, user_info):
    """Put user info"""
    data_user_info = DataUserInfo.random()
    res = app.user_info.put_user_info(user_uuid=user_info[UserStore.USER_UUID],
                                      data=data_user_info,
                                      headers=user_info[UserStore.HEADERS],
                                      type_response=ResponseUserInfo)
    assert res.status_code == 200, "Check code"
    assert res.data.message == "User info updated successfully."