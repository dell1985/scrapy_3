# _*_coding:utf-8_*_
import csv
import json
import scrapy
def qh_date(ymd):
    html_begin='http://www.czce.com.cn/cn/DFSStaticFiles/Future/'
    html_end='/FutureDataHolding.htm'
    m_y=ymd[0:4]
    url=html_begin+m_y+'/'+ymd+html_end
    return url

#data\2019A.csv里存放2018年至今的交易日历
ymd = csv.reader(open("18_1_6.csv"))
#ymd = csv.reader(open("2019A.csv"))
date_list=[]
for row in ymd:
    row=''.join(row)
    date_list.append(row)
print(date_list)

