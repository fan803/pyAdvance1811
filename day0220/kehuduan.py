import socket
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
saddr = ('127.0.0.1', 9001)
sc.bind(saddr)
buffersize = 1024
while True:
    recvdata, recvaddr = sc.recvfrom(buffersize)
    print("收到了",recvaddr,"消息",recvdata.decode("utf-8"))
    sc.sendto(recvdata,recvaddr)

print("服务器收到消息")