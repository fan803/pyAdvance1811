from multiprocessing import Process
import os
import time
def fun(name, age , **kwargs1):
    print(name, age, kwargs1)
    time.sleep(5)
    print(name, age, kwargs1)
    time.sleep(1)
    print(name, age, kwargs1)
    time.sleep(1)
    print(name, age, kwargs1)
    print("parent pid %d" % os.getpid())
    p = Process(name="child", target=fun, args=("zzy", 20), kwargs={"isalive": False})
    p.start()
    print("p name %s pid %d" % (p.name, int(p.pid) ))
    time.sleep(2) #睡眠
    p.terminate()
    p.join() #阻塞
    print("child finish")
fun("11", 18)