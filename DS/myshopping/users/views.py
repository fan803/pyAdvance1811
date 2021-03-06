from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from io import BytesIO
from . import utils


from . import models
# Create your views here.


def user_login(req):
    if req.method == 'GET':
        # try:
        #     next_url = req.GET['next']
        # except:
        #     next_url ='/'
        # print(next_url)
        return render(req,"users/login.html")#{'next_url':next_url}
    elif req.method == "POST":
        username = req.POST['username'].strip()
        password = req.POST['password'].strip()
        next_url= req.POST.get('next','/')
        # 验证码
        ac = req.POST.get('ac')
        if req.session['code'] == ac:
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    # 将验证通过的用户信息保存在req,  req,user返回用户名
                   login(req, user)
                   # return redirect(next_url)
                   return render(req,'users/userInfo.html',{'user':user})
                else:
                    return render(req, "users/login.html", {"error_code": 2, "msg": "你的账号已被锁定"})
            else:
                return render(req, "users/login.html", {"error_code":3, "msg": "用户名或者密码错误，请重新登陆"})
        else:
            return render(req, "users/login.html", {"error_code":4, "msg": "验证码输入有误，请重新输入"})
def register(req):
    if req.method == 'GET':
        return render(req,"users/register.html",{})
    elif req.method == "POST":
        username = req.POST['username'].strip()
        password = req.POST['password'].strip()
        nickname = req.POST['nickname'].strip()
        confirmpwd = req.POST['confirmpwd'].strip()
        #验证码
        ac = req.POST.get('ac')
        if req.session['code'] != ac:

            return render(req, "users/register.html", {"error_code": 4, "msg": "验证码输入有误，请重新输入"})
        #判断密码两次输入是否一样
        elif password != confirmpwd:
            return render(req,"users/register.html",{"error_code":1,"msg":"密码输入不一致"})
        #判断密码长度
        elif len(password) <= 6 or len(password) >= 16:
            return render(req,"users/register.html",{"error_code":5,"msg":"密码错误请输入6~16字符"})
        #用户是否存在
        try:
            User.objects.get(username=username)
            return render(req,"users/register.html",{"error_code":2,"msg":"用户名已存在"})
        except:
            #判断昵称不能重复
            try:
                models.UserInfo.objects.get(username=username)
                return render(req, "users/register.html", {"error_code": 2, "msg": "用户昵称已存在"})
            except:
                #保存用户信息
                user = User.objects.create_user(username=username,password=password)
                userInfo = models.UserInfo(nickname=nickname,user= user)
                user.save()
                userInfo.save()
                return render(req,"users/login.html", {"error_code": 1, "msg": "用户注册成功，请登录"})


def user_logout(req):
    logout(req)
    return render(req, "users/login.html", {"error_code": 4, "msg": "用户退出成功，请重新登录"})


@login_required
def userinfo(req):
    print(req.user.userinfo.header)
    return render(req, "users/userInfo.html", {})


#图片
def createImage(req):
    #准备空间放置验证码图片
    b = BytesIO()
    #生成验证码及图片
    img, code= utils.create_code()
    img.save(b,'png')
    req.session['code'] = code
    return HttpResponse(b.getvalue())



#添加地址
def add_address(req):
    if req.method == "GET":
        return render(req, "users/add_address.html", {})
    else:
        recv_name = req.POST["recv_name"]
        recv_phone = req.POST["recv_phone"]
        provice = req.POST["provice"]
        desc = req.POST["desc"]
        is_default = req.POST["is_default"]
        try:
            #设置默认地址为默认
            is_default = req.POST["is_default"]
            addresses = models.Address.objects.filter(user=req.user)
            for address in addresses:
                address.is_default = False
                address.save()
            address = models.Address(recv_name=recv_name,recv_phone=recv_phone,provice=provice, desc=desc, user=req.user, is_default=True)
            address.save()


        except:
            address = models.Address(recv_name=recv_name, recv_phone=recv_phone, provice=provice, desc=desc, user=req.user,
                                     is_default=False)
            address.save()
        return redirect(reverse("users:address_list"))
def address_list(req):
    addresses = models.Address.objects.filter(user=req.user)
    return render(req,"users/list_address.html",{"addresses":addresses})



















