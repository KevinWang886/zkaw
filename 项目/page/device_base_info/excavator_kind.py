from base.base import Base
from common.readelement import Element
import allure

excavator_kind = Element('device_base_info', 'excavator_kind')


class ExcavatorKind(Base):
    """电铲物料维护类"""

    @allure.step("输入电铲名称")
    def input_excavator_name(self, excavator_name):
        self.send(excavator_kind['电铲名称'], excavator_name)

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
