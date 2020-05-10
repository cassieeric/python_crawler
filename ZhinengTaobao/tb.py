import requests
from bs4 import BeautifulSoup
import pandas as p
import tkinter as tk
from datetime import datetime as dt
from requests.packages import urllib3
import webbrowser as wb   
aa=[]
bb=[]
cc=[]

#主界面
class page:
	def __init__(self):	
		self.ti=dt.now().strftime("%Y/%m/%d %H:%S:%M") 
		self.root= tk.Tk()   #初始化窗口
		self.root.title('淘宝获取商家宝贝V1.0')  #窗口名称
		self.root.geometry("700x700")  #设置窗口大小
		self.root.iconbitmap('q.ico')
		self.root.resizable(width=True,height=True) #设置窗口是否可变，宽不可变，高可变，默认为True
		#创建标签,文字，背景颜色，字体（颜色，大小），标签的高和宽
		self.label1 =tk.Label(self.root,text='店铺首页：',font=('宋体',10),width=12,height=2)
		#创建输入框，标签高度，字体大小颜色，内容显示方式
		self.e2 = tk.Entry(self.root,width=30,show=None, font=('Arial', 12))  # 显示成明文形式
		self.label2 =tk.Label(self.root,text='淘宝直达：',font=('宋体',10),width=12,height=2)
		self.e1 = tk.Entry(self.root,width=30,show=None, font=('Arial', 12))
		#创建按钮 内容  宽高  按钮绑定事件
		self.b1 = tk.Button(self.root, text='解析页面', width=8,height=1,command=self.parse)
		self.b2 =tk.Button(self.root, text='生成excel', width=8,height=1,command=self.sc)
		self.b3 =tk.Button(self.root, text='淘宝搜索', width=8,height=1,command=self.search)
		self.b4 =tk.Button(self.root, text='关闭程序', width=8,height=1,command=self.close)
		self.b5 =tk.Button(self.root, text='保存日志', width=8,height=1,command=self.log)
		#创建文本框
		self.te=tk.Text(self.root,height=40)
		self.label1.place(x=140,y=30,anchor='nw')
		self.label2.place(x=138,y=70,anchor='nw')  
		#将所有部件添加到界面中
		self.e1.place(x=210,y=74,anchor='nw')
		self.e2.place(x=210,y=34,anchor='nw')
		self.b1.place(x=160,y=110,anchor='nw')
		self.b2.place(x=240,y=110,anchor='nw')
		self.b3.place(x=320,y=110,anchor='nw')
		self.b4.place(x=400,y=110,anchor='nw')
		self.b5.place(x=480,y=110,anchor='nw')
		self.te.place(x=40,y=170,anchor='nw')
		#设置输入框开始文本
		self.e1.delete(0, "end")
		self.e1.insert(0, "请输入要搜索的商品")
		self.root.mainloop()



    #网页结构分析
	def res(self):
		#捕获异常
		try:
			urllib3.disable_warnings()  #从urllib3中消除警告
			#网页请求
			rep=requests.get(self.e2.get(),verify=False,timeout=4) #证书验证设为FALSE,设置访问延时
			rep.encoding='gbk'
			soup=BeautifulSoup(rep.content,'html.parser')
			result=soup.find_all('dt',class_='photo') #获取到所有class为photo的dt元素
			for x in result:
				tt=x.find_all('a')  #获取dt下的所有子元素a
				for y in tt:
					for x in y:
						ab=x.find_next_siblings('img') #获取所有的下一个兄弟元素img
						for z in ab:
							#将商品名称和商品图片链接添加到列表aa和bb中
							aa.append(z['alt'])
							bb.append('https:'+z['data-ks-lazyload'])
					cc.append('https:'+y['href'])#将商品链接添加到列表cc中
		except:
			return 	
	
	

    #解析网页内容
	def parse(self):
		self.res() 
		if self.e2.get()=='': #判断输入框的值是否为空值
			#插入值到文本框
			self.te.insert('insert','              。。。。 请 输 入 网 址 。。。。\n')
		elif str(self.e2.get()).find('taobao.com')==-1 or aa=='':
			self.te.insert('insert','              。。。。 地址不正确 。。。。\n')
		else:
			self.te.insert("insert","解析目标网页:%s\n\n"%self.e2.get())
			self.te.insert("insert","             。。。。。解 析 开 始 ：。。。。。\n") #INSERT索引表示插入光标当前的位置
			self.te.insert("insert","\n\n")
			for x,y,z in zip(aa,bb,cc):
				result=x+'\n'+y+'\n'+z+'\n\n'
				self.te.insert("insert",result,"\n\n")
			self.te.insert("insert","\n\n")
			self.te.insert("end","解析完毕。。。。。\n")


	#保存结果到excel
	def sc(self):
		self.te.insert("insert","             。。。。。开 始 生 成 ：。。。。。\n") 
		av={'时间':self.ti,'商品名称':aa,'商品链接':cc,'商品图片链接':bb}
		#生成dataframe 多维数组
		df=p.DataFrame(av,columns=['时间','商品名称','商品链接','商品图片链接'],index=range(len(aa)))
		df.to_excel('22.xlsx', sheet_name='taobao') #生成excel
		self.te.insert("end","            。。。。生 成 完 毕。。。。。\n")


	#搜索商品
	def search(self):
		self.te.insert("insert","             。。。。。打开浏览器 ：。。。。。\n") 
		wb.open('https://s.taobao.com/search?q='+self.e1.get()) #打开 浏览器

	#关闭程序
	def close(self):
		self.te.insert("insert","             。。。。。关闭程序 ：。。。。。\n")
		self.root.destroy()  #销毁窗口
    
    #保存日志
	def log(self):
		ss=str(self.te.get(0.0,'end')).split('\n') #分隔文本框内容
		with open('1.txt','w',encoding='utf8') as f:   #保存日志
			for y in range(len(ss)):
				rea=str(self.ti)+ss[y]+'\n'
				f.write(rea)

if __name__ == '__main__':
	page()





