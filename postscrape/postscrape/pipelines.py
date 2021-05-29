# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector
import psycopg2

class UniPipeline(object):
    def __init__(self):
        self.create_connection()
        # self.create_table()

    # Heroku PostgreSQL database
    # def create_connection(self):
    #     self.conn = psycopg2.connect(
    #         host = 'ec2-54-211-176-156.compute-1.amazonaws.com',
    #         user = 'uhynaqdzydbeuw',
    #         password = '24f34eb6209129ded75b96c646eba043a6f203e4b656ff80d9cd3261ffbbf52f',
    #         database = 'db3oo4gqcpcdmj'
    #     )
    #     self.curr = self.conn.cursor()

    # AWS MySQL database
    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host = 'unihub-db3.cw0hs6efxtbu.ap-southeast-1.rds.amazonaws.com',
    #         user = 'admin',
    #         passwd = 'pass1234',
    #         database = 'unihub'
    #     )
    #     self.curr = self.conn.cursor()

    # Local MySQL database
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'pass1234',
            database = 'test_db'
        )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        if spider.name == 'gtu':
            self.store_db_gtu(item)
            return item
        elif spider.name == 'gtu2':
            self.store_db_gtu2(item)
            return item
        elif spider.name == 'bachKhoa':
            self.store_db_bachKhoa(item)
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
        self.curr.execute("""UPDATE schools
            SET location = %s , score_ielts = %s , score_toefl = %s , score_sat = %s
            WHERE name = %s;""", (
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

    def store_db_bachKhoa(self, item):
        self.curr.execute("""insert into schools (name, country, email, phone, imageURL, logoURL, 
        tuition, tuitionUSD, website, location, score_ielts, score_toefl, score_sat)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item['name'],
            item['country'],
            item['email'],
            item['phone'],
            item['imageURL'],
            item['logoURL'],
            item['tuition'],
            item['tuitionUSD'],
            item['website'],
            item['location'],
            item['score_ielts'],
            item['score_toefl'],
            item['score_sat']
        ))
        self.conn.commit()