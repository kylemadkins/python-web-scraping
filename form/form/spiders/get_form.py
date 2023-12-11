import scrapy


def generate_start_urls():
    entries = [
        {"name": "Alice", "quest": "to seek the grail"},
        {"name": "Bob", "quest": "to learn Python"},
        {"name": "Charles", "quest": "to scrape the web"},
    ]
    return [
        f"http://pythonscraping.com/linkedin/formAction.php?name={entry['name']}&quest={entry['quest']}&color=blue"
        for entry in entries
    ]


class GetFormSpider(scrapy.Spider):
    name = "get_form"
    allowed_domains = ["pythonscraping.com"]
    start_urls = generate_start_urls()

    def parse(self, response):
        return {"text": response.xpath("//div[@class='wrapper']/text()").get().strip()}
