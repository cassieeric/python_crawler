"""
    作者：崔艳飞
    名称：多EXCEL多sheet合并
    功能：文件夹下多EXCEL多sheet合并，自动获取SHEET名
    版本：V2.0
    日期：2019.10.21
"""
import pandas as pd
import xlrd
import os

def main():
    #要合并文件路径
    path = "E:\\PythonCrawler\\python_crawler-master\\MergeExcelSheet\\testfile\\"
    #获取文件夹下所有EXCEL名
    xlsx_names = [x for x in os.listdir(path) if x.endswith(".xlsx")]
    # 获取第一个EXCEL名
    xlsx_names1 = xlsx_names[0]

    aa = path + xlsx_names1
    #打开第一个EXCEL
    first_file_fh=xlrd.open_workbook(aa)
    # 获取SHEET名
    first_file_sheet=first_file_fh.sheets()

    sheet_names=[]

    for sheetname in first_file_sheet:
        sheet_names.append(sheetname.name)

    #定义输出合并结果文件名
    bb = path + 'Python实现多Excel多Sheet合并.xlsx'
    writer = pd.ExcelWriter(bb,engine='openpyxl')
    num = 1

    #按SHEET名循环
    for sheet_name in sheet_names:
        df = None
        # 按EXCEL名循环
        for xlsx_name in xlsx_names:
            sheet_na = pd.ExcelFile(path + xlsx_name).sheet_names
            if sheet_name in sheet_na:
                #print(sheet_name)
                _df = pd.read_excel(path + xlsx_name, sheet_name=sheet_name,header=None)
                if df is None:
                    df = _df
                else:
                    df = pd.concat([df, _df], ignore_index=True)
            else:continue
        # 下面的保存文件处填写writer，结果会不断地新增sheet，避免循环时被覆盖
        df.to_excel(excel_writer=writer, sheet_name=sheet_name, encoding="utf-8", index=False)
        print(sheet_name + "  保存成功！共%d个，第%d个。" % (len(sheet_names),num))
        num += 1
    writer.save()
    writer.close()

if __name__ == '__main__':
    main()