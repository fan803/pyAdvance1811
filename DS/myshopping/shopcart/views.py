from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET


from django.contrib.auth.decorators import login_required
from goods.models import Goods
from . import models



# Create your views here.
@require_GET
@login_required
def add(req, count, goods_id):
    count = req.Get["count"]
    goods_id = req.Get["goods_id"]
    print(goods_id)
    goods = Goods.objects.get(pk=goods_id)

    user =req.user


    try:
        shopCart = models.ShopCart.objects.filter(user=user,goods=goods)
        shopCart.count += int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()

    except:
        shopCart = models.ShopCart(user=user,goods=goods)
        shopCart.count = int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()

    return redirect(reverse("shopcart:list"))



from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from goods.models import Goods
from . import models


@require_GET
@login_required
def add(request, count, goods_id):
    # count = request.GET['count']
    # goods_id = request.GET['goods_id']
    goods = Goods.objects.get(pk=goods_id)
    user = request.user
    try:
        shopCart = models.ShopCart.objects.get(user=user, goods=goods)
        shopCart.count += int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()
    except:
        shopCart = models.ShopCart(goods=goods, user=user)
        shopCart.count = int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()

    return HttpResponse("添加成功")
    # return redirect(reverse("shopcart:list"))


def list(requst):
    shopcarts = models.ShopCart.objects.filter(user=requst.user).order_by("-addTime")
    return render(requst, "shopcart/list.html", {"shopcarts": shopcarts})






