from  threading import Thread, Lock
lock = Lock()
num = 0
def fun():
    global num
    for i in range(1000000):
        #使用资源需要加锁
        lock.acquire()
        num = num+1
        #使用完毕解锁
        lock.release()

t1 = Thread(target=fun)
t1.start()
print(num)
t2 = Thread(target=fun)
t2.start()
print(num)