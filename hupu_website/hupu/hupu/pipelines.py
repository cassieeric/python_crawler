# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from openpyxl import Workbook
from openpyxl import load_workbook

from project.parts import parts

results = {}

class ProjectPipeline(object):
    def process_item(self, item, spider):
        if item['part'] not in results:
            results[item['part']] = []

        comment_all = []
        for comment in item['comment']:
            if comment['comment_quote_author']:  # 有引用
                comment_all.append('评论者:{}, 认可数:{},评论:{}\n引用者:{}, 引用内容:{}\n==================\n'.format(comment['comment_author'],
                                                                                          comment['comment_light'],
                                                                                          comment['comment'],
                                                                                          comment[
                                                                                              'comment_quote_author'],
                                                                                          comment[
                                                                                              'comment_quote_content']))
            else:
                comment_all.append('评论者:{}, 认可数:{},评论:{}\n==================\n'.format(comment['comment_author'],
                                                                         comment['comment_light'],
                                                                         comment['comment'],
                                                                         ))

        results[item['part']].append(
            [item['part'], item['title'], item['author'], item['reply_count'], item['link_count'], item['view_count'],
             ''.join(comment_all)])
        return item

    def close_spider(self, spider):
        for key, value in results.items():
            wb = Workbook()
            ws = wb.active
            ws.append(['专区', '帖子', '楼主', '回复量', '点赞量', '浏览量', '评论者', ' 认可数', '评论', '引用'])
            for item in value:
                ws.append(item)
            wb.save('results/{}.xlsx'.format(key))
