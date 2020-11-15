from django.contrib import admin
from django.urls import path
from basic_app import views
from django.conf.urls import include,url


app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    
]

