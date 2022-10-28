# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
# 访问百度首页
url = "http://www.baidu.com"
browser.get(url)

# 刷新当前页面
browser.refresh()
