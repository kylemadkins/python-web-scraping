from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_crawler.items import Article


class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]

    rules = [
        Rule(LinkExtractor(allow=r"wiki/((?!:).)*$"), callback="parse", follow=True)
    ]

    custom_settings = {
        "CLOSESPIDER_PAGECOUNT": 10,
        "FEEDS": {"articles.json": {"format": "json", "overwrite": True}},
        "ITEM_PIPELINES": {
            "article_crawler.pipelines.ValidateArticlePipeline": 100,
            "article_crawler.pipelines.CleanDatePipeline": 200,
        },
    }

    def parse(self, response):
        article = Article(
            title=response.xpath("//h1/span/text()").get()
            or response.xpath("//h1/i/text()").get(),
            url=response.url,
            last_updated=response.xpath("//li[@id='footer-info-lastmod']/text()").get(),
        )
        return article
