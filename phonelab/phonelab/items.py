# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class PhonelabItemOthers(Item):
    companyName = Field()
    itemName = Field()
    screenPrice = Field()
    batteryPrice = Field()
    

class PhoneLabItemIPad(Item):
    companyName = Field()
    itemName = Field()
    modelNumber = Field()
    screenPrice = Field()