"""
实现分组大小为8个字母的置换密码，实现对英文消息plainxtext的置换加密，并对得到的密文进行解密，核对加解密的正确性；
注意：如果最后一个分组不够8个字母，则用字母A进行填充至8个字母。
"""

import numpy as np
from random import *

def Init_CTX():
    #初始化加密算法工作的环境，主要包括公共参数和版本控制等
    plaintext = 'cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms, to transform messages in ways that are hard to decipher. These deterministic algorithms are used for cryptographic key generation, digital signing, verification to protect data privacy, web browsing on the internet and confidential communications such as credit card transactions and email.'
    #plaintext='hello world'
    En_Key,De_Key=GenKey()
    cipher=Encrypt(plaintext,En_Key)
    print(cipher)
    plain=Decrypt(cipher,De_Key)
    print('\n'+plain)

def GenKey():
    #生成加密密钥和解密密钥
    m=8
    Key=[[0 for j in range(m)]for i in range(m)]
    t=sample(range(m),m)
    for i in range(m):
        Key[i][t[i]]=1
    Key=np.array(Key)
    Key_inverse=np.linalg.inv(Key)
    return Key,Key_inverse.astype(np.int32)

def Encrypt(plain,En_Key):
    #加密函数
    mark=',!.- '
    t=''
    m=len(En_Key)
    cipher=['#' for i in range(len(plain))]
    for j,val in enumerate(plain):
        if val not in mark:
            t+=val
        else:
            cipher[j]=val
        if len(t)==m:
            temp=[ord(i) for i in t]
            temp=list(np.dot(temp,En_Key))
            t=''.join([chr(i) for i in temp])
            for n in range(m):
                for k,val in enumerate(cipher):
                    if val=='#':
                        cipher[k]=t[0]
                        t=t[1:]
                        break
    if t:
        for i in range(m-len(t)):
            t+='A'
            cipher+='#'
        temp=[ord(i) for i in t]
        temp=list(np.dot(temp,En_Key))
        t=''.join([chr(i) for i in temp])
        for n in range(m):
            for k,val in enumerate(cipher):
                if val=='#':
                    cipher[k]=t[0]
                    t=t[1:]
                    break
    return ''.join(cipher)

def Decrypt(cipher,De_Key):
    #解密函数
    mark=',!.- '
    t=''
    m=len(De_Key)
    plain=['#' for i in range(len(cipher))]
    for j,val in enumerate(cipher):
        if val not in mark:
            t+=val
        else:
            plain[j]=val
        if len(t)==m:
            temp=[ord(i) for i in t]
            temp=list(np.dot(temp,De_Key))
            t=''.join([chr(i) for i in temp])
            for n in range(m):
                for k,val in enumerate(plain):
                    if val=='#':
                        plain[k]=t[0]
                        t=t[1:]
                        break
    
    return ''.join(plain).lower()

def main():
    Init_CTX()

if __name__=="__main__":
    main()