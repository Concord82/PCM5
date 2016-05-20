"""PCM5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from PCM import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^userpage/$', views.userpage, name='userpage'),
    url(r'^userpage/(?P<username>\w{1,50})/$', view = views.userpage),
    url(r'^viewday/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$', views.listofday),

    url(r'^viewlist/$', views.view_list, name='viewlist'),

]
