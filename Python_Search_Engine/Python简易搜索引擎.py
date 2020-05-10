import requests 
import json
def down(content,page):
	aq=[]
	rep=requests.get('http://106.15.195.249:8011/search_new?q={}&p={}'.format(content,page))
	rep.encoding=rep.apparent_encoding
	aa=rep.text
	ab=aa.replace("null","123")
	ac=json.loads(ab)
	for y in ac['list']['data']:
		aq.append('文件名：'+y['title']+'链接：'+y['link'])
	return aq

def main():	
	file_name=input('请输入要下载的文件名：')
	page=str(input('请输入下载的页数：'))
	print(down(file_name,page))

main()