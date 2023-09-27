# fixture方法

from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    web = webdriver.Chrome()
    web.maximize_window()
    web.get('https://www.mi.com/')
    web.implicitly_wait(10)
    return web
