from django.urls import path
from first_app import views

urlspatterns = [
    path('', views.index, name='index'),
]
