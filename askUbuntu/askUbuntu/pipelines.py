# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from  DBmodel import db_connect, create_ubuntu_table, ubuntuDB
from scrapy.exceptions import DropItem

class AskubuntuPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_ubuntu_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        session = self.Session()
        db_item = ubuntuDB(**item)
        try:
            session.add(db_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
