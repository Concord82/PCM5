from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
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
