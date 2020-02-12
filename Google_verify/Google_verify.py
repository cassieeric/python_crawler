import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import requests

# 常量
driver: WebDriver
USER = {}
API_KEY = "xxxxxxxxxxxxxxx"


# 初始化
def init():
    global driver
    driver = webdriver.Chrome("chromedriver.exe", desired_capabilities=None)


def open_google():
    driver.get("https://www.google.com/recaptcha/api2/demo")
    data_sitekey = driver.find_element_by_xpath('//*[@id="recaptcha-demo"]').get_attribute("data-sitekey")
    # iframe_src = driver.find_element_by_xpath('//*[@id="recaptcha-demo"]/div/div/iframe').get_attribute("src")
    # iframe_k = url_params_format(iframe_src).get("k")
    print(data_sitekey)
    page_url = "https://www.google.com/recaptcha/api2/demo"
    # print(iframe_k)
    u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
    r1 = requests.get(u1)
    print(r1.json())
    rid = r1.json().get("request")
    u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
    time.sleep(25)
    while True:
        print(u2)
        r2 = requests.get(u2)
        print(r2.json())
        if r2.json().get("status") == 1:
            form_tokon = r2.json().get("request")
            break
        time.sleep(5)
    wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
    submit_js = 'document.getElementById("recaptcha-demo-form").submit();'
    driver.execute_script(wirte_tokon_js)
    time.sleep(1)
    driver.execute_script(submit_js)


if __name__ == '__main__':
    init()
    open_google()
