# -*- coding: utf-8 -*-
import re

import scrapy

from caipiao.items import CaipiaoItem


# print(len(last))
# print(last[0:20])

class CaipiaoscSpider(scrapy.Spider):
    name = 'caipiaosc'
    allowed_domains = ['http://kaijiang.500.com','http:']
    start_urls = ['http://kaijiang.500.com/shtml/ssq/20047.shtml'] #http://kaijiang.500.com/shtml/ssq/20046.shtml

    # @property
    def parse(self, response):
        item=CaipiaoItem()
        item['red1']=response.css('.ball_box01 ul .ball_red::text').extract()[0]
        item['red2']=response.css('.ball_box01 ul .ball_red::text').extract()[1]
        item['red3']=response.css('.ball_box01 ul .ball_red::text').extract()[2]
        item['red4']=response.css('.ball_box01 ul .ball_red::text').extract()[3]
        item['red5']=response.css('.ball_box01 ul .ball_red::text').extract()[4]
        item['red6']=response.css('.ball_box01 ul .ball_red::text').extract()[5]
        item['blue']=response.css('.ball_box01 ul .ball_blue::text').extract()[0]
        item['date']=response.css('.cfont2::text').extract()[0]
        yield item

        # pass
        # last = response.css('tbody tr td a::attr(href)').extract_first()

        # pattern=re.compile('<td colspan="2">\n.*a href="(.*?)" target', re.DOTALL)

        # pattern=re.compile('<a href=(.*?)</a>', re.DOTALL) #('<td colspan="2">\n.*<a href="(.*?)" target="_blank" id="link3061">双色球2020046开奖结果</a>" ', re.DOTALL)
        # last=re.findall(pattern,response.text)

        # print(last)

        # last = response.css('.iSelectBox .iSelectList a::attr(href)').extract()  #提取所有url形成列表

        # response.urljoin(last)

        #last = response.css('.wrap .kj_main01 .kj_main01_right .kjxq_box02 div table tbody tr').extract_first()
        # last = response.css('tr td a').extract_first()
        # last=response.selector.xpath('//*[@id="link3061"]').text()
        # print(last)
        # url=last
        # yield scrapy.Request(url=url, callback=self.parse)

