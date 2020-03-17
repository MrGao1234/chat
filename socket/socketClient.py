# coding=utf-8
import socket
import sys

# 创建socket 对象
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
# 设置端口号
port = 8088
# 设置状态
alive = True

# 根据端口号和ip连接服务器
socketClient.connect((host, port))

# 发送消息
socketClient.send(("{\"type\":\"OPEN\",\"clientName\":\"" + str(port) + "\"}").encode("utf-8"))

print("已登录")

while alive:
    print("正在输入："),
    line = input()

    # 判断是否退出
    if (line == 'q') | (line == 'Q'):
        break
    else:
        socketClient.send(("{\"type\":\"MESSAGE\",\"message\":\"" + line + "\",\"chat\":\"GROUP\"}").encode("utf-8"))

# 接收小于 1024 字节的数据
msg = socketClient.recv(1024)

socketClient.close()
print(msg.decode('utf-8'))
