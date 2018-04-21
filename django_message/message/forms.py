# -*- coding: utf-8 -*-

from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(required=True, min_length=2, max_length=10)
    email = forms.EmailField(required=True, min_length=5, max_length=50)
    address = forms.CharField(required=False, min_length=5, max_length=50)
    message = forms.CharField(required=True, max_length=200)



