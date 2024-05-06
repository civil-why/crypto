'''
5）自动生成一个认证码密钥，采用GMAC，生成plaintext.txt的认证码，并把认证码拼在plaintext.txt的后面
'''
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def main():
    plain=''
    with open("cryptography exam\exam2\实验内容-20240401\plaintext.txt",'r') as file:
        plain=file.read()
    b_plain=bytes(plain,encoding='utf-8')

    key=get_random_bytes(32)
    gmac = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = gmac.encrypt_and_digest(b_plain)

    with open("cryptography exam\exam2\实验内容-20240401\plaintext_GMAC.txt",'w') as file:
        file.write(plain+tag.hex())

if __name__=="__main__":
    main()