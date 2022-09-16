# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProcessItem(scrapy.Item):
    # define the fields for your item here like:
    identificacao = scrapy.Field()
    parte = scrapy.Field()
    numero = scrapy.Field()
    data_autuacao = scrapy.Field()
    meio = scrapy.Field()
    publicidade = scrapy.Field()
    tramite = scrapy.Field()