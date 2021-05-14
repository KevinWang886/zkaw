import time
import allure
import pytest
from common.readelement import Element
from config.conf import TEST_DATA_PATH
from page.device_base_info.excavator_base_info import ExcavatorBaseInfoPage
from page.device_base_info.device_base_info import DeviceBaseInfoPage
from page.device_base_info.excavator_kind import ExcavatorKind
from page.device_base_info.excavator_status import ExcavatorStatus

login_info = Element(TEST_DATA_PATH,  '', 'test_login').data


# 登录并进入到设备基础信息管理模块
@pytest.fixture(scope='session', autouse=True)
def login_and_open_target_page(login, home):
    login.open("/truck-dispatch/?#/login")
    time.sleep(0.5)
    login.input_account(login_info['account'])
    login.input_password(login_info['password'])
    login.click_login_btn()
    time.sleep(0.5)
    with allure.step("设备基础信息管理"):
        home.click_base_info()


@pytest.fixture(scope='session')
def go_to_excavator_management(driver):
    # 创建电铲信息管理对象
    go_to_excavator_management = DeviceBaseInfoPage(driver)
    return go_to_excavator_management


@pytest.fixture(scope='session')
def excavator_base_info(driver):
    # 创建电铲基本信息对象
    excavator_base_info = ExcavatorBaseInfoPage(driver)
    return excavator_base_info


@pytest.fixture(scope='session')
def excavator_kind(driver):
    # 创建电铲物料维护对象
    excavator_kind = ExcavatorKind(driver)
    return excavator_kind


@pytest.fixture(scope='session')
def excavator_status(driver):
    # 创建电铲状态维护对象
    excavator_status = ExcavatorStatus(driver)
    return excavator_status



