# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class RemoveDupLink(object):
    """
    Avoid duplicate crawling
    """
    def __init__(self):
        self.links_seen = set()

    def process_item(self, item, spider):
        # Remove dup and already seen links
        if item.get('url') in self.links_seen:
            raise DropItem("Duplicate item in %s" % item.get('url'))
        else:
            self.links_seen.add(item.get('url'))
            return item


class UrlOutputPipeline(object):
    """
    Output data to file system
    """
    def process_item(self, item, spider):
        line = "%s\t%f\n" %(item.get('url'), item.get('score'))
        with open('output/output-all-%s.txt'%spider.name, 'a+') as fp:
            fp.writelines([line])
        if item.get('score', 0) > 0:
            with open('output/output-positive-score-%s.txt' % spider.name, 'a+') as fp:
                fp.writelines([line])
