# 公共方法封装
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Base:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # 打开网址
    def openweb(self, url):
        self.driver.get(url)

    # 定位
    def locate(self, ele_type, ele_val):
        try:
            ele = self.driver.find_element(ele_type, ele_val)
            return ele
        except:
            raise

    # 输入
    def input(self, ele_type, ele_val, txt):
        self.locate(ele_type, ele_val).send_keys(txt)

    # 点击
    def click(self, ele_type, ele_val):
        self.locate(ele_type, ele_val).click()

    # 鼠标移上
    def move_to_element(self, ele_type, ele_val):
        element = self.locate(ele_type, ele_val)
        ActionChains(self.driver).move_to_element(element).perform()

    # 切换窗口
    def switch_to_windows(self):
        # 获取当前句柄
        current_window = self.driver.current_window_handle
        # 切换到原来句柄
        self.driver.switch_to.window(current_window)
        # 获取所有句柄
        windows = self.driver.window_handles
        # 切换到最新句柄
        self.driver.switch_to.window(windows[-1])

    # 切换到iframe
    def switch_to_iframe(self, iframe_value):
        self.driver.switch_to.frame(iframe_value)

    # 固定等待
    @staticmethod     # python装饰器，用于标记静态方法
    def wait(second_num):
        sleep(second_num)

    # 断言
    def assert_locate(self, ele_type, ele_val):
        # 定位元素后，判断是否为空
        try:
            assert self.locate(ele_type, ele_val) is not None
            return True
        except:
            raise

    # 获取元素的属性值
    def getattribute(self, ele_type, ele_val, attribute_name):
        element = self.locate(ele_type, ele_val)
        if element is not None:
            return element.get_attribute(attribute_name)

    # 退出浏览器
    def quite(self):
        self.driver.quit()