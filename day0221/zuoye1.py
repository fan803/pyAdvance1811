#TCP服务器

import socket
from threading import Thread
def readThread(cli, fromuser):
    BUFFERSIZE = 1024*1024
    while True:
        try:
            databytes = cli.recv(BUFFERSIZE)
            if len(databytes) == 0:
                cli.close()
                clientList.remove((fromuser, cli))
                break
            else:
                datastr = databytes.decode("gbk")
                touser = datastr.split("|")[0]
                info = datastr.split("|")[1]
                print(fromuser, "发给 ", touser, info)
                sendstr = fromuser + "|" + info
                sendbytes = sendstr.encode("gbk")
                for c in clientList:
                    if c[0] == touser:
                        c[1].send(sendbytes)
        except Exception as e:
            print(e)
            break

def listenThread():
    while True:
        try:
            clientSocket, clientAddr = serverSocket.accept()
            # 此处先接受用户名
            usenameBytes = clientSocket.recv(1024 * 1024)
            username = usenameBytes.decode("gbk")
            clientList.append((username, clientSocket))
            print("用户", username, "已连接", "共有客户端", len(clientList))

            rthread = Thread(target=readThread, args=(clientSocket, username))
            rthread.start()
        except Exception as e:
            print(e)


def sendThread():
    #发送给所有客户端公告
    datastr = "好嗨哦"
    for cli in clientList:
        sendBytes = datastr.encode("gbk")
        cli[1].send(sendBytes)

if __name__ == "__main__":
    try:
        # 创建客户端列表 内容格式为（用户名,socket）
        clientList = []
        # 1 创建服务器socket
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2 绑定端口
        SERVERADDR = ("192.168.15.24", 9999)
        serverSocket.bind(SERVERADDR)
        # 3 开启监听
        serverSocket.listen()
        # 4 开启线程用来接受客户端连接
        lthread = Thread(target=listenThread)
        lthread.start()
        sthread = Thread(target=sendThread)
        sthread.start()
    except Exception as e:
        print(e)