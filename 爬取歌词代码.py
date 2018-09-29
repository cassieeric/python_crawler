# -*- coding:utf-8 -*-
import requests
import re
import os
import json
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        html = response.content
        return html
    except:
        print('request error')
        pass

def download_by_music_id(music_id):
    lrc_url = 'http://music.163.com/api/song/lyric?'+'id='+str(music_id) + '&lv=1&kv=1&tv=-1'
    r = requests.get(lrc_url)
    json_obj = r.text
    j = json.loads(json_obj)
    try:
        lrc = j['lrc']['lyric']
        pat = re.compile(r'\[.*\]')
        lrc = re.sub(pat, "",lrc)
        lrc = lrc.strip()
        return lrc
    except:
        pass

def get_music_ids_by_musician_id(singer_id):
    singer_url = 'http://music.163.com/artist?id={}'.format(singer_id)
    r = get_html(singer_url)
    soupObj = BeautifulSoup(r,'lxml')
    song_ids = soupObj.find('textarea').text
    jobj = json.loads(song_ids)
    ids = {}
    for item in jobj:
        print(item['id'])
        ids[item['name']] = item['id']
    return ids

def download_lyric(uid):
    try:
        os.mkdir(str(uid))
    except:
        pass

    os.chdir(str(uid))
    music_ids = get_music_ids_by_musician_id(uid)
    for key in music_ids:
        text = download_by_music_id(music_ids[key])
        file = open(key+'.txt','a')
        file.write(key+'\n')
        file.write(str(text))
        file.close()

if __name__ == '__main__':
    download_lyric(6731)
