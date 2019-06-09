# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import MySQLdb
import MySQLdb.cursors

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi

class ArticlePipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # dumps()函数里边接收字典，需要将其转为字典；第二个参数很重要，支持中文等其他字符的写入
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class MysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        # self.conn = MySQLdb.connect('host', 'user', 'password', 'dbname', charset='utf8', use_unicode=True)
        self.conn = MySQLdb.connect('localhost', 'root', '123456', 'article_spider', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(title, url, release_date, voteup_num)
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["title"], item["url"], item["release_date"], item["voteup_num"]))
        self.conn.commit()

class MysqlTwistedPipeline(object):
    # 采用异步的机制写入mysql
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        # 如果上面的代码看不懂，下面的代码是等价的
        # dbpool = adbapi.ConnectionPool("MySQLdb",
        #     host=settings["MYSQL_HOST"],
        #     db=settings["MYSQL_DBNAME"],
        #     user=settings["MYSQL_USER"],
        #     passwd=settings["MYSQL_PASSWORD"],
        #     charset='utf8',
        #     cursorclass=MySQLdb.cursors.DictCursor,
        #     use_unicode=True)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # 处理异常

    def handle_error(self, failure):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = """
                    insert into jobbole_article(title, url, release_date, voteup_num)
                    VALUES (%s, %s, %s, %s)
                """
        cursor.execute(insert_sql, (item["title"], item["url"], item["release_date"], item["voteup_num"]))


class JsonExporterPipeline(object):
    # 调用Scrapy提供的json exporter导出json文件
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        pass
        for ok, value in results:
            image_file_path = value["path"]
        item["front_image_path"] = image_file_path
        return item