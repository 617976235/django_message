# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, resolve_url
from django.views import View
from .models import Messages
from .forms import MessageForm


class MessageShow(View):
    """
      留言板信息展示和提交
    """
    def get(self, request):
        messages = Messages.objects.all().order_by("-id")
        return render(request, "message.html", {"messages": messages})

    def post(self, request):
        messages = Messages.objects.all().order_by("-id")

        get_name = request.POST.get("name")
        get_email = request.POST.get("email")
        get_address = request.POST.get("address")
        get_message = request.POST.get("message")

        form = MessageForm(request.POST)
        if form.is_valid():
            Messages.objects.create(**form.clean())
            return redirect(resolve_url("messages:message"))
        else:
            form_errors = form.errors
            return render(request, "message.html", locals())
