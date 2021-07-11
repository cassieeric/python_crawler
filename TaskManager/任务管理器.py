from math import *
import tkinter  as t
import psutil
import os
import time
import threading
import datetime
root= t.Tk()    #主窗口
root.title('任务管理器')   #标题
root.geometry('730x630')  #窗口尺寸
root.iconbitmap('1.ico')   #窗口图标 必须是ico格式的图片
root.resizable(width=True, height=True)# 设置窗口宽度，高度可变
root.attributes('-alpha',0.9) #设置窗口透明度
root.wm_attributes('-topmost',1) #实现root窗口的置顶显示
sb=t.Scrollbar(root)
sb.pack(side='left',fill='y')
text=t.Text(root,width=100,height=40)
text.place(x=10,y=36)
sb.config(command=text.yview)
text.config(yscrollcommand=sb.set)
sb.pack(side='right',fill='y')
t1=t.Label(text='')
t2=t.Label(text='')
t3=t.Label(text='')
t1.place(x=10,y=580,width=120)
t2.place(x=150,y=580,width=120)
t3.place(x=300,y=580,width=120)





def yy():
	text.delete(1.0,'end')
	text.insert('insert','进程号   '+'进程名      '+'  进程文件路径'+'\n')
	for y in psutil.pids():
		a=psutil.Process(y)
		if a.name()=='System Idle Process':
			continue
		else:
			text.insert('insert',str(y)+'     '+a.name()+'   '+a.exe()+'\n\n')

	root.update()

def jc():
	text.delete(1.0,'end')
	mm=os.popen('tasklist')
	text.insert('insert',mm.read())
	root.update()

def fw():
	text.delete(1.0,'end')
	mm=os.popen('sc query type= service')
	text.insert('insert',mm.read())
	root.update()

def xn():
	text.delete(1.0,'end')
	l1=t.Label(root,text='开机时间：')
	tm=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
	l2=t.Label(root,text=str(tm))
	l3=t.Label(root,text='当前时间：')
	l4=t.Label(root,text='')
	dq=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	l4.configure(text=str(dq))
	l5=t.Label(root,text='物理内存使用情况(MB)：')
	l6=t.Label(root,text='')
	jh=psutil.virtual_memory()
	tt=int((jh.total)/1024/1024)
	us=int((jh.used)/1024/1024)
	fr=int((jh.free)/1024/1024)
	l6.configure(text='总量：' + str(tt) +'\n'+'使用：'+str(us) +'\n'+'剩余：'+str(fr))
	l7=t.Label(root,text='交换内存使用情况(MB)：')
	l8=t.Label(root,text='')
	hj=psutil.swap_memory()
	ht=int((hj.total)/1024/1024)
	hu=int((hj.used)/1024/1024)
	hf=int((hj.free)/1024/1024)
	l8.configure(text='总量：' + str(ht) + '  '+'使用：'+str(hu) +'  '+'剩余：'+str(hf))
	text.window_create('insert',window=l1)
	text.window_create('insert',window=l2)
	text.insert('insert','\n\n')
	text.window_create('insert',window=l3)
	text.window_create('insert',window=l4)
	text.insert('insert','\n\n')
	text.window_create('insert',window=l5)
	text.window_create('insert',window=l6)
	text.insert('insert','\n\n')
	text.window_create('insert',window=l7)
	text.window_create('insert',window=l8)
	root.update()

def lw():
	text.delete(1.0,'end')
	n = psutil.net_io_counters()
	r=str(float(n.bytes_recv / 1024 / 1024))+'MB'
	s= str(float(n.bytes_sent / 1024 / 1024))+'MB'
	text.insert('insert','网卡接收流量: '+str(r)+'\n'+'网卡发送流量：'+str(s)+'\n')
	root.update()

def yh():
	text.delete(1.0,'end')
	use='    用户'+'      '+'     状态'+'\n'
	text.insert('insert',use)
	for y in psutil.users():
		text.insert('2.0',str(y.name)+'  '+'运行中。。。。'+'\n')
	root.update()
m=t.Menu(root)
#文件菜单
file=t.Menu(m,tearoff=False) 
m.add_cascade(label='文件', menu=file)
file.add_command(label='新建任务',accelerator='(N)')
file.add_command(label='退出任务栏管理器',command=root.quit,accelerator='(x)')


#选项菜单
ii=t.IntVar()
ii.set(1)
o=t.Menu(m,tearoff=False)
m.add_cascade(label='选项',menu=o)
o.add_radiobutton(label='前端显示',variable=ii, value=0)
o.add_radiobutton(label='使用时最小化',variable=ii, value=1)
o.add_radiobutton(label='最小化时隐藏',variable=ii, value=2)


#查看菜单
v=t.Menu(m,tearoff=False)
m.add_cascade(label='查看',menu=v)
v.add_command(label='立即刷新')
#二级菜单
iv=t.IntVar()
iv.set(1)
s=t.Menu(v,tearoff=False)
v.add_cascade(label='更新速度',menu=s)
s.add_radiobutton(label='高',variable=iv, value=0)
s.add_radiobutton(label='普通',variable=iv, value=1)
s.add_radiobutton(label='低',variable=iv, value=2)
s.add_radiobutton(label='暂停',variable=iv, value=3)
v.add_command(label='选项列')


#帮助菜单
h=t.Menu(m,tearoff=False)
m.add_cascade(label='帮助',menu=h)
h.add_command(label='任务管理器帮助主体')
h.add_command(label='关于任务管理器')

b1=t.Button(root,text='应用程序',command=yy)	
b2=t.Button(root,text='进程',command=jc)
b3=t.Button(root,text='服务',command=fw)
b4=t.Button(root,text='性能',command=xn)
b5=t.Button(root,text='联网',command=lw)
b6=t.Button(root,text='用户',command=yh)	
b1.place(x=10,y=15,height=20,width=60)
b2.place(x=70,y=15,height=20,width=60)
b3.place(x=130,y=15,height=20,width=60)
b4.place(x=190,y=15,height=20,width=60)
b5.place(x=250,y=15,height=20,width=60)
b6.place(x=310,y=15,height=20,width=60)



def jcs():
	t1.configure(text='进程数：'+str(len(psutil.pids())))
	root.after(3000,jcs)
def cpu():
	pp=str(ceil(psutil.cpu_percent(1)))
	t2.configure(text='CPU 使用率：'+pp+'%')
	root.after(1500,cpu)
def wlnc():
	f= psutil.virtual_memory().free #剩余内存
	t=psutil.virtual_memory().total#总内存
	wl= float(t-f)/float(t) #为使得最后值更精确，必须用float
	t3.configure(text='物理内存：'+str(floor(wl*100))+'%') 
	root.after(2000,wlnc)
root.bind('<Visibility>',yy()) #当打开窗口时显示第一个按钮选项
root.bind('<Visibility>',jcs())
root.bind('<Visibility>',cpu())
root.bind('<Visibility>',wlnc())
root.configure(menu=m)
root.mainloop() #主窗口循环显示