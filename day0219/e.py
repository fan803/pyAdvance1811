from threading import Thread
import time
def threadmain(name):
    while True:
        time.sleep(1)
        print(name,"你好")
thread = Thread(target=threadmain,arges=("线程一",))
thread.start()
