import socket
import threading

# 客户端的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.20.157.28', 6666))

# 发送
def send_data():
    while True:
        data = input('请输入要发送的数据:')
        client.send(data.encode())

# 接收
def recv_data():
    while True:
        data2 = client.recv(1024)
        print(data2.decode())


threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()

