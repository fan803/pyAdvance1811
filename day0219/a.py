from multiprocessing import Queue
from multiprocessing import ProcessError
q = Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(5)
print(q.get())
print(q.get())
print(q.get())
try:
    print(q.get())
except Exception as p:
    print(p)
print(q.empty())
print(q.full())