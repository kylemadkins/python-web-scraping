# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from datetime import datetime


class ValidateArticlePipeline:
    def process_item(self, article, spider):
        if not article["last_updated"] or not article["url"] or not article["title"]:
            raise DropItem("Missing data")
        return article


class CleanDatePipeline:
    def process_item(self, article, spider):
        article["last_updated"] = (
            article["last_updated"].replace("This page was last edited on", "").strip()
        )
        article["last_updated"] = datetime.strptime(
            article["last_updated"], "%d %B %Y, at %H:%M"
        )
        return article
