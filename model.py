from google.appengine.ext import db
from google.appengine.api import urlfetch
from xml.dom import minidom
from django.utils import simplejson as json

#dom = minidom.parseString('<eg>example text</eg>')

class Link(db.Model):
    title = db.StringProperty()
    url = db.StringProperty()
    summary = db.StringProperty()
    published_at = db.DateTimeProperty()

class WaxyFeed():
    
    def fetch(self):
        url = "http://waxy.org/links/index.xml"
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            return minidom.parseString(result.content)
            
class FourShortLinksFeed():
    
    def fetch(self):
        url = "http://pipes.yahoo.com/pipes/pipe.run?_id=b5896405bdb116feac4ed791f41498ee&_render=json"
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            return json.loads(result.content)