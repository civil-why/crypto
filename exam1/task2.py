"""
实现多表替代密码：维吉尼亚密码、希尔密码,实现对英文消息plaintext的替代加密
"""
import random
import numpy as np

def egcd(a, b):
    r0, r1, s0, s1 = 1, 0, 0, 1
    while(b):
        q, a, b = a//b, b, a%b
        r0, r1 = r1, r0 - q*r1  
        s0, s1 = s1, s0 - q*s1
    return a,r0,s0

alphabet={}
alpha_str='abcdefghijklmnopqrstuvwxyz'

def Init_CTX():
    #初始化加密算法工作的环境，主要包括公共参数和版本控制等
    for i in range(26):
        alphabet[chr(97+i)]=i
    #print(alphabet)

    plaintext ='cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms, to transform messages in ways that are hard to decipher. These deterministic algorithms are used for cryptographic key generation, digital signing, verification to protect data privacy, web browsing on the internet and confidential communications such as credit card transactions and email.'
    #plaintext='hello my world'#[8,5,12,12]测试用例
    plaintext=plaintext.lower()
    
    V_Key=Vigenere_GenKey()
    H_Key0,H_Key1=Hill_GenKey()
    Vigenere_cipher=Vigenere_Encrypt(plaintext,V_Key)
    print("维吉尼亚加密：\n"+Vigenere_cipher)
    Vigenere_plain=Vigenere_Decrypt(Vigenere_cipher,V_Key)
    print("维吉尼亚解密：\n"+Vigenere_plain)

    Hill_cipher=Hill_Encrypt(plaintext,H_Key0)
    print("希尔加密：\n"+Hill_cipher)
    Hill_plain=Hill_Decrypt(Hill_cipher,H_Key1)
    print("希尔解密：\n"+Hill_plain)
    return

def Vigenere_GenKey():
    #生成维吉尼亚加密密钥和解密密钥
    Key=[random.randint(1,10) for i in range(random.randint(2,6))]
    return Key

def Hill_GenKey():
    #生成希尔加密密钥和解密密钥
    m=4
    Key=np.random.randint(2,10,(m,m)) 
    #Key=np.array([[0, 25, 25, 6], [3, 2, 2, 9], [19, 17, 20, 1], [16, 18, 2, 23]])

    Key_det=np.around(np.linalg.det(Key))

    egcd_det=egcd(Key_det,26)
    if egcd_det[0]!=1:
        Key,Key_inverse=Hill_GenKey()
        return Key,Key_inverse
    
    anti_det=egcd_det[1]
    
    if anti_det<0:
        anti_det+=26
    Key_=[0 for i in range(m)]
    Key_=[Key_.copy() for i in range(m)]
    

    for i in range(m):
        for j in range(4):
            temp=Key.T.copy()
            temp=np.delete(temp,i,0)
            temp=list(temp)
            for t in range(m-1):
                temp[t]=np.delete(temp[t],j,0)
            temp=np.array(temp)
            if (i+j)%2==1:
                Key_[i][j]=-1*np.linalg.det(temp)
            elif (i+j)%2==0:
                Key_[i][j]=np.linalg.det(temp)

    

    Key_inverse=((np.around(np.array(Key_))).astype(np.int32))*anti_det

    #Key_inverse=Key_inverse.astype(np.int32)
    # x=np.eye(m)
    # temp=[list(Key[i]).extend(x[i]) for i in range(m)]
    # while temp.all(np.eye(m)):
    #     pass
    #Key_inverse=np.array([[-58044, -3549, 71568, 13419], [42126, -256557, -36099, 90972], [19047, 212205, 42147, -89838], [5754, 184800, -25200, -4725]]       )

    #print(np.dot(Key,Key_inverse)%26)
    return Key,Key_inverse

def Vigenere_Encrypt(str,key):
    #维吉尼亚加密函数
    En_Key=key
    m=len(key)
    cipher=''
    i=0
    for j in str:
        if (ord(j)>=ord('a') and ord(j)<=ord('z')) or (ord(j)>=ord('A') and ord(j)<=ord('Z')):
            j=chr(ord(j)+En_Key[i%m])
            i+=1
            if ord(j)>ord('z'):
                j=chr(ord(j)-26)
            cipher+=j
        else:
            cipher+=j
    return cipher

def Vigenere_Decrypt(str,key):
    #维吉尼亚解密函数
    De_Key=key
    m=len(De_Key)
    plain=''
    i=0
    for j in str:
        if (ord(j)>=ord('a') and ord(j)<=ord('z')) or (ord(j)>=ord('A') and ord(j)<=ord('Z')):
            j=chr(ord(j)-De_Key[i%m])
            i+=1
            if ord(j)<ord('a'):
                j=chr(ord(j)+26)
            plain+=j
        else:
            plain+=j
    return plain

def Hill_Encrypt(str,En_Key):
    #希尔加密函数
    cipher=['#' for i in range(len(str))]
    m=len(En_Key[0])
    i,j,n=0,0,0
    ls_temp=[]
    for temp in str:
        if (ord(temp)>=ord('a') and ord(temp)<=ord('z')) or (ord(temp)>=ord('A') and ord(temp)<=ord('Z')):
            ls_temp.append(alphabet[temp])
            i+=1
            j+=1
        else:
            cipher[i]=temp
            i+=1
        if j==m:
            ls_temp=np.dot(ls_temp,En_Key)
            for k in range(m):
                for n in range(len(cipher)):
                    if ord(cipher[n])==ord('#'):
                        break
                cipher[n]=alpha_str[ls_temp[k]%26]
            ls_temp=[]
            j=0
    return ''.join(cipher)

def Hill_Decrypt(str,De_Key):
    #希尔解密函数
    plain=['#' for i in range(len(str))]
    m=len(De_Key[0])
    i,j,n=0,0,0
    ls_temp=[]
    for temp in str:
        if (ord(temp)>=ord('a') and ord(temp)<=ord('z')) or (ord(temp)>=ord('A') and ord(temp)<=ord('Z')):
            ls_temp.append(alphabet[temp])
            i+=1
            j+=1
        else:
            plain[i]=temp
            i+=1
        if j==m:
            ls_temp=(np.dot(np.array(ls_temp),De_Key)).astype(np.int32)
            for k in range(m):
                for n in range(len(plain)):
                    if ord(plain[n])==ord('#'):
                        break
                plain[n]=alpha_str[ls_temp[k]%26]
            ls_temp=[]
            j=0
    return ''.join(plain)

def main():
    Init_CTX()
    return

if __name__=="__main__":
    main()