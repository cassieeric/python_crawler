# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# 参数数字为像素点
print("设置浏览器宽480像素，高800像素显示")
browser.set_window_size(480, 800)
browser.quit()
