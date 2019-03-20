from django.shortcuts import render
from django.views.decorators.http import require_POST

from users.models import Address
from shopcart.models import ShopCart
from goods.models import Goods
from . import models



@require_POST
def confirm(req):
    g_ids = req.POST.getlist("g_id")
    shopCart = ShopCart.objects.filter(pk__in=g_ids)
    addresses = Address.objects.filter(user = req.user)
    return render(req,"orders/confirm.html",{"shopCart":shopCart,"addresses":addresses})

def pay(req):
    pass


def done(req):
    g_ids = req.POST.getlist("g_id")
    myShopCart = ShopCart.objects.filter(user=req.user)
    myShopCart.goods.objects.filter(pk_in=g_ids)

    # 生成订单
    pass



def list(req):
    pass


def detail(req):
    pass



