from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

import json
import time

payload = {
    "ok": True,
    "timestamp": time.time(),
    "msg": "this is a really important msg"
}

plaintxt = json.dumps(payload).encode()

# plaintxt = "shit".encode()
h = SHA.new(plaintxt)

key = RSA.importKey(open("key.pub", "rb").read())
cipher = PKCS1_v1_5.new(key)
ciphertext = cipher.encrypt(plaintxt)

with open("ct.txt", "wb") as ofile:
    ofile.write(ciphertext)


# from Crypto import Random

# key = RSA.importKey(open('key', 'rb').read())
# dsize = SHA.digest_size
# sentinel = Random.new().read(15+dsize)

# cipher = PKCS1_v1_5.new(key)
# msg = cipher.decrypt(ciphertext, sentinel)

# # digest = SHA.new(msg[:-dsize]).digest()
# print(msg)
# assert msg == plaintxt
# # assert digest == msg[:-dsize]
