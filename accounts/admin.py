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

from __future__ import absolute_import, division, print_function


from django.contrib import admin
from django import forms
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'active')
    search_fields = ['name']
    list_max_show_all = 1000
    list_per_page = 100


admin.site.register(Account, AccountAdmin)