from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from io import BytesIO
from .import utils
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.
from .import models
from . import forms


@csrf_exempt
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
    return render(req,'myblog/index.html',{'msg':'《沁园春·雪》'})

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

@transaction.atomic
def register(req):
    if req.method == 'GET':
        userform = forms.UserForm

        return render(req, 'myblog/register.html',{'userform':userform})
    elif req.method == 'POST':
        '''
        form = forms.UserForm(req.POST)
        print(form.data)
        print(form.data['name'])
        '''
        name = req.POST.get('name')
        age = req.POST.get('age')
        #获取文件
        avater = req.FILES.get('avater')
        #拼接上传路径
        path = 'static/image/'+ avater.name
        #以流的方式打开上传
        with open(path,'wb') as file:
        #分片写入
            for i in avater.chunks():
                file.write(i)

        print(name,age,avater)
        # 设置还原点
        s_id = transaction.savepoint()
        try:
            u=models.Users(name=name,age=age,avater=path)
            u.save()
            transaction.savepoint_commit(s_id)
            return HttpResponse('注册成功')
        except:
            transaction.savepoint_rollback(s_id)
            return HttpResponse('注册失败')

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


def hello(req):
    print(req.session.get('code'))

    return HttpResponse('<h1>jspodjawoprjw</h>')


@csrf_exempt
def jsontest(req):
    if req.method == 'POST':
        u = models.Users.objects.filter(pk=1)[0]
        print(u)
        u = model_to_dict(u)
        return JsonResponse(u)