import socket
#创建客户机socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接到服务端
SERRVERADDR = ("192.168.15.24",9876)
client.connect(SERRVERADDR)
#向服务器发送数据
client.send("你好，服务器".encode("utf-8"))
BUFFERSIZE = 1024
data = client.recv(BUFFERSIZE)
print("收到服务器发来信息",data.decode("utf-8"))