def checkUser(sg):
    def check():
        name = input("请输入用户名：")
        if name == "gs":
            print("登录成功")
            sg()
        else:
            print("未授权")
    return check

@checkUser
def showlist():
    print("订单号有：")
    for i in range(10):
        print('订单'+str(i))

@checkUser
def showBalance():
    print("余额为：1000000￥")

@checkUser
def showCoupons():
    print("优惠券为： 100 10 50 20 ")


showlist()
showBalance()
showCoupons()