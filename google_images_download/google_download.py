# -*- coding: utf-8 -*-
import csv
import os
import sys
from google_images_download import google_images_download

# 实例化一个下载器
downloader = google_images_download.googleimagesdownload()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# 读取关键字文件
csv_file = csv.reader(open(BASE_DIR + "\\google_imageskeywords.csv", "r"))

def download_images(csv_file):
    for key_word in csv_file:
        print(key_word)
        arguments = {"keywords": str(key_word), "limit": 500, "print_urls": True,
                    "chromedriver": "C:\\Python34\\chromedriver.exe",
                    "output_directory": BASE_DIR + "files"}
        downloader.download(arguments)

if __name__ == '__main__':
    download_images(csv_file)
    """
   传入关键字等参数，下载对应的图片文件
   files: 读取的关键字文件
   limit: 爬取的图片数量
   print_urls: 是否显示爬取的图片url
   chromedriver: chromedriver安装的路径。不填此参数，默认爬取前100张图片
   output_directory：自定义保存图片的位置
   """
