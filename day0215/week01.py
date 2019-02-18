import time

def check(f):
    def fun1():
        start =time.time()
        f()
        end =time.time()
        print(f.__name__,'消耗',end-start)
    return fun1
@check
def a1():
    a=[i for i in range(1000000)]
    for s in a:
        print(s)
@check
def a2():
    b=(x for x in range(1000000))
    for j in b:
        print(j)
a1()
a2()