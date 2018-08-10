# -*- coding: utf-8 -*-
import scrapy
import pdf.items
from scrapy.loader import ItemLoader
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['wenku.baidu.com']
    base_urls = 'https://wenku.baidu.com/search?word=imperial+college&org=0&fd=0&lm=0&od=0&pn='

    def start_requests(self):
        for i in range(0, 500, 10):
            url = self.base_urls + str(i)
            yield scrapy.Request(url, callback = self.parse)
		
    def parse(self, response):
        item = pdf.items.PdfItem()

        link = response.xpath('//dt[contains(@class, "logFirstClickTime")]//a/@href').extract()
        title = response.xpath('//dt[contains(@class, "logFirstClickTime")]//a/@title').extract()
        for i in range(0, len(link)):
            l = ItemLoader(item=pdf.items.PdfItem(), response = response)
            l.add_value('link', link[i])
            l.add_value('title', title[i])
            yield l.load_item()
            #print('Link: ' + link[i] + ', ' + 'Title: ' + title[i])
            #print(link)