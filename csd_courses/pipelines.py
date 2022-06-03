# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class CsdCoursesPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('courses.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            ects REAL,
            type TEXT,
            content TEXT
        )""")

    def process_item(self, item, spider):
        self.cursor.execute("""INSERT OR IGNORE INTO courses(title, ects, type, content) VALUES (?,?,?,?)""",
            (item['title'], item['ects'], item['type'], item['content'])
        )
        self.conn.commit()
        return item
