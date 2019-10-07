# -*- coding: utf-8 -*-
import scrapy
'''
pip install scrapy

o que quer? os "href" dentro de: class = "search-body__item"

comando para rodar: scrapy crawl aula_aberta 
(fazer qunado estiver dentro de: 
C:\Users\ADS\PycharmProjects\scrapy\aula_aberta\aula_aberta\spiders)
'''

class AulaAbertaSpider(scrapy.Spider):
    name = 'aula_aberta'
   # allowed_domains = ['startupbase.com.br/home/startups?q=']
    start_urls = ['startupbase.com.br/home/startups?q=&states=all&cities='
                  'all&groups=Internet~Educa%C3%A7%C3%A3o~Varejo%20%2F%20At'
                  'acado~Finan%C3%A7as~Agroneg%C3%B3cio~E-commerce~Comunica%C3'
                  '%A7%C3%A3o%20e%20M%C3%ADdia~Sa%C3%BAde%20e%20Bem-estar&target'
                  's=all&phases=all&models=all&badges=all']

    def parse(self, response):
        lista = response.xpath('//*[@class="search-body__item"]')
        # self.log(lista)
        for itemlista in lista:
            url = itemlista.xpath('./a/@href').extract_first()
            # self.log(url)
            yield scrapy.Request(url=url, callback=self.parsedetalhe())
    def parsedetalhe(self,response):
        pass