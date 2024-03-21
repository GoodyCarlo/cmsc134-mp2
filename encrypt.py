#import libaries
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

import base64
import json

#creating and encrypting message
message = b'You can attack now!'

key = RSA.importKey(open('pk.pem').read())
cipher = PKCS1_OAEP.new(key)
cipher_text = cipher.encrypt(message)

hashed_cipher_text = SHA256.new(cipher_text)

#signing the message
sk = RSA.importKey(open('sk.pem').read(),
                    passphrase=b'password')

signer = pkcs1_15.new(sk)

signature = signer.sign(hashed_cipher_text)

#verify the message
pk = RSA.importKey(open('pk.pem').read())
verifier = pkcs1_15.new(pk)

try:
    verifier.verify(hashed_cipher_text,signature)
    cipher = PKCS1_OAEP.new(sk)
    text = cipher.decrypt(cipher_text)
    print(text.decode())
except:
    print("invalid message")
    