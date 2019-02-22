from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
from multiprocessing import Value
import time
def read(q):
    while True:
        print("pqueue size %d" % q.qsize())
        r = q.get()
        print("get %d" % r)
        print("pqueue size %d" % q.qsize())
def write(q):
    for r in range(5):
        q.put(r)
        print("put %d " % r)
        print("queue size %d" % q.qsize())
        time.sleep(2)

q = Queue(10)
q.put(-1)
q.put(-2)
if __name__ == "__main__":
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    pr.start()
    pw.start()
    pr.join()
    pw.join()
print("finish")