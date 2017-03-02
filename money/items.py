# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoneyItem(scrapy.Item):
    # define the fields for your item here like:
    #pass
    time = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    asset_now = scrapy.Field()
    asset_acc = scrapy.Field()
    add_number = scrapy.Field()
    add_percentage = scrapy.Field()
