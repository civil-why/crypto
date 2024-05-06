'''
1)自动生成一个密钥，用AES对其进行加密，采用ECB模式，并把密文写到文件cipher-ecb.txt
'''
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def main():
    plain=''
    with open("cryptography exam\exam2\实验内容-20240401\plaintext.txt",'r') as file:
        plain=file.read()
        print(plain)
    b_plain=bytes(plain,encoding='utf-8')
    key=get_random_bytes(16)
    cipher=AES.new(key,AES.MODE_ECB)
    crypted_data=cipher.encrypt(pad(b_plain,AES.block_size))

    #with open("cryptography exam\exam2\实验内容-20240401\cipher-ecb.txt",'w') as file:
    #    file.write(str(crypted_data))
    
    file_out = open("cryptography exam\exam2\实验内容-20240401\cipher-ecb.txt", "wb")
    # 在文件中依次写入key、iv和密文encrypted_data
    [file_out.write(x) for x in (key, crypted_data)]



if __name__=="__main__":
    main()