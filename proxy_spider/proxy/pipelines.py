# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class ProxyPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = self.client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def close_spider(self, spider):
        spider.logger.info('=============================== close mongodb')
        if self.client is not None:
            self.client.close()

    def process_item(self, item, spider):
        spider.logger.info('===============================process_item: ' + str(item))
        if item['port'] is not None and 80 <= int(item['port']) <= 65535:
            new_proxy = {
                "ip": item['ip'],
                "port": int(item['port']),
                "protocol": item['protocol'],
            }
            if self.collection.find_one(new_proxy) is None:
                self.collection.insert(new_proxy)
        return item
