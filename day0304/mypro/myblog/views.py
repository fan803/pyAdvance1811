from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from io import BytesIO
from .import utils
# Create your views here.
from .import models


def index(req):
    '''
    第一种插入方法
    au = models.Users.create(name='张三',age=18)
    au.save()
    第二种插入方法
    au = models.Users(name='李四', age=19)
    au.save()
    '''

    # au = models.Users.um.createUser(name='王二', age=20)
    # return HttpResponse("好了")
    # temp = loader.get_template('myblog/index.html')
    # return HttpResponse(temp.render({'msg':'123'},req))
    # u = models.Users.object.get(id=2)
    return render(req,'myblog/index.html',{'msg':'123'})

def login(req):
    if req.method == 'GET':
        return render(req,'myblog/login.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        try:
            models.Users.um.get(name=name)
            return HttpResponse('登录成功')
        except:
            return render(req,'myblog/login.html')

def register(req):
    if req.method == 'GET':
        return render(req, 'myblog/register.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        u = models.Users(name=name,age=age)
        u.save()
        return HttpResponse('注册成功')

def addArticle(req):
    if req.method == 'GET':
        return render(req, 'myblog/addaritcle.html')
    elif req.method == 'POST':
        title = req.POST['title']
        content = req.POST['content']
        user= models.Users.objects.get(pk=1)
        article = models.Article(title=title, content=content, author=user)
        article.save()
        return redirect('myblog:index')

def createImage(req):
    #准备个空间，放置验证码图片
    b = BytesIO()
    #生成验证码及其图片
    imge,code = utils.create_code()
    #把验证吗图片保存到流里面
    imge.save(b,'png')
    req.session['code'] = code
    return HttpResponse(b.getbuffer())