html_ = '''<ul>
<li>
<a href="/rockets" target="_blank">火箭专区</a>
</li>
<li>
<a href="/lakers" target="_blank">湖人专区</a>
</li>
<li>
<a href="/warriors" target="_blank">勇士专区</a>
</li>
<li>
<a href="/spurs" target="_blank">马刺专区</a>
</li>
<li>
<a href="/celtics" target="_blank">凯尔特人区</a>
</li>
<li>
<a href="/thunder" target="_blank">雷霆专区</a>
</li>
<li>
<a href="/cavaliers" target="_blank">骑士专区</a>
</li>
<li>
<a href="/sixers" target="_blank">76人专区</a>
</li>
<li>
<a href="/timberwolves" target="_blank">森林狼专区</a>
</li>
<li>
<a href="/raptors" target="_blank">猛龙专区</a>
</li>
<li>
<a href="/mavericks" target="_blank">独行侠专区</a>
</li>
<li>
<a href="/clippers" target="_blank">快船专区</a>
</li>
<li>
<a href="/knicks" target="_blank">尼克斯专区</a>
</li>
<li>
<a href="/bulls" target="_blank">公牛专区</a>
</li>
<li>
<a href="/nets" target="_blank">篮网专区</a>
</li>
<li>
<a href="/pacers" target="_blank">步行者专区</a>
</li>
<li>
<a href="/blazers" target="_blank">开拓者专区</a>
</li>
<li>
<a href="/heat" target="_blank">热火专区</a>
</li>
<li>
<a href="/wizards" target="_blank">奇才专区</a>
</li>
<li>
<a href="/jazz" target="_blank">爵士专区</a>
</li>
<li>
<a href="/grizzlies" target="_blank">灰熊专区</a>
</li>
<li>
<a href="/suns" target="_blank">太阳专区</a>
</li>
<li>
<a href="/kings" target="_blank">国王专区</a>
</li>
<li>
<a href="/pelicans" target="_blank">鹈鹕专区</a>
</li>
<li>
<a href="/bucks" target="_blank">雄鹿专区</a>
</li>
<li>
<a href="/nuggets" target="_blank">掘金专区</a>
</li>
<li>
<a href="/hawks" target="_blank">老鹰专区</a>
</li>
<li>
<a href="/pistons" target="_blank">活塞专区</a>
</li>
<li>
<a href="/magic" target="_blank">魔术专区</a>
</li>
<li>
<a href="/hornets" target="_blank">黄蜂专区</a>
</li>
</ul>'''

from lxml import html


def get():
    results = {}
    tree = html.fromstring(html_)
    for x in tree.xpath('//li'):
        link = 'https://bbs.hupu.com' + x.xpath('a/@href')[0]
        name = x.xpath('a/text()')[0]
        results[name] = link
    print(results)
    # for resuls in resulst.items():
    #     print(resuls)


if __name__ == '__main__':
    get()
