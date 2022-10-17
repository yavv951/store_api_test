from typing import Any, Dict

import pytest
from dotenv import load_dotenv
from faker import Faker

from endpoints_models.app import StoreApp
from endpoints_models.auth.model import ResponseAuth
from endpoints_models.balance.model import DataBalance, ResponseDataBalance
from endpoints_models.models import UserStore
from endpoints_models.register.model import DataRegister, ResponseRegister
from endpoints_models.store.model import ResponseStore, StoreData
from endpoints_models.store_item.model import DataStoreItem, ResponseStoreItemData
from endpoints_models.user_info.model import DataUserInfo, ResponseUserInfo

fake = Faker()


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def app(request) -> StoreApp:
    url = request.config.getoption("--api-url")
    return StoreApp(url)


@pytest.fixture
def register_user(app) -> Dict[UserStore, Any]:
    """
    Register new user
    """
    data = DataRegister.random()
    res = app.register.post_registred(data=data, type_response=ResponseRegister)
    data_dict = {UserStore.USER: data, UserStore.USER_UUID: res.data.uuid}
    return data_dict


@pytest.fixture
def auth_user(app, register_user):
    res = app.auth.post_auth(
        data=register_user[UserStore.USER], type_response=ResponseAuth
    )
    token = res.data.access_token
    headers = {"Authorization": f"JWT {token}"}
    register_user[UserStore.HEADERS] = headers
    data_dict = register_user
    return data_dict


@pytest.fixture
def user_info(app, auth_user):
    data_user_info = DataUserInfo.random()
    res = app.user_info.post_user_info(
        user_uuid=auth_user[UserStore.USER_UUID],
        data=data_user_info,
        headers=auth_user[UserStore.HEADERS],
        type_response=ResponseUserInfo,
    )
    auth_user[UserStore.USER_INFO] = data_user_info
    data_dict = auth_user
    return data_dict


@pytest.fixture
def store(app, auth_user):
    """Add store"""
    data_store = StoreData.random()
    res = app.store.post_store(
        name_store=data_store.name,
        headers=auth_user[UserStore.HEADERS],
        type_response=ResponseStore,
    )
    auth_user[UserStore.STORE] = res.data
    data_dict = auth_user
    return data_dict


@pytest.fixture
def store_item(app, store):
    """Add store item"""
    data_store_item = DataStoreItem.random(store_id=store[UserStore.STORE].uuid)
    res = app.store_item.post_store_item(
        name_item=fake.name(),
        data=data_store_item,
        headers=store[UserStore.HEADERS],
        type_response=ResponseStoreItemData,
    )
    store[UserStore.ITEM] = res.data
    data_dict = store
    return data_dict


@pytest.fixture
def balance(app, store_item):
    """Add user balance"""
    data_balance = DataBalance.random()
    res = app.balance.post_balance(
        user_id=store_item[UserStore.USER_UUID],
        data=data_balance,
        headers=store_item[UserStore.HEADERS],
        type_response=ResponseDataBalance,
    )
    store_item[UserStore.USER_BALANCE] = res.data
    data_dict = store_item
    return data_dict


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )
