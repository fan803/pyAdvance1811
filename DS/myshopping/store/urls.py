from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^add/$',views.add, name='add'),
    url(r'^list/$',views.list, name='list'),
    url(r'^(?P<s_id>\d+)/update/$',views.update, name='update'),
    url(r'^(?P<s_id>\d+)/detail/$',views.detail, name='detail'),
    url(r'^change/(?P<s_id>\d+)/(?P<change>\d+)/$', views.change, name='change'),
]
