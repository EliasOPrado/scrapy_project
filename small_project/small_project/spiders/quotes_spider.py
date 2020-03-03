import scrapy

class QuotesSpider(scrapy.Spider):
    #will evoque the scrape
    name = "quotes"

    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # will get the page number
        page = response.url.split("/")[-2]
        #will parse the page number into a new html file
        filenames = "quotes-%s.html" % page
        with open(filenames, "wb") as f:
            f.write(response.body)
        self.log("saved file %s" % filenames)