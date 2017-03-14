# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DaomubijiItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = Field()  # 书名
    book_info = Field()  # 书描述
    chapter_name = Field()  # 章节名
    datetime = Field()  # 发表时间
    content = Field()  # 章节内容
