# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import json
import csv
from TencentJobs.items import TencentjobsItem

class TencentjobsPipeline(object):
    #save data to json
    #def open_spider(self, spider):
        #self.file=open('tencent_jobs.csv','w', encoding='utf-8')
        
    #def process_item(self, item, spider):
        #content=json.dumps(dict(item), ensure_ascii=False)
        #self.file.write(content+'\n')
            
        #return item

    #def close_spider(self, spider):
        #self.file.close()

    #save data to csv
    def process_item(self, item, spider):
        f=open('tencent_jobs.csv', 'a+')
        writer=csv.writer(f)
        writer.writerow((item['positionNames'],item['positionTypes'],item['positionNums'],
                         item['workLocations'],item['publishTime'],item['positionLinks']))
        return item
