from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    #验证码
    url(r'^code/$',views.code,name='code'),
]
