'''
4）自动生成一个认证码密钥，采用HMAC，生成plaintext.txt的认证码，并把认证码拼在plaintext.txt的后面
'''
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

def main():
    plain=''
    with open("cryptography exam\exam2\实验内容-20240401\plaintext.txt",'r') as file:
        plain=file.read()
    b_plain=bytes(plain,encoding='utf-8')

    key=get_random_bytes(32)
    hmac=HMAC.new(key,msg=b_plain,digestmod=SHA256)
    hmac_code=hmac.hexdigest()
    final=plain+hmac_code

    with open("cryptography exam\exam2\实验内容-20240401\plaintext_HMAC.txt",'w') as file:
        file.write(final)

if __name__=="__main__":
    main()