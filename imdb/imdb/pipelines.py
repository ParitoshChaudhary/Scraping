# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongoDbPipeline(object):
    collection_name = "best_movies"

    def open_spider(self, spider):
        logging.warning("SPIIDER OPENED FROM PIPELINE")
        self.client = pymongo.MongoClient("mongodb+srv://paritosh:test_imdb@cluster0-t43zk.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["imdb"]

    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED FROM PIPELINE")
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
