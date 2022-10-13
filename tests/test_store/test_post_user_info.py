from endpoints_models.models import UserStore
from endpoints_models.store.model import StoreData, ResponseStore


def test_store(app, auth_user):
    """Add user info"""
    data_store = StoreData.random()
    res = app.store.post_store(name_store=data_store.name,
                               headers=auth_user[UserStore.HEADERS],
                               type_response=ResponseStore)
    assert res.status_code == 201, "Check code"
