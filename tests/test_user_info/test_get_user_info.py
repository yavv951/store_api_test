from endpoints_models.models import UserStore
from endpoints_models.user_info.model import ResponseUserInfoData


def test_get_user_info(app, user_info):
    """Get user info"""
    res = app.user_info.get_user_info(user_uuid=user_info[UserStore.USER_UUID],
                                      headers=user_info[UserStore.HEADERS],
                                      type_response=ResponseUserInfoData)
    data_user_info = user_info[UserStore.USER_INFO]
    assert res.status_code == 200, "Check code"
    assert res.data.phone == data_user_info.phone, "Check phone"
    assert res.data.email == data_user_info.email, "Check email"
    assert res.data.city == data_user_info.address['city'], "Check street"
    assert res.data.street == data_user_info.address['street'], "Check street"