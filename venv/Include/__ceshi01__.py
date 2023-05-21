from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def __ceshi01__():
    driver = webdriver.Chrome()
    driver.get('https://wl.bhzhjz.com/#/login')

    ele = driver.find_element(By.CSS_SELECTOR,
                              '#app > div > div.login-box > div.login-right > div > form > div:nth-child(1) > div > div > span > span > input')

    sleep(3)
    ele.send_keys('18621833404')

    sleep(3)

    ele = driver.find_element(By.CSS_SELECTOR,
                              '#app > div > div.login-box > div.login-right > div > form > div:nth-child(2) > div > div > span > span > input')
    ele.send_keys('123456')
    sleep(3)

    driver.find_element(By.CLASS_NAME, 'ant-form-item-children').click()


__ceshi01__()




