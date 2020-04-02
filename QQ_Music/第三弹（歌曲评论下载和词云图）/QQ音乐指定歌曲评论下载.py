import requests,html,json

def get_id(i):
    global id
    url_1 = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    # 这是请求歌曲评论的url
    headers = {
        'origin':'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer':'https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html',
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
        }
    params = {'ct': '24', 'qqmusic_ver': '1298', 'new_json': '1', 'remoteplace': 'txt.yqq.song', 'searchid': '71600317520820180', 't': '0', 'aggr': '1', 'cr': '1', 'catZhida': '1', 'lossless': '0', 'flag_qc': '0', 'p': '1', 'n': '10', 'w': i, 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0', 'format': 'json', 'inCharset': 'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}
        
    res_music = requests.get(url_1,headers=headers,params=params)
    # 发起请求
    json_music = res_music.json()
    id = json_music['data']['song']['list'][0]['id']
    return id
    # print(id)

def get_comment(i):
    url_3 = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    f2 = open(i+'评论.txt','a',encoding='utf-8')    #存储到txt中
    for n in range(20):
        params = {'g_tk_new_20200303': '5381', 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0', 'format': 'json', 'inCharset': 'utf8', 'outCharset': 'GB2312', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0', 'cid': '205360772', 'reqtype': '2', 'biztype': '1', 'topid': id, 'cmd': '6', 'needmusiccrit': '0', 'pagenum':n, 'pagesize': '15', 'lasthotcommentid': 'song_247347346_3297354203_1576305589', 'domain': 'qq.com', 'ct': '24', 'cv': '10101010'}
        res_music = requests.get(url_3,headers=headers,params=params)
        # 发起请求
        js_2 = res_music.json()
        comments = js_2['comment']['commentlist']
        
        for i in comments:
            comment = i['rootcommentcontent'] + '\n——————————————————————————————————\n'
            f2.writelines(comment)
        # print(comment)
    f2.close()
    input('下载成功，按回车键退出！')

def main(i):

    get_id(i)
    get_comment(i)

main(i = input('请输入需要查询歌词的歌曲名称：'))
