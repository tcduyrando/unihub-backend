# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector

class UniPipeline(object):
    def __init__(self):
        self.create_connection()
        # self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'unihub-db3.cw0hs6efxtbu.ap-southeast-1.rds.amazonaws.com',
            user = 'admin',
            passwd = 'pass1234',
            database = 'unihub'
        )
        self.curr = self.conn.cursor()

    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         user = 'root',
    #         passwd = 'pass1234',
    #         database = 'test_db'
    #     )
    #     self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        if spider.name == 'gtu':
            self.store_db_gtu(item)
            return item
        elif spider.name == 'gtu2':
            self.store_db_gtu2(item)
            return item
        else:
            self.store_db_programs(item)
            return item

    def store_db_gtu(self, item):
        self.curr.execute("""insert into schools (name, country, email, phone, imageURL, logoURL, tuition, tuitionUSD, website)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item['name'],
            item['country'],
            item['email'],
            item['phone'],
            item['imageURL'],
            item['logoURL'],
            item['tuition'],
            item['tuitionUSD'],
            item['website']
        ))
        self.conn.commit()

    def store_db_gtu2(self, item):
        self.curr.execute("""UPDATE schools S
            SET S.location = %s , S.score_ielts = %s , S.score_toefl = %s , S.score_sat = %s
            WHERE S.name = %s;""", (
            item['location'],
            item['score_ielts'],
            item['score_toefl'],
            item['score_sat'],
            item['name2']
        ))
        self.conn.commit()

    def store_db_programs(self, item):
        self.curr.execute("""INSERT INTO programs(name, school_id)
            values(%s,%s)""", (
            item['program'],
            item['school_id']
        ))
        self.conn.commit()