import time
import allure
import pytest
from common.readelement import Element
from config.conf import TEST_DATA_PATH
from page.device_base_info.excavator_base_info import ExcavatorBaseInfoPage
from page.device_base_info.device_base_info import DeviceBaseInfoPage
from page.device_base_info.excavator_kind import ExcavatorKind
from test_case.test_device_base_info import test_excavator_kind

test_excavator_base_info = Element(TEST_DATA_PATH,  '', 'test_excavator_base_info').data


@pytest.fixture(scope='session')
def go_to_excavator_management(driver):
    go_to_excavator_management = DeviceBaseInfoPage(driver)
    return go_to_excavator_management


@pytest.fixture(scope='session')
def excavator_base_info(driver):
    excavator_base_info = ExcavatorBaseInfoPage(driver)
    return excavator_base_info


@pytest.fixture(scope='session')
def excavator_kind(driver):
    excavator_kind = ExcavatorKind(driver)
    return excavator_kind


@pytest.fixture(scope='session', autouse=True)
def open_page(login, home):
    login.open("/truck-dispatch/?#/login")
    time.sleep(0.5)
    login.input_account(test_excavator_base_info['account'])
    login.input_password(test_excavator_base_info['password'])
    login.click_login_btn()
    time.sleep(0.5)
    with allure.step("设备基础信息管理"):
        home.click_base_info()
    time.sleep(0.5)


