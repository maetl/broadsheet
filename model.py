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
from google.appengine.ext import db

class Link(db.Model):
    title           = db.StringProperty()
    url             = db.StringProperty()
    summary         = db.TextProperty()
    published_at    = db.DateTimeProperty()
    weight          = db.IntegerProperty()
    