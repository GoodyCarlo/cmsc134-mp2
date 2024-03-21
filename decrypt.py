#import libaries
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import json
#import keys
pk = RSA.importKey(open('pk.pem').read())
sk = RSA.importKey(open('sk.pem').read(),
                    passphrase=b'password')

#read message and store as dictionary
with open("msg.json", "r") as f:
    hex_message = json.load(f)

f.close()

#convert ciphertext and signature back to bytes:
cipher_text = bytes.fromhex(hex_message['ciphertext'])
signature = bytes.fromhex(hex_message['signature'])

#recreating the hashed file
hashed_cipher_text = SHA256.new(cipher_text)

#verifying and decrypting the file
verifier = pkcs1_15.new(pk)
try:
    verifier.verify(hashed_cipher_text,signature)
    cipher = PKCS1_OAEP.new(sk)
    text = cipher.decrypt(cipher_text)
    print(text.decode())
except:
    print("invalid message")
    