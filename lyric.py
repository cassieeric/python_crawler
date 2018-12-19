import requests
import json
import re
from bs4 import BeautifulSoup
import os
import urllib.request

def download_music_by_id(music_id):
    # lyc_url = 'http://music.163.com/weapi/song/lyric?csrf_token='
    lyc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'
    r = requests.get(lyc_url)
    # print(r.text)
    json_obj = r.text

    j = json.loads(json_obj)
    # print(j['lrc']['lyric'])
    lrc = j['lrc']['lyric']
    pattern = re.compile(r'\[.*\]')
    lrc = re.sub(pattern, '', lrc)
    lrc = lrc.strip()
    # print(lrc)
    return lrc


def get_music_ids_by_musician_id(singer_id):
    singer_url = 'http://music.163.com/artist?id=' + str(singer_id)
    r = requests.get(singer_url).text
    soupObj = BeautifulSoup(r, 'lxml')
    song_ids = soupObj.find('textarea')
    # print(song_ids)
    jsObj = json.loads(song_ids)
    # print(jsObj)
    name_ids = {}
    for item in jsObj:
        # print(item['id'])
        # ids.append(item['id'])
        name_ids[item['name']] = item['id']
        # print(name_ids)
    return name_ids

# def download_song(singer_id):
#     singer_url = 'http://music.163.com/artist?id=' + str(singer_id)
#     print('downloading MP3 {}'.format(singer_id))
#     urllib.request.urlretrieve(singer_url, 'songs\\{}.mp3'.format(singer_id))

def download_lyric(uid):
    # singer_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(uid)
    # try:
    #     os.mkdir(str(uid))
    # except IOError:
    #     pass
    # os.chdir(str(uid))
    music_name_ids = get_music_ids_by_musician_id(uid)
    for key in music_name_ids:
        print('downloading song: ' + key)
        singer_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(music_name_ids[key])
        urllib.request.urlretrieve(singer_url, 'songs\\{}.mp3'.format(key))

        lyric = download_music_by_id(music_name_ids[key])
        print('downloading lyric: ' + key)
        file = open('lyrics\\{}.txt'.format(key), 'a', encoding='utf-8')
        file.write(key + '\n')
        file.write(lyric)
        file.close()

if __name__ == '__main__':
    download_lyric(6731)
