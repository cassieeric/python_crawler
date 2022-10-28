# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# clear()清除文本
browser.find_element_by_id("kw").clear()

# send_keys(value)模拟按键输入
browser.find_element_by_id("kw").send_keys("测试输入值")

# 模拟单机
browser.find_element_by_id("su").click()

# submit()提交
search_text = browser.find_element_by_id("kw")
search_text.send_keys("selenium")
search_text.submit()
browser.quit()
