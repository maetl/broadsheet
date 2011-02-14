#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from model import *

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')
        
class TaskHandler(webapp.RequestHandler):
    def get(self):
        feed = WaxyFeed().fetch()
        items = feed.getElementsByTagName('item')
        for item in items:
            self.response.out.write(item.getElementsByTagName('title')[0].childNodes[0].data + "<br>")
        
        feed = FourShortLinksFeed().fetch()
        for item in feed['value']['items']:
            self.response.out.write(item['title'] + "<br>")
        
        


def main():
    application = webapp.WSGIApplication([('/', MainHandler), ('/tasks/scan', TaskHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()