#!/usr/bin/env python
# ========================================================================
# Broadsheet -- an automated personal newspaper
# 
# Copyright (c) 2011, Mark Rickerby <http://maetl.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import yaml
import feedparser
import datetime
import calendar
from google.appengine.ext import db
from google.appengine.api import urlfetch
from xml.dom import minidom
from model import *

class UniversalFeed():
    """
    Collects links using the Universal Feed Parser
    """
    
    def collect(self, url):
        feed = feedparser.parse(url)
        items = []
        for item in feed.entries:
            obj = {}
            obj['title'] = item.title
            obj['url'] = item.link
            obj['summary'] = item.summary
            obj['updated'] = datetime.datetime.utcfromtimestamp(calendar.timegm(item.updated_parsed))
            items.append(obj)
        return items

class JSONFeed():
    """
    Collects links from Yahoo Pipes JSON feed
    """
    
    def fetch(self, url):
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            return json.loads(result.content)
            
    def collect(self, url):
        feed = self.fetch(url)
        items = []
        for item in feed['value']['items']:
            obj = {}
            obj['title'] = item['title']
            obj['url']   = item['link']
            obj['summary'] = item['content']
            obj['updated'] = datetime.datetime.strptime(item['published'], '%Y-%d-%mT%H:%M:%SZ')
            items.append(obj)
        return items

class Aggregator():
    """
    Aggregates links from feed sources and updates headline weightings for existing links.
    """
    
    def get_sources(self, filename='sources.yaml'):
        return yaml.load(open(filename, 'r').read())
        
    def fetch_feed(self, url):
        feed = feedparser.parse(url)
        items = []
        for item in feed.entries:
            obj = {}
            obj['title'] = item.title
            obj['href'] = item.link
            obj['summary'] = item.summary
            obj['updated'] = datetime.datetime.utcfromtimestamp(calendar.timegm(item.updated_parsed))
            items.append(obj)
        return items
        
    def scan_sources(self):
        sources = self.get_sources()
        for source in sources['sources']:
            items = self.fetch_feed(source['feed'])
            for item in items:
                link = db.GqlQuery("SELECT * FROM Link WHERE href = :1", item['href']).get()
                if not link:
                    link = Link()
                    link.title = item['title']
                    link.href = item['href']
                    link.summary = item['summary']
                    link.updated = item['updated']
                    link.weight = source['influence']
                    link.source = source['name']
                    link.source_href = source['homepage']
                    link.put()
            
    def flush_links(self):
        links = Link.all()
        for link in links:
            link.delete()