"""
随机生成一个以比特为单位进行置换的128个比特置换表，并用该表做密钥，对文件cryptointo.txt进行加密，把密文写到文件pmt-cipher.txt，对得到的密文进行解密，核对正确性。
注意：如果最后一个分组不够128比特，则用1进行填充至128个比特。
"""
import random
import numpy as np

def Init_CTX():
    #初始化加密算法工作的环境，主要包括公共参数和版本控制等
    plaintext=''
    with open('cryptography exam\exam1\古典密码实验内容-20240226\cryptointro.txt','r',encoding='utf-8') as file:
        plaintext=file.readline()
    cipher=Encrypt(plaintext.replace('\n',''))
    print(cipher)
    with open('cryptography exam\exam1\古典密码实验内容-20240226\pmt-cipher.txt','w',encoding='utf-8') as file:
        file.write(cipher)
    #print('\n'+Decrypt(cipher))
    return

def GenKey():
    #生成加密密钥和解密密钥
    m=128
    Key=[[0 for j in range(m)]for i in range(m)]
    t=random.sample(range(m),m)
    for i in range(m):
        Key[i][t[i]]=1
    Key=np.array(Key)
    return Key
    
def Encrypt(plain):
    #加密函数
    En_Key=GenKey()
    cipher=''
    t=''
    mark=',!.- 。，、\n'
    b_plain=[bin(ord(i)).replace('0b','') if i not in mark else i for i in plain]
    temp_text=''.join(b_plain)
    m=len(En_Key)
    cipher=['#' for i in range(len(temp_text))]
    for j,val in enumerate(temp_text):
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
            t+='1'
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

def Decrypt(cipher):
    #解密函数
    pass

def main():
    Init_CTX()
    return

if __name__=="__main__":
    main()