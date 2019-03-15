from django.shortcuts import render,reverse,redirect
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.http import HttpResponse
from store.models import Store
from  . import models
# Create your views here.


def add(req):
    if req.method =="GET":
        return render(req,"store/add.html",{})
    else:
        name = req.POST['name']
        price = req.POST['price']
        stock = req.POST['stock']
        store_id = req.POST['store']
        cover = req.FILES['cover']
        type2 = req.POST['type2']

        intro = req.POST['intro']


        store =Store.objects.get(pk=store_id)

        goodsType = models.GoodsType.objects.get(pk=type2)

        goods = models.Goods(name=name, price=price,stock=stock,intro=intro, count='100', store=store,goodstype=goodsType)
        goods.save()

        goodImage = models.GoodsImage(path=cover,goods=goods)
        goodImage.save()
        print(goodImage.save())
        return redirect(reverse("store:detail",kwargs={"s_id":store_id}))

@require_GET
def findTypeByPId(req):
    parent_id = req.GET['parent_id']
    type2s = models.GoodsType.objects.filter(parent=parent_id)
    return HttpResponse(serialize("json",type2s))


@require_GET
def detail(req,g_id):
    goods = models.Goods.objects.get(pk=g_id)
    return render(req,"goods/detail.html",{"goods":goods})





