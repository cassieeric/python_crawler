# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# 在输入框输入内容
browser.find_element_by_id("kw").send_keys("selenium")

# 删除多输入的内容
browser.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+“教程”
browser.find_element_by_id("kw").send_keys(Keys.SPACE)
browser.find_element_by_id("kw").send_keys("教程")

# 按【Ctrl+A】组合键全选输入框的内容
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# 按【Ctrl+X】组合键剪切输入框中的内容
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# 按【Ctrl+V】组合键将内容粘贴到输入框中
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 通过【Enter】键代替单机操作
browser.find_element_by_id("kw").send_keys(Keys.ENTER)
browser.quit()


