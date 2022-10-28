# -*- coding: utf-8 -*-
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
# 获得输入框的尺寸
size = browser.find_element_by_id("kw").size
print(size)

# 返回百度页面底部备案信息
text = browser.find_element_by_id("s-top-left").text
print(text)

# 返回元素的属性值，可以是id、name、type或其他任意属性
attribute = browser.find_element_by_id("kw").get_attribute("type")
print(attribute)

# 返回元素的结果是否可见，返回结果为True或者alse
result = browser.find_element_by_id("kw").is_displayed()
print(result)
browser.quit()
