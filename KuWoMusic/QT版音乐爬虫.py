#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import os
from PyQt5.Qt import *
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QFileDialog
# from PyQt5.QtWidgets import QApplication
import sys


# 主类
class Window(QWidget):
    # 主窗口和公共数据
    def __init__(self):
        super().__init__()
        # 主界面设置+公共参数
        icon = QIcon("./25.png")
        self.setWindowTitle("Qt可视化爬虫")
        self.setWindowIcon(icon)
        self.resize(600, 400)
        self.setStyleSheet("background-color:cyan")
        self.setup_ui()
        self.widget_w = 150
        self.widget_h = 50
        self.widget_h_margin = 10
        self.top_margin = 50
        self.i = 1

    # 创建按钮和标签
    def setup_ui(self):
        self.label_path = QLabel(self)  # 路径标签
        self.label_input = QLabel(self)  # 输入标签

        self.path_lineedit = QLineEdit(self)  # 路径显示文本框
        self.path_lineedit.textChanged.connect(self.text_signal)  # 显示文本的槽函数

        self.input_lineedit = QLineEdit(self)  # 搜索音乐文本框
        self.input_lineedit.textChanged.connect(self.input_line)

        self.label_out = QTextEdit(self)  # 输出音乐名称
        # self.label_out.textChanged.connect(self.out_line)

        self.choose_button = QPushButton(self)  # 选择路径按钮
        self.choose_button.pressed.connect(self.read_path)

        self.reptile_button = QPushButton(self)  # 合并log按钮
        self.reptile_button.pressed.connect(self.reptile_web)
        self.reptile_button.setEnabled(False)

    # 定义按钮、标签的样式和位置
    def resizeEvent(self, event):
        # 背景色等样式
        cyan = "background-color:cyan;font-size:26px;color:blue"
        line = "background-color:white;font-size:26px;color:blue"
        background = "background-color:#ccffcc;font-size:26px;color:blue"

        # 路径提示标签
        self.label_path.resize(self.widget_w - 38, self.widget_h)
        self.label_path.setText("保存路径：")
        self.label_path.setToolTip("这是一个提示标签")
        self.label_path.setStyleSheet(cyan)

        # 显示音乐名称标签
        self.label_input.resize(self.widget_w - 38, self.widget_h)
        self.label_input.setText("音乐名称：")
        self.label_input.setToolTip("请输入你想要搜索的音乐")
        self.label_input.setStyleSheet(cyan)

        # 下载完毕提示标签
        self.label_out.resize(300, 100)
        self.label_out.setToolTip("任务列表！")
        self.label_out.setStyleSheet(line)

        # 输入音乐文本
        self.input_lineedit.resize(self.widget_w, self.widget_h)
        self.input_lineedit.setToolTip("请输入音乐名称")
        self.input_lineedit.setStyleSheet(line)

        # 路径显示文本
        self.path_lineedit.resize(self.widget_w, self.widget_h - 2)
        self.path_lineedit.setToolTip("你选择的文件夹")
        self.path_lineedit.setStyleSheet(line)

        # 路径选择按钮
        self.choose_button.setText("选择路径")
        self.choose_button.setToolTip("选择一个文件夹")
        self.choose_button.resize(self.widget_w, self.widget_h)
        self.choose_button.setStyleSheet(background)

        # 爬取音乐按钮
        self.reptile_button.setText("点击爬取")
        self.reptile_button.setToolTip("这是开始爬取按钮")
        self.reptile_button.resize(self.widget_w, self.widget_h)
        self.reptile_button.setStyleSheet(background)

        # 按钮及标签位置摆放
        x = (self.width() - self.widget_w) / 2
        y1 = self.top_margin
        y2 = y1 + self.widget_h + self.widget_h_margin
        y3 = y2 + self.widget_h + self.widget_h_margin

        self.label_path.move(x - 130, y1)
        self.label_input.move(x-130, y1+60)
        self.path_lineedit.move(x, y1 + 1)
        self.input_lineedit.move(x, y1+60)
        self.choose_button.move(x + 170, y1)
        self.reptile_button.move(x+170, y1 + 60)
        self.label_out.move(x-60, y1 + 120)
        self.i += 1

    # 判断文本框是否有内容，设置按钮是否可用
    def text_signal(self, text):
        # print("文本内容发生了改变", text)
        # if len(text) > 0:
        #     self.merge_log_button.setEnabled(True)
        # else:
        #     self.merge_log_button.setEnabled(False)
        # 等同于上面四行代码
        self.reptile_button.setEnabled(len(text) > 0)

    # 选择路径函数
    def read_path(self):
        try:
            self.file1 = QFileDialog.getExistingDirectory(self, "选取文件", "G:/")
            self.data = ("'" + self.file1 + "'")
            # print(self.data)
            self.path_lineedit.setText(self.file1)
        except Ellipsis as e:
            # print(e)
            pass

    # 输入音乐
    def input_line(self, text):
        # print("+++++++", text)
        self.text = text

    # 动作按钮
    def reptile_web(self):
        # print("+++", self.text)
        kw = self.text
        # 请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",
            "Cookie": "_ga=GA1.2.1083049585.1590317697; _gid=GA1.2.2053211683.1598526974; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1597491567,1598094297,1598096480,1598526974; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1598526974; kw_token=HYZQI4KPK3P",
            "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
            "csrf": "HYZQI4KPK3P",
        }
        # 参数列表
        params = {
            "key": kw,
            # 页数
            "pn": "1",
            # 音乐数
            "rn": "1",
            "httpsStatus": "1",
            "reqId": "cc337fa0-e856-11ea-8e2d-ab61b365fb50",
        }
        # 创建列表,后面下载需要
        music_list = []

        url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?"
        res = requests.get(url=url, headers=headers, params=params)
        res.encoding = "utf-8"
        text = res.text
        # 转成json数据
        json_list = json.loads(text)
        # 发现data中list是存主要数据的地方
        datapack = json_list["data"]["list"]
        # 遍历拿到所需要的数据，音乐名称，歌手，id...
        for i in datapack:
            # 音乐名
            music_name = i["name"]
            # 歌手
            music_singer = i["artist"]
            # 待会需要的id先拿到
            rid = i["rid"]
            # 随便试听拿到一个音乐的接口,这是的rid就用得上了
            api_music = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3" \
                        "&br=128kmp3&from=web&t=1598528574799&httpsStatus=1" \
                        "&reqId=72259df1-e85a-11ea-a367-b5a64c5660e5".format(rid)
            api_res = requests.get(url=api_music)
            # 打印发现真实的url确实在里面
            # print(api_res.text)
            music_url = json.loads(api_res.text)["url"]
            # 大功告成，试试效果
            # print(music_name)
            # print(music_singer)
            # print(music_url)
            # 把数据存到字典方便下载时查找
            music_dict = {}
            music_dict["name"] = music_name
            music_dict["url"] = music_url
            music_dict["singer"] = music_singer
            music_list.append(music_dict)
        # 看看真实数据数量
        # print(len(music_list))
        # 下载
        xiazai = kw
        # 下载位置
        root = self.file1 + '/'
        for i in range(len(music_list)):
            try:
                if xiazai == music_list[i]["name"]:
                    # 创建文件夹
                    if not os.path.exists(root):
                        os.mkdir(root)
                    # 拿到字典中对应的音乐url数据
                    music_content = requests.get(url=music_list[i]["url"]).content
                    with open(root + "{}({}).mp3".format(music_list[i]['name'], music_list[i]['singer']), "wb") as f:
                        f.write(music_content)
                        # 输出音乐名称标签
                        self.label_out.setPlainText(music_list[i]['name'] + '下载成功')
                        # print("下载成功")
            except Exception as e:
                # print("下载失败", e)
                pass


# 在被其他文档调用时，下面的代码不会被执行
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
