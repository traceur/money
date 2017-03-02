# -*- coding:utf-8 -*-
'''
基金爬虫 By Qiaoy
'''

from money.items import MoneyItem
import scrapy,datetime

def daterange( start_date, end_date ):
    if start_date == end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

start = datetime.date( year = 2011, month = 1, day = 1 )
end = datetime.date( year = 2002, month = 1, day = 1 )


class DmozSpider(scrapy.Spider):
    name = "money"
    allowed_domains = ["www.kjj.com"]
    start_urls = [
        "http://www.kjj.com/indexMore.php?date=%s"%date for date in daterange(start, end)
    ]

    def parse(self, response):
    	money = MoneyItem()
        for i in response.xpath('//*[@class="tr"]'):
        	td = i.xpath('td')
        	value = td.xpath('string(.)').extract()
        	money['time'] = value[1]
        	money['number'] = value[2]
        	money['name'] = value[3]
        	money['asset_now'] = value[4]
        	money['asset_acc'] = value[5]
        	money['add_number'] = value[6]
        	money['add_percentage'] = value[7]
        	yield money
