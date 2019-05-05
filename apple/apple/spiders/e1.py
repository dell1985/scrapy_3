# -*- coding: utf-8 -*-
import scrapy
import re

class A1Spider(scrapy.Spider):


    name = 'e1'
    allowed_domains = ['http://czce.com.cn']
    url='http://www.czce.com.cn/cn/DFSStaticFiles/Future/2019/20190422/FutureDataHolding.htm'
    start_urls = [url]

    def parse(self, response):
        #这里取回期货品种的数据
        #/html/body/div/table/tbody/tr/td[1]/b 这是第一个的期货品种名称
        #所有期货名称的节点列表1/html/body/div/table/tbody/tr/td/
        name_form_heml = response.xpath('/html/body/div/table/tbody/tr/td/b/text()')
        # 所有期货交易信息
        jydate_list_html=response.xpath('/html/body/div/table/tbody/tr/td/text()')
        jydate_list_html1=response.xpath('/html/body/div/table/tbody/tr[1361]/td/text()')
        jydate_list_html2=response.xpath('/html/body/div/table/tbody/tr/td')
        # 用来存放所有的item字段
        i=1

        o=0
        jydate_list=[]
        for jydate in jydate_list_html1:

            a=(jydate.extract())
            print(i)
            i=i+1
            print(a)
            # #数据整理

            a = ("".join(a))
            print(type(a))
            print(a)
            jydate_list.append(a)
            print(jydate_list)
            #ydate_save = (jydate_list[o:o + 1])
            # c=['1', '华泰期货', '18,332', '-14,037', '华泰期货', '7,591', '462', '中信期货', '8,432', '404']
            print(i)
            i=i+1

        #     # print(d[0:10])
        #     # #print(d)
        #     # #print(jydate_list)
        #     # print(d[0:1])
        #     # print(d[1:2])
        #     # print(jydate_list[2:3])
        #     # print(jydate_list[3:4])
        #     # print(jydate_list[4:5])
        #     # print(jydate_list[5:6])
        #     # print(jydate_list[6:7])
        #     # print(jydate_list[7:8])
        #     # print(jydate_list[8:9])
        #     # print(jydate_list[9:10])
        #     # print(jydate_list[12:13])

            c=jydate_list
        #
        #     print(type(c))
        #     print(c)
        yield {

            "a0":c[0:1],
            "a1":c[1:2],
            "a2":(c[2:3]),
            "a3":c[3:4],
            "a4":c[4:5],
            "a5":c[5:6],
            "a6":c[6:7],
            "a7":c[7:8],
            "a8":c[8:9],
            "a9":c[9:10],

        }
