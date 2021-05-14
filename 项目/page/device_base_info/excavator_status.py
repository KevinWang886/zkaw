import random
import time

from config.conf import ELEMENT_PATH
from base.base import Base
from common.readelement import Element
import allure


excavator_status = Element(ELEMENT_PATH, 'device_base_info', 'excavator_status')


class ExcavatorStatus(Base):
    '''电铲状态维护类'''

    @allure.step("输入电铲名称")
    def input_excavator_name(self, excavator_name):
        self.send(excavator_status["电铲名称输入框"], excavator_name)

    @allure.step("点击【查询】按钮")
    def click_query_btn(self):
        self.click(excavator_status["查询"])

    @allure.step("点击'修改'")
    def click_modify_btn(self):
        self.click(excavator_status["修改"])

    @allure.step("获取列表中电铲名称")
    def get_excavator_name_in_table(self):
        excavator_name = self.get_text(excavator_status["列表电铲名称"])
        return excavator_name

    @allure.step("获取列表中电铲状态")
    def get_excavator_status_in_table(self):
        status = self.get_text(excavator_status["列表电铲状态"])
        return status

    @allure.step("修改电铲状态")
    def modify_excavator_status(self):
        if self.get_excavator_status_in_table() == "就绪":
            self.select_breakdown()
        elif self.get_excavator_status_in_table() == "故障":
            self.select_backup()
        else:
            self.click(excavator_status["状态-就绪"])

    @allure.step("输入起始时间")
    def select_start_end_time(self, ):
        self.click(excavator_status["起始时间"])
        time.sleep(0.5)
        self.click(excavator_status["此刻"])

    @allure.step("选择'故障'")
    def select_breakdown(self):
        self.click(excavator_status["状态-故障"])
        self.select_start_end_time()
        self.click(excavator_status["下拉箭头"])
        time.sleep(0.5)
        num = random.randint(1, 6)
        if num == 1:
            self.click(excavator_status["故障-路段拥堵"])
        elif num == 2:
            self.click(excavator_status["故障-排队"])
        elif num == 3:
            self.click(excavator_status["故障-检修"])
        elif num == 4:
            self.click(excavator_status["故障-加油"])
        else:
            self.click(excavator_status["故障-非正常熄火"])

    @allure.step("选择'备用'")
    def select_backup(self):
        self.click(excavator_status["状态-备用"])
        self.click(excavator_status["下拉箭头"])
        time.sleep(0.5)
        num = random.randint(1, 6)
        if num == 1:
            self.click(excavator_status["备用-路段拥堵"])
        elif num == 2:
            self.click(excavator_status["备用-排队"])
        elif num == 3:
            self.click(excavator_status["备用-检修"])
        elif num == 4:
            self.click(excavator_status["备用-加油"])
        else:
            self.click(excavator_status["备用-非正常熄火"])

    @allure.step("点击【取消】按钮")
    def click_cancel_btn(self):
        self.click(excavator_status["取消"])

    @allure.step("点击【确定】按钮")
    def click_confirm_btn(self):
        self.click(excavator_status["确定"])

    @allure.step("获取提示信息")
    def get_alert_msg(self):
        alert_msg = self.get_text(excavator_status["提示"])
        return alert_msg


