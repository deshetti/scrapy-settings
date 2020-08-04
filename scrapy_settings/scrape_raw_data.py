import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

settings=get_project_settings()
settings.set("CUSTOM_SETTING", "Super Custom Setting")
print("Custom setting:", settings.get('CUSTOM_SETTING'))
print("Default bot name:", settings.get('BOT_NAME'))
settings.update({
    "BOT_NAME": "NEW_BOT_NAME"
})

print("After updating bot name:", settings.get('BOT_NAME'))


process = CrawlerProcess(settings)
process.crawl(QuotesSpider)
process.start() # the script will block here until the crawling is finished