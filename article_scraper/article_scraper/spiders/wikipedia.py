from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Article


class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]

    rules = [
        Rule(LinkExtractor(allow=r"wiki/((?!:).)*$"), callback="parse", follow=True)
    ]

    custom_settings = {"FEED_URI": "articles.json", "FEED_FORMAT": "json"}

    def parse(self, response):
        article = Article(
            title=response.xpath("//h1/span/text()").get()
            or response.xpath("//h1/i/text()").get(),
            url=response.url,
            last_updated_utc=response.xpath(
                "//li[@id='footer-info-lastmod']/text()"
            ).get(),
        )
        return article
