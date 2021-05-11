from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
import os
import yaml
from common import log
from config.conf import TEST_DATA_PATH

"""封装selenium基本操作"""


# class LocatorTypeError(Exception):
#     pass
#
#
# class ElementNotFound(Exception):
#     pass


class Base():
    """基于原生的selenium做二次封装"""

    def __init__(self, driver:webdriver.Chrome, base_url='',  timeout=10, t=0.5):
        self.driver = driver
        self.timeout = timeout
        self.t = t
        self.base_url = base_url

    def open(self, url):
        '''跟get方法一样，这里支持相对路径url'''
        if "http" in url:
            self.driver.get(url)
            log.logger("打开网页：%s" % (self.base_url + url))
        self.driver.get(self.base_url + url)

    def find(self, locator):
        """locator必须是元祖类型：loc = ('id','value1') 定位到元素，返回元素对象，没定位到，Timeout异常"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            log.logger("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            try:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            except TimeoutException as msg:
                raise log.logger("定位元素出现超时！！！！")
            return ele

    def finds(self, locator):
        '''复数定位，返回elements对象 list  '''
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            log.logger("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            return eles

    def send(self, locator, text):
        '''发送文本'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.clear()
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法输入，解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    def click(self, locator):
        '''点击元素'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法点击，解决办法：定位唯一元素，或先让元素可见，或者用js点击")

    def clear(self, locator):
        '''清空输入框文本'''
        ele = self.find(locator)
        ele.clear()

    def is_selected(self, locator):
        """判断元素是否被选中，返回bool值"""
        ele = self.find(locator)
        r = ele.is_selected()
        return r

    def is_element_exist(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_title(self, title):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text):
        """返回bool值"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value):
        """返回bool值，value为空字符串，返回False"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        '''判断alert是否存在，存在返回alert对象'''
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_text(self, locator):
        """获取文本"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            t = self.find(locator).text
            return t
        except:
            log.logger("获取text失败，返回''")
            return ""

    def get_attribute(self, locator, name):
        """获取属性"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            element = self.find(locator)
            return element.get_attribute(name)
        except:
            log.logger("获取%s属性失败，返回''"%name)
            return ''

    def js_focus_element(self, locator):
        """聚焦元素"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        """通过索引，index是索引第几个，从0开始，默认第一个"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """通过value属性"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def select_object(self, locator):
        '''返回select对象'''
        element = self.find(locator)
        return Select(element)

    def switch_iframe(self, id_index_locator):
        """切换iframe"""
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            log.logger("iframe切换异常")

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            log.logger("alert不存在")
            return ""
        else:
            return r

    def get_alert_text(self):
        '''获取alert文本值, 并点确定'''
        alert = self.is_alert()
        if alert:
            text = alert.text
            log.logger("获取到alert内容：%s" % text)
            # 点确定按钮
            alert.accept()
            log.logger("点alert确定按钮")
        else:
            text = ""
            log.logger("没有获取到alert内容：")
        return text

    def move_to_element(self, locator):
        """鼠标悬停操作"""
        if not isinstance(locator, tuple):
            raise log.logger("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        ele = self.find(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_data(self, file_name):  # 获取测试用例测试数据的yaml文件
        yaml_path = os.path.join(TEST_DATA_PATH, file_name)
        file = open(yaml_path, mode='r', encoding='utf-8')
        data = yaml.safe_load(file)
        return data

#
# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     web = Base(driver)  # 实例化
#     driver.get("https://www.baidu.com")
#     loc_1 = ("id", "kw")
#     web.send(loc_1, "hello")
#
#     # Python is likely shutting down
#     driver.close()
