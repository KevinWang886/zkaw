import time
import pytest
import allure
from common.readelement import Element
from config.conf import TEST_DATA_PATH

test_excavator_kind = Element(TEST_DATA_PATH,  'test_device_base_info', 'test_excavator_kind').data


class TestExcavatorKind:

    @pytest.fixture(scope='module', autouse=True)
    def go_to_excavator_kind(self, go_to_excavator_management, excavator_base_info):
        # 判断电铲信息管理菜单是否打开
        if go_to_excavator_management.is_excavator_info_menu_open():
            with allure.step("点击电铲信息管理"):
                go_to_excavator_management.click_excavator_info()
        time.sleep(0.5)
        with allure.step("点击电铲物料维护"):
            excavator_base_info.click_excavator_kind()
            time.sleep(0.5)

    @allure.severity("blocker")
    @allure.story("电铲物料维护")
    @allure.title("查询电铲物料")
    def test_search_excavator(self, excavator_kind):
        with allure.step("1、输入电铲名称"):
            excavator_kind.input_excavator_name(test_excavator_kind['excavator_name'])
        with allure.step("2、点击【查询】按钮"):
            excavator_kind.click_query_btn()
        time.sleep(0.5)
        with allure.step("3、断言："):
            assert test_excavator_kind['excavator_name'] == excavator_kind.get_excavator_name()

    @allure.severity("blocker")
    @allure.story("电铲物料维护")
    @allure.title("修改电铲物料")
    def test_modify_excavator_kind(self, excavator_kind):
        with allure.step("1、点击'修改'"):
            excavator_kind.click_modify_btn()
        with allure.step("2、修改物料并【保存】"):
            excavator_kind.select_kind()
        time.sleep(0.5)
        with allure.step("3、断言："):
            assert excavator_kind.get_alert_msg() == test_excavator_kind['alert_msg']
