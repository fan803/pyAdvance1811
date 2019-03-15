from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from goods.models import GoodsType,Goods
from . import models


@login_required
def add(req):
    if req.method == "GET":
        return render(req,'store/add.html',{})
    else:
        name = req.POST['name'].strip()
        intro = req.POST['intro'].strip()
        try:
            cover = req.FILES['cover']
            store = models.Store(name=name,intro=intro,cover=cover,user=req.user)
        except:
            store = models.Store(name=name, intro=intro, user=req.user)
        store.save()

        return redirect(reverse("store:detail",kwargs={'s_id':store.id}))



@require_GET
@login_required
def list(req):
    stores = models.Store.objects.filter(user=req.user,status__in=[0,1])
    return render(req,'store/list.html',{'stores':stores})




@login_required
def update(req,s_id):
    if req.method == "GET":
        store = models.Store.objects.get(pk=s_id)
        return render(req,'store/update.html',{"store":store})
    else:
        name = req.POST['name'].strip()
        intro = req.POST['intro'].strip()
        try:
            cover = req.FILES['cover']
            print(cover)
            store = models.Store(name=name,intro=intro,cover=cover,user=req.user)
        except:
            store = models.Store(name=name, intro=intro, user=req.user)
        store.save()

        return redirect(reverse("store:detail",kwargs={'s_id':store.id}))




@require_GET
@login_required
def detail(req,s_id):
    store = models.Store.objects.get(pk=s_id)
    type1 = GoodsType.objects.filter(parent__isnull=True)

    goods = Goods.objects.filter(store=store)

    return render(req,'store/detail.html',{'store':store,'type1':type1,'goods':goods})


@require_GET
@login_required
def change(req,s_id,change):
   store = models.Store.objects.get(id=s_id)
   store.status = int(change)
   store.save()
   if store.status == 2:
       return redirect(reverse("store:list"))
   else:
       return render(req,'store/detail.html',{'store':store})
