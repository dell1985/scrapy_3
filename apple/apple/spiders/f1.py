# -*- coding: utf-8 -*-
import scrapy
import re

#这是每天交易数据，无期货合约的名称
class A1Spider(scrapy.Spider):
    name = 'f1'
    allowed_domains = ['http://czce.com.cn']
    url = 'http://www.czce.com.cn/cn/DFSStaticFiles/Future/2019/20190423/FutureDataHolding.htm'
    start_urls = [url]

    def parse(self, response):
        # 这里取回期货品种的数据
        # /html/body/div/table/tbody/tr/td[1]/b 这是第一个的期货品种名称
        # 所有期货名称的节点列表1/html/body/div/table/tbody/tr/td/
        name_form_heml = response.xpath('/html/body/div/table/tbody/tr/td/b/text()')
        # 所有期货交易信息
        jydate_list_html = response.xpath('/html/body/div/table/tbody/tr/td/text()')
        jydate_list_html1 = response.xpath('/html/body/div/table/tbody/tr[1362]/td')
        jydate_list_html2 = response.xpath('/html/body/div/table/tbody/tr/td/text()')
        j = '/html/body/div/table/tbody/tr[1361]/td'

        i = 0

        print(type(jydate_list_html2))
        o = 0
        jydate_list = []
        for jydate in jydate_list_html2:
            a = (jydate.extract())
            print(a)
            d = a.split(" ")
            print('type====', type(a))
            jydate_list.append(a)
            print(i)
            i = i + 1
        # print(type(jydate_list))
        # print(len(jydate_list))
        # print(jydate_list)
        #jydate_list用来存放所有的交易字段
        endk = len(jydate_list)

        for j in range(0,endk,10):
                print(j,j+10)
                a1 = jydate_list[j:j+10]
                print(a1)
                #if j<endk-10:
                pda=(a1[0:1])
                print(type(pda),pda)
                print("".join(pda))
                # if (pda==['合计']or(pda==['合计 '])):
                #     pass
                # else:

                yield {

                        "名次": a1[0:1],
                        "会员简称": a1[1:2],
                        "成交量（手）": a1[2:3],
                        "增减量": a1[3:4],
                        "会员简称": a1[4:5],
                        "持买仓量": a1[5:6],
                        "增减量": a1[6:7],
                        "会员简称": a1[7:8],
                        "持卖仓量": a1[8:9],
                        "增减量": a1[9:10],
                }

