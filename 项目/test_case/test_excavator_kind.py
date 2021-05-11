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
    @allure.title("查询电铲")
    def test_search_excavator(self, excavator_kind):
        with allure.step("1、输入电铲名称"):
            excavator_kind.input_excavator_name(excavator_name=
                                                Base.get_data(excavator_kind, file_name='test_excavator_kind.yaml')
                                                ['test_excavator_kind']['excavator_name'])
        with allure.step("2、点击【查询】按钮"):
            excavator_kind.click_query_btn()
        with allure.step("3、断言："):
            assert excavator_kind.get_excavator_name() == \
                   Base.get_data(excavator_kind, file_name='test_excavator_kind.yaml')['test_excavator_kind']\
                       ['excavator_name']
