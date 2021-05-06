import time
from page.home_page import HomePage
import pytest
import allure
from page.login import LoginPage
from base.base import Base


class TestLoin():

    @pytest.fixture(autouse=True)
    def open_page(self, login):
        login.open("/truck-dispatch/?#/login")
        time.sleep(0.5)

    @allure.severity("blocker")
    @allure.story("登录")
    @allure.title("正确账号密码登录")
    def test_login(self, login):
        with allure.step("1、输入账号"):
            login.input_account(Base.get_data(login, file_name='test_login.yaml')['test_login']['account'])
        with allure.step("2、输入密码"):
            login.input_password(Base.get_data(login, file_name='test_login.yaml')['test_login']['password'])
        with allure.step("3、点击登录按钮"):
            login.click_login_btn()
        with allure.step("4、断言"):
            assert HomePage.get_username(login) == \
                   Base.get_data(login, file_name='test_login.yaml')['test_login']['username']
            assert HomePage.get_title(login) == \
                Base.get_data(login, file_name='test_login.yaml')['test_login']['title']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("不输入账号密码登录")
    def test_login_without_account_and_pwd(self, login):
        with allure.step("3、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("4、断言"):
            # print(LoginPage.get_account_error(login))
            assert LoginPage.get_account_error(login) == \
                   Base.get_data(login, file_name='test_login.yaml')['test_login']['account_error']
            assert LoginPage.get_pwd_error(login) == \
                Base.get_data(login, file_name='test_login.yaml')['test_login']['password_error']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("不输入账号登录")
    def test_login_without_account(self, login):
        with allure.step("2、输入密码"):
            login.input_password(Base.get_data(login, file_name='test_login.yaml')['test_login']['password'])
        with allure.step("3、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("4、断言"):
            # print(LoginPage.get_account_error(login))
            assert LoginPage.get_account_error(login) == \
                   Base.get_data(login, file_name='test_login.yaml')['test_login']['account_error']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("不输入密码登录")
    def test_login_without_password(self, login):
        with allure.step(Base.get_data(login, file_name='test_login.yaml')['test_login']['account']):
            login.input_account("wcy")
        with allure.step("3、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("4、断言"):
            # print(LoginPage.get_account_error(login))
            assert LoginPage.get_pwd_error(login) == \
                   Base.get_data(login, file_name='test_login.yaml')['test_login']['password_error']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("输入错误账号密码登录")
    def test_login_with_wrong_account(self, login):
        with allure.step(Base.get_data(login, file_name='test_login.yaml')['test_login']['incorrect_account']):
            login.input_account(Base.get_data(login, file_name='test_login.yaml')['test_login']['incorrect_password'])
        with allure.step("2、输入密码"):
            login.input_password("123456")
        with allure.step("3、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("4、断言"):
            # print(LoginPage.get_account_error(login))
            assert LoginPage.get_error_msg(login) == \
                   Base.get_data(login, file_name='test_login.yaml')['test_login']['error_msg']
