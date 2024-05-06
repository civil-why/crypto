'''
3)自动生成一个密钥，用AES对其进行加密，采用CTR模式，并把密文写到文件cipher-ctr.txt
'''
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
from Crypto.Util.number import bytes_to_long
import os

def main():
    plain=''
    with open("cryptography exam\exam2\实验内容-20240401\plaintext.txt",'r') as file:
        plain=file.read()
    b_plain=bytes(plain,encoding='utf-8')
    key=get_random_bytes(16)
    
    ctr = Counter.new(AES.block_size * 8, initial_value=bytes_to_long(bytes(os.urandom(16))))
    cipher=AES.new(key,counter=ctr,mode=AES.MODE_CTR)
    crypted_data=cipher.encrypt(b_plain)

    #with open("cryptography exam\exam2\实验内容-20240401\cipher-ecb.txt",'w') as file:
    #    file.write(str(crypteddata))
    
    file_out = open("cryptography exam\exam2\实验内容-20240401\cipher-ctr.txt", "wb")
    # 在文件中依次写入key、iv和密文encrypted_data
    [file_out.write(x) for x in (key,ctr,crypted_data)]



if __name__=="__main__":
    main()