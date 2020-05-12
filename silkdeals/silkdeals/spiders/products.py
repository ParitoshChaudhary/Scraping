# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest


class ProductsSpider(scrapy.Spider):
    name = 'products'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )


    def parse(self, response):
        driver = response.request.meta['driver']
        search_input = driver.find_element_by_xpth("//input[@id=search_form_input_homepage]")
        search_input.send_keys("Hello World")

        drive.save_screenshot('input.png')
