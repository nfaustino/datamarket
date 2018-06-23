# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DatamarketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	
	dim_8q8e = scrapy.Field()
	dim_8q8g = scrapy.Field()
	dim_8q8f = scrapy.Field()	
	Year	 = scrapy.Field()
	People	 = scrapy.Field()

    pass
