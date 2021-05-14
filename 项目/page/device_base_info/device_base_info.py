from base.base import Base
from common.readelement import Element
import allure
from config.conf import ELEMENT_PATH

device_base_info = Element(ELEMENT_PATH, 'device_base_info', 'device_base_info')


# 设备基础信息管理模块
class DeviceBaseInfoPage(Base):
    """设备基础信息管理类"""

    @allure.step("点击电铲信息管理")
    def click_excavator_info(self):
        self.click(device_base_info['电铲信息管理'])

    @allure.step("查看电铲信息管理菜单是否展开")
    def is_excavator_info_menu_open(self):
        if self.find(device_base_info['电铲信息管理菜单']).get_attribute('style') == 'display: none;':
            return True
        else:
            return False

    @allure.step("点击卸点信息管理")
    def click_uploading_info(self):
        self.click(device_base_info['卸点信息管理'])

    @allure.step("点击卡车信息管理")
    def click_truck_info(self):
        self.click(device_base_info['卡车信息管理'])

    @allure.step("点击班组管理")
    def click_group(self):
        self.click(device_base_info['班组管理'])

    @allure.step("点击班次管理")
    def click_switch(self):
        self.click(device_base_info['班次管理'])

    @allure.step("点击司机管理")
    def click_driver(self):
        self.click(device_base_info['司机管理'])
