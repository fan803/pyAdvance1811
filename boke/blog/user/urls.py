from django.conf.urls import url
from . import views

app_name = 'user'
#子路径
urlpatterns = [
    url(r'^index/',views.index),
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^addarticle/',views.addArticle,name='addarticle'),
    url(r'^createImg/',views.createImg,name='createImg'),
    url(r'^leacots/',views.leacots,name='leacots'),
]
