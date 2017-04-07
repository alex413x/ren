"""renaissance URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
# from chatapi import views
# from renaissance import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('la_website.urls')),
    url(r'^lchat/', include('chatapi.urls')),
    url(r'^bb/', include('baseball.urls')),
    #url(r'^', views.index, name='index'),
    #url(r'^api-auth/', include('chatapi.urls', namespace='chatapi')),
    #url(r'^lchat/(?P<pk>[0-9]+)$', views.lBotDetail.as_view())
    #url(r'^lchat/bots$', views.lBotList.as_view()),

]
