import time
from config.conf import ELEMENT_PATH
from base.base import Base
from common.readelement import Element
import allure

excavator_kind = Element(ELEMENT_PATH, 'device_base_info', 'excavator_kind')


class ExcavatorKind(Base):
    """电铲物料维护类"""

    @allure.step("输入电铲名称")
    def input_excavator_name(self, excavator_name):
        self.send(excavator_kind['电铲名称'], excavator_name)
        self.click_query_btn()

    @allure.step("点击【查询】按钮")
    def click_query_btn(self):
        self.click(excavator_kind['查询'])

    @allure.step("点击【修改】")
    def click_modify_btn(self):
        self.click(excavator_kind['修改'])

    @allure.step("获取查询列电铲名称")
    def get_excavator_name(self):
        excavator_name = self.find(excavator_kind['列表电铲名称']).text
        return excavator_name

    @allure.step("获取修改页面物料")
    def get_kind_name(self):
        kind_name = self.find(excavator_kind['下拉选项']).text
        return kind_name

    @allure.step("点击下拉选项")
    def click_dropdown_arrow(self):
        self.click(excavator_kind['下拉选项'])

    @allure.step("选中物料")
    def select_kind(self):
        kind_name = self.get_kind_name()
        self.click_dropdown_arrow()
        if kind_name == "岩石":
            time.sleep(0.5)
            self.click(excavator_kind['矿石'])
        else:
            time.sleep(0.5)
            self.click(excavator_kind['岩石'])
        self.click_confirm_btn()

    @allure.step("点击【取消】按钮")
    def click_cancel_btn(self):
        self.click(excavator_kind['取消按钮'])

    @allure.step("点击【确定】按钮")
    def click_confirm_btn(self):
        self.click(excavator_kind['确定按钮'])

    @allure.step("获取提示信息")
    def get_alert_msg(self):
        alert_msg = self.find(excavator_kind['提示']).text
        return alert_msg
