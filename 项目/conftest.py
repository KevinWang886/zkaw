import pytest
import os
import allure
from selenium import webdriver

driver = None


# 打开浏览器
@pytest.fixture(scope="session", name="driver")
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()
    yield driver
    # quit是退出浏览器
    driver.quit()


# 测试地址根路径
@pytest.fixture(scope="session")
def base_url():
    # url = Base(self).get_data()['test_url']['base_url']
    url = "http://61.189.55.170:8074/"
    return url


# 测试用例执行失败获取截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
