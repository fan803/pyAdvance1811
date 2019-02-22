from socket import *
ss = socket(AF_INET, SOCK_STREAM)
saddr = ('127.0.0.1', 9001)
ss.bind(saddr)
ss.listen(100)
print("服务启动了")
while True:
    sc, caddr = ss.accept()
    receivebytes = sc.recv(1024)
    receivedata = receivebytes.decode("utf-8")
    print("收到：%s" % receivedata)
    sendenbytes = receivebytes
    sc.send(sendenbytes)
    # sc.close()
ss.close()