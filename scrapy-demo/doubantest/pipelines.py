# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bson import ObjectId
from scrapy.conf import settings
import pymongo
import logging

# 接收并处理数据
class DoubantestPipeline(object):

    collection_name = 'doubanmovie'

    def __init__(self):
        self.host = settings['MONGODB_HOST']
        self.port = settings['MONGODB_PORT']
        self.db_name = settings['MONGODB_DBNAME']
        self.client = None
        self.database = None

    def open_spider(self, spider):
        spider.logger.info('=============================== open mongodb')
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.database = self.client[self.db_name]

    def close_spider(self, spider):
        spider.logger.info('=============================== close mongodb')
        if self.client is not None:
            self.client.close()

    def process_item(self, item, spider):
        # print '=============================== ', item
        try:
            document = dict(item)
            document['_id'] = ObjectId().__str__()
            self.database[self.collection_name].insert(document)
        except Exception as e:
            logging.error('mongodb insert error ', e.message, e)
        return item
