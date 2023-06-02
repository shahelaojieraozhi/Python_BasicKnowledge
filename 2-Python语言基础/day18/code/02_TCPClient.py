
import socket

# 客户端的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 主动连接服务器
client.connect(('10.20.157.28', 6666))

# 发送和接收数据
while True:
    # 先发送
    data = input('请输入要发送的数据:')
    client.send(data.encode())

    # 接收
    data2 = client.recv(1024)
    print('服务器回复:', data2.decode())


