# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# submit()提交
search_text = browser.find_element_by_id("kw")
search_text.send_keys("selenium")
search_text.submit()
browser.quit()
