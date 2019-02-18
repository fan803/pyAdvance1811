import sys

l1 = [1,2]      #内存计数1
print(sys.getrefcount(l1))
l2 = [3,4]      #内存计数1
print(sys.getrefcount(l2))
l1.append(l2)   #内存计数为2
print(sys.getrefcount(l2))
l2.append(l1)   #内存计数为2
print(sys.getrefcount(l1))

del l1    #内存计数为1

del l2    #内存计数为1

