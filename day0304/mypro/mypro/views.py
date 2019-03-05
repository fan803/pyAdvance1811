from django.http import HttpResponse


def index(request):
    #处理请求
    print(request)
    #做出应答
    return HttpResponse('<h1>好嗨哦，感觉人生已经到达了巅峰。。。。</h1>')
