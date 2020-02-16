#python  selenium应用javascript
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url="https://www.12306.cn/index/"
driver=webdriver.Firefox()
driver.get(url)
date = ['2019-10-17', '2020-1-17', '2020-2-17']
for i in date:
    js = "document.getElementById('train_date').value='" + i + "'"
    driver.execute_script(js)
