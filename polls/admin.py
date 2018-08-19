# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Poll, Choice

# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice)
