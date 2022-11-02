import requests


def download_video(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
    }
    response = requests.get(url=url, headers=headers)

    with open(f"{url.split('/')[-1]}", "wb") as f:
        f.write(response.content)
    print("下载完成")


if __name__ == '__main__':
    with open('decoded_dataSrc.txt', 'r', encoding='utf-8') as f:
        for video_url in f.readlines():
            download_video(video_url)

