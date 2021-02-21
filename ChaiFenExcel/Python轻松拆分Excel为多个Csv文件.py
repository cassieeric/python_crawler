
from tkinter import filedialog
import pandas as pd
import xlrd

def main():
    path = filedialog.askopenfilename().replace('/', '\\')
    first_file_fh=xlrd.open_workbook(path)
    # 选择要拆分的文件
    first_file_sheet=first_file_fh.sheets()
    # 获取sheet名
    sheet_names=[]
    for sheetname in first_file_sheet:
        sheet_names.append(sheetname.name)
    df = pd.read_excel(path, sheet_name=sheet_names[0])
    # 读取要拆分的sheet
    list_c = df['地市'].unique()
    # 获取要拆分列的内容
    for c in list_c:
        # 根据列的内容循环读取
        df2=df[df['地市']==c]
        # 根据列的内容进行筛选
        df2.to_csv('./excel_csv/auto_ok/'+c+'.csv', encoding='gbk',index=None)
        # 筛选后的内容保存为CSV

if __name__ == '__main__':
    main()
