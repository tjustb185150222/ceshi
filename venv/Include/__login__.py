import time
from urllib import response

from Tools.scripts.serve import app
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开一个CSDN网址
driver.get('https://www.csdn.net/')
# 获取页面地址
print(driver.current_url)
# 打印页面标题
print(driver.title)
# 通过Id定位搜索框，输入搜索的问题
driver.find_element(By.ID, "toolbar-search-input").send_keys("软件测试面试题")
time.sleep(5)
# 通过Id定位到搜索按钮的位置，进行点击，此时跳转到一个新的页面
driver.find_element(By.ID, "toolbar-search-button").click()
'''
在selenium中默认不切换到新的页面，若跳转到新的页面需要定位到新打开的页面（窗口）
'''
# 切换到新的页面（窗口）,driver.window_handles[-1]获取当前页面即跳转后的页面
# driver.switch_to_window(driver.window_handles[-1])selenium4.0版本以下使用
driver.switch_to.window(driver.window_handles[-1])
# driver.refresh()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/div[1]/h3/a').click()
'''
driver.find_element(By.CSS_SELECTOR, '#app > div.so-list-detail > div.main.clearfix > div.main-lt > div.list-container '
                                     '> div > div.list-item.isFirst > div > div.item-hd > h3 > a').click()
'''
# driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/div[1]/h3/a")
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element(By.CLASS_NAME, "isdefault").click()
time.sleep(3)
driver.switch_to.frame('passport_iframe')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "body > div > div > div > div.login-box > div.login-box-bottom > div > div > span.login-third-item.login-third-qq").click()
time.sleep(3)
driver.find_element(By.ID,"img_out_2558513267").click()
time.sleep(3)
# quit()关闭所有的浏览器窗口
driver.quit()
# close()关闭单个的浏览器窗口
# driver.close()
