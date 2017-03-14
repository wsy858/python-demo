# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DoubantestItem(Item):
    # define the fields for your item here like:
    title = Field()  # 标题
    info = Field()  # 描述
    star = Field()  # 评分
    quote = Field()  # 名句
