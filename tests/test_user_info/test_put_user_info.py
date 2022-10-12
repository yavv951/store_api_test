from endpoints_models.models import UserStore
from endpoints_models.user_info.model import DataUserInfo, ResponseUserInfo


def test_put_user_info(app, user_info):
    """Put user info"""
    data_user_info = DataUserInfo.random()
    res = app.user_info.put_user_info(user_uuid=user_info[UserStore.USER_UUID],
                                      data=data_user_info,
                                      headers=user_info[UserStore.HEADERS],
                                      type_response=ResponseUserInfo)
    assert res.status_code == 200, "Check code"
    assert res.data.message == "User info updated successfully."