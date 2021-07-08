import time
from  tkinter import  filedialog
import tkinter as t
from PIL import Image
from tkinter import messagebox
import os
class gui:
	def __init__(self):
		self.tl=[]
		self.aa=''
		self.fg=os.path.join(os.path.expanduser("~"), 'Desktop')
		self.root=t.Tk()
		self.root.title('淘宝主图视频生成器v1.0')
		self.root.iconbitmap('1.ico')
		self.root.geometry('700x600')
		self.root.attributes('-alpha',0.9)
		self.root.wm_attributes('-topmost',1) 
		self.tt=t.Text(self.root,width=75,height=30)
		self.b1=t.Button(self.root,text='打开图片文件',font =("宋体",13,'bold'),command=self.open_file)
		self.b3=t.Button(self.root,text='打开音频文件',font =("宋体",13,'bold'),command=self.adio)
		self.b7=t.Button(self.root,text='打开文件并批量修改',font =("宋体",13,'bold'),command=self.xg)
		self.b8=t.Button(self.root,text='查看照片',font =("宋体",13,'bold'),command=self.ck)
		self.l1=t.Label(self.root,text='视频文件名：')
		self.e=t.Entry(self.root)
		self.b2=t.Button(self.root,text='生成主图视频',font =("宋体",13,'bold'),command=self.video)
		self.b4=t.Button(self.root,text='播放音频文件',font =("宋体",13,'bold'),command=self.play)
		self.b5=t.Button(self.root,text='清空文本框内容',font =("宋体",13,'bold'),command=self.close)
		self.b6=t.Button(self.root,text='预览视频内容',font =("宋体",13,'bold'),command=self.player)
		self.l2=t.Label(self.root,text='视频分辨率：')
		self.l3=t.Label(self.root,text='长：')
		self.e1=t.Entry(self.root,width=5)
		self.l4=t.Label(self.root,text='宽：')
		self.e2=t.Entry(self.root,width=5)
		self.tt.place(x=10,y=50)
		self.b1.place(x=100,y=10)
		self.l1.place(x=120,y=460)
		self.e.place(x=200,y=460)
		self.b2.place(x=200,y=550)
		self.b3.place(x=240,y=10)
		self.b4.place(x=550,y=120)
		self.b5.place(x=550,y=200)
		self.b6.place(x=550,y=300)
		self.l2.place(x=120,y=500)
		self.l3.place(x=200,y=500)
		self.l4.place(x=280,y=500)
		self.e1.place(x=230,y=500)
		self.e2.place(x=310,y=500)
		self.b7.place(x=380,y=10)
		self.b8.place(x=580,y=10)
		self.root.mainloop()

	def ck(self):
		aa=filedialog.askopenfilename(title='打开图片文件',filetypes=[('ico','ICO'),('png','PNG'),('jpg','JPG'),('All Files', '*')])
		im=Image.open(aa)
		im.show()


	def open_file(self):
		aa=filedialog.askopenfilenames(title='选择所有主图文件',filetypes=[('png','PNG'),('jpg','JPG'),('All Files', '*')])
		bb=list(aa)
		self.tl=bb
		if len(bb)>0:
			self.tt.insert('insert','---------插入图片文件--------')
			self.tt.insert('insert','\n')
			for y in bb:
				self.tt.insert('insert',y+'\n')
			self.tt.insert('insert','\n')
		else:
			return None


	def video(self):
		if self.tl=='' or self.aa=='':
			messagebox.showwarning(title='警告',message='请先选择图片和音频文件')
		else:
			ac=self.tl
			ab=os.path.dirname(ac[0])
			
			if ac[0].endswith('.png'):
				if os.path.exists('1.txt'):
					os.popen('ffmpeg -r 0.1 -t 300 -i {}/%d.png -i {} -strict -2 -f mp4 -s {}x{} {} >{} 2>&1'.format(ab,self.aa,str(self.e1.get()),str(self.e2.get()),os.path.join(self.fg,self.e.get()+'.mp4'),os.path.join(self.fg,'1.txt')))
					self.tt.insert('insert','---------正在生成主图视频-------- \n\n')	
					try:
						f=open(os.path.join(self.fg,'1.txt'),'r',encoding='utf-8')
					except:
						messagebox.showinfo(title='提示',message='-----成功生成主图视频文件失败----')
					finally:
						self.tt.insert('insert',f.read()+'\n')
						self.tt.insert('insert','\n')
						messagebox.showinfo(title='提示',message='-----成功生成主图视频文件成功----\n 文件名为： %s.mp4'%self.e.get())
						f.close()
				else:
					af=open(os.path.join(self.fg,'1.txt'),'w')
					af.close()
			if ac[0].endswith('.jpg'):
				if os.path.exists('2.txt'):
					os.popen('ffmpeg -r 0.1 -t 300 -i {}/%d.jpg -i {} -strict -2 -f mp4 -s {}x{} {} >{} 2>&1'.format(ab,self.aa,str(self.e1.get()),str(self.e2.get()),os.path.join(self.fg,self.e.get()+'.mp4'),os.path.join(self.fg,'2.txt')))
					if not os.path.exists(self.e.get()+'.mp4'):
						self.tt.insert('insert','---------正在生成主图视频-------- \n')	
						try:					
							ff=open(os.path.join(self.fg,'2.txt'),'r')											
						except:
							messagebox.showinfo(title='提示',message='-----成功生成主图视频文件失败----')
						finally:	
							self.tt.insert('insert',ff.read()+'\n')
							self.tt.insert('insert','\n')
							messagebox.showinfo(title='提示',message='-----成功生成主图视频文件成功----\n 文件名为： %s.mp4'%self.e.get())
							ff.close()
					else:
						messagebox.showinfo(title='提示',message='文件已经存在,请重新命名')
				else:
					fa=open(os.path.join(self.fg,'2.txt'),'w')
					fa.close()
			else:
				messagebox.showinfo(title='提示',message='选择错误')


	def adio(self):
		self.aa=filedialog.askopenfilename(title='打开音频文件',filetypes=[('WAV','wav'),('MP3','mp3'),('All Files', '*')])
		if len(self.aa)>0:
			self.tt.insert('insert','---------插入音频文件--------')
			self.tt.insert('insert','\n')	
			self.tt.insert('insert',self.aa)
			self.tt.insert('insert','\n')
		else:
			return None


	def play(self):
		if self.aa=='':
			messagebox.showwarning(title='警告',message='请先选择音频文件')
		else:
			os.popen(self.aa)


	def close(self):
		self.tt.delete('1.0','end')


	def player(self):
		if self.e.get()=='' or self.aa=='' or self.tl=='':
			messagebox.showwarning(title='警告',message='请先生成视频文件在观看')
		time.sleep(2)
		os.popen(self.e.get()+'.mp4')


	def yy(self):
		messagebox.showinfo(title='提示',message='请先将照片改为0.jpg(0.png)....格式')


	def xg(self):
		aa=filedialog.askopenfilenames(title='打开图片文件',filetypes=[('png','PNG'),('jpg','JPG'),('All Files', '*')])
		bb=list(aa)
		for y in range(len(bb)):
			im=Image.open(bb[y])
			im.save(str(y)+'.jpg')

	
gui()