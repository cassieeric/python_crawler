import pandas as pd
import os

path = r'E:\PythonCrawler\python_crawler-master\MergeExcelSheet\file\777'
file_list = []
for root, dirs, filename in os.walk(path):
    for file in filename:
        file_list.append(path + '\\' + file)

# The_All_data = pd.DataFrame()
All_data = pd.DataFrame()

for Prowler in file_list:
    ereader = pd.ExcelFile(Prowler)    # 读到文件名称
    one_sheet_name = ereader.sheet_names   # 读到文件中所有sheet的名字
    for Sheet_Prowler in one_sheet_name:
        All_sheet_data = pd.read_excel(ereader, sheet_name=Sheet_Prowler)     # 读取文件名称中所有sheet的数据
        temp = pd.concat([All_data, All_sheet_data])
        All_data = pd.DataFrame(temp)
    # Montage = pd.concat([The_All_data, All_sheet_data])    # 拼接表格:将一个一个表格中所有sheet的数据放到汇总表之中
    # The_All_data = pd.DataFrame(Montage)                  # 将添加了新的数据的表格赋值给总表，下一次就会接到这个表的最后面。

print(All_data)

All_data.to_csv(r'E:\PythonCrawler\python_crawler-master\MergeExcelSheet\file\777\The_All_data.csv')

