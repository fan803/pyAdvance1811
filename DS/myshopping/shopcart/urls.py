from django.conf.urls import url
from . import views


urlplatterns =[
    url(r"(?P<count>\d+)/(?P<g_id>)/add/",views.add,name="add")
]