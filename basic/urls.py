
from re import template
from django.urls import path, include

from . import views

from django.views.generic import TemplateView



app_name = 'basic'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]