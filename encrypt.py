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
    hashed_text = SHA256.new(text)
    signer = pkcs1_15.new(sk)
    signature = signer.sign(hashed_text)

    return signature
