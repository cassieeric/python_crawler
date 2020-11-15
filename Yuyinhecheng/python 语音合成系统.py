from aip import AipSpeech
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import os
import sys
class play:
	def __init__(self):
		self.root=tk.Tk()
		self.root.title("语音合成系统") 
		self.root.geometry("700x700")
		self.lb=tk.Label(self.root,text='请选择语音类型')
		self.tt=tk.Text(self.root,width=80,height=30)
		self.cb=ttk.Combobox(self.root, width=12)
		self.cb['values'] = ('请选择-----','甜美型','萝莉型','大叔型','精神小伙型') #设置下拉列表框的内容   
		self.cb.current(0)    #将当前选择状态置为0,也就是第一项
		self.cb.bind("<<ComboboxSelected>>",self.go)  #绑定go函数，然后触发事件
		self.lb1=tk.Label(self.root,text='请输入文件名：')
		self.e=tk.Entry(self.root,width=30,show=None, font=('Arial', 12))
		self.b1=tk.Button(self.root, text='生成音频文件', width=10,height=1,command=self.sc)
		self.b1.place(x=200,y=520)
		self.lb.place(x=30,y=30)
		self.cb.place(x=154,y=30)
		self.e.place(x=130,y=490)
		self.lb1.place(x=30,y=490)
		self.tt.place(x=30,y=60)
		self.root.mainloop()     #启动页面
		

	def go(self,*arg):
		self.APP_ID = '18386899'
		self.API_KEY = 'OcPQ4cGoGBRtW23jemKvgmU5'
		self.SECRET_KEY = 'n2rGtvq9HmOGxgxG8H9a5kqFOes8ggHx'
		self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
		
		if self.cb.get()=='请选择-----':
			self.tt.delete('1.0','end')
		elif self.cb.get()=='甜美型':
			self.res=self.client.synthesis(self.tt.get('0.0','end'),'zh',1,{'vol':3,'spd':3,'pit':4,'per':0})
			return self.res
		elif self.cb.get()=='萝莉型':
			self.res=self.client.synthesis(self.tt.get('0.0','end'),'zh',1,{'vol':2,'spd':2,'pit':3,'per':0})
			return self.res
		elif self.cb.get()=='大叔型':
			self.res=self.client.synthesis(self.tt.get('0.0','end'),'zh',1,{'vol':5,'spd':7,'pit':6,'per':1}) 
			return self.res
		elif self.cb.get()=='精神小伙型':
			self.res=self.client.synthesis(self.tt.get('0.0','end'),'zh',1,{'vol':7,'spd':8,'pit':8,'per':1})
			return self.res	
			    
	def sc(self):
		self.go()
		aa=self.tt.get('0.0','end')
		ab=os.path.dirname(sys.argv[0])+os.sep+self.e.get()+'.mp3'
		if len(aa)>=1024:
			messagebox.showerror(title = '出错了！',message='^_^最多不超过1024个字节^_^')
		
		else:
			if not os.path.exists(ab):
				with open(ab,'wb') as f:
					f.write(self.res)
					messagebox.showinfo(title = '完毕！',message='生成完毕，文件在程序目录下')

			else:
				messagebox.showerror(title = '出错了！',message='文件名已存在')

play()
