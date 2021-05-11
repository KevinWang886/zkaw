import time
import pytest
import allure
from base.base import Base


class TestExcavatorKind:

    @pytest.fixture(scope='session', autouse=True)
    def open_page(self, login, home, go_to_excavator_management, excavator_base_info):
        login.open("/truck-dispatch/?#/login")
        time.sleep(0.5)
        login.input_account(Base.get_data(login, file_name='test_excavator_kind.yaml')
                            ['test_excavator_kind']['account'])
        login.input_password(Base.get_data(login, file_name='test_excavator_kind.yaml')
                             ['test_excavator_kind']['password'])
        login.click_login_btn()
        time.sleep(0.5)
        with allure.step("设备基础信息管理"):
            home.click_base_info()
        time.sleep(0.5)
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
        with allure.step("1、输入电铲名称并点击【查询】"):
            excavator_kind.input_excavator_name(Base.get_data(excavator_kind, file_name='test_excavator_kind.yaml')
                                                ['test_excavator_kind']['excavator_name'])
        with allure.step("2、断言："):
            assert excavator_kind.get_excavator_name() == \
                   Base.get_data(excavator_kind, file_name='test_excavator_kind.yaml')['test_excavator_kind']\
                       ['excavator_name']

    @allure.severity("blocker")
    @allure.story("电铲物料维护")
    @allure.title("修改电铲物料")
    def test_modify_excavator_kind(self, excavator_kind):
        with allure.step("1、点击'修改'"):
            excavator_kind.click_modify_btn()
        with allure.step("2、修改物料并【保存】"):
            excavator_kind.select_kind()
        time.sleep(1)
        with allure.step("3、断言："):
            assert excavator_kind.get_alert_msg() == \
                   Base.get_data(excavator_kind, file_name='test_excavator_kind.yaml')['test_excavator_kind']\
                       ['alert_msg']
