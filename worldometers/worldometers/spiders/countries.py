# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()
        # countries = response.xpath('//td/a/text()').getall()
        countries = response.xpath('//td/a')
        for country in countries:
            name = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()

            # yield{
            #     'country_name' : name,
            #     'country_link' : country_link
            # }
            # absolute_url = f"https://www.worldometers.info{country_link}"
            # absolute_url = response.urljoin(country_link)
            yield response.follow(url=country_link, callback = self.parse_country, meta={'country_name' : name})


    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')

        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/strong/text()').get()

            yield {
                'country_name' : name,
                'year' : year,
                'population' : population
            }
