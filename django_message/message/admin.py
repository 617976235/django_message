# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from message.models import Messages

# Register your models here.


@admin.register(Messages)
class MessagesA(admin.ModelAdmin):
    list_display = ["name", "email", "address", "message", "message_time"]
    search_fields = ["name", "email", "message"]
    list_filter = ["name"]
