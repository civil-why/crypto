"""
实现对替代密码的攻击,找到1）中密文对应的解密密钥；
已知加密类型攻击
"""
#plaintext = 'cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms, to transform messages in ways that are hard to decipher. These deterministic algorithms are used for cryptographic key generation, digital signing, verification to protect data privacy, web browsing on the internet and confidential communications such as credit card transactions and email.'

cipher_txt = 'fubswrjudskb lv d phwkrg ri surwhfwlqj lqirupdwlrq dqg frppxqlfdwlrqv wkurxjk wkh xvh ri frghv, vr wkdw rqob wkrvh iru zkrp wkh lqirupdwlrq lv lqwhqghg fdq uhdg dqg surfhvv lw. lq frpsxwhu vflhqfh, fubswrjudskb uhihuv wr vhfxuh lqirupdwlrq dqg frppxqlfdwlrq whfkqltxhv ghulyhg iurp pdwkhpdwlfdo frqfhswv dqg d vhw ri uxoh-edvhg fdofxodwlrqv fdoohg dojrulwkpv, wr wudqvirup phvvdjhv lq zdbv wkdw duh kdug wr ghflskhu. wkhvh ghwhuplqlvwlf dojrulwkpv duh xvhg iru fubswrjudsklf nhb jhqhudwlrq, gljlwdo vljqlqj, yhulilfdwlrq wr surwhfw gdwd sulydfb, zhe eurzvlqj rq wkh lqwhuqhw dqg frqilghqwldo frppxqlfdwlrqv vxfk dv fuhglw fdug wudqvdfwlrqv dqg hpdlo.'

def Init_CTX():
    #初始化加密算法工作的环境，主要包括公共参数和版本控制等
    text=' the '#最简单的匹配文字，不失有效性
    plain=Attack(cipher_txt)
    Key=0
    plain_text=''
    for j,i in enumerate(plain):
        if text in i:
            Key=j
    print('加密方式为凯撒密码，密钥为：'+'{}'.format(Key))
    print('明文为：')
    print(plain[Key])
    return

def Attack(cipher):
    #默认已知密码体制，进行移位密码穷尽
    plain=[]
    alpha_str='abcdefghijklmnopqrstuvwxyz'
    for i in range(25):
        temp=''
        for j in cipher:
            if j in alpha_str:
                t=chr(ord(j)-i)
                if t in alpha_str:
                    temp+=t
                else:
                    t=chr(ord(t)+26)
                    temp+=t
            else:
                temp+=j
        plain.append(temp)
    return plain

def main():
    Init_CTX()

if __name__=="__main__":
    main()