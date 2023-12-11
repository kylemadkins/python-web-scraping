from datetime import datetime
from scrapy.spiders import XMLFeedSpider


def generate_start_urls():
    dates = [datetime(y, m, 1) for y in range(2013, 2024) for m in range(1, 13)]
    return [
        f"https://www.cnn.com/sitemaps/article-{d.strftime('%Y-%m')}.xml" for d in dates
    ]


class CnnSpider(XMLFeedSpider):
    name = "cnn"
    allowed_domains = ["cnn.com"]
    start_urls = generate_start_urls()
    itertag = "urlset"

    custom_settings = {
        "FEEDS": {"cnn.csv": {"format": "csv", "overwrite": True}},
    }

    def parse_node(self, response, node):
        return {"url": response.url, "count": response.text.count("<url>")}
