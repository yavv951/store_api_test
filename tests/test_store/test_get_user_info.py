from endpoints_models.models import UserStore
from endpoints_models.store.model import ResponseStore


def test_get_store(app, store):
    """Get user info"""
    res = app.store.get_store(name_store=store[UserStore.STORE].name,
                              headers=store[UserStore.HEADERS],
                              type_response=ResponseStore)
    assert res.status_code == 200, "Check code"
    data_store = store[UserStore.STORE]
    assert res.data.name == data_store.name, "Check name"