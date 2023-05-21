import asyncio
import logging
import time
import webbrowser
from asyncio import wait

from selenium import webdriver
from selenium.webdriver.common.by import By

from Comm.Log import log_init

webdriver = webdriver.Chrome()
webdriver.maximize_window()


def test01():
    webdriver.get("https://www.baidu.com/")
    webdriver.find_element(By.LINK_TEXT, 'hao123').click()
    time.sleep(3)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    time.sleep(3)
    webdriver.find_element(By.LINK_TEXT, "网易").click()
    time.sleep(3)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    webdriver.current_url
    time.sleep(5)
    webdriver.quit()


def test02(test):
    webdriver.get("https://www.csdn.net/")
    webdriver.find_element(By.ID, "toolbar-search-input").send_keys("软件测试面试题")
    time.sleep(3)
    webdriver.find_element(By.ID, "toolbar-search-button").click()
    time.sleep(3)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    time.sleep(3)
    webdriver.find_element(By.LINK_TEXT, test).click()
    time.sleep(3)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    time.sleep(3)
    text01 = webdriver.find_element(By.CLASS_NAME,"title-article").text
    print(text01)
    if text01 == '软件测试面试题（全）':
        print("搜索功能正常")
        webdriver.get_screenshot_as_file('E:\pycharmdata\ceshi\img\CSDN搜索功能成功.png')
    else:
        print("搜索功能失败")




def teardown():
    webdriver.quit()

if __name__ == '__main__':
    test01()
    log_init()
    logging.getLogger('mian.test01')

