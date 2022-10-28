# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome()
# 设置隐式等待为10秒
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
