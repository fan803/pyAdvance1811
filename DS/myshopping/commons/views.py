from django.shortcuts import render


def index(req):
   return render(req,'index.html',{'msg':'首页'})

def code(req):
    pass