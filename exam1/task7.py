"""
了解base64编码，读取上述cryptointro.txt和pmt-cipher.txt，并以base64编码输出并显示。
"""
import base64

'''
失败用例
Base64Dcountry={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',
                        8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',
                        15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',
                        22:'W',23:'X',24:'Y',25:'Z',26:'a',27:'b',28:'c',
                        29:'d',30:'e',31:'f',32:'g',33:'h',34:'i',35:'j',
                        36:'k',37:'l',38:'m',39:'n',40:'o',41:'p',42:'q',
                        43:'r',44:'s',45:'t',46:'u',47:'v',48:'w',49:'x',
                        50:'y',51:'z',52:'0',53:'1',54:'2',55:'3',56:'4',
                        57:'5',58:'6',59:'7',60:'8',61:'9',62:'+',63:'/'}

def encode_base64(b_str):
    final_str=''
    t=''
    while(len(b_str)>=24):
        final_str+=Base64Dcountry[int(b_str[:6],2)]
        b_str=b_str[6:]
    while(len(b_str)%6!=0):
        b_str+='0'
    while b_str:
        t+=Base64Dcountry[int(b_str[:6],2)]
        b_str=b_str[6:]
    while(len(t)!=4):
        t+='='
    return final_str+t

def main():
    str1,str2='',''
    with open("cryptography exam\exam1\古典密码实验内容-20240226\cryptointro.txt",'r',encoding='utf-8') as file:
        str1=file.read()
    str_temp=[bin(ord(i)).replace('0b','') for i in(str1)]
    str_temp=''.join(str_temp)
    print(encode_base64(str_temp))
    with open("cryptography exam\exam1\古典密码实验内容-20240226\pmt-cipher.txt",'r',encoding='utf-8') as file:
        str2=file.read()
    print(encode_base64(str2))
'''

def main():
    str1,str2='',''
    with open("cryptography exam\exam1\古典密码实验内容-20240226\cryptointro.txt",'r',encoding='utf-8') as file:
        str1=file.read()
    encodestr=base64.b64encode(str1.encode('utf-8'))
    print(encodestr)
    with open("cryptography exam\exam1\古典密码实验内容-20240226\pmt-cipher.txt",'r',encoding='utf-8') as file:
        str2=file.read()
    encodestr=base64.b64encode(str2.encode('utf-8'))
    print(encodestr)

if __name__=="__main__":
    main()
