# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
# 访问百度首页
first_url = "http://www.baidu.com"
print("now access first url: %s" % first_url)
browser.get(first_url)

# 访问新闻首页
second_url = "http://news.baidu.com"
print("now access second url: %s" % second_url)
browser.get(second_url)

# 返回（后退）到百度首页
print("back to first url: %s" % first_url)
browser.back()

# 前进到新闻页
print("forword to second url: %s" % second_url)
browser.forward()

browser.quit()