"""
实现单表替代密码：凯撒密码,实现对英文消息plainxtext的替代加密
"""
def Init_CTX():
    #初始化加密算法工作的环境，主要包括公共参数和版本控制等
    plaintext = 'cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms, to transform messages in ways that are hard to decipher. These deterministic algorithms are used for cryptographic key generation, digital signing, verification to protect data privacy, web browsing on the internet and confidential communications such as credit card transactions and email.'.lower()
    cipher=Encrypt(plaintext)
    print(cipher)
    #print('\n'+Decrypt(cipher))
    return

def GenKey():
    #生成加密密钥和解密密钥
    K=3
    return K

def Encrypt(str):
    #加密函数
    temp=''
    Key=GenKey()
    for j in str:
        if ord(j)<=ord('z') and ord(j)>=ord('a'):
            t=chr(ord(j)+Key)
            if ord(t)>ord('z'):
                temp+=chr(ord(t)-26)
            else:
                temp+=t
        else:
            temp+=j
    return temp

"""
def Decrypt(str):
    #解密函数
    temp=''
    Key=GenKey()
    for i in str:
        if ord(i)<=ord('z') and ord(i)>=ord('a'):
            t=chr(ord(i)-Key)
            if ord(t)<ord('a'):
                temp+=chr(ord(t)+26)
            else:
                temp+=t
        else:
            temp+=i
    return temp
"""

def main():
    Init_CTX()
    return

if __name__=="__main__":
    main()