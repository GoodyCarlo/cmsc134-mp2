# import libaries
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

import json


def encrypt(pk, plaintext):
    cipher = PKCS1_OAEP.new(pk)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def sign(sk, text):
    # Hash is mandatory for this implementation of PKCS #1: https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_v1_5.html
    hashed_text = SHA256.new(text)
    signer = pkcs1_15.new(sk)
    signature = signer.sign(hashed_text)

    return signature


if __name__ == "__main__":
    sign_private_key = RSA.importKey(open("sk.pem").read(), passphrase="password")
    encrypt_public_key = RSA.importKey(open("pk.pem").read())

    message = b"You can attack now!"

    ciphertext = encrypt(encrypt_public_key, message)
    signature = sign(sign_private_key, ciphertext)

    message = {"ciphertext": ciphertext.hex(), "signature": signature.hex()}

    with open("msg.json", "w") as f:
        f.write(json.dumps(message, indent=4))