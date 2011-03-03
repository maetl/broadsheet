#!/usr/bin/env python
# == Part of More Short Links ==
# 
# Copyright Mark Rickerby <http://maetl.net>, 2011
#
# # Licensed under the Apache License, Version 2.0 (the "License");
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
from google.appengine.ext import db
from google.appengine.api import urlfetch
from xml.dom import minidom
from django.utils import simplejson as json
from model import *
    
class RSS2Feed():
    
    def fetch(self, url):
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            return minidom.parseString(result.content)
            
    def collect(self, url):
        feed = self.fetch(url)
        items = []
        for item in feed.getElementsByTagName('item'):
            obj = {}
            obj['title'] = item.getElementsByTagName('title')[0].childNodes[0].data
            obj['url']  = item.getElementsByTagName('link')[0].childNodes[0].data
            obj['summary'] = item.getElementsByTagName('description')[0].childNodes[0].data
            items.append(obj)
        return items

class JSONFeed():
    
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
            items.append(obj)
        return items


class Aggregator():
    "Aggregates links from feed sources and updates headline weightings for existing links."
    
    parsers = {
        'RSS':  'RSS2Feed',
        'JSON': 'JSONFeed'
    }
    
    def get_sources(self, filename='sources.yaml'):
        return yaml.load(open(filename, 'r').read())
        
    def scan_sources(self):
        sources = self.get_sources()
        for source in sources['sources']:
            if source['format'] == 'JSON':
                parser = JSONFeed()
            else:
                parser = RSS2Feed()
            self.update_source(parser.collect(source['url']))
    
    def update_source(self, items):
        for item in items:
            link = db.GqlQuery("SELECT * FROM Link WHERE url = :1", item['url']).get()
            if not link:
                link = Link()
                link.title = item['title']
                link.url = item['url']
                link.summary = item['summary']
                link.put()
            
