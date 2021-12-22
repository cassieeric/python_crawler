# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import os
# 参考链接：https://mp.weixin.qq.com/s/kSY6n6t4l3mabm14gQ93iA
# define a starting point of time
start = datetime.datetime.now()


def Set_Work_Path(x):
    try:
        os.chdir(x)
        route = os.getcwd()
        print(route)
        return route
    except Exception:
        print("No Result")


work_path = r"E:\\PythonCrawler\\python_crawler-master\\MergeExcelSheet\\file\\"
Set_Work_Path(work_path)


# define a function to get all the xlsx file names after deleting old file if there.
def Get_Dedicated_4Letter_File_List(x):
    path = os.getcwd()
    old_name = path + os.sep + "汇总数据" + ".xlsx"  # dim a txt name
    if os.path.exists(old_name):
        os.remove(old_name)
    files = os.listdir(path)  # print(files) #check all files name in the path
    current_list = []
    for i in range(0, len(files), 1):
        try:
            if files[i][-4:] == x and files[i][:4] != "汇总数据":
                current_list.append(files[i])
        except Exception:
            pass
    return current_list


Current_Excel_list = Get_Dedicated_4Letter_File_List("xlsx")
print(Current_Excel_list)


# define a function to read all sheets one by one in excel file
def Get_All_Sheets_Excel(x):
    file = pd.ExcelFile(x)
    list_sht_name = file.sheet_names  # get list of sheets' names
    print(list_sht_name)
    list_sht_data = []  # get all sheet data sets into a list
    for i in range(0, len(list_sht_name), 1):
        list_sht_data.append(pd.read_excel(x, header=0, sheet_name=list_sht_name[i], index_col=None))
    # merge all data sets together
    df = pd.concat(list_sht_data)
    # delete blank data
    df.dropna(axis=0, how="all", inplace=True)
    print(df)
    return df


# define a list to get all data from sheets from different excel files
data_list = []
for i in range(0, len(Current_Excel_list), 1):
    # print(Current_Excel_list[i])
    data_list.append(Get_All_Sheets_Excel(Current_Excel_list[i]))
data = pd.concat(data_list)
data.dropna(axis=0, how="all", inplace=True)
print(data)

# save the data into excel file
writer = pd.ExcelWriter("王宁大佬的汇总数据.xlsx")
data.to_excel(writer, encoding="utf_8_sig", sheet_name="DATA", index=False)
# get the target pivot datasets
writer.save()

end = datetime.datetime.now()
run_time = round((end-start).total_seconds()/60, 2)
show = "程序运行消耗时间为: %s 分钟" % run_time+",搞定!"
print(show)
