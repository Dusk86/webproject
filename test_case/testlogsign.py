import pytest
import allure
import logging
from selenium.webdriver.common.by import By
from webjob1.common.yamlutil import YamlUtil
from webjob1.configs.base_tools import Base
import sys
sys.setrecursionlimit(100000)

"""
一般实际项目开发中都会使用requirements.txt文件保存插件名
通过：pip install -r requirements.txt 安装所有插件

#关闭当前窗口
driver.close

冻结页面,在控制台输入代码
setTimeout(function(){debugger}, 500)
"""
base_page = Base('https://www.mi.com/')
logger = logging.getLogger()
class Testcase:
    # @pytest.mark.parametrize('loginfo', YamlUtil().userlogin('E:/webproject/webjob1/data/login.yml', 'login'))
    # @allure.title('登录')
    # def test_clicklogin(self, loginfo):
    #     print(loginfo['login']['username'])
    #     with allure.step('1.点击登录按钮'):
    #         base_page.click(By.CLASS_NAME, 'user-name')
    #         base_page.wait(5)
    #     with allure.step(f"2.输入账号: {loginfo['login']['username']}"):
    #         base_page.input(By.NAME, 'account', loginfo['login']['username'])
    #     with allure.step(f"3.输入密码：{loginfo['login']['password']}"):
    #         base_page.input(By.NAME, 'password', loginfo['login']['password'])
    #         base_page.wait(1)
    #     with allure.step('4.显示密码，两秒后隐藏'):
    #         base_page.click(By.XPATH, '//div[@class="mi-password-field__adornment mi-input-adornment"]')
    #         base_page.wait(2)
    #         base_page.click(By.XPATH, '//div[@class="mi-password-field__adornment mi-input-adornment"]')
    #         base_page.wait(1)
    #     with allure.step('5.点击登录按钮'):
    #         base_page.click(By.XPATH, '//button[@type="submit"]')
    #         base_page.wait(1)
    #     with allure.step('6.弹出弹窗'):
    #         base_page.assert_locate(By.XPATH, '//div[@class="mi-toast mi-toast-desktop"]')
    #     with allure.step('7.判断弹窗文字是否为：请您同意用户条款'):
    #         prompt_text = base_page.getattribute(By.XPATH, '//div[@class="mi-toast mi-toast-desktop"]/div', 'textContent')
    #         assert prompt_text == '请您同意用户条款'
    #         base_page.wait(1)
    #     with allure.step('8.点击 已阅读并同意小米账号 用户协议 和 隐私政策'):
    #         base_page.click(By.XPATH, '//input[@class="ant-checkbox-input"]')
    #         base_page.wait(1)
    #     with allure.step('9.点击登录按钮'):
    #         base_page.click(By.XPATH, '//button[@type="submit"]')
    #         base_page.wait(1)
    #     with allure.step('10.用户名或密码不正确'):
    #         base_page.assert_locate(By.XPATH, '//div[@class="mi-form-helper-text mi-form-helper-text--error"]')
    #         base_page.wait(2)

    @pytest.mark.parametrize('sigin', YamlUtil().userlogin('E:/webproject/webjob1/data/login.yml', 'signin'))
    @allure.title('注册')
    def test_sign_in(self, sigin):
        with allure.step('1.点击登录按钮'):
            base_page.click(By.CLASS_NAME, 'user-name')
        with allure.step('1.点击注册'):
            base_page.click(By.XPATH, '//div[@class="ant-tabs-tab"]')
            base_page.wait(5)
        with allure.step('2.国家是否默认中国'):
            prompt_text = base_page.getattribute(By.XPATH, '//span[@title="中国"]', 'textContent')
            assert prompt_text == '中国'
        with allure.step('3.鼠标移上是否有提示'):
            base_page.move_to_element(By.XPATH, '//div[@class="mi-select-field mi-select-field--with-label mi-form-field mi-form-field--fullwidth mi-form-field--bordered"]')
            base_page.wait(2)
            toast = base_page.getattribute(By.XPATH, '//div[@class="mi-status-text__text"]', 'textContent')
            assert toast == '系统会根据您选择的国家/地区的法律法规存储您的个人信息'
            base_page.wait(1)
        with allure.step('4.点击 选择国家/地区，是否有选择框'):
            base_page.click(By.XPATH, '//div[@class="mi-select-field mi-select-field--with-label mi-form-field mi-form-field--fullwidth mi-form-field--bordered"]')
            base_page.assert_locate(By.XPATH, '//div[@class="rc-virtual-list-holder"]')
        with allure.step('5.选择国家'):
            # base_page.click(By.XPATH, '//div[@class="ant-select-item ant-select-item-option ant-select-item-option-grouped"]/*[position()=17]')
            # country_name = base_page.getattribute(By.XPATH, '//div[@class="mi-region-field__name"]', 'textContent')
            country_name = base_page.locate(By.XPATH, '//div[@class="mi-region-field__name"]')
            for i in country_name:
                print()
            print('控制台上打印：', country_name)
            base_page.wait(5)
        base_page.quite()

































