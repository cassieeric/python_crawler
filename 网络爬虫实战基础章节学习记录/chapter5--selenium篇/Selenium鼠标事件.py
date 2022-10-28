# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# 定位到要悬停的元素
above = browser.find_element_by_link_text("新闻")
# 对定位到的元素进行鼠标指针悬停操作
ActionChains(browser).move_to_element(above).perform()

