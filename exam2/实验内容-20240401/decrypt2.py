# task2的解码，用于反推加密是否正确

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# 从前边文件中读取出加密的内容
file_in = open("cryptography exam\exam2\实验内容-20240401\cipher-cbc.txt", "rb")
# 依次读取key、iv和密文encrypted_data，16等是各变量长度，最后的-1则表示读取到文件末尾
key,iv, encrypted_data = [file_in.read(x) for x in (16,AES.block_size,-1)]

# 实例化加密套件
cipher = AES.new(key, AES.MODE_CBC,iv)
k=cipher.decrypt(encrypted_data)
data = unpad(k, AES.block_size)
print(data)