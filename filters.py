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
from google.appengine.ext.webapp import template
from django.utils import timesince

def since(value):
    """
    Tidies up the default timesince filter to make it more readable.
    Changes:
      - '2 hours, 17 minutes' to '2 hours ago' 
      - '1 day, 7 hours' to '1 day ago'
    """
    value = timesince.timesince(value)
    return value.split(',')[0] + ' ago'

register = template.create_template_register()
register.filter(since)