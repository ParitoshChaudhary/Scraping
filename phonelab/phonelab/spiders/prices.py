# -*- coding: utf-8 -*-
import scrapy
from phonelab.items import PhoneLabItemIPad, PhonelabItemOthers


class PricesSpider(scrapy.Spider):
    name = 'prices'
    allowed_domains = ['www.thephonelab.nl']
    start_urls = ['https://thephonelab.nl/prijzen/']


    def parse(self, response):
        # tables = response.xpath("(//table[@class='pricing-table'])[1]/tbody/tr")
        tables = response.xpath("//table[@class='pricing-table']/thead/tr/th[1]")
        count = 1
        for table in tables:
            table_name = table.xpath(".//text()").get()
            table_data = response.xpath(f"(//table[@class='pricing-table'])[{count}]/tbody/tr")
            count += 1
            print(type(count))
            
            for item in table_data:
                if count == 4:
                    items = PhoneLabItemIPad()
                    name = item.xpath(".//td[1]/text()").get()
                    model_number = item.xpath(".//td[2]/text()").get()
                    screen_price = item.xpath(".//td[3]/text()").get()
                    
                    items['companyName'] = table_name
                    items['itemName'] = name
                    items['modelNumber'] = model_number
                    items['screenPrice'] = screen_price
                    
                    yield items
                    
                else:
                    items = PhonelabItemOthers()
                    name = item.xpath(".//td[1]/text()").get()
                    screen_cost = item.xpath(".//td[2]/text()").get()
                    battery_price = item.xpath(".//td[3]/text()").get()
                    
                    items['companyName'] = table_name
                    items['itemName'] = name
                    items['screenPrice'] = screen_cost
                    items['batteryPrice'] = battery_price
                    
                    yield items