import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        return {
            "rfc_no": response.xpath("//span[@class='rfc-no']/text()").get(),
            "title": response.xpath("//span[@class='title']/text()").get(),
            "date": response.xpath("//span[@class='date']/text()").get(),
            "text": w3lib.html.remove_tags(
                response.xpath("//div[@class='text']").get()
            ),
            "author_name": response.xpath("//span[@class='author-name']/text()").get(),
            "author_company": response.xpath(
                "//span[@class='author-company']/text()"
            ).get(),
            "author_phone": response.xpath("//span[@class='phone']/text()").get(),
            "author_email": response.xpath("//span[@class='email']/text()").get(),
        }
