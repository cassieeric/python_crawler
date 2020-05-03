def parser():
	aa=[]
	headers={
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
	rep=requests.get('http://v.u00.cn:93/iappce.htm#sp',timeout=5,headers=headers)
	rep.encoding='utf-8'
	soup=BeautifulSoup(rep.text,'html.parser')
	res=soup.find_all('a',class_='videoDown')#获取所有的a标签
	for y in res:
		aa.append('http://v.u00.cn:93'+y.attrs['href']) #将a标签的href属性添加到aa这个列表里面
	return aa #返回列表
def down(y,x): #下载函数
	print('------下载第',str(x),'课-------')
	ss=str(y.split('.')[3:4]) #截取文件名
	sa=ss.replace('[','').replace(']','')#替换文件名中的特殊符号
	ree=requests.get(y)
	with open('%d.%s.mp4'%(x,sa),'wb') as f:
		f.write(ree.content) #保存文件
def main():	
	for y in range(len(parser())):
		down(parser()[y],y) #下载

main()