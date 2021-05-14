import time
import pytest
import allure
import random
from common.readelement import Element
from config.conf import TEST_DATA_PATH

test_excavator_base_info = Element(TEST_DATA_PATH,  'test_device_base_info', 'test_excavator_base_info').data


class TestExcavatorBaseInfo():

    @pytest.fixture(scope='module', autouse=True)
    def go_to_excavator_base_info(self, go_to_excavator_management, excavator_base_info):
        if go_to_excavator_management.is_excavator_info_menu_open():
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
        with allure.step("1、点击新增按钮"):
            excavator_base_info.click_add_btn()
        time.sleep(0.5)
        with allure.step("2、输入电铲编号"):
            excavator_base_info.input_excavator_no(excavator_no=random.randint(10000, 99999))
        with allure.step("3、输入电铲名称"):
            excavator_base_info.input_excavator(excavator="电铲" + str(random.randint(10000, 99999)))
        with allure.step("4、修改铲斗容量"):
            excavator_base_info.input_excavator_volume(volume=random.randint(10, 100))
        with allure.step("5、修改区域半径"):
            excavator_base_info.input_radius(radius=random.randint(10, 20))
        with allure.step("6、修改小圆半径"):
            excavator_base_info.input_cricle_radius(cricle_radius=random.randint(5, 10))
        with allure.step("7、输入定位设备编码"):
            excavator_base_info.input_device_loc_no(device_loc_no=random.randint(5, 10))
        with allure.step("8、选择电铲类型"):
            excavator_base_info.click_excavator_kind_arrow()
            time.sleep(0.5)
            excavator_base_info.select_excavator_kind()
        time.sleep(0.5)
        with allure.step("9、点击【确定】按钮"):
            excavator_base_info.click_confirm_btn()
        with allure.step("10、断言：操作成功！"):
            assert excavator_base_info.get_alert_msg() == test_excavator_base_info['success_tip']
        time.sleep(1)

    @allure.severity("blocker")
    @allure.story("电铲基本信息")
    @allure.title("查询电铲")
    def test_search_excavator(self,  excavator_base_info):
        with allure.step("1、输入电铲名称"):
            excavator_base_info.input_excavator_name(test_excavator_base_info['excavator_name'])
        with allure.step("2、点击【查询】按钮"):
            excavator_base_info.click_search_btn()
            time.sleep(0.5)
        with allure.step("3、断言：查询结果"):
            assert excavator_base_info.get_excavator_name() == test_excavator_base_info['excavator_name']

    @allure.severity("blocker")
    @allure.story("电铲基本信息")
    @allure.title("修改电铲")
    def test_modify_excavator(self, excavator_base_info):
        with allure.step("1、点击“修改"):
            excavator_base_info.click_modify_excavator()
        time.sleep(0.5)
        with allure.step("2、修改铲斗容量"):
            excavator_base_info.input_excavator_volume(volume=random.randint(10, 100))
        with allure.step("3、修改区域半径"):
            excavator_base_info.input_radius(radius=random.randint(10, 20))
        with allure.step("4、修改小圆半径"):
            excavator_base_info.input_cricle_radius(cricle_radius=random.randint(5, 10))
            time.sleep(0.5)
        with allure.step("5、点击【确定】按钮"):
            excavator_base_info.click_confirm_btn()
        time.sleep(1)
        with allure.step("6、断言：操作成功！"):
            assert excavator_base_info.get_alert_msg() == test_excavator_base_info['success_tip']



