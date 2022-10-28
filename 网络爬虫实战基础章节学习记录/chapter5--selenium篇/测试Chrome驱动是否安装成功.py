from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
source_code = browser.page_source  # 获取网页源代码
print(source_code)
