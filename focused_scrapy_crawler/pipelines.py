# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
import time

class RemoveDupLink(object):
    def __init__(self):
        self.links_seen = set()

    def process_item(self, item, spider):
        links = item.get('links', [])
        # Remove dup and already seen links
        for link in links:
            if link.get("found", False):
                continue
            if link.get('link') in self.links_seen:
                link['found'] = True
                link['last_updated'] = time.time()
            else:
                self.links_seen.add(link.get('link'))
        return item