from django.conf.urls import url
from django.contrib import admin
from .import views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^delete/$',views.delete)
]