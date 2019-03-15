from django.shortcuts import render
from goods.models import GoodsType,Goods
# from goods import models



def index(req):
    #第一个一级类型数据
    good_type1 = GoodsType.objects.filter(pk=10001)
    good_type1_2 = GoodsType.objects.filter(parent=good_type1)
    goods1_list = Goods.objects.filter(goodstype__in=good_type1_2)[:5]


    # 第二个一级类型数据
    good_type2 = GoodsType.objects.filter(pk=10002)
    good_type2_2 = GoodsType.objects.filter(parent=good_type2)
    goods2_list = Goods.objects.filter(goodstype__in=good_type2_2)[:5]


    # 第三个一级类型数据
    good_type3 = GoodsType.objects.filter(pk=10003)
    good_type3_2 = GoodsType.objects.filter(parent=good_type3)
    goods3_list = Goods.objects.filter(goodstype__in=good_type3_2)[:5]


    # 第四个一级类型数据
    good_type4 = GoodsType.objects.filter(pk=10004)
    good_type4_2 = GoodsType.objects.filter(parent=good_type4)
    goods4_list = Goods.objects.filter(goodstype__in=good_type4_2)[:5]


    # 第五个一级类型数据
    good_type5 = GoodsType.objects.filter(pk=10005)
    good_type5_2 = GoodsType.objects.filter(parent=good_type5)
    goods5_list = Goods.objects.filter(goodstype__in=good_type5_2)[:5]


    # 第六个一级类型数据
    good_type6 = GoodsType.objects.filter(pk=10006)
    good_type6_2 = GoodsType.objects.filter(parent=good_type6)
    goods6_list = Goods.objects.filter(goodstype__in=good_type6_2)[:5]


    # 第7个一级类型数据
    good_type7 = GoodsType.objects.filter(pk=10007)
    good_type7_2 = GoodsType.objects.filter(parent=good_type7)
    goods7_list = Goods.objects.filter(goodstype__in=good_type7_2)[:5]



    allGoodsType = GoodsType.objects.filter(parent__isnull=True)
    return render(req,'index.html',{'allGoodsType':allGoodsType,\
                                    'goods1_list':goods1_list, \
                                    'goods2_list': goods2_list, \
                                    'goods3_list': goods3_list, \
                                    'goods4_list': goods4_list, \
                                    'goods5_list': goods6_list, \
                                    'goods6_list': goods6_list, \
                                    'goods7_list': goods7_list,\
                                    })



def code(req):
    pass