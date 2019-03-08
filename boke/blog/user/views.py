from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from io  import BytesIO
from .import untils
# Create your views here.


def index(req):
    return render(req,'user/index.html')

def register(req):
    if req.method == 'GET':
        return render(req,'user/register.html')
    elif req.method =='POST':
        name = req.POST.get('name')
        account = req.POST.get('account')
        age = req.POST.get('age')
        gender = req.POST.get('gender')
        phone = req.POST.get('phone')
        addr = req.POST.get('addr')
        print(name,account,age,gender,phone,addr)
        user = models.Users(name=name,account=account,age=age,gender=gender,phone=phone,addr=addr)
        user.save()

        return render(req,'user/index.html')
def login(req):
    if req.method == 'GET':
        return render(req,'user/login.html')
    elif req.method =='POST':
        account = req.POST.get('account')
        seccode = req.POST.get('seccode')
        if req.session['code'] == seccode:
            try:
                models.Users.objects.get(account=account)
            except:
                return render(req,'user/login.html')
            return render(req,'user/index.html')
        else:
            return render(req, 'user/login.html')

#发布文章
def addArticle(req):
    if req.method == 'GET':
        return render(req, 'user/addarticle.html')
    elif req.method == 'POST':
        title = req.POST.get('title')
        concent = req.POST.get('concent')
        print(title,concent)
        user = models.Users.objects.get(id=1)
        article = models.ArticleType(title=title,concent=concent,author=user)
        article.save()

        return render(req,'user/index.html',{'msg_title':title,'msg_concent':concent})

def createImg(req):
    #准备一个空间，放置验证码图片
    b = BytesIO()
    #生成验证码及图片
    img,code = untils.create_code()
    #验证码及图片保存到流当中
    img.save(b,'PNG')
    req.session['code'] = code
    print(code)
    return HttpResponse(b.getvalue())

def leacots(req):
    return render(req,'user/leacots.html')


