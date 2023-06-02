
import socket

# SOCK_DGRAM: 表示UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('10.20.157.28', 6667))
print("UDP服务器已启动！正在等待客户端发送数据...")

# 接收和发送数据
while True:
    # 接收
    data, client_addr = server.recvfrom(1024)
    print(f'【{client_addr[0]}】说:', data.decode())

    # 发送
    server.sendto('今晚吃鸡'.encode(), client_addr)

