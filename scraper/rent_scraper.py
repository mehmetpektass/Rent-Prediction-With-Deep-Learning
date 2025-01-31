import scrapy

class BlogSpider(scrapy.Spider):
    name = 'homespider'
    start_urls = ['https://www.sahibinden.com/kiralik/istanbul']

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.prevNextBut'):
            yield response.follow(next_page, self.parse)