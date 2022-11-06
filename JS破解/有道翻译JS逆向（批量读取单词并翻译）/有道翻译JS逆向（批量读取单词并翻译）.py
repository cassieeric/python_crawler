# coding: utf-8
import requests
import json
import time
import random
import hashlib
import pandas as pd

def get_word():
    df = pd.read_excel("六级词汇.xlsx", usecols=[0])
    df_li = df.values.tolist()
    word_list = []
    for word in df_li:
        word_list.append(word[0])
    return word_list

def write_to_excel(translate_result):
    df = pd.read_excel(r"六级词汇.xlsx")
    df['翻译结果'] = translate_result
    df.to_excel(r'六级词汇.xlsx', index=None)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
def md5_ua(user_agent):
    hash = hashlib.md5()
    hash.update(user_agent.encode('utf-8'))
    return hash.hexdigest()

def sign_b(word, salt):
    sign = 'fanyideskweb' + word + str(salt) + 'Y2FYu%TNSbMCxc3t2u^XT'
    return md5_ua(sign)

def translate(word):
    salt = int(time.time() * 1000) + random.randint(0, 9)
    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"92\"",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://fanyi.youdao.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://fanyi.youdao.com/",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    cookies = {
        "P_INFO": "pdcfighting",
        "OUTFOX_SEARCH_USER_ID": "-835551069@223.104.228.2",
        "JSESSIONID": "aaaYcIqS8p-7RfbzltPUx",
        "OUTFOX_SEARCH_USER_ID_NCOO": "242914410.9668874",
        "fanyi-ad-id": "115021",
        "fanyi-ad-closed": "1",
        "___rl__test__cookies": "1630632997739"
    }
    params = {
        "smartresult": "rule"
    }
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign_b(word=word, salt=salt),
        "lts": salt,
        "bv": md5_ua(user_agent),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
    res = requests.post(
        "https://fanyi.youdao.com/translate_o",
        params=params,
        headers=headers,
        cookies=cookies,
        data=data
    )
    return res


if __name__ == '__main__':
    translate_result = []
    words = get_word()
    for word in words:
        try:
            res = translate(word=word)
            result = json.loads(res.text)
            for k in result['translateResult']:
                result_tgt = k[0]['tgt']
                result_src = k[0]['src']
                # print(result_tgt)
                print(f"""‘{result_src}’的翻译是: ‘{result_tgt}’""")
                translate_result.append(result_tgt)
        except Exception as e:
            print('有道翻译已经升级！ ', e)
    write_to_excel(translate_result)

