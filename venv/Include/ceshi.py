# 导包
from time import sleep
from selenium import webdriver
#from selenium.webdriver import ActionChains

# 实例化浏览器
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 打开网址
driver.get('https://www.jjjgyy.com:6443/pangu/login')

# 需求(输入用户名)
#ele = driver.find_element_by_id('username')
ele = driver.find_element(By.ID,'username')
#ele = driver.find_element(By.css_selecto,"#kv")
ele.send_keys('demo@ys')
sleep(2)

#需求（输入密码）
ele = driver.find_element(By.ID,'password')
#ele = driver.find_element(By.css_selecto,"#kv")
ele.send_keys('1234568')
sleep(3)




# 清空
#ele.clear()
#ele.send_keys('王嘉尔')

#ele = driver.find_element_by_id('su').click()



ele = driver.find_element(By.CLASS_NAME,'ant-btn').click()
sleep(3)


re = driver.find_element(By.CLASS_NAME,'ant-message-custom-content').text

if re == "账号或密码错误":
     driver.get_screenshot_as_file('E:\pycharmdata\ceshi\img\登陆失败.png')
     print("登陆失败")
else:
    print("登陆成功")



# 时间轴看效果
sleep(3)

# 关闭页面
#driver.quit()
