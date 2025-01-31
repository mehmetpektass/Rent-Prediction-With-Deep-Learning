import scrapy

class BlogSpider(scrapy.Spider):
    name = 'homespider'
    start_urls = ['https://www.sahibinden.com/kiralik/istanbul-sancaktepe']

    def parse(self, response):
        for href in response.css('.searchResultsRowClass a::attr(href)').getall():
            extracted_data = scrapy.Request("https://www.sahibinden.com/"+href,
                                            callback=self.parse_rent)
            yield extracted_data


        for next_page in response.css('a.prevNextBut'):
            yield response.follow(next_page, self.parse)
            
            
            
            
            
            
            
    def parse_rent(self, response):   
        description = response.css(".classifiedDetailTitle h1::text").extract()[0]
        
        return dict (
           description = description
        )
        
            
            
            
            
            
            
            
    # def parse_rent(self, response):
    #     description = response.css(".classifiedDetailTitle h1::text").get()
    #     price = response.css(".classified-price-wrapper span::text").get()
    #     location_parts = response.css(".classifiedInfo h2 a::text").getall()
    #     location = ", ".join(location_parts)
        
    #     features = {}
    #     for li in response.css(".classifiedInfoList li"):
    #         key = li.css("strong::text").get()
    #         value = li.css("span::text").get()
    #         if key and value:
    #             features[key.strip()] = value.strip()

    #     # Yield the extracted data
    #     yield {
    #         "description": description.strip() if description else None,
    #         "price": price.strip() if price else None,
    #         "location": location.strip() if location else None,
    #         "features": features,  # Dictionary of key-value pairs
    #         "url": response.url,  # Include the URL of the listing
    #     }