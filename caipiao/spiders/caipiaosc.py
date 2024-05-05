# -*- coding: utf-8 -*-
'''
定义爬取的开始url，以及结束的url
'''
import scrapy
from caipiao.items import CaipiaoItem
import requests
from scrapy.http import HtmlResponse

class CaipiaoscSpider(scrapy.Spider):

    name = 'caipiaosc'
    url = 'https://kaijiang.500.com/shtml/ssq/24049.shtml'
    allowed_domains = [url, 'http:']
    start_urls = [url]

    def parse(self, response):
        url = 'https://kaijiang.500.com/shtml/ssq/24049.shtml'
        headers = {
            'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        }
        res = requests.get(url, headers=headers).content
        response = HtmlResponse(url=url, body=res)
        all_urls = response.css('.iSelectBox .iSelectList a::attr(href)').extract()
        for url_new in all_urls:
            res = requests.get(url_new, headers=headers).content
            response = HtmlResponse(url=url_new, body=res)
            item = CaipiaoItem()
            item['red1'] = response.css('.ball_box01 ul .ball_red::text').extract()[0]
            item['red2'] = response.css('.ball_box01 ul .ball_red::text').extract()[1]
            item['red3'] = response.css('.ball_box01 ul .ball_red::text').extract()[2]
            item['red4'] = response.css('.ball_box01 ul .ball_red::text').extract()[3]
            item['red5'] = response.css('.ball_box01 ul .ball_red::text').extract()[4]
            item['red6'] = response.css('.ball_box01 ul .ball_red::text').extract()[5]
            item['blue'] = response.css('.ball_box01 ul .ball_blue::text').extract()[0]
            item['date'] = response.css('.cfont2 strong::text').extract()[0]

            yield item


