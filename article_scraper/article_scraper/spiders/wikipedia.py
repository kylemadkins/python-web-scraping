from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import w3lib.html


class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]

    rules = [
        Rule(LinkExtractor(allow=r"wiki/((?!:).)*$"), callback="parse", follow=True)
    ]

    def parse(self, response):
        return {
            "title": response.xpath("//h1/span/text()").get()
            or response.xpath("//h1/i/text()").get(),
            "url": response.url,
            "last_edited": w3lib.html.remove_tags(
                response.xpath("//li[@id='footer-info-lastmod']").get()
            ),
        }
