# -*- coding: utf-8 -*-
import scrapy
import re

#这是每天交易数据，无期货合约的名称
class A1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['http://czce.com.cn']
    url = 'http://www.czce.com.cn/cn/DFSStaticFiles/Future/2019/20190423/FutureDataHolding.htm'
    start_urls = [url]

    def parse(self, response):
        # 这里取回期货品种的数据
        # /html/body/div/table/tbody/tr/td[1]/b 这是第一个的期货品种名称
        # 所有期货名称的节点列表1/html/body/div/table/tbody/tr/td/
        name_form_heml = response.xpath('/html/body/div/table/tbody/tr/td/b/text()')
        # 所有期货交易信息
        jydate_from_html = response.xpath('/html/body/div/table/tbody/tr/td/text()')
        i = 1
        o=0
        name_list = []
        for pz in name_form_heml:
            print(pz)
            # 数据整理
            a = pz.extract()
            a = ("".join(a))
            print(a)
            a = a.replace("\n", '')
            # a=a.replace(" ","")
            a = a.replace("\xa0\xa0\xa0\xa0日期：", "")
            a = a.replace("合约：", "")
            a = a.replace("品种：", "")
            # b=日期
            b = a[-10:]
            name = a.replace(b, "")
            # 格式整理完毕

            # 单个期货名称数据添加到列表name_list中
            name_list.append(name)
            print(name_list)
            i = i + 1
            name_save = (name_list[o:o + 1])
        #name_list存放整理完成的期货名称（品种）
        print(name_list)
        z = 0
        #列表jydate_list 存放交易数据
        jydate_list = []
        for jydate in jydate_from_html:
            a = (jydate.extract())
            print(a)
            d = a.split(" ")
            print('type====', type(a))
            jydate_list.append(a)
            print(z)
            z = z + 1

        #jydate_list用来存放所有的交易字段
        endk = len(jydate_list)
        y=0
        for j in range(0,endk,10):
                print(j,j+10)
                a1 = jydate_list[j:j+10]


                pda=(a1[0:1])

                if (pda==['合计']or(pda==['合计 '])):
                    yield {
                        "日期": b,
                        "期货品种": name_list[y:y + 1],
                        "名次": a1[0:1],
                        "会员简称0": a1[1:2],
                        "成交量（手）": a1[2:3],
                        "增减量0": a1[3:4],
                        "会员简称1": a1[4:5],
                        "持买仓量": a1[5:6],
                        "增减量1": a1[6:7],
                        "会员简称2": a1[7:8],
                        "持卖仓量": a1[8:9],
                        "增减量2": a1[9:10],
                    }
                    y=y+1

                    pass
                else:

                    yield {
                            "日期":b,
                            "期货品种":name_list[y:y+1],
                            "名次": a1[0:1],
                            "会员简称0": a1[1:2],
                            "成交量（手）": a1[2:3],
                            "增减量0": a1[3:4],
                            "会员简称1": a1[4:5],
                            "持买仓量": a1[5:6],
                            "增减量1": a1[6:7],
                            "会员简称2": a1[7:8],
                            "持卖仓量": a1[8:9],
                            "增减量2": a1[9:10],
                    }

