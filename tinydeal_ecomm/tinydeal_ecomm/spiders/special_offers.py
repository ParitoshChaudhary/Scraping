# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):
        products = response.xpath("//ul[@class='productlisting-ul']/div/li")
        for product in products:
            title = product.xpath(".//a[@class='p_box_title']/text()").get()
            url = product.xpath(".//a[@class='p_box_title']/@href").get()
            absolute_url = response.urljoin(url)
            discounted_price = product.xpath(".//div[@class='p_box_price']/span[1]/text()").get()
            original_price = product.xpath(".//div[@class='p_box_price']/span[2]/text()").get()
            # print(response.request.headers['User-Agent'])

            yield{
                'title' : title,
                'url' : absolute_url,
                'discounted_price' : discounted_price,
                'original_price' : original_price,
            }

        next_page = response.xpath("//a[@class='nextPage']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
