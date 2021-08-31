# -*- coding: utf-8 -*-
# [url=home.php?mod=space&uid=238618]@Time[/url] : 2021/8/27 9:50
# [url=home.php?mod=space&uid=686208]@AuThor[/url] : Melon
# [url=home.php?mod=space&uid=406162]@site[/url] :
# [url=home.php?mod=space&uid=786562]@note[/url] :
# [url=home.php?mod=space&uid=267492]@file[/url] : WeiBoHotLite.py
# @Software: PyCharm
import json
import logging
import re
import time
# import traceback

import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
headers = {
    'content-type': "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}


def getHot(url):
    new_hot_list = []
    key_words = {"boom": "爆", "new": "新", "hot": "热", "None": "—", "fei": "沸", "jian_yellow": "荐"}
    result = requests.get(url=url).text
    # 热搜榜单结果 51条，第一条为推荐, 切片方式去除
    result = json.loads(result)["cards"][0]["card_group"][1:]
    for i in result:
        # 排名
        hot = re.search(r'(?<=search_).*(?=.png)', i["pic"]).group()
        if not hot.isdigit():  # 广告推荐过滤
            continue
        # 爆 荐 热 新 沸 空
        if "icon" in i:
            key_word = re.search(r'(?<=_).*(?=.png)', i["icon"]).group()
        else:
            key_word = "None"
        # 链接
        open_url = "https://m.weibo.cn/search" + re.search(r'(?<=searchall).*(?=&isnewpage)', i["scheme"]).group()
        # 热度
        hot_num = re.search(r'\d+', i["desc_extr"]).group()
        new_hot_list.append({"hot": hot, "text": i["desc"], "key_word": key_words[key_word], "hot_num": hot_num,
                             "open_url": open_url})
    logging.info(new_hot_list)
    return new_hot_list


def send_msg(head, body):
    logging.info('----------start send_msg')
    url = 'http://push.ijingniu.cn/send'
    data = {
        'key': 'ff2a933b372e405d8b303cb4610a5115',
        'head': head,
        'body': body
    }
    requests_post = requests.post(url=url, data=data)
    logging.info(requests_post.text)
    if requests_post.ok:
        return json.loads(requests_post.text)['status']
    else:
        return False


if __name__ == '__main__':
    while True:
        try:
            hot = getHot("https://api.weibo.cn/2/guest/page?containerid=106003&filter_type=realtimehot")
            str = ""
            for i in hot[0:10]:
                str = str + i['hot'] + ' ' + i['text'] + ' [' + i['key_word'] + "]\n"
            str += '\n\n<======= (排名，关键词，热度，阅读量) =======>\n\n'
            for i in hot:
                # str = str + i['hot'] + ' ' + i['text'] + ' -- ' + i['key_word'] + "\n"
                str = str + "[" + i['hot'] + ' ' + i['text'] + ' -- ' + i['key_word'] + ' (' + i['hot_num'] + ")](" + i[
                    'open_url'] + ")\n"
            logging.info(str)
            send_msg(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), str)
            time.sleep(60 * 30)
        except Exception as e:
            # traceback.print_exc()
            logging.error('------- error -----> %s', e)
            time.sleep(5)
