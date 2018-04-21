# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Messages(models.Model):
    """
      留言信息数据表。
    """
    name = models.CharField(max_length=15, verbose_name=u"姓名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")
    message_time = models.DateTimeField(auto_now=True, verbose_name=u"留言时间")

    class Meta():
        db_table = "messages"
        managed = True
        ordering = ["id"]
        verbose_name = "留言板数据表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.message

