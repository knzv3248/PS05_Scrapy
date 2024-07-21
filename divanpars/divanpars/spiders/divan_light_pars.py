import scrapy


class DivanLightParsSpider(scrapy.Spider):
    name = "divan_light_pars"
    allowed_domains = ["https://www.divan.ru/chelyabinsk/"]
    start_urls = ["https://www.divan.ru/chelyabinsk/category/svet"]

    def parse(self, response):
        lightings = response.css('div.WdR1o')
        for lighting in lightings:
            yield{
                'name' : lighting.css('div.lsooF span::text').get(),
                'price' : lighting.css('div.pY3d2 span::text').get(),
                'url' : lighting.css('a').attrib['href']
            }
