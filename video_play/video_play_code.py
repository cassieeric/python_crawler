from selenium import webdriver
from tkinter import *
from PIL import ImageTk, Image

def OpenHtml(url):
    driver = webdriver.Firefox()
    url = 'http://jx.598110.com/?url={0}'.format(url)
    driver.get(url)

def GUI():
    top = Tk()
    canvas = Canvas(top, width=533, height=300, bd=0, highlightthickness=0)
    imgpath = '李沁.gif'
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(266, 150, image=photo)
    canvas.pack()
    top.title('VIP视频播放软件')
    top.geometry("533x300")   #设置软件窗口大小
    label_1 = Label(top, text='请输入视频网址', bg="plum", font=("华文行楷", 20), fg="OrangeRed",padx=0, pady=0)
    label_2 = Label(top, text='VIP视频播放软件', bg="plum", font=("华文行楷", 20), fg="OrangeRed", padx=0, pady=0)
    search_text = StringVar()
    e = Entry(top, textvariable=search_text)
    e.focus_get()
    btn = Button(text=u'播放',  command=lambda : OpenHtml(search_text.get()),
                 bg="SlateBlue", font=("华文行楷", 20), fg="OrangeRed")
    label_1.place(x=330, y=50)
    label_2.place(x=0, y=0)
    e.place(x=320, y=100, width=300, height=30)
    btn.place(x=400, y=150, width=50, height=50)
    top.mainloop()
def main():
    #l='https://www.iqiyi.com/v_19rwbtapc4.html?vfrm=pcw_home&vfrmblk=G&vfrmrst=711219_home_zongyi_float_pic_play4'
    GUI()
if __name__ == '__main__':
    main()
