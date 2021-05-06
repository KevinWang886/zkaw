from base.base import Base
from common.readelement import Element
import allure

login = Element('login_and_home', 'login')


class LoginPage(Base):
    """登录类"""
    @allure.step("输入账号")
    def input_account(self, account):
        self.send(login['账号'], account)
        # sleep()

    @allure.step("输入密码")
    def input_password(self, pwd):
        self.send(login['密码'], pwd)

    @allure.step("点击登录按钮")
    def click_login_btn(self):
        self.click(login['登录'])

    @allure.step("获取错误账号空提示")
    def get_account_error(self):
        account_error = self.get_text(login['账号空'])
        return account_error

    @allure.step("获取错误密码空提示")
    def get_pwd_error(self):
        password_error = self.get_text(login['密码空'])
        return password_error

    @allure.step("获取错误提示")
    def get_error_msg(self):
        error_msg = self.find(login['错误提示']).text
        return error_msg
