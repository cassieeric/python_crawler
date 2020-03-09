import sys
sys.path.append('E:/python_plus/Lib/site-packages')
import json
import time
def response(flow):
    url = 'https://aweme-lq.snssdk.com/aweme/v1/hot/search/list/?detail_list'   #
    if url in flow.request.url:
        time_stamp = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))  # 时间戳
        text=flow.response.text
        result = json.loads(text)
        for i in result['data']['word_list']:
            content = str(i['word'])
            hotNum = str(i['hot_value'])
            with open('1.txt', 'a') as f:
                f.write(content+','+hotNum+','+time_stamp+'\n')


