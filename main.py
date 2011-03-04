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

class MainHandler(webapp.RequestHandler):
    def get(self):
        values = {
            'links': Link.all()
        }
        path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
        self.response.out.write(template.render(path, values))
        
class TaskHandler(webapp.RequestHandler):
    def get(self):
        aggregator = Aggregator()
        aggregator.scan_sources()

        
        
def main():
    application = webapp.WSGIApplication([('/', MainHandler), ('/tasks/scan', TaskHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
