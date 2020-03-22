from mailmerge import MailMerge
import pandas as pd

data = pd.read_excel('模板.xlsx') #注意路径，此处我将模板放在python目录下，使用相对路径
rows = data.shape[0] #获取行数 
for i in range(rows):
    name = data["姓名"][i]
    id = data["身份证号"][i] #以上三行为遍历Excel每行数据并赋值
    # print(name,id)
    template = '模板.docx'
    document = MailMerge(template)
    document.merge(
        name = str(name),
        id = str(id)
    )
    document.write(str(name)+'复工证明.docx') #以上六行为mailmerge方法

input('操作成功，按回车键退出！')
