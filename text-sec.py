"""+++++++++++++++++++++++"""
import numpy as np
import base64

"""___________________Keys for caser cipher encryption __________________________________"""
# Keys for encrypt
def KeyUpperCase(char,K):
    return chr((ord(char)-65 +K)% 26 + 65)
def KeyLowerCase(char,K):
    return chr((ord(char)-97 +K)% 26 + 97)
def keyNumber(char,K):
    return chr((ord(char)-48 +K)% 10 + 48)

# Keys for decrypt 
def DKeyUpperCase(char,K):
    return chr((ord(char)-65 -K)% 26 + 65)
def DKeyLowerCase(char,K):
    return chr((ord(char)-97 -K)% 26 + 97)
def DkeyNumber(char,K):
    return chr((ord(char)-48 -K)% 10 + 48)
"""----------------------------------------------------------------------------"""

"""------------------caser cipher encerption------------------"""
def encrypt_CC(data,K):
    s=''
    for i in data:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            s += KeyUpperCase(i,K)
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            s += KeyLowerCase(i,K)
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            s+= keyNumber(i,K)
        else:
            s+=i
    return s

"""---------------caser cipher decerption-----------------------------"""
def decrypt_CC(data, K):
    s = ''
    for i in data:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            s += DKeyUpperCase(i, K)
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            s += DKeyLowerCase(i, K)
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            s += DkeyNumber(i, K)
        else:
            s += i
    return s
"""--------------rail fence cipher encode--------------------------"""
def encode_RFC(x):
    if len(x) % 2 != 0:
        x += ' '

    C = len(x)
    p1 = ''
    p2 = ''
    i = 0
    while i < C - 1:
        p1 += x[i]
        p2 += x[i + 1]
        i += 2
    c = p1 + p2
    return c
"""-------------rail fence cipher encode--------------"""
def decode_RFC(c):
    D = len(c)
    INC=int(0.5*D)
    plain=''
    p1=''
    p2=''
    for i in range(INC):
        p1+=c[i]
        p1+=c[int(i+INC)]


    plain=p1
    return plain

def multi_encode(x):
    print('encode')
    """en rfb"""
    c=encode_RFC(x)
    """enc"""
    c=c.encode('utf-8')
    """base en"""
    c=base64.b64encode(c)
    """dec"""
    c=c.decode('utf-8')
    """en rfc"""
    c=encode_RFC(c)
    c=c.encode('utf-8')
    """base en"""
    c=base64.b64encode(c)
    """dec"""
    c=c.decode('utf-8')
    """enc cc"""
    c=encrypt_CC(c,8)
    return c
def multi_dencode(c):
    print('decode.....')
    """dec cc"""
    c=decrypt_CC(c,8)
    """enc"""
    c=c.encode('utf-8')
    """base dec"""
    c=base64.b64decode(c)
    """dec"""
    c=c.decode('utf-8')
    """dec rfc"""
    c=decode_RFC(c)
    """enc"""
    c=c.encode('utf-8')
    """base dec"""
    c=base64.b64decode(c)
    """dec"""
    c=c.decode('utf-8')
    """dec rfd"""
    c=decode_RFC(c)
    return c

ch = ''
print('''        \t   \t      THE_secret_V1 
+++++++++++++++++++encrypt and decrypt your textual data ++++++ ''')
while ch !='exit':
    ch = input("""
        for encode press 1
        for decode press 2
        file press 3
        for exit type exit
        >>:""")
    if ch == "1":
        text = input("ender your text : ")
        x = multi_encode(text)
        print(f"your encarption:  {x}")
    elif ch =="2":
        text = input("""ender your base64 : """)
        x = multi_dencode(text)
        print(f"ypur decription:  {x}")
    elif ch == "3":
        path = input("ente the path your file ")
        op = input('''
        for encerypt the file press 1
        for decypt the ile press 2 
        >>:''')
        with open(path,'r') as file:

                if op =='1':
                    file_name = input("save as : ")
                    for line in file.readlines():
                        x = multi_encode(line)

                        with open(file_name,'a') as f:
                            f.write(str(x)+ '\n')
                    f.close()

                elif op == "2":
                    file_name = input("save as : ")
                    for line in file.readlines():
                        x = multi_dencode(line)
                        with open(file_name,'a') as f2:
                            f2.write(x+ '\n')
                    f2.close()


        file.close()
    elif ch =='exit':
        break
    else:
        print("invaled input try agin")

