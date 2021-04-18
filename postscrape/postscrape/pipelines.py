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
            host = 'localhost',
            user = 'root',
            passwd = 'pass1234',
            database = 'scrapeduni'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS info_tb""")
        self.curr.execute("""create table info_tb(
            name text,
            email text,
            phone text,
            location text,
            admissionWeb text
            )
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    # def store_db(self, item):
    #     self.curr.execute("""insert into info_tb (name, email, phone, location, admissionWeb)
    #         values (%s,%s,%s,%s,%s)""", (
    #         item['name'],
    #         item['email'],
    #         item['phone'],
    #         item['location'],
    #         item['admissionWeb']
    #     ))
    #     self.conn.commit()

    def store_db(self, item):
        self.curr.execute("""UPDATE info_tb I
            SET I.tuition = %s , I.website = %s
            WHERE I.name = %s;""", (
            item['tuition'],
            item['website'],
            item['name2']
        ))
        self.conn.commit()
