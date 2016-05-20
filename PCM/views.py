# -*- coding: utf-8 -*-
import datetime
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from forms import AuthForm, date_select_form
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_auth_ldap.backend import LDAPBackend
from django.http import HttpResponseRedirect, HttpResponse, Http404

from .models import State
User = get_user_model()

# Create your views here.
def index(request):
    if request.user.is_authenticated():

        curent_date = datetime.date.today()
        State_list = State.objects.filter (LogOn__year=curent_date.year, LogOn__month=curent_date.month, LogOn__day=curent_date.day).order_by('id')

        other_var = {}

        other_var['Date'] = curent_date

        paginator = Paginator(State_list, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)


        #for State_rows in State_list:
        #    LDAPBackend().populate_user(State_rows.User)


        return render(request, 'index.html', {'State_list': contacts, 'other_var': other_var})
    else:
        return render(request, 'index.html')

def login(request):
    if not request.user.is_authenticated():
        form = AuthForm (request.POST or None)
        if request.POST and form.is_valid():
            user = form.login (request)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/")# Redirect to a success page.
        return render(request, 'index.html', {'login_form': form })
    else:
        auth.logout(request)
        form = AuthForm()
        return render(request, 'index.html', {'login_form': form })

# Вывод страницы с пользовательским профилем.
def userpage(request, username=None):

    if username == None:
        username = request.user.get_username()
    State_list = State.objects.filter(User=username)
    try:
        userprofile = User.objects.get(login_name=username)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'userpage.html', {'userprofile': userprofile, 'State_list': State_list})

def listofday(request, year=None, month=None, day=None):
    if request.user.is_authenticated():
        other_var = {}

        other_var['Date'] = datetime.date(int(year),int(month),int(day))

        if year is None or month is None or day is None:
            raise Http404
        State_list = State.objects.filter(LogOn__year=year, LogOn__month=month, LogOn__day=day, LogOff__isnull=False).order_by('id')
        paginator = Paginator(State_list, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        #for State_rows in State_list:
        #    LDAPBackend().populate_user(State_rows.User)

        return render(request, 'view_list.html', {'State_list': contacts, 'other_var': other_var})

    else:
        return Http404

def view_list(request):
    if request.user.is_authenticated():
        curent_date = datetime.date.today()
        if request.method == 'POST':
            date_form = date_select_form(request.POST)
            if date_form.is_valid():
                curent_date = date_form.cleaned_data['dateinput']

            if 'forward' in request.POST:
                curent_date = datetime.datetime.strptime(request.POST.get('curent_form_data'), '%d-%m-%Y') - datetime.timedelta(days=1)
            elif 'backward' in request.POST:
                curent_date = datetime.datetime.strptime(request.POST.get('curent_form_data'), '%d-%m-%Y') + datetime.timedelta(days=1)
            elif 'page' in request.POST:
                curent_date = datetime.datetime.strptime(request.POST.get('curent_form_data'), '%d-%m-%Y')

        else:
            date_form = date_select_form()
            date_form.fields['dateinput'].initial = curent_date

        other_var = {}
        other_var['Date'] = curent_date

        State_list = State.objects.filter(LogOn__year=curent_date.year, LogOn__month=curent_date.month, LogOn__day=curent_date.day, LogOff__isnull=False).order_by('id')
        paginator = Paginator(State_list, 25)  # Show 25 contacts per page

        page = request.POST.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'view_list.html', {'State_list': contacts, 'other_var': other_var, 'date_form': date_form})
    else:
        raise Http404