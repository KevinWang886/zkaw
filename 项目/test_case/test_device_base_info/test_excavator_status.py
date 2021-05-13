import time
import pytest
import allure
from common.readelement import Element
from config.conf import TEST_DATA_PATH

test_excavator_status = Element(TEST_DATA_PATH, '', 'test_excavator_status').data


class TestExcavatorStatus:

    @pytest.fixture(scope="module", autouse=True)
    def go_to_excavator_status(self, go_to_excavator_management, excavator_base_info):
        if go_to_excavator_management.is_excavator_info_menu_open():
            with allure.step("点击电铲信息管理"):
                go_to_excavator_management.click_excavator_info()
        time.sleep(0.5)
        with allure.step("点击电铲状态维护"):
            excavator_base_info.click_excavator_status()
            time.sleep(0.5)

    @allure.severity("blocker")
    @allure.story("电铲状态维护")
    @allure.title("查询电铲名称")
    def test_query_excavator(self, excavator_status):
        with allure.step("1、输入电铲名称"):
            excavator_status.input_excavator_name(excavator_name=test_excavator_status["excavator_name"])
        with allure.step("2、点击【查询】"):
            excavator_status.click_query_btn()
        time.sleep(0.5)
        with allure.step("3、断言："):
            assert excavator_status.get_excavator_name_in_table() == test_excavator_status["excavator_name"]

    @allure.severity("blocker")
    @allure.story("电铲状态维护")
    @allure.title("修改电铲状态")
    def test_modify_excavator_status(self, excavator_status):
        with allure.step("1、点击'修改'"):
            excavator_status.click_modify_btn()
        time.sleep(0.5)
        with allure.step("2、修改电铲状态"):
            excavator_status.modify_excavator_status()
        with allure.step("3、点击【确定】"):
            excavator_status.click_confirm_btn()
        time.sleep(0.5)
        with allure.step("4、断言："):
            assert excavator_status.get_alert_msg() == test_excavator_status["alert_msg"]
