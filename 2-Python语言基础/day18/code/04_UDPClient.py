
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 发送
    data = input('请输入要发送的数据:')
    client.sendto(data.encode(), ('10.20.157.28', 6667))

    # 接收
    data2, addr = client.recvfrom(1024)
    print('=> 接收到服务器的回复:', data2.decode())


