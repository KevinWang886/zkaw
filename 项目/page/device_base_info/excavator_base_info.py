from base.base import Base
from common.readelement import Element
import allure

excavator_base_info = Element('device_base_info', 'excavator_base_info')


class ExcavatorBaseInfoPage(Base):
    """设备基础信息管理类"""

    @allure.step("点击电铲基本信息")
    def click_excavator_base_info(self):
        self.click(excavator_base_info['电铲基本信息'])

    @allure.step("点击【新增】按钮")
    def click_add_btn(self):
        self.click(excavator_base_info['新增'])

    @allure.step("点击【查询】按钮")
    def click_search_btn(self):
        self.click(excavator_base_info['查询'])

    @allure.step("输入电铲名称")
    def input_excavator_name(self, excavator_name):
        self.send(excavator_base_info['电铲名称输入框'], excavator_name)

    @allure.step("获取列表第一行第二列（电铲名称）")
    def get_excavator_name(self):
        excavator_name = self.find(excavator_base_info['电铲名称']).text
        return excavator_name

    @allure.step("点击列表第一行第十一列（修改）")
    def click_modify_excavator(self):
        self.click(excavator_base_info['修改'])

    @allure.step("输入电铲编码")
    def input_excavator_no(self, excavator_no):
        self.send(excavator_base_info['电铲编码输入框'], excavator_no)

    @allure.step("输入电铲名称")
    def input_excavator(self, excavator):
        self.send(excavator_base_info['电铲名称输入'], excavator)

    @allure.step("输入铲斗容量")
    def input_excavator_volume(self, volume):
        self.send(excavator_base_info['铲斗容量'], volume)

    @allure.step("输入区域半径")
    def input_radius(self, radius):
        self.send(excavator_base_info['区域半径'], radius)

    @allure.step("输入小圆半径")
    def input_cricle_radius(self, cricle_radius):
        self.send(excavator_base_info['小圆半径'], cricle_radius)

    @allure.step("输入定位设备编码")
    def input_device_loc_no(self, device_loc_no):
        self.send(excavator_base_info['定位设备编码'], device_loc_no)

    @allure.step("点击【取消】按钮")
    def click_cancel_btn(self):
        self.click(excavator_base_info['取消按钮'])

    @allure.step("点击【确定】按钮")
    def click_confirm_btn(self):
        self.click(excavator_base_info['确定按钮'])

    @allure.step("获取提示")
    def get_alert_msg(self):
        msg = self.find(excavator_base_info['提示']).text
        return msg
