# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem


class JsonSerializer(object):

    def __init__(self):
        # TODO - get information from settings
        self.filename = 'item.json'
        self.mode = 'w+'

    def open_spider(self, spider):
        self.file = open(self.filename, self.mode)

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        items = []
        items.append(dict(item))

        line = json.dumps(items, indent=2)
        self.file.write(line)
        return item


class RemoveDupLink(object):
    def __init__(self):
        self.links_seen = set()

    def process_item(self, item, spider):
        if item['link'] in self.links_seen:
            raise DropItem("Duplicate link found: %s" % item)
        else:
            self.links_seen.add(item['link'])
            return item