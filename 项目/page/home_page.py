from base.base import Base
from common.readelement import Element
import allure

home = Element('login_and_home', 'home')


class HomePage(Base):
    """主页类"""
    @allure.step("获取登录用户名")
    def get_username(self):
        username = self.find(home['用户名']).text
        return username

    @allure.step("获取页面标题")
    def get_title(self):
        title = self.find(home['标题']).text
        return title

    @allure.step("点击首页")
    def click_home(self):
        self.click(home['首页'])

    @allure.step("点击系统管理")
    def click_sys_management(self):
        self.click(home['系统管理'])

    @allure.step("点击设备基础信息管理")
    def click_base_info(self):
        self.click(home['设备基础信息管理'])

    @allure.step("点击路网管理")
    def click_net_management(self):
        self.click(home['路网管理'])

    @allure.step("点击卡车调度")
    def click_trucl_dispatch(self):
        self.click(home['卡车调度'])

    @allure.step("点击产量查询")
    def click_workload_query(self):
        self.click(home['产量查询'])

    @allure.step("点击铲齿管理")
    def click_excavator_teeth(self):
        self.click(home['设置铲齿管理'])

    @allure.step("点击大块统计")
    def click_big_tatistics(self):
        self.click(home['大块统计'])

    @allure.step("点击报表")
    def click_report(self):
        self.click(home['报表'])
