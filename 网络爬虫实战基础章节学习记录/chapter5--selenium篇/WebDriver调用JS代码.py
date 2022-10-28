# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 设置窗口大小
driver.set_window_size(500, 500)

# 搜索
search_text = driver.find_element_by_id("kw")
search_text.send_keys("selenium")
sleep(2)
search_text.submit()
# driver.find_element_by_class_name("bg s_btn").click()

# sleep(2)

# 通过JS设置浏览器窗口的滚动条位置
js = "window.scrollTo(100, 450);"
driver.execute_script(js)
sleep(3)
