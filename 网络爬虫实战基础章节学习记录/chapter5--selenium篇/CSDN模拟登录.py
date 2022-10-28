# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://passport.csdn.net/login")
# 有可能网络加载慢，这里设置加载时进行暂停
sleep(10)

# 因为CSDN登录页面默认是扫码登录，所以打开登录页面之后需要模拟
driver.find_element_by_xpath("//div[@class='main-select']/ul/li[2]").click()
# 先暂停3秒，以防止页面未加载完成导致获取不到用户名、密码元素
sleep(3)

# 自动填充用户密码
username = driver.find_element_by_xpath("//input[@placeholder='手机号/邮箱/用户名']")
username.send_keys("1111@qq.com")
passwd = driver.find_element_by_xpath("//input[@placeholder='密码']")
passwd.send_keys("Gou1213520")

# 获取登录按钮，模拟单机提交
driver.find_element_by_xpath("//div[@class='form-group']/div/button[@data-type='account']").click()

