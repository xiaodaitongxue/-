# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class CaipiaoPipeline(object):

    def __init__(self):
        # 连接Mysql数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='Huawei123', database='caipiao', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        # SQL 插入语句
        red1 = item['red1']
        red2 = item['red2']
        red3 = item['red3']
        red4 = item['red4']
        red5 = item['red5']
        red6 = item['red6']
        blue = item['blue']
        date = item['date']
        sql = "insert into shuangseqiu(riqi, red1, red2, red3, red4, red5, red6, blue) values('{}', '{}','{}','{}','{}','{}','{}','{}')".format(date, red1, red2, red3, red4, red5, red6, blue)
        self.cursor.execute(sql)
        self.connect.commit()

        return item

    def close_spide(self, spider):
        self.cursor.close()
        self.connect.close()




if __name__ == '__main__':
    test = CaipiaoPipeline()