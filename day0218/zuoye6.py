import os
from multiprocessing import Process
import time
def process(a, b, c, **kwargs):
    print(a, b, c, kwargs)
    time.sleep(2)
    print(" 进程A执行了， 进程id为", os.getpid())

def main():
    print("主进程id", os.getpid())
    p1 = Process(name="进程A", target=process, args=(4,5,6), kwargs= {"name": "zzy"})
    p1.start()
    # join方法能够阻塞主进程，print(p1.name)陷入等待 等待p1进程执行完毕
    print(p1.is_alive())

    # terminate  结束进程
    p1.join()
    print(p1.name)
    print(p1.is_alive(),p1.pid)

if __name__ == "__main__":
    main()