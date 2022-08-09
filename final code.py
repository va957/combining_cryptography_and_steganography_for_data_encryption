
from sympy import randprime
import numpy as np
from PIL import Image


def gcd(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:    # gcd * k % mod phi = 1
            return x
    return None
keysize=16
p1=0
p2=0
while p1==p2 or (p1*p2)>2**keysize:
    p1=randprime(3,2**keysize)
    p2=randprime(3,2**keysize)
    
print("1st Prime Number is " + str(p1))
print("2nd Prime Number is " + str(p2))

rsa_modulus=p1*p2
totient=(p1-1)*(p2-1)

e=0
for i in range(3,totient-1):
    if gcd(i,totient)==1:
        e=i
        break


print("  Public-Key exponent, e -----> " + str(e))
print("  Public Key -----> (" + str(e) + ", " + str(rsa_modulus) + ")")

d = modinv(e,totient)
print("  Private-Key exponent, d -----> " + str(d))
print("  Private Key -----> (" + str(d) + ", " + str(rsa_modulus) + ")")


def mod(x,y):
    if(x<y):
        return y
    else:
        c=x%y
        return c

def encryptString(plainText):
    message=""
    for x in list(plainText):
        c = mod(ord(x)**e,rsa_modulus)
        message+=(chr(c))
    return message

def decryptString(plainText):
    plain=""
    for x in list(plainText):
        c = mod(ord(x)**d,rsa_modulus)
        plain+=(chr(c))
    return plain


def Encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4    
    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully")
def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4   
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Hidden Message:", message[:-5])
    else:
        print("No Hidden Message Found")
def Stego():
    print("--Welcome to $t3g0--")
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        print("Enter Source Image Path")
        src = input()
        print("Enter Message to Hide")
        message = input()
        print("Enter Destination Image Path")
        dest = input()
        print("Encoding...")
        Encode(src, message, dest)

    elif func == '2':
        print("Enter Source Image Path")
        src = input()
        print("Decoding...")
        Decode(src)

    else:
        print("ERROR: Invalid option chosen")
Stego()



