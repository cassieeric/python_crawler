from pprint import pprint
import time
import random
import requests
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

login_v2_dict = {
    "captchaType": 11,  # ok
    "username": "18903916120",  # ok
    # 需要构建 js 获取密码
    "password": "",
    "keep": True,
    # 通过 commbine 获取
    "key": "",
    "goUrl": "",

    # 通过 2captcha 获取
    "challenge": "",
    "validate": "",
    "seccode": ""
}

API_KEY = "be308827049bfeb0c4c222b76e8b1c92"
method = "geetest"
gt = "b6cc0fc51ec7995d8fd3c637af690de3"
# challenge = "0fb2ae2da43962c1f7aec1dd3f9a58fe"
pageurl = "https://passport.bilibili.com/login"
api_server = "api.geetest.com"

def getChallengeAndKey():
    commbine_header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Cookie": "sid=9qe9dmi7",
        "Host": "passport.bilibili.com",
        "Referer": "https://passport.bilibili.com/login",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

    commbine_url = "https://passport.bilibili.com/web/captcha/combine?plat=11"
    response_commbine = requests.get(url=commbine_url, headers=commbine_header)
    # print(response_commbine.text)

    # pprint(response_commbine.json())
    key = response_commbine.json().get("data").get("result").get("key")
    challenge = response_commbine.json().get("data").get("result").get("challenge")
    return key, challenge


def get2CaptchaChallengeAndValidateSeccode(challenge):
    captcha_url = f"https://2captcha.com/in.php?key={API_KEY}&method={method}&gt={gt}&challenge={challenge}&pageurl={pageurl}&api_server={api_server}&json=1"
    r = requests.get(captcha_url)
    print(r.json())
    rid = r.json().get("request")

    # print(rid, type(rid))

    time.sleep(15)

    while True:
        re_cpatcha_url = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
        # print(re_cpatcha_url)
        r2 = requests.get(re_cpatcha_url)
        print(r2.json())
        if r2.json().get("status") == 1:
            geetest_challenge = r2.json().get("request").get("geetest_challenge")
            geetest_validate = r2.json().get("request").get("geetest_validate")
            geetest_seccode = r2.json().get("request").get("geetest_seccode")

            return geetest_challenge, geetest_validate, geetest_seccode

        time.sleep(5)


# 密码加密
def crack_pwd(hash: str, pwd: str):
    key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDjb4V7EidX/ym28t2ybo0U6t0n
6p4ej8VjqKHg100va6jkNbNTrLQqMCQCAYtXMXXp2Fwkk6WR+12N9zknLjf+C9sx
/+l48mjUU8RqahiFD1XT/u2e0m2EN029OhCgkHx3Fc/KlFSIbak93EH/XlYis0w+
Xl69GV6klzgxW6d2xQIDAQAB
-----END PUBLIC KEY-----
"""
    # 注意上述key的格式
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    new_pwd = hash + pwd
    cipher_text = base64.b64encode(
        cipher.encrypt(new_pwd.encode("utf-8"))
    )  # 对传递进来的用户名或密码字符串加密
    value = cipher_text.decode('utf8')  # 将加密获取到的bytes类型密文解码成str类型
    return value


# 获取key
def get_act():
    act_header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "sid=9qe9dmi7; _uuid=A8F38E21-6734-4291-C4EC-404AEA0294C750293infoc; buvid3=8548F035-99E8-41F8-BDA1-C63065B96FD5155813infoc",
        "Host": "passport.bilibili.com",
        "Referer": "https://passport.bilibili.com/login",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    r1 = random.random()
    c_url = f"https://passport.bilibili.com/login?act=getkey&r={r1}"
    print("url:", c_url)
    response = requests.get(c_url, headers=act_header)

    # print(response.json())
    hash = response.json().get("hash")
    key = response.json().get("key")
    # print(hash)
    # print(key)
    return hash, key


def login_v2():
    login_v2_header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Cookie": "sid=9qe9dmi7",
        "Host": "passport.bilibili.com",
        "Referer": "https://passport.bilibili.com/login",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }
    login_v2_url = "https://passport.bilibili.com/web/login/v2"
    r1 = requests.post(login_v2_url, headers=login_v2_header, data=login_v2_dict)
    pprint(r1.json())
    print(r1.cookies.get_dict())

if __name__ == '__main__':
    v2_key, challenge = getChallengeAndKey()
    # print(v2_key, challenge)

    geetest_challenge, geetest_validate, geetest_seccode = get2CaptchaChallengeAndValidateSeccode(challenge)

    # print(geetest_challenge)
    # print(geetest_validate)
    # print(geetest_seccode)

    hash, key_public_key = get_act()

    n = crack_pwd(hash, "tian1936")

    login_v2_dict["key"] = v2_key
    login_v2_dict["challenge"] = geetest_challenge
    login_v2_dict["validate"] = geetest_validate
    login_v2_dict["seccode"] = geetest_seccode
    login_v2_dict["password"] = n

    print(n)

    print(login_v2_dict)
    login_v2()
