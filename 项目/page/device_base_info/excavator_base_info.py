from base.base import Base
from common.readelement import Element
import allure
import random
from config.conf import ELEMENT_PATH

excavator_base_info = Element(ELEMENT_PATH, 'device_base_info', 'excavator_base_info')


class ExcavatorBaseInfoPage(Base):
    """电铲基本信息管理类"""

    @allure.step("点击电铲基本信息")
    def click_excavator_base_info(self):
        self.click(excavator_base_info['电铲基本信息'])

    @allure.step("点击电铲物料维护")
    def click_excavator_kind(self):
        self.click(excavator_base_info['电铲物料维护'])

    @allure.step("点击电铲状态维护")
    def click_excavator_status(self):
        self.click(excavator_base_info['电铲状态维护'])

    @allure.step("点击禁止卸点维护")
    def click_excavator_prohibat_uploading(self):
        self.click(excavator_base_info['禁止卸点维护'])

    @allure.step("点击锁定卡车维护")
    def click_excavator_lock_truck(self):
        self.click(excavator_base_info['锁定卡车维护'])

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

    @allure.step("点击电铲类型下拉箭头")
    def click_excavator_kind_arrow(self):
        self.click(excavator_base_info['下拉箭头'])

    @allure.step("选择电铲类型")
    def select_excavator_kind(self):
        excavator_kind = random.randint(1, 5)
        if excavator_kind == 1:
            self.click(excavator_base_info['下拉选项-大铲车'])
        elif excavator_kind == 2:
            self.click(excavator_base_info['下拉选项-小铲车'])
        elif excavator_kind == 3:
            self.click(excavator_base_info['下拉选项-中型铲'])
        else:
            self.click(excavator_base_info['下拉选项-巨型铲'])

    @allure.step("选择电铲状态")
    def select_excavator_status(self):
        excavator_status = random.randint(1, 3)
        if excavator_status == 1:
            self.click(excavator_base_info['禁用'])
        else:
            self.click(excavator_base_info['启用'])

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
