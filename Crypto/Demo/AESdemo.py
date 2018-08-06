from Crypto.Cipher import AES
from base64 import standard_b64encode


def sanitize (data):
    data1 = data.encode('utf-8')
    pad = block_size - len(data1) % block_size
    print("pad=" + str(pad))
    data1 = data1 + (pad * chr(pad)).encode('utf-8')
    print("data:=" + data1)
    return data1

def encrypt(data):
    data = sanitize(data)
    return standard_b64encode(cipher.encrypt(data)).decode('utf-8')
    #return standard_b64encode(cipher.encrypt(data)).decode('utf-8')
key = "B374A26A71490437AA024E4FADD5B497"
print("key:="+key)
cipher = AES.new(key, AES.MODE_ECB)
block_size = 16

data = "\x00"*14+'ab'
data = sanitize(data)
print( standard_b64encode(cipher.encrypt(data)).decode('utf-8'))


cipher = AES.new(key, AES.MODE_CFB)
block_size = 16

data = "\x00"*14+'ab'
data = sanitize(data)
print( standard_b64encode(cipher.encrypt(data)).decode('utf-8'))


