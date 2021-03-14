"""
    作者：崔艳飞
    名称：查找最近的经纬度点
    功能：查找两张表中，最近的经纬度站点,跳过站名相同的站
    版本：V2.0
    日期：2020.5.26

"""
import pandas as pd
import xlrd
import os


from math import radians, cos, sin, asin, sqrt,pi


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371.137  # 地球平均半径，单位为公里
    return c * r * 1000

def main():
    path="D:/a/"
    #获取文件夹下所有EXCEL名
    bb = path + 'result.xlsx'
    writer = pd.ExcelWriter(bb,engine='openpyxl')
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
    df1 = pd.read_excel(aa, sheet_name=sheet_names[0])
    df2 = pd.read_excel(aa, sheet_name=sheet_names[1])
    df3 = pd.read_excel(aa, sheet_name=sheet_names[2])
    d2 = pd.DataFrame(columns=df2.columns.values)
    h1=df1.iloc[:, 0].size
    h2 = df2.iloc[:, 0].size
    resultdata1 = pd.DataFrame(columns=df1.columns.values)
    resultdata2 = pd.DataFrame(columns=df2.columns.values)
    resultdata3 = pd.DataFrame(columns=df3.columns.values)
    n8=len(df1['地市'])
    n9=1
    for i in range(h1):
        w1=df1.loc[i,'纬度']
        j1 = df1.loc[i,'经度']
        d1 = df1.loc[i, :]
        d0=float('inf')
        print("原小区第%d个。" %(i+1))
        test_dict = {'距离': [d0]}
        d3 = pd.DataFrame(test_dict)
        print('第{}个共{}个'.format(n9, n8))
        n9 += 1
        for l in range(h2):
            w2=df2.loc[l, '纬度']
            j2=df2.loc[l,'经度']
            d=haversine(j1, w1, j2, w2)
            if d<d0:
                d0=d
                d2 = df2.loc[l, :]
                test_dict = {'距离': [d0]}
                d3 = pd.DataFrame(test_dict)
            else:continue
        resultdata1 = resultdata1.append(d1)
        resultdata2 = resultdata2.append(d2)
        resultdata3 = resultdata3.append(d3)
    resultdata1.to_excel(excel_writer=writer, sheet_name='原小区', encoding="utf-8", index=False)
    resultdata2.to_excel(excel_writer=writer, sheet_name='最近小区', encoding="utf-8", index=False)
    resultdata3.to_excel(excel_writer=writer, sheet_name='距离', encoding="utf-8", index=False)
    writer.save()
    writer.close()

if __name__ == '__main__':
    main()
