# import requests
# from bs4 import  BeautifulSoup
# res = requests.get('https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E9%82%93%E7%B4%AB%E6%A3%8B')
# bs = BeautifulSoup(res.text,'html.parser')
# list = bs.find_all(class_='songlist__songname_txt')
# for m in list:
#     print(m['title'])
# print(list)



# import requests
# import json
# res = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=64113167330747138&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E9%82%93%E7%B4%AB%E6%A3%8B&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# json = res.json()
# list = json['data']['song']['list']
# for m in list:
#     print('歌曲：'+m['name'])
#     # 以name为键，查找歌曲名
#     print('所属专辑：'+m['album']['name'])
#     # 查找专辑名
#     print('播放链接：https://y.qq.com/n/yqq/song/'+m['mid']+'.html\n\n')
#     # 查找播放链接



# import requests
# url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# name = input('请输入要查询的歌手姓名：')
# page = int(input('请输入需要查询的歌曲页数：'))
# for x in range(page):
#     params = {
#     'ct':'24',
#     'qqmusic_ver': '1298',
#     'new_json':'1',
#     'remoteplace':'sizer.yqq.song_next',
#     'searchid':'64405487069162918',
#     't':'0',
#     'aggr':'1',
#     'cr':'1',
#     'catZhida':'1',
#     'lossless':'0',
#     'flag_qc':'0',
#     'p':str(x+1),
#     'n':'20',
#     'w':name,
#     'g_tk':'5381',
#     'loginUin':'0',
#     'hostUin':'0',
#     'format':'json',
#     'inCharset':'utf8',
#     'outCharset':'utf-8',
#     'notice':'0',
#     'platform':'yqq.json',
#     'needNewCode':'0'    
#     }
#     res = requests.get(url,params=params)
#     json = res.json()
#     list = json['data']['song']['list']
#     for music in list:
#         print(music['name'])
#         print('所属专辑：'+music['album']['name'])
#         print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')




import requests,openpyxl
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
        # 以song_name为键，查找歌曲名，把歌曲名赋值给name
        album = music['album']['name']
        # 查找专辑名，把专辑名赋给album
        link = 'https://y.qq.com/n/yqq/song/' + str(music['mid']) + '.html\n\n'
        # 查找播放链接，把链接赋值给link
        sheet.append([song_name,album,link])
        # 把name、album和link写成列表，用append函数多行写入Excel
        
wb.save(name+'个人单曲排行前'+str(page*20)+'清单.xlsx')            
#最后保存并命名这个Excel文件

input('下载成功，按回车键退出！')