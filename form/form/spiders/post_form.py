import scrapy
from scrapy.http import FormRequest


class PostFormSpider(scrapy.Spider):
    name = "post_form"
    allowed_domains = ["pythonscraping.com"]

    def start_requests(self):
        entries = [
            {"name": "Alice", "quest": "to seek the grail"},
            {"name": "Bob", "quest": "to learn Python"},
            {"name": "Charles", "quest": "to scrape the web"},
        ]
        return [
            FormRequest(
                "http://pythonscraping.com/linkedin/formAction2.php",
                formdata={"name": entry["name"], "quest": entry["quest"]},
                callback=self.parse,
            )
            for entry in entries
        ]

    def parse(self, response):
        return {"text": response.xpath("//div[@class='wrapper']/text()").get().strip()}
