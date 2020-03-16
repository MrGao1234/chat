import socket
import sys

# 创建socket 对象
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 8088

# 设置端口号
socketClient.connect((host, port))

socketClient.send("测试".encode())
socketClient.send("测试".encode())
socketClient.send("测试".encode())
socketClient.send("测试".encode())

# 接收小于 1024 字节的数据
msg = socketClient.recv(1024)

socketClient.close()
print(msg.decode('utf-8'))
