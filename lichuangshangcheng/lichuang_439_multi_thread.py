# -*- coding: utf-8 -*-
# /usr/bin/env python

'''
Author: dcp
Email: pdcfighting@163.com
Wechat: pycharm1314
Blog: https://blog.csdn.net/pdcfighting
公众号: Python爬虫与数据挖掘

date: 2019/5/22 10:30
desc:
'''

import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import json
import time
import os
import threading
import xlwt

data = []
index = 1

part=0
currentp=1

lock=threading.Lock()
newTable2 = 'other_pages.xls'  # 表格名称
wb = xlwt.Workbook(encoding='utf-8')  # 创建excel文件，声明编码
ws = wb.add_sheet('other_page')  # 用于创建表格
headDate = ['商品名称', '商品编号', '封装规格', '品牌', '型号', '描述',
			'增值税', '1 ~ 9 个', '10 ~ 29 个', '30 ~ 99 个', '100 ~ 499 个', '500 ~ 999 个', '1000 个以上',
			'大小', '近期约售', '库存', '状态']  # 表格头部信息
#
def getHeader(urlref):

	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
		"Referer": urlref,
	}
	return headers

for column in range(0, 17):
	ws.write(0, column, headDate[column], xlwt.easyxf('font: bold on'))

container=[]
currentthread=0
maxthread=15



def getpost(catttlog,page):
	post_data = {
		'catalogNodeId': catttlog,
		'pageNumber':page,
		'querySortBySign': 0,
		'showOutSockProduct': 1,
		'queryProductGradePlateId': '',
		'queryProductArrange': '',
		'keyword': '',
		'queryBeginPrice': '',
		'queryEndPrice': '',
		'queryProductStandard': '',
		'queryParameterValue': '',
		'lastParamName': '',
		'baseParameterCondition': 'undefined',
		'parameterCondition': ''
	}
	return post_data

def writtxt():
	global part,currentp
	part+=1
	with open('data/'+str(currentp)+'.txt','a',encoding='utf-8') as fw:
		w = ['\t'.join([str(x).strip() for x in js_item]) for js_item in container]
		fw.write('\n'.join(w) + '\n')

	if part>50:
		currentp+=1
		part=0
	container.clear()
	print('Save:')
	print('Remain:',len(container))


def getchild_(catttlog,page,urlref):
	global currentthread
	main_url = 'https://list.szlcsc.com/products/list'
	post_data=getpost(catttlog,page)
	headers=getHeader(urlref)
	result_data_txt = requests.post(main_url, data=post_data, headers=headers).text
	try :
		result_data=json.loads(result_data_txt)
	except:
		print(page,'ERR')
		print(result_data_txt)
		lock.acquire()
		currentthread -= 1
		lock.release()
		return

	datas = result_data["productRecordList"]
	print('pageFinish:', page)
	lock.acquire()
	currentthread-=1
	lock.release()
	try:
		for i in range(30):
			# print(i)
			js_item = []
			try:
				title = datas[i]["lightCatalogName"] + "/" + datas[i]["lightProductName"]
				js_item.append(title)
			except:
				title = ""
				js_item.append(title)
			try:
				lightProductCode = datas[i]["lightProductCode"]
				js_item.append(lightProductCode)
			except:
				lightProductCode = ""
				js_item.append(lightProductCode)

			try:
				lightBrandName = datas[i]["lightBrandName"]
				js_item.append(lightBrandName)
			except:
				lightBrandName = ""
				js_item.append(lightBrandName)

			try:
				lightStandard = datas[i]["lightStandard"]
				js_item.append(lightStandard)
			except:
				lightStandard = ""
				js_item.append(lightStandard)

			try:
				lightProductModel = datas[i]["lightProductModel"]
				js_item.append(lightProductModel)
			except:
				lightProductModel = ""
				js_item.append(lightProductModel)

			try:
				lightProductIntro = datas[i]["lightProductIntro"]
				js_item.append(lightProductIntro)
			except:
				lightProductIntro = ""
				js_item.append(lightProductIntro)

			js_item.append("")

			try:
				numberprices = datas[i]["numberprices"]
				js_item.append(numberprices)
			except:
				numberprices = ""
				js_item.append(numberprices)

			js_item.append("")

			js_item.append("")

			js_item.append("")

			js_item.append("")

			js_item.append("")

			try:
				productMinEncapsulation = datas[i]["productMinEncapsulationNumber"]
				js_item.append(productMinEncapsulation)
			except:
				productMinEncapsulation = ""
				js_item.append(productMinEncapsulation)

			try:
				encapsulateProduct = datas[i]["encapsulateProductMinEncapsulationNumber"]
				js_item.append(encapsulateProduct)
			except:
				encapsulateProduct = ""
				js_item.append(encapsulateProduct)

			try:
				validStockNumber = datas[i]["validStockNumber"]
				js_item.append(validStockNumber)
			except:
				validStockNumber = ""
				js_item.append(validStockNumber)

			# print("")
			js_item.append("")

			container.append(js_item)
			lock.acquire()
			if len(container) > 300:
				writtxt()
			lock.release()

	except Exception as AAA:
		print('Except:---',AAA)
		pass



def get_deail(url,catttlog,urlref):
	global currentthread
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
		"Referer": "https://www.szlcsc.com/catalog.html"
	}
	response = requests.get(url, headers=headers).text.encode("latin1").decode("utf-8")
	soup = BeautifulSoup(response, 'html.parser')

	try:

		total_number = soup.find(attrs={'id': 'totalNums'}).get_text()
		# print(total_number)
		page_number = int(int(total_number) / 30) + 1
		print("Page: ", page_number)
		for i in range(924, page_number+1):
			while currentthread>maxthread:
				time.sleep(0.01)
			t=threading.Thread(target=getchild_,args=(catttlog,i,urlref,))
			t.start()
			lock.acquire()
			currentthread+=1
			lock.release()

		while currentthread > 0:
			time.sleep(0.001)

	except:
		print('some error in page 2!')





if __name__ == '__main__':
	url = 'https://list.szlcsc.com/catalog/439.html'
	get_deail(url=url,catttlog=439,urlref=url)
	# t = threading.Thread(target=get_deail, args=(url, ))
	# t.start()
	# urls = []
	# for line in open("lichuang_url.txt", "r"):  # 设置文件对象并读取每一行文件
	#	 urls.append(line)  # 将每一行文件加入到list中
	#
	# for url in urls:
	#	 print(url)
	#	 time.sleep(1)
	#	 regex_str = 'https://list.szlcsc.com/catalog/(\d+).html'
	#	 match_obj = re.match(regex_str, url)
	#	 if match_obj:
	#		 url_number = match_obj.group(1)
	#		 print(url_number)
	#	 get_deail(str(url))
