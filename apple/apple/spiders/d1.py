# -*- coding: utf-8 -*-
import scrapy



class A1Spider(scrapy.Spider):


    name = 'd1'
    allowed_domains = ['http://czce.com.cn']
    url='http://www.czce.com.cn/cn/DFSStaticFiles/Future/2019/20190422/FutureDataHolding.htm'
    start_urls = [url]

    def parse(self, response):
        #这里取回期货品种的数据
        #/html/body/div/table/tbody/tr/td[1]/b 这是第一个的期货品种名称
        #所有期货名称的节点列表1/html/body/div/table/tbody/tr/td/
        name_form_heml = response.xpath('/html/body/div/table/tbody/tr')
        # 所有期货交易信息
        jydate_list=response.xpath('/html/body/div/table/tbody/tr/td/text()')
        # 用来存放所有的item字段
        i=1

        o=0
        name_list=[]
        for pz in name_form_heml:
            print(pz)
            # #数据整理
            a=pz.extract()
            print(a)
            a = (" ".join(a))
            print(a)

            # a=a.replace("\xa0\xa0\xa0\xa0日期：","")
            # a=a.replace("合约：", "")
            # a=a.replace("品种：", "")
            # # b=日期
            # b=a[-10:]
            # name=a.replace(b,"")
            # #格式整理完毕
            #
            # #单个期货名称数据添加到列表name_list中
            # name_list.append(name)
            # i=i+1
            # name_save=(name_list[o:o+1])
            # print(name_save)
            # print(jydate_list)
            o = o + 1
            print(o)
            # # l=0
            # # for jydate in jydate_list:
            # #     l=l+1
            # #     print(jydate)
            #
            # yield {
            #     '日期':b,
            #     '品种': name_save
            # }
