import allure
from allure_commons.types import Severity

from endpoints_models.models import UserStore
from endpoints_models.store_item.model import (
    ResponseStoreItemData,
    ResponseStoreItemsData,
)


@allure.tag("WEB API")
@allure.severity(Severity.CRITICAL)
@allure.label("Owner", "Vadim")
@allure.feature("Testing api site store")
@allure.story(f"Тест кейс 010 Получение товара в магазине")
@allure.link("https://github.com/yavv951", name="Owner")
def test_get_store_item(app, store_item):
    """Get store item"""
    res = app.store_item.get_store_item(
        name_item=store_item[UserStore.ITEM].name,
        headers=store_item[UserStore.HEADERS],
        type_response=ResponseStoreItemData,
    )
    data_store_item = store_item[UserStore.ITEM]
    assert res.status_code == 200, "Check code"
    assert res.data.price == data_store_item.price, "Check price"
    assert res.data.itemID == data_store_item.itemID, "Check itemID"
    assert res.data.description == data_store_item.description, "Check description"


@allure.tag("WEB API")
@allure.severity(Severity.CRITICAL)
@allure.label("Owner", "Vadim")
@allure.feature("Testing api site store")
@allure.story(f"Тест кейс 011 Получение товаров в магазине")
@allure.link("https://github.com/yavv951", name="Owner")
def test_get_store_items(app, store_item):
    """Get store items"""
    res = app.store_item.get_store_items(
        headers=store_item[UserStore.HEADERS], type_response=ResponseStoreItemsData
    )
    assert res.status_code == 200, "Check code"
