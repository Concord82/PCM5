# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.admin import widgets
from datetimewidget.widgets import DateWidget, DateTimeWidget
from mptt.forms import TreeNodeChoiceField
from .models import Departament


class AuthForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(_("Sorry, that login was invalid. Please try again."))
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class date_select_form(forms.Form):
    dateinput = forms.DateField(widget=DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3), input_formats=['%d %m %Y'], localize=True, required=False)
    #departament = TreeNodeChoiceField(queryset=Departament.objects.all(),)



