def checkUser(f):
    def check(*args):
        name = input("请输入用户名：")
        if name == "gs":
           return f(*args)
        else:
            print("未授权")
    return check
@checkUser
def showlist(n):
    print('订单列表第'+str(n)+'页')

@checkUser
def showm(a):
    print('余额为'+str(a))

@checkUser
def showa():
    return '你好'


showlist(10)
showm(10000000)
print(showa())