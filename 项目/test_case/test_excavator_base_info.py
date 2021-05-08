import time
import pytest
import allure
import random
from base.base import Base


class TestExcavatorBaseInfo():

    @pytest.fixture(scope='session', autouse=True)
    def open_page(self, login, home, go_to_excavator_management, excavator_base_info):
        login.open("/truck-dispatch/?#/login")
        time.sleep(0.5)
        login.input_account(Base.get_data(login, file_name='test_excavator_base_info.yaml')
                            ['test_excavator_base_info']['account'])
        login.input_password(Base.get_data(login, file_name='test_excavator_base_info.yaml')
                             ['test_excavator_base_info']['password'])
        login.click_login_btn()
        time.sleep(0.5)
        with allure.step("设备基础信息管理"):
            home.click_base_info()
        time.sleep(0.5)
        with allure.step("点击电铲信息管理"):
            go_to_excavator_management.click_excavator_info()
        time.sleep(0.5)
        with allure.step("点击电铲基本信息"):
            excavator_base_info.click_excavator_base_info()
            time.sleep(0.5)

    @allure.severity("blocker")
    @allure.story("电铲基本信息")
    @allure.title("新增电铲")
    def test_add_new_excavator(self, excavator_base_info):
        with allure.step("点击新增按钮"):
            excavator_base_info.click_add_btn()
        time.sleep(0.5)
        with allure.step("输入电铲编号"):
            excavator_base_info.input_excavator_no(excavator_no=random.randint(10000, 99999))
        with allure.step("输入电铲名称"):
            excavator_base_info.input_excavator(excavator="电铲" + str(random.randint(10000, 99999)))
        with allure.step("修改铲斗容量"):
            excavator_base_info.input_excavator_volume(volume=random.randint(10, 100))
        with allure.step("修改区域半径"):
            excavator_base_info.input_radius(radius=random.randint(10, 20))
        with allure.step("修改小圆半径"):
            excavator_base_info.input_cricle_radius(cricle_radius=random.randint(5, 10))
        with allure.step("输入定位设备编码"):
            excavator_base_info.input_device_loc_no(device_loc_no=random.randint(5, 10))
        with allure.step("选择电铲类型"):
            excavator_base_info.click_excavator_kind_arrow()
            time.sleep(0.5)
            excavator_base_info.select_excavator_kind()
        time.sleep(0.5)
        with allure.step("点击【确定】按钮"):
            excavator_base_info.click_confirm_btn()
        with allure.step("断言：操作成功！"):
            assert excavator_base_info.get_alert_msg() == \
                   Base.get_data(excavator_base_info, file_name='test_excavator_base_info.yaml')\
                       ['test_excavator_base_info']['success_tip']
        time.sleep(1)

    @allure.severity("blocker")
    @allure.story("电铲基本信息")
    @allure.title("查询电铲")
    def test_search_excavator(self, excavator_base_info):
        with allure.step("输入电铲名称"):
            excavator_base_info.input_excavator_name(
                Base.get_data(excavator_base_info, file_name='test_excavator_base_info.yaml')
                ['test_excavator_base_info']['excavator_name'])
        with allure.step("点击【查询】按钮"):
            excavator_base_info.click_search_btn()
            time.sleep(0.5)
        with allure.step("断言：查询结果"):
            assert excavator_base_info.get_excavator_name() == \
                   Base.get_data(excavator_base_info, file_name='test_excavator_base_info.yaml')\
                       ['test_excavator_base_info']['excavator_name']

    @allure.severity("blocker")
    @allure.story("电铲基本信息")
    @allure.title("修改电铲")
    def test_modify_excavator(self, excavator_base_info):
        with allure.step("点击“修改"):
            excavator_base_info.click_modify_excavator()
        time.sleep(0.5)
        with allure.step("修改铲斗容量"):
            excavator_base_info.input_excavator_volume(volume=random.randint(10, 100))
        with allure.step("修改区域半径"):
            excavator_base_info.input_radius(radius=random.randint(10, 20))
        with allure.step("修改小圆半径"):
            excavator_base_info.input_cricle_radius(cricle_radius=random.randint(5, 10))
            time.sleep(0.5)
        with allure.step("点击【确定】按钮"):
            excavator_base_info.click_confirm_btn()
        with allure.step("断言：操作成功！"):
            assert excavator_base_info.get_alert_msg() == \
                   Base.get_data(excavator_base_info, file_name='test_excavator_base_info.yaml')\
                       ['test_excavator_base_info']['success_tip']
        time.sleep(1)




