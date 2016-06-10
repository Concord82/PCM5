# -*- coding: utf-8 -*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
#from django_mptt_admin.admin import DjangoMpttAdmin
from django.utils.html import format_html
# Register your models here.

from .models import State, Departament, User_Options
from django.utils.translation import ugettext_lazy as _



class AdminState(admin.ModelAdmin):
    list_display = [
        'User', 'LogOn', 'LogOff','Host', 'ipAddr', 'Trust',

    ]
    list_filter = ['LogOn', 'LogOff','Trust',]
    search_fields = ['User', 'Host', 'ipAddr',]

admin.site.register(State, AdminState)

class DepartamentAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20
    mptt_indent_field = "name"
    list_display=('tree_actions', 'indented_title')
    list_display_links=('indented_title',)




admin.site.register(Departament, DepartamentAdmin)

class User_OptionsAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'skip_blank', 'mail_send', 'extendet_mail',
    ]


admin.site.register(User_Options, User_OptionsAdmin)

