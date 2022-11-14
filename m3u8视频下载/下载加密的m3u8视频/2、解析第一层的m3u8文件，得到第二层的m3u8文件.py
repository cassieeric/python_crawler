# coding: utf-8
import requests

src_url = "https://vod1.bdzybf1.com"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

def get_second_url():
    with open("first.m3u8", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            print(line)
            second_url = src_url + line
            # print(second_url)
        return second_url

def get_second_m3u8_file(url):
    resonse = requests.get(url, headers=headers)
    with open("second.m3u8", "wb") as f:
        f.write(resonse.content)


if __name__ == '__main__':
    url = get_second_url()
    get_second_m3u8_file(url)
    print("下载完成")
