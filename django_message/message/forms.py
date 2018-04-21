# -*- coding: utf-8 -*-

from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(required=True, min_length=2, max_length=10)
    email = forms.EmailField(required=True, min_length=5)
    address = forms.CharField(required=True, min_length=5)
    message = forms.CharField(required=True)



