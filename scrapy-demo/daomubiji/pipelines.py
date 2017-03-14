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
class DaomubijiPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        database = client[db_name]
        self.collection = database.daomubiji

    def process_item(self, item, spider):
        # print '=============================== ', item
        try:
            document = dict(item)
            document['_id'] = ObjectId().__str__()
            self.collection.insert(document)
        except Exception as e:
            logging.error('mongodb insert error ', e.message, e)
        return item
