# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
import csv


def qh_date(ymd):
    html_begin='http://www.czce.com.cn/cn/DFSStaticFiles/Future/'
    html_end='/FutureDataHolding.htm'
    m_y=ymd[0:4]
    url=html_begin+m_y+'/'+ymd+html_end
    return url


ymd = csv.reader(open("2019A.csv"))
date_list=[]
for row in ymd:
    row = ''.join(row)
    date_list.append(row)


#这是一天交易数据
class A1Spider(scrapy.Spider):

    name = 'h3'
    allowed_domains = ['czce.com.cn']
    url = 'http://www.czce.com.cn/cn/DFSStaticFiles/Future/2018/20180102/FutureDataHolding.htm'
    start_urls = [url]

    def parse(self, response):
        print(Request.url)

        date_list.pop(0)
        a=date_list[0:1]
        b=(''.join(a))
        next=qh_date(b)
        print(next)
        yield Request(next)
