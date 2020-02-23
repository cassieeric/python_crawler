# -*- coding: UTF-8 -*-

import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

with open('js.txt', 'r') as rf:
    txt=rf.read()

jl=json.loads(txt)

res=jl['data']['searchResult']
with open('r.txt', 'w') as f:
    f.write(u'店名' + '\t' + u'星级' + '\t' + u'评论数' + '\t' + u'关键词' + '\t' + u'地址' + '\t' + u'人均消费'+'\r\n')
    for i in res:
        f.write(i['title']+'\t'+str(i['avgscore'])+'\t'+str(i['comments'])+'\t'+i['areaname']+'\t'+i['address']+'\t'+str(i['avgprice']))
        f.write('\r\n')
