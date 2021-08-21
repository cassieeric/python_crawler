# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :jd.py
# @Time      :2021/8/21 10:22
# @Author    :Mtc
 

import  requests
import  json
import  time
import  openpyxl  #第三方模块，用于操作Excel文件的
#模拟浏览器发送请求并获取响应结果
import random

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
def get_comments(productId,page):
    url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={0}&score=0&sortType=5&page={1}&pageSize=10&isShadowSku=0&fold=1'.format(productId,page) # 商品id
    resp=requests.get(url,headers=headers)
    #print(resp.text)  #响应结果进行显示输出
    s1=resp.text.replace('fetchJSON_comment98(','') #fetchJSON_comment98(
    s=s1.replace(');','')
    #将str类型的数据转成json格式的数据
    # print(s,type(s))
    # print('*'*100)
    res=json.loads(s)
    print(type(res))
    return res

def get_max_page(productId):
    dic_data=get_comments(productId,0)  #调用刚才写的函数，向服务器发送请求，获取字典数据
    return dic_data['maxPage']

def get_info(productId):
    #调用函数获取商品的最大评论页数
    #max_page=get_max_page(productId)
    # max_page=10
    lst=[]  #用于存储提取到的商品数据
    for page in range(0,get_max_page(productId)):   #循环执行次数
        #获取每页的商品评论
        comments=get_comments(productId,page)
        comm_lst=comments['comments']   #根据key获取value，根据comments获取到评论的列表（每页有10条评论）
        #遍历评论列表，分别获取每条评论的中的内容，颜色，鞋码
        for item in comm_lst:   #每条评论又分别是一个字典，再继续根据key获取值
            content=item['content']  #获取评论中的内容
            color=item['productColor'] #获取评论中的颜色
            size=item['productSize'] #鞋码
            lst.append([content,color,size])  #将每条评论的信息添加到列表中
        time.sleep(3)  #延迟时间，防止程序执行速度太快，被封IP
    save(lst)  #调用自己编写的函数，将列表中的数据进行存储

def save(lst):
    wk=openpyxl.Workbook () #创建工作薄对象
    sheet=wk.active  #获取活动表
    #遍历列表，将列表中的数据添加到工作表中,列表中的一条数据，在Excel中是 一行
    for item in lst:
        sheet.append(item)
    #保存到磁盘上
    wk.save('销售数据.xlsx')

if __name__ == '__main__':
    productId='10029693009906' # 单品id
    get_info(productId)