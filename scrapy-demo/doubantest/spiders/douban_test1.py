# _*_ coding:UTF-8 _*_
import scrapy

from doubantest.items import DoubantestItem

'''
豆瓣电影TOP250爬虫示例
'''
class DoubanSpider(scrapy.Spider):
    # 爬虫的识别名，它必须是唯一的，在不同的爬虫中你必须定义不同的名字.
    name = "douban"
    # 包含了Spider在启动时进行爬取的url列表。
    start_urls = ['https://movie.douban.com/top250']

    # 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
    # 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self, response):
        # print response.body
        item = DoubantestItem()
        for li in response.css('ol.grid_view li'):
            # 标题
            titles = li.css('.info span.title::text').extract()
            full_title = ''
            for t in titles:
                full_title += t
            # 描述
            info = li.css('.bd p::text').extract_first()
            if info is not None:
                info = info.strip()  # 去掉空格
            # 评分
            star = li.css('.star .rating_num::text').extract_first()
            # 名言
            quote = li.css('.quote .inq::text').extract_first()
            if quote is None:
                quote = ''
            item['title'] = full_title
            item['info'] = info
            item['star'] = star
            item['quote'] = quote
            yield item
        next_page = response.css('.paginator .next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
