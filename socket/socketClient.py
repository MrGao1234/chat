# coding=utf-8
import socket
import threading
import time

# 1，创建socket 对象
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
# host = socket.gethostname()
host = '148.70.100.4'
# 设置端口号
port = 8088
# 设置状态
alive = True

# 2，根据端口号和ip连接服务器
socketClient.connect((host, port))

# 3，发送消息，用来让服务器记住开启线程
socketClient.send(("{\"type\":\"OPEN\",\"clientName\":\"" + time.strftime('%M%S', time.localtime(time.time())) + "\"}").encode("utf-8"))

# print("已登录")


# 4，启动一个监听线程，用来接收服务器返回信息
def listen(num):
    # 接收小于 1024 字节的数据
    msg = socketClient.recv(1024)
    print(msg.decode('utf-8'))


if __name__ == '__main__':
    t1 = threading.Thread(target=listen, args=(13,))
    t1.start()

# 5，循环输入，向服务器发送信息
while alive:
    print("正在输入："),
    line = input()

    # 判断是否退出
    if (line == 'q') | (line == 'Q'):
        break
    else:
        socketClient.send(("{\"type\":\"MESSAGE\",\"message\":\"" + line + "\",\"chat\":\"GROUP\"}").encode("utf-8"))

socketClient.close()






