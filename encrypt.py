#import libaries
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

import json
#loading keys
sk = RSA.importKey(open('sk.pem').read(),
                    passphrase=b'password')
pk = RSA.importKey(open('pk.pem').read())

#creating and encrypting message
message = b'You can attack now!'
cipher = PKCS1_OAEP.new(pk)
cipher_text = cipher.encrypt(message)


#signing the message
hashed_cipher_text = SHA256.new(cipher_text)
signer = pkcs1_15.new(sk)
signature = signer.sign(hashed_cipher_text)

#encrypting message to a file
message = {
    'ciphertext': cipher_text.hex(),
    'signature': signature.hex()
}

with open("msg.json","w") as f:
    f.write(json.dumps(message,indent=4))

f.close()