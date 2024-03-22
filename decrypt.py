# import libaries
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import json


def verify(pk, text, signature):
    # Hash is mandatory for this implementation of PKCS #1: https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_v1_5.html
    hashed_text = SHA256.new(text)
    verifier = pkcs1_15.new(pk)
    verifier.verify(hashed_text, signature)


def decrypt(sk, ciphertext):
    cipher = PKCS1_OAEP.new(sk)
    text = cipher.decrypt(ciphertext)
    return text


if __name__ == "__main__":
    # import keys
    verify_public_key = RSA.importKey(open("pk.pem").read())
    decrypt_private_key = RSA.importKey(open("sk.pem").read(), passphrase="password")

    # read message and store from dictionary
    with open("msg.json", "r") as f:
        hex_message = json.load(f)

        # convert ciphertext and signature back to bitstring
        ciphertext = bytes.fromhex(hex_message["ciphertext"])
        signature = bytes.fromhex(hex_message["signature"])

    verify(verify_public_key, ciphertext, signature)
    plaintext = decrypt(decrypt_private_key, ciphertext)
    print(plaintext.decode())
