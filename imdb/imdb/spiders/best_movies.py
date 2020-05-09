# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    def start_requests(self):
        yield scrapy.Request(url="https://www.imdb.com/chart/top/?ref_=nv_mv_250", headers={
            'User-Agent' : self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//tbody[@class='lister-list']/tr/td[@class='titleColumn']/a",)), callback='parse_item', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title' : response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year' : response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration' : response.xpath("normalize-space((//time)[1]/text())").get(),
            'genre' : response.xpath("//div[@class='subtext']/a/text()").get(),
            'rating' : response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'movie_url' : response.url,
            'user_agent' : response.request.headers['User-Agent'],
        }
