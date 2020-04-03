import requests,openpyxl,html,json
from wordcloud import WordCloud
import jieba
import numpy
import PIL.Image as Image

class QQ():
    def menu(self):
        print('欢迎使用QQ音乐爬虫系统，以下是功能菜单，请选择。\n')
        while True:
            try:
                print('功能菜单\n1.获取指定歌手的歌曲信息\n2.获取指定歌曲歌词\n3.获取指定歌曲评论\n4.生成词云图\n5.退出系统\n')
                choice = int(input('请输入数字选择对应的功能：'))
                if choice == 1:
                    self.get_info()
                elif choice == 2:
                    self.get_id()
                    self.get_lyric()
                elif choice == 3:
                    self.get_id()
                    self.get_comment()
                elif choice == 4:
                    self.wordcloud()
                elif choice == 5:
                    print('感谢使用！')
                    break
                else:
                    print('输入错误,请重新输入。\n')
            except:
                print('输入错误,请重新输入。\n')      

    def get_info(self):
        wb=openpyxl.Workbook()  
        #创建工作薄
        sheet=wb.active 
        #获取工作薄的活动表
        sheet.title='song' 
        #工作表重命名

        sheet['A1'] ='歌曲名'     #加表头，给A1单元格赋值
        sheet['B1'] ='所属专辑'   #加表头，给B1单元格赋值
        sheet['C1'] ='播放链接'   #加表头，给C1单元格赋值
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        name = input('请输入要查询的歌手姓名：')
        page = int(input('请输入需要查询的歌曲页数：'))
        for x in range(page):
            params = {
            'ct':'24',
            'qqmusic_ver': '1298',
            'new_json':'1',
            'remoteplace':'sizer.yqq.song_next',
            'searchid':'64405487069162918',
            't':'0',
            'aggr':'1',
            'cr':'1',
            'catZhida':'1',
            'lossless':'0',
            'flag_qc':'0',
            'p':str(x+1),
            'n':'20',
            'w':name,
            'g_tk':'5381',
            'loginUin':'0',
            'hostUin':'0',
            'format':'json',
            'inCharset':'utf8',
            'outCharset':'utf-8',
            'notice':'0',
            'platform':'yqq.json',
            'needNewCode':'0'    
            }
            res = requests.get(url,params=params)
            json = res.json()
            list = json['data']['song']['list']
            for music in list:
                song_name = music['name']
                # 查找歌曲名，把歌曲名赋值给song_name
                album = music['album']['name']
                # 查找专辑名，把专辑名赋给album
                link = 'https://y.qq.com/n/yqq/song/' + str(music['mid']) + '.html\n\n'
                # 查找播放链接，把链接赋值给link
                sheet.append([song_name,album,link])
                # 把name、album和link写成列表，用append函数多行写入Excel
                
        wb.save(name+'个人单曲排行前'+str(page*20)+'清单.xlsx')            
        #最后保存并命名这个Excel文件
        print('下载成功！\n')

    def get_id(self):
        self.i = input('请输入歌曲名：')
        url_1 = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        # 这是请求歌曲评论的url
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        params = {'ct': '24', 'qqmusic_ver': '1298', 'new_json': '1', 'remoteplace': 'txt.yqq.song', 'searchid': '71600317520820180', 't': '0', 'aggr': '1', 'cr': '1', 'catZhida': '1', 'lossless': '0', 'flag_qc': '0', 'p': '1', 'n': '10', 'w': self.i, 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0', 'format': 'json', 'inCharset': 'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}  
        res_music = requests.get(url_1,headers=headers,params=params)
        json_music = res_music.json()
        self.id = json_music['data']['song']['list'][0]['id']
        # print(self.id)

    def get_lyric(self):
        url_2 = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        # 这是请求歌曲评论的url
        headers = {
        'origin':'https://y.qq.com',
        'referer':'https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        params = {
            'nobase64':'1',
            'musicid':self.id,
            '-':'jsonp1',
            'g_tk':'5381',
            'loginUin':'0',
            'hostUin':'0',
            'format':'json',
            'inCharset':'utf8',
            'outCharset':'utf-8',
            'notice':'0',
            'platform':'yqq.json',
            'needNewCode':'0',
            }

        res_music = requests.get(url_2,headers=headers,params=params)
        js_1 = res_music.json()
        lyric = js_1['lyric']
        lyric_html = html.unescape(lyric)   #用了转义字符html.unescape方法
        # print(lyric_html)
        f1 = open(self.i+'歌词.txt','a',encoding='utf-8')    #存储到txt中
        f1.writelines(lyric_html)
        f1.close()
        print('下载成功！\n')
    
    def get_comment(self):
        page = input('请输入要下载的评论页数：')
        url_3 = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        f2 = open(self.i+'评论.txt','a',encoding='utf-8')    #存储到txt中
        for n in range(int(page)):
            params = {'g_tk_new_20200303': '5381', 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0', 'format': 'json', 'inCharset': 'utf8', 'outCharset': 'GB2312', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0', 'cid': '205360772', 'reqtype': '2', 'biztype': '1', 'topid': self.id, 'cmd': '6', 'needmusiccrit': '0', 'pagenum':n, 'pagesize': '15', 'lasthotcommentid':'', 'domain': 'qq.com', 'ct': '24', 'cv': '10101010'}
            res_music = requests.get(url_3,headers=headers,params=params)
            js_2 = res_music.json()
            comments = js_2['comment']['commentlist']
            for i in comments:
                comment = i['rootcommentcontent'] + '\n——————————————————————————————————\n'
                f2.writelines(comment)
            # print(comment)
        f2.close()
        print('下载成功！\n')

    def wordcloud(self):
        self.name = input('请输入要生成词云图的文件名称：')
        def cut(text):
            wordlist_jieba=jieba.cut(text)
            space_wordlist=" ".join(wordlist_jieba)
            return space_wordlist
        with open(self.name+".txt" ,encoding="utf-8")as file:
            text=file.read()
            text=cut(text)
            mask_pic=numpy.array(Image.open("心.png"))
            wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
            collocations=False,
            max_words= 100,
            min_font_size=10, 
            max_font_size=500,
            mask=mask_pic).generate(text)
            # image=wordcloud.to_image()
            # image.show()
            wordcloud.to_file(self.name+'云词图.png')  # 把词云保存下来 
        print('生成成功！\n')

qq = QQ()
qq.menu()