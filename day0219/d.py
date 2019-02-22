# import threading
# num = 1
# def fun1():
#     num = 2
#     print(num)
# fun1()
# print(num)
# def fun2():
#     global num
#     num = 3
#     print(num)
# fun2()
# print(num)
# def fun3():
#     global num
#     num = 4
#     print(num)
# t = threading.Thread(target=fun3)
# t.start()
# print(num)
# 一个进程内的线程直接可以共享全局变量
# 多个线程同时操作共享变量造成数据混乱

import threading,time
num = 0
def fun1():
    for r in range(1000000):
        global num
        num += 1
p1 = threading.Thread(target=fun1)
p1.start()
# time.sleep(2) 注释取消会改变结果
class MyThread(threading.Thread):
    def run(self):
        for r in range(1000000):
            global num
            num += 1
t = MyThread()
t.start()
time.sleep(2)
print(num)
