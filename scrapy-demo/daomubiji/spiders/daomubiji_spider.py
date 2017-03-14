# _*_ coding:UTF-8 _*_
import scrapy

from daomubiji.items import DaomubijiItem

'''
盗墓笔记爬虫示例
'''


class DaomubijiSpider(scrapy.Spider):
    # 爬虫的识别名，它必须是唯一的，在不同的爬虫中你必须定义不同的名字.
    name = "daomubiji"
    # 包含了Spider在启动时进行爬取的url列表。
    start_urls = ['http://www.daomubiji.com/']

    book_info_dict = {}

    # 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
    # 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self, response):
        # print response.body
        # item = DaomubijiItem()
        for href in response.css(".article-content  a::attr(href)").extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_book)

        for article_content in response.css('.homebook'):
            book_name = article_content.css('h2::text').extract_first()
            book_info = article_content.css('p.homedes::text').extract_first()
            self.book_info_dict[book_name] = book_info

    # 处理主页每本书链接
    def parse_book(self, response):
        for href in response.css("div.excerpts .excerpt-c3 a::attr(href)").extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_chapter)

    # 处理每章节内容
    def parse_chapter(self, response):
        item = DaomubijiItem()
        book_name = response.css('.content .item-3 a::text').extract_first()
        book_info = self.book_info_dict.get(book_name, '')
        chapter_name = response.css('.content .article-title::text').extract_first()
        datetime = response.css('.content .item-1::text').extract_first()
        full_content = ''
        for c_p in response.css('.content .article-content p').extract():
            full_content += c_p
        item['book_name'] = book_name
        item['book_info'] = book_info
        item['chapter_name'] = chapter_name
        item['datetime'] = datetime
        item['content'] = full_content
        yield item
