from selenium import webdriver
from time import sleep



driver = webdriver.Chrome()
driver.get('https://xqgl.bhteda.com/#/login')

def test_login() :
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/form/div[1]/div/div[1]/input').send_keys('bhteda')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/form/div[2]/div/div/input').send_keys('teda123456')
    sleep(2)

    driver.find_element_by_class_name('el-button').click()

    sleep(3)
    driver.get_screenshot_as_file('E:\pycharmdata\ceshi\img\智慧社区登陆成功.png')
    sleep(5)

test_login()
'''
xnz = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[1]/div/span').click()
sleep(3)

xnzg = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[1]/ul/li[4]/span').click()
sleep(5)

xn = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/button/span').click()
sleep(3)



xn_ll = driver.find_element_by_xpath('//*[@id="el-collapse-content-5558"]/div/div/div[2]/div/div/div/input').send_keys('测试')

'''
