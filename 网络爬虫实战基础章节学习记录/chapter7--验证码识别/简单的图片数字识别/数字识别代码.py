# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import os

def recognize_image():
    path1 = "E:\\PythonCrawler\\chapter7--验证码识别\\简单的图片数字识别\\"
    path2 = "0824.jpg"
    text = pytesseract.image_to_string(Image.open(path1+path2), lang="chi_sim")
    print(text.replace(" ", ""))

if __name__ == '__main__':
    recognize_image()
