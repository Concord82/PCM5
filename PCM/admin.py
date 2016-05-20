from django.contrib import admin

# Register your models here.

from .models import State




class AdminState(admin.ModelAdmin):
    list_display = [
        'User', 'LogOn', 'LogOff','Host', 'ipAddr', 'Trust',

    ]
    list_filter = ['LogOn', 'LogOff','Trust',]
    search_fields = ['User', 'Host', 'ipAddr',]

admin.site.register(State, AdminState)