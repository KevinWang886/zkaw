import pytest
from page.device_base_info.excavator_base_info import ExcavatorBaseInfoPage
from page.device_base_info.device_base_info import DeviceBaseInfoPage
from page.device_base_info.excavator_kind import ExcavatorKind


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


