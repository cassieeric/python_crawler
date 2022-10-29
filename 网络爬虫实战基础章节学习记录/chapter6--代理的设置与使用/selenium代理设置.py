# -*- coding: utf-8 -*-
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://171.214.214.185:1133")
browser = webdriver.Chrome(chrome_options=chromeOptions)

# 查看本机IP，查看代理是否起作用
browser.get("http://myip.kkcha.com")
print(browser.page_source)

# 退出，清除浏览器缓存
browser.quit()
