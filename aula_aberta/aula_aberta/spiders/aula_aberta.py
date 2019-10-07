# -*- coding: utf-8 -*-
import scrapy
'''
pip install scrapy

o que quer? os "href" dentro de: class = "search-body__item"

comando para rodar: scrapy crawl aula_aberta 
(fazer qunado estiver dentro de: 
C:\Users\ADS\PycharmProjects\scrapy\aula_aberta\aula_aberta\spiders)

nome da startup ->    //h2[@class='publ-header__name sb-size-4']

localização da startup -> //*[@class="publ-header__location is-uppercase"]

descração ->  //*[@class= "publ-header__description sb-size-8 has-text-weight-light"]

mercado -> //div[1]/div[2]/section/article[1]/p

publico alvo -> //div[1]/div[2]/section/article[2]/p

modelo de receita -> //div[1]/div[2]/section/article[3]/p

momento -> //div[1]/div[2]/section/article[4]/p

sobre -> //app-card/div/p[2]
'''

class AulaAbertaSpider(scrapy.Spider):
    name = 'aula_aberta'
   # allowed_domains = ['startupbase.com.br/home/startups?q=']
    start_urls = ['https://startupbase.com.br/home/startups?q=&states='
                  'all&cities=all&groups=Internet~Educa%C3%A7%C3%A3o~'
                  'Varejo%20%2F%20Atacado~Finan%C3%A7as~Agroneg%C3%B3cio~'
                  'E-commerce~Comunica%C3%A7%C3%A3o%20e%20M%C3%ADdia~Sa%C3%BA'
                  'de%20e%20Bem-estar&targets=all&phases=all&models=all&badges=all']

    def parse(self, response):
        lista = response.xpath('//*[@class="search-body__item"]')
        # self.log(lista)
        for itemlista in lista:
            url = itemlista.xpath('./a/@href').extract_first()
            # self.log(url)
            yield scrapy.Request(url=url, callback=self.parsedetalhe())
    def parsedetalhe(self,response):
        pass