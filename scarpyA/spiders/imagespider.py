# -*- coding: utf-8 -*-
import scrapy
from scarpyA.items import ImageItem

class ImagespiderSpider(scrapy.Spider):
    name = 'imagespider'
    allowed_domains = ['https://tianqi.moji.com/liveview/']
    start_urls = ['https://tianqi.moji.com/liveview/china/shaanxi/qujiang-ocean-world']

    def parse(self, response):
        item = ImageItem()
        item['image_urls'] = response.xpath('//img[@data-original]/@data-original').extract()
        return item
        pass
