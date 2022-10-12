from endpoints_models.auth.model import DataAuth, ResponseAuth
from endpoints_models.models import UserStore


def test_auth(app, register_user):
    """"""
    res = app.auth.post_auth(data=register_user[UserStore.USER], type_response=ResponseAuth)
    assert res.status_code == 200, "Check code"
