from django.conf.urls import url
from . import views

aap_name = 'myboke'

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^(?P<name>\w+)/hello/$', views.hello),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^addaritcle/$', views.addArticle, name='addaritcle'),
url(r'^createImage/$', views.createImage, name='createImage'),
]
