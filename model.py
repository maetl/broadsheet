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
from google.appengine.ext import db

class Link(db.Model):
    title           = db.StringProperty()
    href            = db.LinkProperty()
    summary         = db.TextProperty()
    updated         = db.DateTimeProperty()
    weight          = db.IntegerProperty()
    tweets          = db.IntegerProperty()
    mentions        = db.IntegerProperty()
    source          = db.StringProperty()
    source_href     = db.LinkProperty()
    
    def col(self):
        if self.weight < 30:
            return 'col-1'
        else:
            return 'col-2'
    
    @classmethod
    def headlines(self):
        return self.all().order('-tweets').fetch(32)