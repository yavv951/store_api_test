from endpoints_models.models import UserStore
from endpoints_models.user_info.model import ResponseUserInfo


def test_delete_user_info(app, user_info):
    """Get user info"""
    res = app.user_info.delete_user_info(user_uuid=user_info[UserStore.USER_UUID],
                                      headers=user_info[UserStore.HEADERS],
                                      type_response=ResponseUserInfo)
    assert res.status_code == 200, "Check code"
    assert res.data.message == "User info deleted."
    res = app.user_info.get_user_info(user_uuid=user_info[UserStore.USER_UUID],
                                      headers=user_info[UserStore.HEADERS],
                                      type_response=ResponseUserInfo)
    assert res.status_code == 404, "Check code"
    assert res.data.message == "User info not found"
