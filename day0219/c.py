import time
import threading
def prt():
    print("hello")
    time.sleep(3)
start = time.time()
for r in range(5):
    prt()
end = time.time()
print(end-start)

start = time.time()
for i in range(5):
    t = threading.Thread(target=prt)
    t.start()
end = time.time()
print(end-start)