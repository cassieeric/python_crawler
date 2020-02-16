#python  selenium应用javascript
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url="https://v.qq.com/"
driver=webdriver.Firefox()
driver.get(url)
for i in range(1,11):
    h=(i/10)
    js='window.scrollTo(0, %s*document.body.clientHeight)'%h
    driver.execute_script(js)
    time.sleep(0.5)
