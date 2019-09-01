# -*- coding: utf-8 -*-
# Copyright 2017 Kevin Nguyen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'KevinNguyen'

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect , render_to_response, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.core import serializers

import logging

logger = logging.getLogger(__name__)

import os
import string 
import json
import sys
import time

# set the default Django settings module for the Telegram interactive module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
# get settings instance for using enviroment variable
from django.conf import settings

# Create your views here.

def AlertInfo(request):
    return HttpResponse(settings.FAUST_BROKER_URL, content_type='application/json', status=200)