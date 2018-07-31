from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random

def myDecrypt(key, ct):
    dsize = SHA.digest_size
    sentinel = Random.new().read(15 + dsize)

    cipher = PKCS1_v1_5.new(key)
    return cipher.decrypt(ct, sentinel)


if __name__ == "__main__":
    key = RSA.importKey(open('key', 'rb').read())
    print(myDecrypt(key, open('ct.txt', 'rb').read()))
