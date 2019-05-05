# -*- coding: utf-8 -*-
import scrapy



class A1Spider(scrapy.Spider):


    name = 'a1'
    allowed_domains = ['http://czce.com.cn']
    url='http://www.czce.com.cn/cn/DFSStaticFiles/Future/2019/20190422/FutureDataHolding.htm'
    start_urls = [url]

    def parse(self, response):
        #这里取回期货[品种]和[合约]名称的数据
        #品种是合约的组合
        #期货品种（合约）
        name_form_heml = response.xpath('/html/body/div/table/tbody/tr/td/b/text()')
        #期货交易信息
        jydate_form_html=response.xpath('/html/body/div/table/tbody/tr/td/text()')
        # 用来存放所有的item字段
        i=1

        o=0
        name_list=[]
        for pz in name_form_heml:
            print(pz)
            #数据整理
            a=pz.extract()
            a = ("".join(a))
            print(a)
            a = a.replace("\n", '')
            #a=a.replace(" ","")
            a=a.replace("\xa0\xa0\xa0\xa0日期：","")
            a=a.replace("合约：", "")
            a=a.replace("品种：", "")
            # b=日期
            b=a[-10:]
            name=a.replace(b,"")
            #格式整理完毕

            #单个期货名称数据添加到列表name_list中
            name_list.append(name)
            print(name_list)
            i=i+1
            name_save=(name_list[o:o+1])
            print(name_save)
            # print(jydate_list)
            o = o + 1
            # l=0
            # for jydate in jydate_list:
            #     l=l+1
            #     print(jydate)

            yield {
                '日期':b,
                '品种': name_save
            }
        print(name_save)
        print(name_list)