import base64
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import random

api_username = "username"
api_password = "passowrd"
file_name = "bg.png"
api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
yzm_min = "1"
yzm_max = "1"
yzm_type = "1318"
tools_token = ""


# 初始化
def init():
    # 定义为全局变量，方便其他模块使用
    global url, browser, username, password, wait
    options = webdriver.ChromeOptions()

    # 登录界面的url
    url = 'https://passport.bilibili.com/login'
    # 实例化一个chrome浏览器
    browser = webdriver.Chrome(r"G:\installPage\chromedriver_win32 _78.0.3904.70\chromedriver.exe")
    browser.maximize_window()
    time.sleep(2)
    # 用户名
    username = 'qweqwe'
    # 密码
    password = 'asdfasdf'
    # 设置等待超时
    wait = WebDriverWait(browser, 20)


# 登录
def login():
    # 打开登录页面
    browser.get(url)
    # 获取用户名输入框
    user = wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
    # 获取密码输入框
    passwd = wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
    # 输入用户名
    user.send_keys(username)
    # 输入密码
    passwd.send_keys(password)

    # 获取登录按钮
    login_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-login')))
    # 随机延时点击
    time.sleep(random.random() * 5)
    login_btn.click()
    time.sleep(1.5)


# 下载 带缺口的背景图
def downfile():
    # 下面的js代码根据canvas文档说明而来
    JS = 'return document.getElementsByClassName("geetest_canvas_bg geetest_absolute")[0].toDataURL("image/png")'
    # 执行 JS 代码并拿到图片 base64 数据
    im_info = browser.execute_script(JS)  # 执行js文件得到带图片信息的图片数据
    im_base64 = im_info.split(',')[1]  # 拿到base64编码的图片信息
    im_bytes = base64.b64decode(im_base64)  # 转为bytes类型
    with open('bg.png', 'wb') as f:  # 保存图片到本地
        f.write(im_bytes)


# 获取 缺口图片位置坐标
def get_geetest_postion():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': (file_name, open(file_name, 'rb'), 'image/png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token
    }
    s = requests.session()
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    print(r.json(), type(r.json()))
    postion = r.json().get("data").get("val")  # type:str
    x, y = postion.split(",")
    # print(x,y)
    return int(x)


# 构造滑动轨迹
def get_track(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


# 模拟拖动
def move_to_gap(trace):
    # 得到滑块标签

    slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.geetest_slider_button')))

    ActionChains(browser).click_and_hold(slider).perform()
    for x in trace:
        # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
    # 模拟人类对准时间
    time.sleep(0.1)
    # 释放滑块
    ActionChains(browser).pause(0.5).release().perform()


def slide():
    distance = get_geetest_postion()
    print('计算偏移量为：%s Px' % distance)
    # 计算移动轨迹
    trace = get_track(distance - 10)
    # 移动滑块
    move_to_gap(trace)


if __name__ == '__main__':
    init()
    login()
    downfile()
    slide()

# 效果如下
哔哩哔哩最后效果.gif
