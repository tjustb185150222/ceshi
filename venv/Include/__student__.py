import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

'''学生管理系统登录功能'''


def testLogin(username, password, text01=None):
    driver.get('http://localhost:8090')
    driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(3)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#form > div.mt-20.skin-minimal > div:nth-child(3) > div > ins").click()
    time.sleep(3)
    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(3)
    '''text01 = driver.find_element(By.CSS_SELECTOR,
                                 "#tabs > div.tabs-panels.tabs-panels-noborder > div > div > p:nth-child(1)").text'''
    dizhi = driver.current_url
    print(dizhi)
    if dizhi == 'http://localhost:8090/system/index':
        text01 = driver.find_element(By.CSS_SELECTOR,
                                     "#tabs > div.tabs-panels.tabs-panels-noborder > div > div > p:nth-child(1)").text
        if text01 == "admin":
            print("登陆成功")
            driver.get_screenshot_as_file('E:\pycharmdata\ceshi\img\学生管理系统登录功能成功.png')
    if dizhi != 'http://localhost:8090/system/index':
        text02 = driver.find_element(By.CSS_SELECTOR,
                                     "body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text
        if text02 == "用户名或密码错误":
            print("登陆失败")
            driver.get_screenshot_as_file('E:\pycharmdata\ceshi\img\学生管理系统登录功能失败.png')


'''学生管理系统-学生信息管理-学生列表-添加功能'''


def __addStudent__(student01, password, phone, qq):
    testLogin("admin", 123456)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "nav").click()
    time.sleep(3)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="tabs"]/div[2]/div[2]/div/iframe'))
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "l-btn-text").click()
    time.sleep(3)
    # 清空输入框内容
    driver.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys(student01)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[3]/td[2]/span/span/a').click()
    time.sleep(3)
    driver.find_element(By.ID, "_easyui_combobox_i1_0").click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[4]/td[2]/span/input[1]').send_keys(phone)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[5]/td[2]/span/input[1]').send_keys(qq)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[6]/td[2]/span/span/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="_easyui_combobox_i6_1"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[7]/td[2]/input').send_keys(
        'E:\pycharmdata\ceshi\img\学生管理系统登录功能失败.png')
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/a[1]/span/span[1]').click()
    time.sleep(3)


def testTearDown():
    driver.quit()


if __name__ == "__main__":
    # testLogin('admin', 123456)
    __addStudent__("测试学生添加01", 123456, 18545632563, 2558646325)
    testTearDown()





