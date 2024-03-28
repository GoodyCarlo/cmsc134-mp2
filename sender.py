# import libaries
import json
from pathlib import Path

from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


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


def main(
    message,
    sskPATH=Path("keys/signing_sk.pem"),
    epkPATH=Path("keys/encryption_pk.pem"),
    messagePath=Path("msg.json"),
    pwd="password",
):

    sign_private_key = RSA.importKey(
        open(sskPATH).read(),
        passphrase=pwd,
    )
    encrypt_public_key = RSA.importKey(
        open(epkPATH).read(),
    )

    message = message.encode("utf-8")

    ciphertext = encrypt(encrypt_public_key, message)
    signature = sign(sign_private_key, ciphertext)

    message = {"ciphertext": ciphertext.hex(), "signature": signature.hex()}

    with open(messagePath, "w") as f:
        f.write(json.dumps(message, indent=4))


if __name__ == "__main__":
    from args import senderParser

    args = senderParser.parse_args()

    main(
        args.message,
        args.signing_sk,
        args.encryption_pk,
        args.message_path,
        args.password,
    )
