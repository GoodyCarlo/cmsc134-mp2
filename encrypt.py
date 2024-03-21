#import libaries
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import base64
import json

#creating and encrypting message
message = b'You can attack now!'

key = RSA.importKey(open('pk.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
msg = {
    "ciphertext": str(base64.b64encode(ciphertext),'utf-8')
}

with open("msg.json","w") as f:
    f.write(json.dumps(msg,indent=4))
f.close()