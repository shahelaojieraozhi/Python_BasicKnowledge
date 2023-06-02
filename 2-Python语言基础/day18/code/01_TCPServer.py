
import socket
# AF_INET: IPV4
# SOCK_STREAM: 表示tcp协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口
server.bind(('10.20.157.28', 6666))
server.listen(6)  # 设置监听数量，客户端连接数量

# 等待客户端连接
print('服务器已经启动！ 正在等待客户端连接...')
client, addr = server.accept()  # 会暂停，直到有客户端连接
print(client, addr)
# <socket.socket fd=324, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('10.20.157.28', 6666), raddr=('10.20.157.28', 60451)>
# ('10.20.157.28', 60451)

# 发送数据:  send()
# 接收数据:  recv()
while True:
    # 先接收,会暂停
    data = client.recv(1024)
    print('客户端说:', data.decode())

    # 发送数据
    client.send(f'你说的（{data.decode()}）很好'.encode())


