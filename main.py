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
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from model import *
from aggregator import *

webapp.template.register_template_library('filters')

class IndexPage(webapp.RequestHandler):
    """
    Displays the HTML newspaper index
    """
    
    def get(self):
        values = {
            'links': Link.headlines()
        }
        path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
        self.response.out.write(template.render(path, values))
        
class ScanSourcesTask(webapp.RequestHandler):
    """
    Periodically scans sources and adds new links
    """
    
    def get(self):
        aggregator = Aggregator()
        aggregator.scan_sources()

class LinkRankingsTask(webapp.RequestHandler):
    """
    Refreshes link weightings based on Twitter popularity
    """
    
    def get(self):
        aggregator = Aggregator()
        aggregator.calculate_rankings()

class FlushLinksTask(webapp.RequestHandler):
    """
    Flushes expired links from the datastore
    """
    
    def get(self):
        aggregator = Aggregator()
        aggregator.flush_links()
        
def main():
    application = webapp.WSGIApplication([
                                    ('/', IndexPage),
                                    ('/task/scan', ScanSourcesTask),
                                    ('/task/rankings', LinkRankingsTask),
                                    ('/task/flush', FlushLinksTask)
                                ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
