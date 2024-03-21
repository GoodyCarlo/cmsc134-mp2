#import libaries

from Crypto.Cipher import PKCS1_OAEP

from Crypto.PublicKey import RSA

#generate and export public and private key
mykey = RSA.generate(3072)

pwd = b'password'

with open("sk.pem", "wb") as f:

    data = mykey.export_key(passphrase=pwd,
                            pkcs=8,
                            protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                            prot_params={'iteration_count':131072})

    f.write(data)

f.close()


with open("pk.pem", "wb") as f:

    data = mykey.public_key().export_key()

    f.write(data)

f.close()