import csv

import requests
from scrapy.http import HtmlResponse

from caipiao.items import CaipiaoItem

url='http://kaijiang.500.com/shtml/ssq/20047.shtml'
headers= {
    'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
}

res=requests.get(url,headers=headers).content
response = HtmlResponse(url=url, body=res)
last = response.css('.iSelectBox .iSelectList a::attr(href)').extract()
# print(last)
# last=last[0:10]

infolist = []
for i in last:

    res = requests.get(i, headers=headers).content
    response = HtmlResponse(url=i, body=res)
    item={}
    r=response.css('.ball_box01 ul .ball_red::text').extract()
    print(len(r))
    if len(r)==6:
        item['red1'] = response.css('.ball_box01 ul .ball_red::text').extract()[0]
        item['red2'] = response.css('.ball_box01 ul .ball_red::text').extract()[1]
        item['red3'] = response.css('.ball_box01 ul .ball_red::text').extract()[2]
        item['red4'] = response.css('.ball_box01 ul .ball_red::text').extract()[3]
        item['red5'] = response.css('.ball_box01 ul .ball_red::text').extract()[4]
        item['red6'] = response.css('.ball_box01 ul .ball_red::text').extract()[5]
        item['blue'] = response.css('.ball_box01 ul .ball_blue::text').extract()[0]
        item['date'] = response.css('.cfont2 strong::text').extract()[0]
    else:
        pass
    print(item)
    infolist.append(item)
    # print(len(infolist))
    # print(infolist)
with open('caipiaofinal1.csv','a',newline='') as f:
    print(len(infolist))
    header = ['red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue','date']
    dictWriter=csv.DictWriter(f,fieldnames=header)
    dictWriter.writeheader()
    for i in infolist:
        dictWriter.writerow(i)
