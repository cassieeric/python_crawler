import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 抽屉账号密码
PHONE = "18903916120"
PWD = "tian1936"
# 抽屉url
url = 'https://dig.chouti.com/'

# 初始化
def init():
    # 定义为全局变量，方便其他模块使用
    global browser, wait
    # 实例化一个chrome浏览器
    browser = webdriver.Chrome(r"G:\installPage\chromedriver_win32 _78.0.3904.70\chromedriver.exe")
    # 最大化窗口
    browser.maximize_window()
    time.sleep(2)
    # 设置等待超时
    wait = WebDriverWait(browser, 20)


# 登录
def login():
    # 打开登录页面
    browser.get(url)
    # # 获取用户名输入框
    browser.find_element_by_id("login_btn").click()
    # browser.find_element_by_class_name("input login-phone").send_keys(PHONE)
    # browser.find_element_by_class_name("input pwd-input pwd-input-active pwd-password-input").send_keys(PHONE)

    # 输入账号密码
    browser.find_element_by_name("phone").send_keys(PHONE)
    browser.find_element_by_name("password").send_keys(PWD)

    # 点击登录
    time.sleep(2)
    click_login_btn_js = 'document.getElementsByClassName("btn-large")[0].click()'
    browser.execute_script(click_login_btn_js)
    time.sleep(15)

    # 获取cookie
    get_cookies_js = "return document.cookie"
    cookie = browser.execute_script(get_cookies_js)
    print(cookie)

    with open("cookie.txt", "w", encoding="utf-8") as f:
        f.write(cookie)
    # page_source = browser.page_source
    # with open("page.html","w",encoding="utf-8") as f:
    #     f.write(page_source)


if __name__ == '__main__':
    init()
    login()

自动登录抽屉
