import requests
from lxml import etree


def get_detail_url(url):
    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)
    selectors = html.xpath('//div/ul[@id="mediasList"]/li/div[1]/a/@href')
    detail_urls = []
    for selector in selectors:
        detail_url = 'https://www.meipai.com' + selector
        # print(detail_url)
        detail_urls.append(detail_url)
    return detail_urls


def get_video_url(url):
    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)
    # video_url = html.xpath('//div[@class="mp-h5-player-layer-video"]/video/@src')
    dataSrc = html.xpath('//div[@id="detailVideo"]/@data-video')[0]
    print(dataSrc)
    with open("dataSrc.txt", 'a', encoding='utf-8') as f:
        f.write(dataSrc + '\n')


if __name__ == '__main__':
    url = 'https://www.meipai.com/medias/hot'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    detail_urls = get_detail_url(url)
    for detail_url in detail_urls:
        get_video_url(detail_url)

