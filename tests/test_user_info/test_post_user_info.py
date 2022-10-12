from endpoints_models.models import UserStore
from endpoints_models.user_info.model import DataUserInfo, ResponseUserInfo


def test_user_info(app, auth_user):
    """Add user info"""
    data_user_info = DataUserInfo.random()
    res = app.user_info.post_user_info(user_uuid=auth_user[UserStore.USER_UUID],
                                       data=data_user_info,
                                       headers=auth_user[UserStore.HEADERS],
                                       type_response=ResponseUserInfo)
    assert res.status_code == 200, "Check code"
    assert res.data.message == "User info created successfully."
