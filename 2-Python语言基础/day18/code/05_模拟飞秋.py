
import socket

feiqiu = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = '1:2:建国同志:特朗普:32:你好'

for i in range(5):
    feiqiu.sendto(msg.encode('GBK'), ('10.20.157.28', 2425))

