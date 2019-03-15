from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from goods.models import Goods
from .import models

# Create your views here.

@require_GET
@login_required
def add(req, count, goods_id):
    goods= Goods.objects.set(pk=goods_id)
    user = req.user

    try:
        shopCart = models.ShopCart.objects.get(user=user,goods=goods)
        shopCart.count += int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()
    except:
        shopCart = models.ShopCart(user=user,goods=goods)
        shopCart.count = int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()
    return redirect(reverse("shopcart:list"))


def list(req):
    shopcarts = models.ShopCart.filter(user=req.user).order_by("-aadTime")

    return render(req,"shopcart/list.html",{"shopcarts":shopcarts})