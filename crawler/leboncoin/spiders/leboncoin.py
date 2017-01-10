# -*- coding: utf-8 -*-
import scrapy


class House(scrapy.Item):
    id = scrapy.Field()
    price = scrapy.Field()
    surface = scrapy.Field()


class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin'
    start_urls = [
        'https://www.leboncoin.fr/ventes_immobilieres/offres/aquitaine/gironde/?th=1&f=p&parrot=0'
    ]

    def parse(self, response):
        house = House()

        for leBonCoinHouse in response.css('#listingAds section.list a.list_item'):
            house['id'] = leBonCoinHouse.css('.saveAd').xpath('./@data-savead-id').extract_first()
            house_description_url = leBonCoinHouse.xpath('./@href').extract_first()
            yield scrapy.Request(
                url=response.urljoin(house_description_url),
                callback=self.parse_house,
                meta={'house': house}
            )

        next_page = response.css('a#next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_house(self, response):
        house = response.meta['house']
        house['price'] = int(response.css('section.properties h2.item_price').xpath('./@content').extract_first())
        house['surface'] = int(response.css('section.properties h2').xpath('.//span[.="Surface"]/following-sibling::span/text()').extract_first().lower().replace("m", "").replace("", "").strip())
        yield house
