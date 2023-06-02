import socket
import threading

# 服务端socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.20.157.28', 6666))
server.listen(60)  # 设置监听数量，客户端连接数量

# 聊天室的所有用户
online_list = []

# 线程：一个线程对应一个客户端
def client_thread(client, addr):
    while True:
        try:
            # 先接收,会暂停
            data = client.recv(1024)
            print(f'客户端【{addr[0]}】说:', data.decode())

            # 发送数据: 群发
            for online in online_list:
                online.send(f'【{addr[0]}】:{data.decode()}'.encode())
        except:
            if client in online_list:
                online_list.remove(client)

# 等待客户端连接
while True:
    print('服务器已经启动！ 正在等待客户端连接...')
    client, addr = server.accept()  # 会暂停，直到有客户端连接

    # 当有新客户端连接时，就加入到online_list中
    online_list.append(client)

    # 创建线程
    threading.Thread(target=client_thread, args=(client, addr)).start()

