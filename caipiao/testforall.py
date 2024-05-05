# import MySQLdb
# import datetime
#
# '''连接数据库'''
# db = MySQLdb.connect(host = 'localhost',#本地数据库
#
#                              user = 'root', #用户名
#
#                              passwd = 'XXXXX', #数据库密码
#
#                              db = 'test', #数据库名
#
#                              charset = 'utf8')  #数据库编码
#
#
# '''待插入的数据'''
#  Url = "http://www.baidu.com"
#  Time = datetime.datetime.now() #系统当前时刻
#
# '''插入数据'''
#
# '''关闭连接'''
# db.close()
#
#
#
# sql = "insert into test2(url, time) values('%s','%s')" % (Url，Time)
# cursor = db.cursor()
# try:
#      cursor.execute(sql)
#      db.commit() #提交到数据库执行，一定要记提交哦
# except Exception,e:
#     db.rollback() #发生错误时回滚
#     print e
# cursor.close()
#
# sql = "insert into test2(url, time) values(%s,%s)" #注意此处与前一种形式的不同
# par = (Url，Time)
# cursor = db.cursor()
# try:
#      cursor.execute(sql，par)
#      db.commit() #提交到数据库执行，一定要记提交哦
# except Exception,e:
#     db.rollback() #发生错误时回滚
#     print e
# cursor.close()
#
# par = (Url，None)


#encoding: utf-8

# HOSTNAME = "127.0.0.1"
# PORT = "3306"
# DATABASE = "shop"
# USERNAME = "root"
# PASSWORD = "Huawei123"
#
# db_url = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
#     format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)
#
# from sqlalchemy import create_engine
#
# engine = create_engine(db_url)
# print(engine)
# conn = engine.connect()
# sql = "insert into students(name, city, addr, pin) values('%s','%s','%s','%s')" % ('daixin', 'beijing', 'changping', '11')
# result = conn.execute(sql)
# print(result.fetchone())



import pymysql
# 打开数据库连接
db = pymysql.connect(host='localhost', user='root', password='Huawei123', database='shop', port=3306)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql = "insert into students(id, name, city, addr, pin) values('%s', '%s','%s','%s','%s')" % (10, 'daixin', 'beijing', 'changping', '11')
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 执行sql语句
   db.commit()
   print("insert ok")
except:
   # 发生错误时回滚
   db.rollback()
# 关闭数据库连接
db.close()







# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


# engine = create_engine('mysql+pymysql://root:Huawei123@localhost:3306/blog?charset=utf8')
# Base = declarative_base()


# class User(Base):
#
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String(64), nullable=False, index=True)
#     password = Column(String(64), nullable=False)
#     email = Column(String(64), nullable=False, index=True)
#
#
#     def __repr__(self):
#         return '%s(%r)' % (self.__class__.__name__, self.username)

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
