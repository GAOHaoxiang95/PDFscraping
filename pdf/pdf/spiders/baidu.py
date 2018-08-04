# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['wenku.baidu.com']
    base_urls = 'https://wenku.baidu.com/search?word=imperial+college&org=0&fd=0&lm=0&od=0&pn='

    def start_requests(self):
        for i in range(0, 500, 10):
            url = self.base_urls + str(i)
            yield scrapy.Request(url, callback = self.parse)
		
    def parse(self, response):
        link = response.xpath('//dt[contains(@class, "logFirstClickTime")]//a/@href').extract()
        print(link)