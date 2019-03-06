from django.http import HttpResponse


def index(request):
    #处理请求
    print(request)
    #做出应答
    return HttpResponse('<h1>就是那么帅，不接受反驳。。。。</h1>')

def findall(request):
    #处理请求
    print(request)
    #做出应答
    return HttpResponse('<h3><a href="addgood.html">绣春刀</a></h3>')

def addgood(request):
    #处理请求
    print(request)
    #做出应答
    return HttpResponse('<h3><a href="delete.html">绣春刀123</a></h3>')

def delete(request):
    #处理请求
    print(request)
    #做出应答
    return HttpResponse('<h3><a href="index.html">绣春刀456</a></h3>')