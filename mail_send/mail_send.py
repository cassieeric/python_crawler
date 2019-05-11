import poplib  # 引入poplib模块
from email.parser import Parser  # 引入解析模块
from email.header import decode_header  # 获取头文件的编码信息
from email.utils import parseaddr  # 格式化邮件信息
import smtplib  # 引入smtp模块
from email.mime.text import MIMEText  # 邮件内容为纯文本或HTML页面
from email.header import Header # 从email引入Header方法，Header()用来构建邮件头

def login_in():  # 登录阶段
    global email,password,pop_server,server1,server2

    email=input('请输入您的邮箱账号：')  # 输入邮件地址
    password=input('请输入第三方授权码:')  # 输入第三方授权码
    pop_server=input('请输入POP3服务器地址:')  # 输入pop服务器地址

    server1=poplib.POP3_SSL(pop_server)  # 连接到POP3服务器(当使用的邮箱pop服务有加密时，使用POP3_SSL)
    print(server1.getwelcome().decode('utf-8'))  # 打印POP3服务器的欢迎文字

    # 身份认证
    server1.user(email)
    server1.pass_(password)

def handle_command(user_cmd,email_title):  # 处理命令
    if user_cmd=='1':
        #  展示出主要信息
        print('邮件总数: %s; 占用的空间大小: %s;' % server1.stat())  # 利用stat()可返回邮件数量和占用空间
    elif user_cmd=='2':
        resp,lines,octets=server1.retr(email_title)
        msg_content=b'\r\n'.join(lines).decode('utf-8')  # 获取邮件的原始文本
        msg=Parser().parsestr(msg_content)  # 解析邮件的原始文本
        print_infor(msg)
    else :
        print('error command!\n')

def print_infor(msg,indent=0):  # 输出信息
    if indent==0:  # indent用于缩进显示
        for header in ['From','To','Subject']:
            value=msg.get(header,'')
            if value:
                if header=='Subject':
                    value=decode_str(value)   # 解码主题信息
                else :                     
                    hdr,addr=parseaddr(value)  # 解码发件人和收件人信息
                    name=decode_str(hdr)
                    value=u'%s <%s>'%(name,addr)
            print('%s%s: %s'%('  '*indent,header,value))
            
    # 将组合邮件对象分离
    if msg.is_multipart():
        parts=msg.get_payload()  # 提取msg的子对象
        for n,part in enumerate(parts):
            print('%spart %s'%('  '*indent,n))
            print('%s---------------'%('  '*indent))
            print_infor(part,indent+1)
    # 逐一打印邮件对象
    else:
        content_type=msg.get_content_type()   # 获取邮件对象的格式
        if content_type=='text/plain' or content_type=='text/html':  # 若为文本邮件，直接打印
            content=msg.get_payload(decode=True)
            charset=guess_charset(msg)  # 检测编码
            if charset:
                content=content.decode(charset) # 解码
            print('%sText: %s'%('  '*indent,content+'...'))  # 打印文本内容
        else:
            print('%sAttachment :%s'%('  '*indent,content_type))  # 否则为附件，获取附件信息

def decode_str(s):  # 解码
    value,charset=decode_header(s)[0]
    if charset:
        value=value.decode(charset)  # 如果存在编码问题，则进行相应的解码
    return value;

# 定义一个检测编码的函数
def guess_charset(msg):
    charset=msg.get_charset()   # 采用get_charset()的方法获取编码
    if charset is None:       # 若获取不到，则在原始文本中寻找
        content_type=msg.get('Content-Type','').lower()   # lower()把字符串全改为小写
        pos=content_type.find('charset=')  # 在原始文本中找'charset'字符串
        if pos>=0:                        # 若存在，则获取其后面的编码信息
            charset=content_type[pos+8:].strip()   # strip()用于去除字符串前后空格字符
    return charset

def sendmail():
    to_add=input('请输入收件邮箱：')
    server_smtp=input('请输入SMTP服务器地址：')
    text=input('请编辑您的邮件内容(按Enter键结束)\n')
    msg=MIMEText(text,'plain','utf-8')
    # 构建邮件头(发件人、收件人、邮件主题)
    msg['From']=Header(email)
    msg['To']=Header(to_add)
    msg['Subject']=Header(input('请编辑邮件主题：\n'))
    server2=smtplib.SMTP()
    server2.connect(server_smtp,25)  # 链接服务器
    server2.login(email,password)  # 登录邮箱
    server2.sendmail(email,to_add,msg.as_string())
    #server2.quit()

def start():  # 开始
    login_in()  # 调用登录阶段的login_in函数

    resp,mails,octets=server1.list()  # 获取邮件列表
    print(mails)  # 打印所有邮件编号及占用大小
    index=len(mails)  # 邮件总数目赋值给index
    print(index)
    print('\n--------------------------------------------')
    print('输入"0"退出邮箱\n输入"1" 获取收件箱的主要信息.\n输入"2" 查看具体的邮件信息\n输入"3"发送邮件')
    print('--------------------------------------------\n')

    while True:
        command=input('请输入您的操作指令：\n')
        if command=='0':
            break

        elif command=='2':
            email_num=input('请输入您想要查看的邮箱编号:')
            handle_command(command,email_num)
        elif command=='3':
            sendmail()
            print('\n邮件发送成功!')
        else:
            handle_command(command,0)
        print("\n")
    server1.quit()
    print('您已成功退出pop3邮箱服务器！')

start()
