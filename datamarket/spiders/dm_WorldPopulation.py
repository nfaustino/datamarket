# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 23:56:08 2018

@author: faustnun
"""

from scrapy.spiders import CSVFeedSpider
from datamarket.items import DatamarketItem

#import pandas as pd

class MySpider(CSVFeedSpider):
    name = 'csvexample'
    start_urls = ['https://datamarket-api.qlik.com/api/v6/table.csv?ds=516m']
    delimiter = ','
    headers = ['dim_8q8e','dim_8q8g','dim_8q8f','Year','People']
    
    def parse_row(self, response, row):
        log.msg('Hi, this is a row!: %r' % row)
        item = DatamarketItem()
        item['dim_8q8e'] = row['Address']
	item['dim_8q8g'] = row['Address']
	item['dim_8q8f'] = row['Address']
        item['Year']	 = row['Year']
	item['People']	 = row['People']
        return item
#df = pd.read_csv('https://datamarket-api.qlik.com/api/v6/table.csv?ds=516m')
