# -*- coding: utf-8 -*-
"""
MySQL数据库操作
Created on 2016年12月9日
@author: evan wang
"""

# windows环境下安装MySQL-python-1.2.3.win-amd64-py2.7.exe
import MySQLdb


# mysql连接工具类
class MySqlUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="123456", db="test")
        # print "db connected-------"
        return db

    @staticmethod
    def close_connection(db):
        if db is not None:
            db.close()
            # print "db closed----------"


# 显示数据库版本
def show_database_version():
    db = MySqlUtil.get_connection()
    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    print "Database version : %s " % data
    cursor.execute("show databases")
    data = cursor.fetchall()
    for i in data:
        print i[0]
    MySqlUtil.close_connection(db)


# 创建表
def create_table():
    try:
        db = MySqlUtil.get_connection()
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
              ID INTEGER AUTO_INCREMENT PRIMARY KEY,
              FIRST_NAME  CHAR(20) NOT NULL,
              LAST_NAME  CHAR(20),
              AGE INT,
              SEX CHAR(1),
              INCOME FLOAT )"""
        cursor.execute(sql)
    except Exception as e:
        print e.message
    finally:
        MySqlUtil.close_connection(db)


# 插入表
def insert():
    db = None
    try:
        db = MySqlUtil.get_connection()
        cursor = db.cursor()
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
              LAST_NAME, AGE, SEX, INCOME)
              VALUES """
        i = 1
        while i <= 100:
            sql = sql + "('Mac"+str(i)+"', 'Moran"+str(i)+"', 20, 'M', 2000)"
            if i != 100:
                sql += ','
            i = i+1
        print(sql)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        if db is not None:
            db.rollback()
        print "insert error", e.message
    finally:
        MySqlUtil.close_connection(db)


# 查询单条
def query_one():
    db = None
    try:
        db = MySqlUtil.get_connection()
        cursor = db.cursor()
        sql = "SELECT * FROM EMPLOYEE WHERE ID = '%d' " % 1
        cursor.execute(sql)
        result = cursor.fetchone()
        for column in result:
            print column
    except Exception as e:
        print "query one error", e.message
    finally:
        MySqlUtil.close_connection(db)


# 查询所有
def query_all():
    db = None
    try:
        db = MySqlUtil.get_connection()
        cursor = db.cursor()
        sql = "SELECT * FROM EMPLOYEE WHERE ID = '%d' " % 1
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            fname = row[1]
            lname = row[2]
            age = row[3]
            sex = row[4]
            income = row[5]
            print "id=%d,fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                  (id, fname, lname, age, sex, income)
    except Exception as e:
        print "query all error", e.message
    finally:
        MySqlUtil.close_connection(db)


# 更新
def update():
    db = None
    try:
        db = MySqlUtil.get_connection()
        cursor = db.cursor()
        sql = """ UPDATE EMPLOYEE SET SEX = 'F' WHERE ID = 1"""
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        if db is not None:
            db.rollback()
        print "update error", e.message
    finally:
        MySqlUtil.close_connection(db)


# 删除
def delete():
    db = None
    try:
        db = MySqlUtil.get_connection()
        cursor = db.cursor()
        sql = """ DELETE FROM EMPLOYEE WHERE ID = 1"""
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        if db is not None:
            db.rollback()
        print "update error", e.message
    finally:
        MySqlUtil.close_connection(db)


# 测试方法
if __name__ == "__main__":
    show_database_version()
    # create_table()
    insert()
    # query_one()
    # query_all()
    # update()
    # delete()
