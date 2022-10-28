# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
print("*********搜索以前***********")

# 打印当前页面的title
title = browser.title
print(title)

# 打印当前页面的URL
now_url = browser.current_url
print(now_url)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
sleep(1)

print("*********弹出搜索***********")
# 再次打印当前页面的title
title = browser.title
print(title)

# 打印当前页面的URL
now_url = browser.current_url
print(now_url)

# 获取结果数目
user = browser.find_element_by_class_name("nums").text
print(user)

browser.quit()
