# -*- coding: utf-8 -*-
import scrapy

from TencentJobs.items import TencentjobsItem

class TencentjobSpider(scrapy.Spider):
    name = 'tencentjob'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']
    base_url = 'https://hr.tencent.com/'

    def parse(self, response):

        next_page = response.xpath('//a[@id="next"]/@href').extract_first()
        
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentjobsItem()
            item['positionNames']=each.xpath('./td[1]/a/text()').extract_first()
            item['positionTypes']=each.xpath('./td[2]/text()').extract_first()
            item['positionNums']=each.xpath('./td[3]/text()').extract_first()
            item['workLocations']=each.xpath('./td[4]/text()').extract_first()
            item['publishTime']=each.xpath('./td[5]/text()').extract_first()
            item['positionLinks']=each.xpath('./td[1]/a/@href').extract_first()

            yield item

        yield scrapy.Request(url=self.base_url + next_page, callback=self.parse)


    
            
