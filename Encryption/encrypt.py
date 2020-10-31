from cryptography.fernet import Fernet

def generate_key():
    return(Fernet.generate_key())


def encrypt(key, filez):
    with open(filez, 'rb') as f:
        data = f.read()
        print(data)
    with open(filez, 'wb') as f:
        f.write(Fernet(key).encrypt(data))
def decrypt(key, filez):
    with open(filez, 'rb') as f:
        data = f.read()
    with open(filez, 'wb') as f:
        f.write(Fernet(key).decrypt(data))

key = b'obVkxTpAW5PaiEXiDzI5C-yN_Q2BX2pMch8KdwTjF2A='
#print(key)



print("text.txt".split('.')[1])