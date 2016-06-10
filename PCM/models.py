# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from extuser.models import MyUser

# Create your models here.
class State(models.Model):
    LogOn = models.DateTimeField(
        verbose_name=_('Logon Current Session'),
        null=True
    )
    LogOff = models.DateTimeField(
        verbose_name=_('Logoff Current Session'),
        null=True
    )
    Host = models.CharField(
        verbose_name=_('Host name'),
        max_length=64,
    )
    ipAddr = models.GenericIPAddressField(
        verbose_name=_('IP Address'),
        max_length=16
    )
    User = models.CharField(
        verbose_name=_('User Name'),
        max_length=64
    )
    Trust = models.BooleanField(
        verbose_name=_('Trust to current value'),
        default=True
    )

    class Meta:
        verbose_name = 'Отчет о работе'
        verbose_name_plural = 'Отчет о работе'



class User_Options(models.Model):
    user = models.OneToOneField(MyUser)
    skip_blank = models.BooleanField(
        verbose_name='Пропускать пустое',
        default=True,
        blank=True
    )
    mail_send = models.BooleanField(
        verbose_name='Отправлять отчеты',
        default=False,
        blank=True
    )
    extendet_mail = models.BooleanField(
        verbose_name='Расширенное письмо',
        default=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Параметры пользователя'
        verbose_name_plural = 'Параметры пользователя'


class Departament(MPTTModel):
    name = models.CharField(max_length=64, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Подразделения'
        verbose_name_plural = 'Подразделения'

