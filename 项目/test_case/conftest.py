import time
import pytest
from page.device_base_info.excavator_base_info import ExcavatorBaseInfoPage
from page.login import LoginPage
from page.device_base_info.device_base_info import DeviceBaseInfoPage
from page.home_page import HomePage
from page.device_base_info.excavator_kind import ExcavatorKind


@pytest.fixture(scope='session')
@pytest.mark.usefixtures('base_url')
def login(driver, base_url):
    login = LoginPage(driver, base_url)
    time.sleep(0.5)
    return login


@pytest.fixture(scope='session')
def home(driver):
    home = HomePage(driver)
    time.sleep(0.5)
    return home


