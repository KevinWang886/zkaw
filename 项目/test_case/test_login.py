import time
from common.readelement import Element
from page.home_page import HomePage
import pytest
import allure
from page.login import LoginPage
from config.conf import TEST_DATA_PATH


test_login = Element(TEST_DATA_PATH,  '', 'test_login').data


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
            # login.input_account(Base.get_data(login, file_name='test_login.yaml')['test_login']['account'])
            login.input_account(test_login["account"])
        with allure.step("2、输入密码"):
            login.input_password(test_login["password"])
        with allure.step("3、点击登录按钮"):
            login.click_login_btn()
        with allure.step("4、断言"):
            assert HomePage.get_username(login) == test_login["username"]
            assert HomePage.get_title(login) == test_login['title']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("不输入账号密码登录")
    def test_login_without_account_and_pwd(self, login):
        with allure.step("1、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("2、断言"):
            assert LoginPage.get_account_error(login) == test_login['account_error']
            assert LoginPage.get_pwd_error(login) == test_login['password_error']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("不输入账号登录")
    def test_login_without_account(self, login):
        with allure.step("1、输入密码"):
            login.input_password(test_login['password'])
        with allure.step("2、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("3、断言"):
            # print(LoginPage.get_account_error(login))
            assert LoginPage.get_account_error(login) == test_login['account_error']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("不输入密码登录")
    def test_login_without_password(self, login):
        with allure.step("1、输入账号"):
            login.input_account(test_login['account'])
        with allure.step("2、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("3、断言"):
            # print(LoginPage.get_account_error(login))
            assert LoginPage.get_pwd_error(login) == test_login['password_error']

    @allure.severity("normal")
    @allure.story("登录")
    @allure.title("输入错误账号密码登录")
    def test_login_with_wrong_account(self, login):
        with allure.step("1、输入错误账号"):
            login.input_account(test_login['incorrect_account'])
        with allure.step("2、输入错误密码"):
            login.input_password(test_login['incorrect_password'])
        with allure.step("3、点击登录按钮"):
            login.click_login_btn()
            time.sleep(0.5)
        with allure.step("4、断言"):
            # print(LoginPage.get_account_error(login))
            assert LoginPage.get_error_msg(login) == test_login['error_msg']
