import json
import requests
import re
import tkinter as tk 
from tkinter import ttk
 



class gui:
  def __init__(self):
    self.root=tk.Tk()
    self.root.title("爱奇艺热播好剧提前搜v1.0") 
    self.root.geometry("700x600")
    self.lb=tk.Label(self.root,text='请选择搜索类型')
    self.tt=tk.Text(self.root,width=40,height=30)
    self.cb=ttk.Combobox(self.root, width=12)
    self.cb['values'] = ('请选择-----','综合排序','热播榜','好评榜','新上线') #设置下拉列表框的内容   
    self.cb.current(0)    #将当前选择状态置为0,也就是第一项
    self.cb.bind("<<ComboboxSelected>>",self.go)  #绑定go函数，然后触发事件
    self.lb.place(x=30,y=30)
    self.cb.place(x=154,y=30)
    self.tt.place(x=30,y=60,width=600,height=600)
    self.root.mainloop()     #启动页面

  
  #获取页面请求状态
  def get_page(self,url):
    response = requests.get(url)
    if response.status_code == 200: #返回码200正常请求
      return response.text
    return None
 
 #解析页面获取评分，电影名，主演
  def parse_page(self,html):
    #编译页面电影内容正则
    pattern = re.compile('<li.*?qy-mod-li.*?text-score">(.*?)<.*?title.*?>(.*?)<.*?title.*?>(.*?)<', re.S)
    items = re.findall(pattern, html)  #查找
    for item in items:
      yield {
        'Movie_Name':  item[1],              #电影名
        'Movie_actor': item[2].strip()[3:],  #演员
        'Movie_score': item[0]               #评分
        
      } 
 
    
   #将内容写入到文本文件
  def write_to_file(self,content):
    with open('movie.txt', 'a', encoding='utf8')as f:
      f.write(json.dumps(content, ensure_ascii=False) + '\n')  #写入文件

  #主函数
  def main(self,url):
    html = self.get_page(url)
    for item in self.parse_page(html):
      self.tt.insert('insert',item)#将内容插入到文本框
      self.tt.insert('insert','\n')
      self.tt.update()  #更新内容
      self.write_to_file(item) #内容写入文件


  #下拉列表框事件
  def go(self,*arg):
    if self.cb.get()=='请选择-----':
      self.tt.delete('1.0','end')
    elif self.cb.get()=='综合排序':
      self.tt.delete('1.0','end')
      self.main('https://list.iqiyi.com/www/1/-------------24-1-1-iqiyi--.html')
    elif self.cb.get()=='热播榜':
      self.tt.delete('1.0','end')
      self.main('https://list.iqiyi.com/www/1/-------------11-1-1-iqiyi--.html')  
    elif self.cb.get()=='好评榜':
      self.tt.delete('1.0','end')
      self.main('https://list.iqiyi.com/www/1/-------------8-1-1-iqiyi--.html')  
    elif self.cb.get()=='新上线':
      self.tt.delete('1.0','end')
      self.main('https://list.iqiyi.com/www/1/-------------4-1-1-iqiyi--.html')  

gui()

# import requests
# from bs4 import BeautifulSoup
# rep=requests.get('https://list.iqiyi.com/www/1/-------------24-1-1-iqiyi--.html')
# soup=BeautifulSoup(rep.text,'lxml')
# aa=soup.find('div','qy-list-wrap')
# ab=aa.find('ul','qy-mod-ul')
# for y in ab.find_all_next('li'):
#   aa=y.find_next('img','qy-mod-cover fadeOutIn-enter-active')
#   ab=y.find_next('p','sub')
#   ac=y.find_next('span','text-score')
#   print('Movie_Name:'+aa.attrs['alt']+' '+'Movie_actor:'+ab.attrs['title']+' '+'Movie_score:'+ac.text)

