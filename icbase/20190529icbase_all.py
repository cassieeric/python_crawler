# -*- coding: utf-8 -*-
# /usr/bin/env python

import requests
import re
from lxml import etree
import threading
import time
import random

lock=threading.Lock()
pagecontainer=[]
maxpagecontainer=30

currentthread=0
maxthread=20

def writetxt():
	global prox
	with open('icbase_data.txt','a') as fw:
		fw.write('\n'.join(pagecontainer)+'\n')
		print('Write to File!')
	pagecontainer.clear()


def get_urls():
	urls = []
	for line in open('icbase_urls', 'r'):
		urls.append(line.strip())
	return urls


def get_header():
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
	}
	return headers


def get_post(html):
	post=dict()
	submit=html.xpath("//input[@type='hidden']")
	if submit:
		for one in submit:
			name=one.xpath('./@name')
			value=one.xpath('./@value')
			if value is None or len(value)==0:
				value=['']
			if name and len(name)>0:
				post[name[0]]=value[0]
	post['__EVENTTARGET'] = 'Pager1'
	return post


def get_list(html):
	trs = html.xpath('//table[@id="SGVClass4Pro"]/tr')
	lines=[]
	for selector in trs:
		td = selector.xpath('child::td')
		if td and len(td) > 6:
			pass
		else:
			continue
		t1 = td[1]
		t2 = td[2]
		t3 = td[3]
		t4 = td[5]
		t5 = td[6]

		tbshui=t5.xpath('./table/tr')
		t5txt=''
		if tbshui and len(tbshui)>0:
			tmp=[]
			for tr in tbshui:
				tmp.append(tr.xpath('string(.)'))
			t5txt+=','.join(tmp)
		else:
			t5txt += t5.xpath('string(.)').strip()


		items = [t1.xpath('string(.)').strip(),
		         t2.xpath('string(.)').strip(),
		         t3.xpath('string(.)').strip(),
		         t4.xpath('string(.)').strip(),
		         t5txt]
		lines.append('\t'.join([s.replace('\r','').replace('\n',' ').replace('\t',' ') for s in items]))
	lock.acquire()
	pagecontainer.append('\n'.join(lines))
	if len(pagecontainer)>maxpagecontainer:
		writetxt()
	lock.release()


def do_post(url,post):
	global currentthread,prox

	lock.acquire()
	currentthread += 1
	lock.release()

	#proxys,ip=get_proxy()

	try:
		childs = requests.post(url, headers=get_header(), data=post).text
		print(url,post['__EVENTARGUMENT'],'finish!',',remain：',currentthread)
		htmlc = etree.HTML(childs)
		get_list(htmlc)
	except :
		print(url,'，page:'+post['__EVENTARGUMENT'],'，ERROR')
		do_post(url, post)

	finally:
		lock.acquire()
		currentthread -= 1
		lock.release()


def get_detail_info(url):

	response = requests.get(url, headers=get_header()).text
	print(url, 1,'finish!')
	html = etree.HTML(response)
	get_list(html)
	pages=html.xpath('//*[@class="P_Page"]')
	totalpage=''
	if pages:
		totalpage=pages[0].xpath('string(.)').strip().split('/')[-1]
	if  len(totalpage)>0:
		pagenum=int(totalpage)
		if pagenum>1:
			postor = get_post(html)
			for i in range(2,pagenum+1):
				post=postor.copy()
				post['__EVENTARGUMENT'] = str(i)
				#do_post(url,post)
				while currentthread>maxthread:
					time.sleep(0.001)
				t=threading.Thread(target=do_post,args=(url,post,))
				t.start()

	while currentthread > 0:
		time.sleep(0.001)


if __name__ == '__main__':
	#urls = ['https://www.icbase.com/ClassList3.aspx?id=1728']
	urls=get_urls()
	#urls=['https://www.icbase.com/ClassList3.aspx?id=1728']
	print('get_url:finish')
	st=True
	for url in urls:
		response = get_detail_info(url)
	writetxt()

