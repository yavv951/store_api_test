from typing import Dict, Union, Any

import pytest

from endpoints_models.app import StoreApp
from endpoints_models.auth.model import ResponseAuth
from endpoints_models.models import UserStore
from endpoints_models.register.model import DataRegister, ResponseRegister
from endpoints_models.store.model import StoreData, ResponseStore
from endpoints_models.user_info.model import DataUserInfo, ResponseUserInfo


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
    res = app.auth.post_auth(data=register_user[UserStore.USER], type_response=ResponseAuth)
    token = res.data.access_token
    headers = {"Authorization": f"JWT {token}"}
    register_user[UserStore.HEADERS] = headers
    data_dict = register_user
    return data_dict


@pytest.fixture
def user_info(app, auth_user):
    data_user_info = DataUserInfo.random()
    res = app.user_info.post_user_info(user_uuid=auth_user[UserStore.USER_UUID],
                                       data=data_user_info,
                                       headers=auth_user[UserStore.HEADERS],
                                       type_response=ResponseUserInfo)
    auth_user[UserStore.USER_INFO] = data_user_info
    data_dict = auth_user
    return data_dict

@pytest.fixture
def store(app, auth_user):
    """Add user info"""
    data_store = StoreData.random()
    res = app.store.post_store(name_store=data_store.name,
                               headers=auth_user[UserStore.HEADERS],
                               type_response=ResponseStore)
    auth_user[UserStore.STORE] = res.data
    data_dict = auth_user
    return data_dict

def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )
