
import hashlib

# md5加密: 不可逆,明文和密文一一配对
#    明文     密文
#   "123" => 32位的16进制数

# RSA加密: 非对称加密, 一对密钥:私钥,公钥
# AES DES

m = hashlib.md5()
m.update('ABCabc123?,.def'.encode())
print(m.hexdigest())
# e99a18c428cb38d5f260853678922e03
# a003015df861e3309ddb45ef338e3c11



