import requests
from lxml import etree
import re
import csv
import time
import random


def get_html(asin):
    headers = {
        "authority": "www.amazon.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "max-age=0",
        "device-memory": "8",
        "downlink": "0.5",
        "dpr": "1.5",
        "ect": "4g",
        "rtt": "250",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1.5",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-viewport-width": "853",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70",
        "viewport-width": "853"
    }
    cookies = {
        "session-id": "132-2638305-6857035",
        "session-id-time": "2082787201l",
        "i18n-prefs": "USD",
        "sp-cdn": "\"L5Z9:CN\"",
        "ubid-main": "135-2259680-3327567",
        "session-token": "Ajhud35JUjMdsmOyFY3MTNhPLc9Y87p/lPjhZVprK2jdxCg0PAGVQNfpuCx/84ZtAtoo1fNUWGw9hTnSCGTJGwE5qJ0zKUQM8cU4sYaMxaWKUjH+U/ujteYeQC3MyXaMcs+n1/3iL9ij/ipc7xC45OuCGpupPRo0JAA8zjhVvkyYl72Cf88ruCKiIgmtjZ7ivQY2MEHHqpiwJ3yxohd8yWotG99DIKsM",
        "csm-hit": "tb:s-QSR3MEQ26CJE037780E7|1662014894291&t:1662014894868&adb:adblk_no"
    }
    url = "https://www.amazon.com/product-reviews/" + asin + "/ref=cm_cr_arp_d_viewopt_fmt"
    params = {
        "ie": "UTF8",
        "reviewerType": "all_reviews",
        "formatType": "current_format",
        "pageNumber": "1"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    # print(response.text)
    # print(url)
    # print(response)
    html = etree.HTML(response.text)
    try:
        rating_review = html.xpath('//div[contains(@class,"a-row") and contains(@class,"a-spacing-base") '
                               'and contains(@class,"a-size-base")]/text()')[0].strip()
    except:
        rating_review = "None"
    if rating_review != "None":
        print(rating_review)
        ratings1 = rating_review.split(', ')[0].split('total ')[0]
        review1 = rating_review.split(', ')[1].split('with ')[0]
        f = open('rating_review.csv', mode='a', newline="")
        csvwriter = csv.writer(f)
        csvwriter.writerow([ratings1, review1])
        f.close()
    else:
        print(f"{asin}的rating和review获取失败...")


if __name__ == '__main__':
    with open('asin.txt', 'r', encoding='utf-8') as f:
        asins = f.readlines()
    # print(len(asins))
    for asin in asins:
        # print(asin.strip())
        get_html(asin.strip())
        sleep_time = random.choice([1, 2, 3])
        time.sleep(sleep_time)
        # break
